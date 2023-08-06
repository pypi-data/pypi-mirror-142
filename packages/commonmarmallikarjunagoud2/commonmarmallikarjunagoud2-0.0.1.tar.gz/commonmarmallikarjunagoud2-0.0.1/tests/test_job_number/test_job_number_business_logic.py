# test_job_number_business_logic.py

import unittest
from unittest.mock import patch
import azure.functions as func
from tests.load_environment_variables import EnvironmentVariable
EnvironmentVariable()
from jobNumber.business_logic.job_number_details import JobNumberDetails
import json

class JobNumberBusinessLogic(unittest.TestCase):

    @patch('jobNumber.business_logic.job_number_details.SqlOperation')
    def test_get_job_number_bl_return_ok(self,mocked):
        get_job_number_details = ['{"jobnumber":"B-2122-2758","exam_id":3187521,"error_msg":null}']
        mocked.return_value.fetch_one.return_value = get_job_number_details
        response, status_code = JobNumberDetails().get_job_number_info('2')
        self.assertEqual(status_code, 200)

    @patch('jobNumber.business_logic.job_number_details.SqlOperation')
    def test_get_job_number_bl_return_nocontent(self,mocked):
        get_job_number_details = None
        mocked.return_value.fetch_one.return_value = get_job_number_details
        response, status_code = JobNumberDetails().get_job_number_info('2')
        self.assertEqual(status_code, 204)

    @patch('jobNumber.business_logic.job_number_details.SqlOperation')
    def test_get_job_number_bl_return_nocontent_invalidjson(self,mocked):
        get_job_number_details = ['{"jobnumber":"B-2122-2758""exam_id":3187521,"error_msg":null}']
        mocked.return_value.fetch_one.return_value = get_job_number_details
        response, status_code = JobNumberDetails().get_job_number_info('2')
        self.assertEqual(status_code, 204)

    @patch('jobNumber.business_logic.job_number_details.SqlOperation')
    def test_get_job_number_bl_return_internalservererror(self,mocked):
        mocked.side_effect = ConnectionError
        response, status_code = JobNumberDetails().get_job_number_info('2')
        self.assertEqual(status_code, 500)

    @patch('jobNumber.business_logic.job_number_details.SqlOperation')
    def test_post_job_number_bl_return_created(self,mocked):
        save_job_number_details ='{"examkey":2,"jobnumber":"B-2122-372;63ANG5788","current_user_key":"9725949A-1EB7-497E-B397-A511422AFAFE"}'
        mocked.return_value.fetch_one.return_value = ['{"save_status":1,"error_msg":null}']
        response, status_code = JobNumberDetails().post_job_number_info(json.loads(save_job_number_details))
        self.assertEqual(status_code, 201)

    @patch('jobNumber.business_logic.job_number_details.SqlOperation')
    def test_post_job_number_bl_return_badrequest(self,mocked):
        save_job_number_details ='{"jobnumber":"B-2122-372;63ANG5788","current_user_key":"9725949A-1EB7-497E-B397-A511422AFAFE"}'
        mocked.return_value.fetch_one.return_value = '{"save_status":1,"error_msg":null}'
        response, status_code = JobNumberDetails().post_job_number_info(json.loads(save_job_number_details))
        self.assertEqual(status_code, 400)
    
    @patch('jobNumber.business_logic.job_number_details.SqlOperation')
    def test_post_job_number_bl_return_internal_server_error(self,mocked):
        save_job_number_details ='{"examkey":2,"jobnumber":"B-2122-372;63ANG5788","current_user_key":"9725949A-1EB7-497E-B397-A511422AFAFE"}'
        mocked.side_effect = ConnectionError
        response, status_code = JobNumberDetails().post_job_number_info(json.loads(save_job_number_details))
        self.assertEqual(status_code, 500)