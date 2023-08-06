# test_job_number_init.py

import unittest
from unittest.mock import patch
import azure.functions as func
from tests.load_environment_variables import EnvironmentVariable
EnvironmentVariable()
from jobNumber import main

class JobNumberInitTest(unittest.TestCase):

    @patch('jobNumber.JobNumberDetails')
    def test_init_get_return_ok(self, mocked):
        get_job_number_details ='{"jobnumber":"B-2122-2758","exam_id":3187521,"error_msg":null}'
        mocked.return_value.get_job_number_info.return_value = get_job_number_details, 200
        http_request = func.HttpRequest(
            method='GET',
            body='',
            url = '',
            params={'examKey': '2'}
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_body(),
            b'{"jobnumber":"B-2122-2758","exam_id":3187521,"error_msg":null}'
        )

    @patch('jobNumber.JobNumberDetails')
    def test_init_post_return_created(self, mocked):

        save_job_number_details ='{"examkey":2,"jobnumber":"B-2122-372;63ANG5788","current_user_key":"9725949A-1EB7-497E-B397-A511422AFAFE"}'
        mocked.return_value.post_job_number_info.return_value = '{"save_status":1,"error_msg":null}', 201
        http_request = func.HttpRequest(
            method='POST',
            body=save_job_number_details.encode('utf8'),
            url='/jobNumber', 
            params=''
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.get_body(),
            b'{"save_status":1,"error_msg":null}',
        )

    @patch('jobNumber.JobNumberDetails')
    def test_init_post_return_bad_request(self, mocked):
        mocked.return_value.get_job_number_info.return_value = '', 400
        http_request = func.HttpRequest(
            method='GET',
            body='',
            url='/jobNumber', 
            params={'examKey':''}
        )

        response = main(http_request)
        self.assertEqual(response.status_code, 400)

    @patch('jobNumber.JobNumberDetails')
    def test_init_post_return_internal_server(self, mocked):
        mocked.return_value.post_job_number_info.return_value = '', 500
        http_request = func.HttpRequest(
            method='POST',
            body='',
            url='/jobNumber', 
            params=''
        )

        response = main(http_request)

        self.assertEqual(response.status_code, 500)