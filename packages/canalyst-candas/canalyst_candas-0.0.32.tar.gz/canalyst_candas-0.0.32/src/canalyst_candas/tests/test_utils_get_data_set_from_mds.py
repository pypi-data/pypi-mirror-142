from io import StringIO
from unittest import mock
import unittest
import json
from unittest.mock import Mock, patch

import pandas
from requests.models import Response

from canalyst_candas import settings

from canalyst_candas.utils import (
    LogFile,
    CsvDataKeys,
    get_data_set_from_mds,
    _get_data_set_csv_url,
    _get_data_set_urls_from_mds,
)


class MdsBulkDataUtilsTests(unittest.TestCase):
    """
    Test cases for the get_data_set_from_mds() method and associated methods
    """

    def setUp(self) -> None:
        # returned from https://mds.canalyst.com/api/equity-model-series/VNEXIO0198/equity-models/Q3-2021.21/
        self.ex_json_str = """
        {
            "equity_model_series": {
                "csin": "VNEXIO0198",
                "self": "https://mds.canalyst.com/api/equity-model-series/VNEXIO0198/"
            },
            "model_version": {
                "name": "Q3-2021.21",
                "self": "https://mds.canalyst.com/api/model-versions/VNEXIO0198/periods/Q3-2021/revisions/21/"
            },
            "most_recent_period": {
                "name": "Q3-2021",
                "period_duration_type": "fiscal_quarter",
                "start_date": "2021-08-01",
                "end_date": "2021-10-30",
                "self": "https://mds.canalyst.com/api/equity-model-series/VNEXIO0198/equity-models/Q3-2021.21/historical-periods/Q3-2021/"
            },
            "trading_currency": {
                "description": "USD",
                "unit_type": "currency",
                "symbol": "$",
                "self": "https://mds.canalyst.com/api/units/0w4VjmAaWr-j2aZcniqNQA/"
            },
            "candascsvdata_set": [
                "https://mds.canalyst.com/api/candas-csv-data/forecast-data/19868/",
                "https://mds.canalyst.com/api/candas-csv-data/historical-data/19867/",
                "https://mds.canalyst.com/api/candas-csv-data/name-index/19866/",
                "https://mds.canalyst.com/api/candas-csv-data/model-info/19865/"
            ],
            "earnings_update_type": "regular",
            "published_at": "2021-12-15T06:00:41.609512Z",
            "time_series_categories": "https://mds.canalyst.com/api/equity-model-series/VNEXIO0198/equity-models/Q3-2021.21/time-series-categories/",
            "time_series_set": "https://mds.canalyst.com/api/equity-model-series/VNEXIO0198/equity-models/Q3-2021.21/time-series/",
            "historical_periods": "https://mds.canalyst.com/api/equity-model-series/VNEXIO0198/equity-models/Q3-2021.21/historical-periods/",
            "forecast_periods": "https://mds.canalyst.com/api/equity-model-series/VNEXIO0198/equity-models/Q3-2021.21/forecast-periods/",
            "scenarios": "https://mds.canalyst.com/api/equity-model-series/VNEXIO0198/equity-models/Q3-2021.21/scenarios/",
            "historical_data_points": "https://mds.canalyst.com/api/equity-model-series/VNEXIO0198/equity-models/Q3-2021.21/historical-data-points/",
            "self": "https://mds.canalyst.com/api/equity-model-series/VNEXIO0198/equity-models/Q3-2021.21/"
        }
        """
        self.json_response = json.loads(self.ex_json_str)

        self.url = f"{settings.MDS_HOST}/api/candas-csv-data/{CsvDataKeys.HISTORICAL_DATA.value}/19867/"
        self.url_candidates = self.json_response.get("candascsvdata_set")
        self.mock_log = Mock(spec=LogFile)

        self.mock_get_request_json_content = patch(
            "canalyst_candas.utils.get_request_json_content"
        ).start()
        self.mock_get_request = patch("canalyst_candas.utils.get_request").start()

    def tearDown(self):
        patch.stopall()

    def test_get_data_set_from_mds_success(self):
        with patch("requests.models.Response") as response_mock:
            some_csv_file = (
                '"header1", "header2", "header3"\n "data1", "data2", "data3"'
            )
            get_csv_response = response_mock
            type(get_csv_response).content = mock.PropertyMock(  # type: ignore
                return_value=bytes(some_csv_file, "utf-8")
            )

            self.mock_get_request.return_value = get_csv_response
            self.mock_get_request_json_content.return_value = self.json_response

            result = get_data_set_from_mds(
                CsvDataKeys.HISTORICAL_DATA,
                "ABCDE12345",
                "Q1-2021.20",
                {},
                self.mock_log,
                "mds_host",
            )

            self.assertEqual(
                result.to_string(), pandas.read_csv(StringIO(some_csv_file)).to_string()
            )

    def test_get_data_set_from_mds_url_is_null(self):
        json_response_without_csv_data_set = self.json_response
        json_response_without_csv_data_set["candascsvdata_set"] = []
        self.mock_get_request_json_content.return_value = (
            json_response_without_csv_data_set
        )

        result = get_data_set_from_mds(
            CsvDataKeys.HISTORICAL_DATA,
            "ABCDE12345",
            "Q1-2021.20",
            {},
            self.mock_log,
            "mds_host",
        )

        self.assertIsNone(result)
        self.mock_log.write.assert_called_once_with(
            f"Candas: Error with retrieving the '{CsvDataKeys.HISTORICAL_DATA.value}' URL from the list '[]'."
        )

    def test_get_data_set_csv_url_success(self):
        result = _get_data_set_csv_url(
            self.url_candidates, CsvDataKeys.HISTORICAL_DATA.value, self.mock_log
        )
        self.assertEqual(result, self.url)

    def test_get_data_set_csv_url_data_set_is_empty(self):
        result = _get_data_set_csv_url(
            [], CsvDataKeys.HISTORICAL_DATA.value, self.mock_log
        )
        self.assertIsNone(result)
        self.mock_log.write.assert_called_once_with(
            f"Candas: Error with retrieving the '{CsvDataKeys.HISTORICAL_DATA.value}' URL from the list '[]'."
        )

    def test_get_data_set_csv_url_multiple_matches(self):
        expected_result = self.url
        url_candidates = [
            f"{settings.MDS_HOST}/api/candas-csv-data/forecast-data/19868/",
            expected_result,
            f"{settings.MDS_HOST}/api/candas-csv-data/name-index/19866/",
            f"{settings.MDS_HOST}/api/candas-csv-data/model-info/19865/",
            expected_result,
        ]

        result = _get_data_set_csv_url(
            url_candidates,
            CsvDataKeys.HISTORICAL_DATA.value,
            self.mock_log,
        )

        self.assertIsNone(result)
        self.mock_log.write.assert_called_once_with(
            f"Candas: Error with retrieving the '{CsvDataKeys.HISTORICAL_DATA.value}' URL from the list '{url_candidates}'."
        )

    def test_get_data_set_urls_from_mds_success(self):
        self.mock_get_request_json_content.return_value = self.json_response

        result = _get_data_set_urls_from_mds(
            "ABCDE12345",
            "Q1-2021.20",
            {},
            self.mock_log,
            "mds_host",
        )

        expected_result = self.url_candidates

        self.assertEqual(result, expected_result)

    def test_get_data_set_urls_from_mds_hanldes_error(self):
        self.mock_get_request_json_content.return_value = None

        result = _get_data_set_urls_from_mds(
            "ABCDE12345",
            "Q1-2021.20",
            {},
            self.mock_log,
            "mds_host",
        )

        self.assertEqual(result, [])
