#test_save_task_list_status_init_.py

import sys
import os
import unittest
from unittest import mock
from unittest.mock import patch, Mock, MagicMock, create_autospec
from test.support import EnvironmentVarGuard
import azure.functions as func
from tests.load_environment_variables import EnvironmentVariable
EnvironmentVariable()
from postTaskListStatus import main

class TaskListStatusUpdateInitTest(unittest.TestCase):

    @patch('postTaskListStatus.TaskListStatus')
    def test_init_return_updated(self, mocked):

        mocked_dates ='[{"exam_sr_key": "6","task_list_id": "20","task_list_stat": "1596"}]'
        mocked_value = '{"success":{"status":201,"supplier_json":"null","pdf_json":"null","detail":"Data updated successfully"}'
        http_response = func.HttpResponse(status_code=201,body=mocked_value)
        mocked.return_value.save_task_list_status.return_value = http_response
        http_request = func.HttpRequest(
            method='POST',
            body=mocked_dates.encode('utf8'),
            url='/postTaskListStatus',
            params={'userKey': 'A22AF4A1-611E-4C65-B018-287A3B81F873','roleName':'Supplier Planner'}
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 201)

    @patch('postTaskListStatus.TaskListStatus')
    def test_init_return_updated_other_than_supplier(self, mocked):
        mocked_dates ='[{"exam_sr_key": "1890","task_list_id": "3","task_list_stat": "1597"}]'
        mocked_value = '{"success":{"status": 201,"supplier_json": [{"Supplier_Id": 4}], "pdf_json": [{ "region": "Southern","route": "Kent","area": "London Bridge","elr": "HHH","railway_id": "W63","mileage_from": 0.875, "mileage_to": null,"asset_grp": "Bridge","asset_type": "Viaduct","asset_desc": "GREAT SUFFOLK STREET VIADUCT ARCHES 22 - 31A","asset_guid": "3978559C2D8345D9E04400306E4AD01A","exam_id": 3013501,"job_number": null,"hce_flg": "No","bcmi_required": null,"specific_exam_req": "Monthly cyclical examination to monitor the concrete slab movement. The examiner has to take base reading during first inspection. The base readings are to be used against futures inspection/readings to monitor any lateral movements or deterioration. 4 No. monthly cyclical examinations are required, and I will let you know after the review of initial four monthly data that if we require an extension of the monitoring.","nr_internal_note": null,"tenanted_arch": null,"exam_frequency": "0y 1m 0d","due_date_earliest": null,"due_dt": "2020-04-15","due_date_latest": null,"max_tolerance_date": null,"task_list_stat": "Agreed","exam_req_stat": "Scheduled", "exam_rpt_stat": null, "exam_planned_date": "2020-04-15", "exam_actual_date": "2020-06-21","other_supplier_comment": null,"change_req_id": null}],"detail": "Data updated successfully"}'
        http_response = func.HttpResponse(status_code=201,body=mocked_value)
        mocked.return_value.save_task_list_status.return_value = http_response
        http_request = func.HttpRequest(
            method='POST',
            body=mocked_dates.encode('utf8'),
            url='/postTaskListStatus',
            params={'userKey': 'A22AF4A1-611E-4C65-B018-287A3B81F873','roleName':'Super User'}
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 201)

    @patch('postTaskListStatus.TaskListStatus')
    def test_init_return_bad_request(self, mocked):

        mocked_dates ='[{"exam_sr_key": "6","task_list_id": "20","task_list_stat": "1596"}]'
        mocked_value = '{"error": {"types": "Invalid Request","title": "Header/Param validation failure","status": 400,"detail": "userkey or roleName query parameter is missing.","instance": "TaskListStatus"}'
        http_response = func.HttpResponse(status_code=400,body=mocked_value)
        mocked.return_value.save_task_list_status.return_value = http_response
        http_request = func.HttpRequest(
            method='POST',
            body=mocked_dates.encode('utf8'),
            url='/postTaskListStatus'
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 400)
    
    @patch('postTaskListStatus.TaskListStatus')
    def test_init_return_bad_request_invalid_schema(self, mocked):

        mocked_dates ='[{"exam_sr_key": "test","task_list_id": "test","task_list_stat": "test"}]'
        mocked_value = '{"error": {"types": "Invalid Request","title": "Header/Param validation failure","status": 400,"detail": "","instance": "TaskListStatus"}'
        http_response = func.HttpResponse(status_code=400,body=mocked_value)
        mocked.return_value.save_task_list_status.return_value = http_response
        http_request = func.HttpRequest(
            method='POST',
            body=mocked_dates.encode('utf8'),
            url='/postTaskListStatus',
            params={'userKey': 'A22AF4A1-611E-4C65-B018-287A3B81F873','roleName':'CEFA PM'}
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 400)
    
    @patch('postTaskListStatus.TaskListStatus')
    def test_init_return_bad_request_invalid_json(self, mocked):

        mocked_dates ='Test'
        mocked_value = '{"error": {"types": "Invalid Request","title": "Header/Param validation failure","status": 400,"detail": "","instance": "TaskListStatus"}'
        http_response = func.HttpResponse(status_code=400,body=mocked_value)
        mocked.return_value.save_task_list_status.return_value = http_response
        http_request = func.HttpRequest(
            method='POST',
            body=mocked_dates.encode('utf8'),
            url='/postTaskListStatus',
            params={'userKey': 'A22AF4A1-611E-4C65-B018-287A3B81F873','roleName':'CEFA PM'}
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 400)
        
    @patch('postTaskListStatus.TaskListStatus')
    def test_init_return_internal_server_error(self, mocked):

        mocked_dates ='[{"exam_sr_key": "6","task_list_id": "20","task_list_stat": "1596"}]'
        mocked_value = '{"error": {"types": "Invalid Request","title": "Header/Param validation failure","status": 400,"detail": "User does not have permission to save/submit for next level","instance": "TaskListStatus"}'
        http_response = func.HttpResponse(status_code=500,body=mocked_value)
        mocked.return_value.save_task_list_status.return_value = http_response
        http_request = func.HttpRequest(
            method='POST',
            body=mocked_dates.encode('utf8'),
            url='/postTaskListStatus',
            params={'userKey': 'A22AF4A1-611E-4C65-B018-287A3B81F873','roleName':'Test'}
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 500)
  
   

