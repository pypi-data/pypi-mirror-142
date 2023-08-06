#test_save_exam_dates_business_logic.py

import sys
import os
import unittest
from unittest import mock
from unittest.mock import patch, Mock, MagicMock, create_autospec
from test.support import EnvironmentVarGuard
import azure.functions as func
from tests.load_environment_variables import EnvironmentVariable
EnvironmentVariable()
from postExamDates import SaveExamDates

class SaveExamDatesBusinessLogicTest(unittest.TestCase):

    @patch('postExamDates.businesslogic.save_exam_dates.SqlOperation')
    def test_return_return_updated(self, mocked):  
        edit_exam_dates ='[{"examkey": 1,"plannedExamDate": "28/02/2021","actualExamDate": "28/01/2021"}]'
        mocked_value = (True,None)
        http_request = func.HttpRequest(
            method='POST',
            body=edit_exam_dates.encode('utf8'),
            url='/postExamDates',
            params={'userKey': 'A22AF4A1-611E-4C65-B018-287A3B81F873'}
        )
        mocked.return_value.fetch_one.return_value  = mocked_value
        instance = SaveExamDates()
        response = instance.save_exam_date(http_request)
        self.assertEqual(response.status_code, 201) 

    @patch('postExamDates.businesslogic.save_exam_dates.SqlOperation')
    def test_return_bad_request(self, mocked):  
        edit_exam_dates ='[{"examkey": 1,"plannedExamDate": "28/02/2021","actualExamDate": "28/01/2021"}]'
        mocked_value = '{"error": {"types": "Invalid Request", "title": "Header/Param validation failure", "status": 400, "detail": "Invalid User Key", "instance": "TaskListDetails"}'
        http_request = func.HttpRequest(
            method='POST',
            body=edit_exam_dates.encode('utf8'),
            url='/postExamDates',
        )
        mocked.return_value.fetch_one.return_value  = mocked_value
        instance = SaveExamDates()
        response = instance.save_exam_date(http_request)
        self.assertEqual(response.status_code, 400) 

    @patch('postExamDates.businesslogic.save_exam_dates.SqlOperation')
    def test_return_internal_server_error(self, mocked):  
        edit_exam_dates ='[{"examkey": 1,"plannedExamDate": "28/01/2021","actualExamDate": "28/01/2021"}]'
        mocked_value = (False, 'The planned date cannot be in the past')
        http_request = func.HttpRequest(
            method='POST',
            body=edit_exam_dates.encode('utf8'),
            url='/postExamDates',
            params={'userKey': 'A22AF4A1-611E-4C65-B018-287A3B81F873'}
        )
        mocked.return_value.fetch_one.return_value  = mocked_value
        instance = SaveExamDates()
        response = instance.save_exam_date(http_request)
        self.assertEqual(response.status_code, 500) 

