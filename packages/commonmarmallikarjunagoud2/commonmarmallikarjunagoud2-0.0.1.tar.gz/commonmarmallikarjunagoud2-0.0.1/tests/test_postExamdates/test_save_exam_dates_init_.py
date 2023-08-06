#test_save_exam_dates_init_.py

import sys
import os
import unittest
from unittest import mock
from unittest.mock import patch, Mock, MagicMock, create_autospec
from test.support import EnvironmentVarGuard
import azure.functions as func
from tests.load_environment_variables import EnvironmentVariable
EnvironmentVariable()
from postExamDates import main

class SaveExamDatesInitTest(unittest.TestCase):

    @patch('postExamDates.SaveExamDates')
    def test_init_return_updated(self, mocked):

        edit_exam_dates ='[{"examkey": 1,"plannedExamDate": "28/02/2021","actualExamDate": "28/01/2021"}]'
        mocked_value = '{"success":{"status":201,"detail":"Data updated successfully"}'
        http_response = func.HttpResponse(status_code=201,body=mocked_value)
        mocked.return_value.save_exam_date.return_value = http_response
        http_request = func.HttpRequest(
            method='POST',
            body=edit_exam_dates.encode('utf8'),
            url='/postExamDates',
            params={'userKey': 'A22AF4A1-611E-4C65-B018-287A3B81F873'}
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 201)

    @patch('postExamDates.SaveExamDates')
    def test_init_return_bad_request(self, mocked):

        edit_exam_dates ='[{"examkey": 1,"plannedExamDate": "28/01/2021","actualExamDate": "28/01/2021"}]'
        mocked_value = '{"error": {"types": "Invalid Request","title": "Header/Param validation failure","status": 400,"detail": "Invalid User Key","instance": "TaskListDetails"}'
        http_response = func.HttpResponse(status_code=400,body=mocked_value)
        mocked.return_value.save_exam_date.return_value = http_response
        http_request = func.HttpRequest(
            method='POST',
            body=edit_exam_dates.encode('utf8'),
            url='/postExamDates',
            
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 400)
        
    @patch('postExamDates.SaveExamDates')
    def test_init_return_internal_server_error(self, mocked):

        edit_exam_dates ='[{"examkey": 1,"plannedExamDate": "28/01/2021","actualExamDate": "28/01/2021"}]'
        mocked_value = '{"error": {"types": "Invalid Request","title": "Header/Param validation failure","status": 400,"detail": "The planned date cannot be in the past","instance": "TaskListDetails"}'
        http_response = func.HttpResponse(status_code=500,body=mocked_value)
        mocked.return_value.save_exam_date.return_value = http_response
        http_request = func.HttpRequest(
            method='POST',
            body=edit_exam_dates.encode('utf8'),
            url='/postExamDates',
            params={'userKey': 'A22AF4A1-611E-4C65-B018-287A3B81F873'}
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 500)
  
   

