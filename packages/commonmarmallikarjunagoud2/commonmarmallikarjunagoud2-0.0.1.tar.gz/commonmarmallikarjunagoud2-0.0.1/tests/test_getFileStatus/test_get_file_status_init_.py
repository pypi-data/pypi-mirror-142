#test_get_exam_data_status_init_.py

import sys
import os
import unittest
from unittest import mock
from unittest.mock import patch, Mock, MagicMock, create_autospec
from test.support import EnvironmentVarGuard
import azure.functions as func
from getFileStatus import main
from tests.load_environment_variables import EnvironmentVariable
EnvironmentVariable()


class ExamDataStatusInitTest(unittest.TestCase):

    @patch('getFileStatus.ExamDataStatus')
    def test_init_return_ok(self, mocked):
        mocked_value = '{"searchdatacount":{"currentpage":1,"totalcount":0,"totalpages":0},"searchresult":[]}'
        mocked.return_value.exam_data_status.return_value = mocked_value,200
        http_request = func.HttpRequest(
            method='GET',
            body='None',
            url = '/getFileStatus',
            headers={'X-File-Status-Filter':'{"supplier_key": 4, "search_start_date": "2021-09-01", "search_end_date": "2021-09-02","upload_type": "Exam Data Upload","upload_status": [],"user_id": 99999,"filename": null,"isexporttodoc": "N","sortcolumn": "StartMileage","sortorder": "asc","pageno": 1,"rowsperpage": 25}'}
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 200)
        
    
    @patch('getFileStatus.ExamDataStatus')
    def test_init_return_bad_request(self, mocked):
        mocked_value = '{"error": {"types": "Invalid Request","title": "Header/Param validation failure","status": 400,"detail": "fileName query parameter is missing.","instance": "ExamDataStatus"}'
        http_response = func.HttpResponse(status_code=400,body=mocked_value)
        mocked.return_value.exam_data_status.return_value = http_response
        http_request = func.HttpRequest(
            method='GET',
            body='None',
            url = '/getFileStatus',
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 400)