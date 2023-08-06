#test_get_task_list_assets_init.py

import sys
import os
import unittest
from unittest.mock import patch
from unittest import IsolatedAsyncioTestCase
import azure.functions as func
from tests.load_environment_variables import EnvironmentVariable
EnvironmentVariable()
from getTaskListAssets import main

class TaskListAssetsSearchInitTest(unittest.TestCase):
    
    @patch('getTaskListAssets.businesslogic.get_task_list_assets.TaskListAssets')
    async def test_task_list_assets_init_return_ok_n(self, mocked):
        mocked_value = b'{"searchdatacount": {"currentpage": 1,"totalcount": 1,"totalpages": 1},"tasklistkeys": [{"exam_sr_key": "2040","task_list_id": "174","task_list_stat": "1596"}],"searchresult": [{"asset_guid": "3978559C3CDB45D9E04400306E4AD01A","region": "Southern","route": "Kent","area": "Orpington","elr": "VIR","start_mileage": "11.005681","end_mileage": "11.005681","railway_id": "70A","asset_desc": "WENDOVER ROAD FOOTBRIDGE","asset_grp": "Bridge","asset_type": "Footbridge","hce_flg": "No","exam_id": "12194673","exam_frequency": "1y 0m 0d","exam_req_stat": "In Progress","exam_rpt_stat": "Received","exam_type": "Visual","compliance_dt": null,"supplier": "Amey Rail","due_dt": "2020-05-27","onsite_pre_compl_tol_dt": null,"onsite_post_compl_tol_dt": null,"baseline_plan_dt": "2020-05-27","plan_dt": "2020-05-27","exam_dt": "2020-05-13","submission_dt": "2020-05-29","signed_off_dt": null,"cr_id": null,"specific_exam_req": null,"tenanted_arch": null,"task_list_stat": "Issued","nr_internal_note": null,"comments_to_sec": null,"other_pplier_comment": null,"posession_critical": null,"job_number": null,"bcmi_required": null,"due_dt_earliest": null,"due_dt_latest": null,"max_tolerance_dt": null,"task_list_id": "174"}]}'
        mocked.return_value.get_task_list_assets.return_value = mocked_value, 200
        http_request = func.HttpRequest(
            method='GET',
            body='',
            url='', 
            params= {'isSupplierSearch:N'},
            headers= {'X-TaskList-Filters': '{"region_name":"Southern","route_id":9,"area_id":3,"supplier_id":0,"exam_type_id":1,"exam_status_id":0,"elr_id":0,"start_mileage_from":10.000000,"start_mileage_to":99999,"railway_id":null,"ast_grp_id":0,"ast_typ_id":[0],"exam_id":12194673,"task_list_stat_id":0,"compliance_date_from":"1/1/1900","compliance_date_to":"31/12/9999","tasklist_yr_id":1294,"due_date_from":"1/1/1900","due_date_to":"31/12/9999","is_export_to_doc":"N","sort_column":"StartMileage","sort_order":"asc","page_no":1,"rows_per_page":25}'}
        )

        response = await main(http_request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_body(),
            b'{"searchdatacount": {"currentpage": 1,"totalcount": 1,"totalpages": 1},"tasklistkeys": [{"exam_sr_key": "2040","task_list_id": "174","task_list_stat": "1596"}],"searchresult": [{"asset_guid": "3978559C3CDB45D9E04400306E4AD01A","region": "Southern","route": "Kent","area": "Orpington","elr": "VIR","start_mileage": "11.005681","end_mileage": "11.005681","railway_id": "70A","asset_desc": "WENDOVER ROAD FOOTBRIDGE","asset_grp": "Bridge","asset_type": "Footbridge","hce_flg": "No","exam_id": "12194673","exam_frequency": "1y 0m 0d","exam_req_stat": "In Progress","exam_rpt_stat": "Received","exam_type": "Visual","compliance_dt": null,"supplier": "Amey Rail","due_dt": "2020-05-27","onsite_pre_compl_tol_dt": null,"onsite_post_compl_tol_dt": null,"baseline_plan_dt": "2020-05-27","plan_dt": "2020-05-27","exam_dt": "2020-05-13","submission_dt": "2020-05-29","signed_off_dt": null,"cr_id": null,"specific_exam_req": null,"tenanted_arch": null,"task_list_stat": "Issued","nr_internal_note": null,"comments_to_sec": null,"other_pplier_comment": null,"posession_critical": null,"job_number": null,"bcmi_required": null,"due_dt_earliest": null,"due_dt_latest": null,"max_tolerance_dt": null,"task_list_id": "174"}]}'
        )


    @patch('getTaskListAssets.businesslogic.get_task_list_assets.TaskListAssets')
    async def test_task_list_assets_init_return_ok_y(self, mocked):
        mocked_value = b'{"searchdatacount": {"currentpage": 1,"totalcount": 2,"totalpages": 1},"tasklistkeys": [{"exam_sr_key": "123759","task_list_id": "0","task_list_stat": "281"},{"exam_sr_key": "123760","task_list_id": "1","task_list_stat": "281"}],"searchresult": [{"asset_guid": "3978559C30E245D9E04400306E4AD01A","region": "Southern","route": "Kent","area": "London Bridge","elr": "XTD","start_mileage": "0.575568","end_mileage": "0.575568","railway_id": "14A","asset_desc": "BUCKLEY STREET/FRANCIS STREET (S)","asset_grp": "Bridge","asset_type": "Underline Bridge","hce_flg": "Yes","exam_id": "13247762","exam_frequency": "1y 0m 0d","exam_req_stat": "Planned","exam_rpt_stat": null,"exam_type": "Visual","compliance_dt": null,"supplier": "Amey Rail","due_dt": "2021-02-03","onsite_pre_compl_tol_dt": null,"onsite_post_compl_tol_dt": null,"baseline_plan_dt": null,"plan_dt": null,"exam_dt": null,"submission_dt": null,"signed_off_dt": null,"cr_id": null,"specific_exam_req": null,"tenanted_arch": null,"task_list_stat": "Ready for CEFA PM Riew","nr_internal_note": null,"comments_to_sec": null,"other_supplier_comment": null,"posession_critical": null,"job_number": null,"bcmi_required": null,"due_dt_earliest": null,"due_dt_latest": null,"max_tolerance_dt": null,"task_list_id": "0"},{"asset_guid": "3978559C380845D9E04400306E4AD01A","region": "Southern","route": "Kent","area": "London Bridge","elr": "BTH1","start_mileage": "3.137500","end_mileage": "3.137500","railway_id": "1184","asset_desc": "CONSORT ROAD","asset_grp": "Bridge","asset_type": "Underline Bridge","hce_flg": "No","exam_id": "13247763","exam_frequency": "1y 0m 0d","exam_req_stat": "Planned","exam_rpt_stat": null,"exam_type": "Visual","compliance_dt": null,"supplier": "Amey Rail","due_dt": "2021-02-03","onsite_pre_compl_tol_dt": null,"onsite_post_compl_tol_dt": null,"baseline_plan_dt": null,"plan_dt": null,"exam_dt": null,"submission_dt": null,"signed_off_dt": null,"cr_id": null,"specific_exam_req": null,"tenanted_arch": null,"task_list_stat": "Ready for CEFA PM Review","nr_internal_noe": null,"comments_to_sec": null,"other_supplier_comment": null,"posession_critical": null,"job_number": null,"bcmi_required": null,"due_dt_earliest": null,"due_dt_latest": null,"max_tolerance_dt": null,"task_list_id": "1"}]}'
        mocked.return_value.get_task_list_assets.return_value = mocked_value, 200
        http_request = func.HttpRequest(
            method='GET',
            body='',
            url='', 
            params= {'isSupplierSearch:Y'},
            headers= {'X-TaskList-Filters': '{"region_name":"Southern","route_id":9,"area_id":2,"supplier_id":4,"exam_type_id":1,"exam_status_id":0, "elr_id":1076,"start_mileage_from":5.5,"start_mileage_to":99999,"railway_id":null,"ast_grp_id":0,"ast_typ_id":[0], "exam_id":0,"task_list_stat_id":0,"compliance_date_from":"1/1/1900","compliance_date_to":"31/12/9999", "tasklist_yr_id":1294,"due_date_from":"1/1/1999","due_date_to":"31/12/1988", "is_export_to_doc":"N", "sort_column":"StartMileage","sort_order":"asc","page_no":1,"rows_per_page":10}'}
        )

        response = await main(http_request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.get_body(),
            b'{"searchdatacount": {"currentpage": 1,"totalcount": 2,"totalpages": 1},"tasklistkeys": [{"exam_sr_key": "123759","task_list_id": "0","task_list_stat": "281"},{"exam_sr_key": "123760","task_list_id": "1","task_list_stat": "281"}],"searchresult": [{"asset_guid": "3978559C30E245D9E04400306E4AD01A","region": "Southern","route": "Kent","area": "London Bridge","elr": "XTD","start_mileage": "0.575568","end_mileage": "0.575568","railway_id": "14A","asset_desc": "BUCKLEY STREET/FRANCIS STREET (S)","asset_grp": "Bridge","asset_type": "Underline Bridge","hce_flg": "Yes","exam_id": "13247762","exam_frequency": "1y 0m 0d","exam_req_stat": "Planned","exam_rpt_stat": null,"exam_type": "Visual","compliance_dt": null,"supplier": "Amey Rail","due_dt": "2021-02-03","onsite_pre_compl_tol_dt": null,"onsite_post_compl_tol_dt": null,"baseline_plan_dt": null,"plan_dt": null,"exam_dt": null,"submission_dt": null,"signed_off_dt": null,"cr_id": null,"specific_exam_req": null,"tenanted_arch": null,"task_list_stat": "Ready for CEFA PM Riew","nr_internal_note": null,"comments_to_sec": null,"other_supplier_comment": null,"posession_critical": null,"job_number": null,"bcmi_required": null,"due_dt_earliest": null,"due_dt_latest": null,"max_tolerance_dt": null,"task_list_id": "0"},{"asset_guid": "3978559C380845D9E04400306E4AD01A","region": "Southern","route": "Kent","area": "London Bridge","elr": "BTH1","start_mileage": "3.137500","end_mileage": "3.137500","railway_id": "1184","asset_desc": "CONSORT ROAD","asset_grp": "Bridge","asset_type": "Underline Bridge","hce_flg": "No","exam_id": "13247763","exam_frequency": "1y 0m 0d","exam_req_stat": "Planned","exam_rpt_stat": null,"exam_type": "Visual","compliance_dt": null,"supplier": "Amey Rail","due_dt": "2021-02-03","onsite_pre_compl_tol_dt": null,"onsite_post_compl_tol_dt": null,"baseline_plan_dt": null,"plan_dt": null,"exam_dt": null,"submission_dt": null,"signed_off_dt": null,"cr_id": null,"specific_exam_req": null,"tenanted_arch": null,"task_list_stat": "Ready for CEFA PM Review","nr_internal_noe": null,"comments_to_sec": null,"other_supplier_comment": null,"posession_critical": null,"job_number": null,"bcmi_required": null,"due_dt_earliest": null,"due_dt_latest": null,"max_tolerance_dt": null,"task_list_id": "1"}]}'
        )

    async def test_task_list_bad_request_without_header(self):
        http_request = func.HttpRequest(
            method='GET',
            body=None,
            url='/getTaskListAssets', 
            headers= {}
        )

        response = await main(http_request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.get_body(),
            b'{"error": {"types": "Invalid Request", "title": "Header/Param validation failure", "status": [400, "Bad Request"], "detail": "Bad Request", "instance": "TaskListAssets"}}'
        ) 

    async def test_task_list_bad_request_invalid_header(self):
        http_request = func.HttpRequest(
            method='GET',
            body=None,
            url='/getTaskListAssets', 
            headers= {'X-TaskList-Filters': ""}
        )

        response = await main(http_request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(
            response.get_body(),
             b'{"error": {"types": "Invalid Request", "title": "Header/Param validation failure", "status": [400, "Bad Request"], "detail": "Bad Request", "instance": "TaskListAssets"}}'
        ) 

    async def test_task_list_bad_request_invalid_input(self):
        http_request = func.HttpRequest(
            method='GET',
            body=None,
            url='/getTaskListAssets', 
            headers= {'X-TaskList-Filters': '{"region_name":"Southern","route_id":0,"area_id":2,"supplier_id":0,"exam_type_id":1,"exam_status_id":1,"elr_id":9,"start_mileage_from":5,"start_mileage_to":4999,"railway_id":null,"ast_grp_id":0,"ast_typ_id":[0],"exam_id":0,"task_list_stat_id":0,"compliance_date_from":"1/1/1900","compliance_date_to":"31/12/9999","tasklist_yr_id":1294,"due_date_from":"1/1/1900","due_date_to":"31/12/9999","isexporttodoc":"N","sortcolumn":"StartMileage","sortorder":"asc","pageno":1,"rowsperpage":25}'}
        )

        response =await main(http_request)
        self.assertEqual(response.status_code, 400)
    
        
