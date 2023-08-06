#task_list_assets_filter_req.py

"""Business Logic Class"""
import sys
import os

class TaskListFilterRequest:

    """ Task list filter class to get all task list assets json response """

    def __init__(self):
        self.task_list_req_default = {
                                    "region_name": None,
                                    "route_id":0,
                                    "area_id":0,
                                    "supplier_id":0,
                                    "exam_type_id": 0,
	                                "exam_status_id": 0,
	                                "elr_id":[0],	
	                                "start_mileage_from": -1,
	                                "start_mileage_to": 99999,
	                                "railway_id": None,
	                                "ast_grp_id": 0,
	                                "ast_typ_id": [0],
	                                "exam_id": 0,
	                                "task_list_stat_id": 0,
	                                "compliance_date_from": '1/1/1900',
	                                "compliance_date_to": '31/12/9999',
	                                "tasklist_yr_id": 0,
	                                "due_date_from": '1/1/1900',
	                                "due_date_to": '31/12/9999',
                                    "is_export_to_doc":"N",
                                    "sort_column":"StartMileage",
                                    "sort_order":"asc",
                                    "page_no":1,
                                    "rows_per_page":25
        }