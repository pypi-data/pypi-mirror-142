#test_get_exam_data_status_business_logic_.py
import sys
import os
import unittest
from unittest import mock
from unittest.mock import patch, Mock, MagicMock, create_autospec
from test.support import EnvironmentVarGuard
import azure.functions as func
from tests.load_environment_variables import EnvironmentVariable
EnvironmentVariable()
from getFileStatus import ExamDataStatus

class GetExamDataStatusBusinessLogicTest(unittest.TestCase):

    @patch('getFileStatus.businesslogic.get_exam_data_status.SqlOperation')
    def test_return_return_ok(self, mocked):  
        mocked_value = b'{"success":"No","message":"Validation Failed in Task List Planned Dates."}',
        file_status_request = '{"supplier_key": 4, "search_start_date": "2021-09-01", "search_end_date": "2021-09-02","upload_type": "Exam Data Upload","upload_status": [],"user_id": "99999","filename": null,"isexporttodoc": "N","sortcolumn": "StartMileage","sortorder": "asc","pageno": 1,"rowsperpage": 25}'
        mocked.return_value.fetch_one.return_value  = mocked_value
        instance = ExamDataStatus()
        response, status_code = instance.exam_data_status(file_status_request)
        self.assertEqual(status_code, 200)
    
    @patch('getFileStatus.businesslogic.get_exam_data_status.SqlOperation')
    def test_return_return_bad_request(self, mocked):  
        mocked_value = b'{"success":"No","message":"Validation Failed in Task List Planned Dates."}',
        file_status_request = '{"supplier_key": 4, "search_start_date": "2021-09-01", "search_end_date": "2021-09-02","upload_type": "Exam Data Upload","upload_status": [],"user_id": 99999,"filename": null,"isexporttodoc": "N","sortcolumn": "StartMileage","sortorder": "asc","pageno": 1,"rowsperpage": 25}'
        mocked.return_value.fetch_one.return_value  = mocked_value
        instance = ExamDataStatus()
        response, status_code = instance.exam_data_status(file_status_request)
        self.assertEqual(status_code, 400)