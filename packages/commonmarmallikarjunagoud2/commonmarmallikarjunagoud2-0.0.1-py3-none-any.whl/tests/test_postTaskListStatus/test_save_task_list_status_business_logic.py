#test_save_task_list_status_business_logic.py

import sys
import os
import unittest
from unittest import mock
from unittest.mock import patch, Mock, MagicMock, create_autospec
from test.support import EnvironmentVarGuard
import azure.functions as func
from tests.load_environment_variables import EnvironmentVariable
EnvironmentVariable()
from postTaskListStatus import TaskListStatus

class SaveTaskListStatusBusinessLogicTest(unittest.TestCase):

    @patch('postTaskListStatus.businesslogic.task_list_status.SqlOperation')
    def test_return_return_updated(self, mocked):  
        mocked_dates ='[{"exam_sr_key": "6","task_list_id": "20","task_list_stat": "1596"}]'
        mocked_value = (True,None,[],[])
        http_request = func.HttpRequest(
            method='POST',
            body=mocked_dates.encode('utf8'),
            url='/postTaskListStatus',
            params={'userKey': 'A22AF4A1-611E-4C65-B018-287A3B81F873','roleName':'CEFA PM'}
        )
        mocked.return_value.fetch_one.return_value  = mocked_value
        instance = TaskListStatus()
        response = instance.save_task_list_status(http_request)
        self.assertEqual(response.status_code, 201) 

    @patch('postTaskListStatus.businesslogic.task_list_status.SqlOperation')
    def test_return_bad_request(self, mocked):  
        mocked_dates ='[{"exam_sr_key": "test","task_list_id": "test","task_list_stat": "test"}]'
        mocked_value = '{"error": {"types": "Invalid Request", "title": "Header/Param validation failure", "status": 400, "detail": "userkey or roleName query parameter is missing", "instance": "TaskListStatus"}'
        http_request = func.HttpRequest(
            method='POST',
            body=mocked_dates.encode('utf8'),
            url='/postTaskListStatus',
        )
        mocked.return_value.fetch_one.return_value  = mocked_value
        instance = TaskListStatus()
        response = instance.save_task_list_status(http_request)
        self.assertEqual(response.status_code, 400) 

    @patch('postTaskListStatus.businesslogic.task_list_status.SqlOperation')
    def test_return_internal_server_error(self, mocked):  
        mocked_dates ='[{"exam_sr_key": "6","task_list_id": "20","task_list_stat": "1596"}]'
        mocked_value = (False, 'User does not have permission to save/submit for next level',[],[])
        http_request = func.HttpRequest(
            method='POST',
            body=mocked_dates.encode('utf8'),
            url='/postTaskListStatus',
            params={'userKey': 'A22AF4A1-611E-4C65-B018-287A3B81F873','roleName':'Test'}
        )
        mocked.return_value.fetch_one.return_value  = mocked_value
        instance = TaskListStatus()
        response = instance.save_task_list_status(http_request)
        self.assertEqual(response.status_code, 500) 

