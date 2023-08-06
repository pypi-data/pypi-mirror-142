#get_task_list_assets.py

"""Business Logic class"""
import sys
import os
from common import Logger
import json
from common.utilities.json_helper import JsonHelper 
from common.validate.validation_helper import ValidationHelper
from datetime import datetime, timezone
from common import CustomLog, AppStatus, SharedConstants,ErrorResponse, SqlOperation
from ..constants.get_task_list_assets import GetTaskListAssetsConstants
from getTaskListAssets.model.task_list_assets_filter_req import TaskListFilterRequest

FunctionApp = GetTaskListAssetsConstants.task_list_assets_function
Schema = SharedConstants.schema
JsonSchemaFile = GetTaskListAssetsConstants.task_list_assets_json_schema
istraceenabled = os.environ[SharedConstants.trace_enabled]


class TaskListAssets:
    """ task list assets class to get all task list assets json response """ 

    def __init__(self):
        self.response = str({})
        self.status_code = AppStatus.ok.value[0]
        self.sql_query = """
                          EXEC [CES].[sp_Get_TaskList_SearchResult]
                          @Input_JSON = ?, @IsSupplierSearch = ?
                          """
        self.properties = {CustomLog.task_list_assets : CustomLog.task_list_assets_val}
        self.properties[CustomLog.start_time] = datetime.now(timezone.utc).isoformat()
        self.properties[CustomLog.status] = True
        Logger.__init__( self,name = TaskListAssets.__name__, start_time = datetime.now(timezone.utc))
        self.json_helper = JsonHelper()
        self.taskList_default =  TaskListFilterRequest()
        self.data_mapper = {'region_name':'region_name',
                            'route_id':'route_id',
                            'area_id':'area_id',
                            'supplier_id':'supplier_id',
                            'exam_type_id':'exam_type_id',
	                        'exam_status_id': 'exam_status_id',
	                        'elr_id':'elr_id',	
	                        'start_mileage_from': 'start_mileage_from',
	                        'start_mileage_to': 'start_mileage_to',
	                        'railway_id': 'railway_id',
	                        'ast_grp_id': 'ast_grp_id',
	                        'ast_typ_id': 'ast_typ_id',
	                        'exam_id': 'exam_id',
	                        'task_list_stat_id': 'task_list_stat_id',
	                        'compliance_date_from': 'compliance_date_from',
	                        'compliance_date_to': 'compliance_date_to',
	                        'tasklist_yr_id': 'tasklist_yr_id',
	                        'due_date_from': 'due_date_from',
	                        'due_date_to': 'due_date_to',
	                        'is_export_to_doc': 'isexporttodoc',
	                        'sort_column': 'sortcolumn',
	                        'sort_order': 'sortorder',
	                        'page_no': 'pageno',
	                        'rows_per_page': 'rowsperpage'
                        }

    def validate_json(self, req):
        with open(os.path.join(os.getcwd(),FunctionApp,Schema,JsonSchemaFile), SharedConstants.file_read_mode) as _json_file:
            schema = self.json_helper.parse_json(_json_file.read())
        is_invalid_schema, errors = ValidationHelper().validate_json(req,schema[1])
        if is_invalid_schema:
            self.status_code = AppStatus.bad_Request.value[0]
            self.response = ErrorResponse(SharedConstants.request_val_failure,SharedConstants.invalid_input_value_msg,
                                              AppStatus.bad_Request.value, self.json_helper.stringify_json(errors)[1],
                                              TaskListAssets.__name__).__str__()

    def map_dictionary(self, json_req) -> str:
        """
        Method to map the request column to the db column

        Args:
            json_req(json)

        Returns:
            json(str) 
        
        """
       
        return  self.json_helper.stringify_json(dict((self.data_mapper.get(k, k), v) for (k, v) in json_req.items()))[1] 
             
    def populate_default(self, tasklist_request):
        """
        Function to populate default value for task list assets filters
       
        Args:
            tasklist_request (json)

        Returns:
            tasklist_request_params (json)    
        """

        return {key: tasklist_request.get(key, self.taskList_default.task_list_req_default[key]) 
                         for key in self.taskList_default.task_list_req_default} if isinstance(tasklist_request, dict) else tasklist_request
       
    def get_all_task_list_assets_json(self, req, is_supplier_search_param_value):
        """
        Function to call database to get all task list assets json based on filter condition
       
        Args:
            req (str)
        """
        tasklist_filter_param = self.map_dictionary(req)
        data = json.loads(tasklist_filter_param)
        if(str(data['region_name']).replace(' ','') == str("North, West and Central").replace(' ','')):
            data['region_name']= ("North, West and Central")
            tasklist_filter_param = json.dumps(data)
            self.properties["tasklist_filter_param"] = tasklist_filter_param
        self.properties[CustomLog.sp_req_param] = CustomLog.Input_JSON + SharedConstants.colon + tasklist_filter_param + SharedConstants.comma + CustomLog.is_supplier_search_param + SharedConstants.colon + is_supplier_search_param_value
        request_params = tasklist_filter_param, is_supplier_search_param_value
        self.properties[CustomLog.sprequest_time] = datetime.now(timezone.utc).isoformat()
        response = SqlOperation().fetch_one(self.sql_query, request_params)
        self.properties[CustomLog.sprequestend_time] = datetime.now(timezone.utc).isoformat()
        is_valid_response,json_res = self.json_helper.parse_json(response[0] if response else None)
        if is_valid_response:
            self.response = response[0]
        else:   
            self.status_code = AppStatus.no_content.value[0]

    
    def get_task_list_assets(self, task_list_filter, is_supplier_search_param_value):
        """
        Function to get all task list assets json based on filter condition
       
        Args:
            task_list_filter (str)
            is_supplier_search_param_value(str)

        Returns:
            json(str) 
            statuscode(int)     - 204 No Content
                                - 200 Success
                                - 500 Internal Server Error 
                                - 400 Bad Request
        """
        try:
            is_parse_json_sucess, req = self.json_helper.parse_json(task_list_filter)
            if is_parse_json_sucess:
               req_default = self.populate_default(req)
               self.validate_json(req_default)
               self.get_all_task_list_assets_json(req_default, is_supplier_search_param_value)
            else:
               self.status_code = AppStatus.bad_Request.value[0]   
               self.response = ErrorResponse(SharedConstants.request_val_failure, TaskListAssets.__name__,
                                              AppStatus.bad_Request.value, SharedConstants.bad_json_request_msg,
                                              TaskListAssets.__name__).__str__()  
               self.properties[CustomLog.error_messsage] =  req
        except:
            self.properties[CustomLog.error_messsage] =  str(sys.exc_info())
            self.properties[CustomLog.status] = False
            self.status_code = AppStatus.internal_server_error.value[0]
            self.response = ErrorResponse(str(sys.exc_info()[0]),TaskListAssets.__name__,
                                 AppStatus.internal_server_error.value, str(sys.exc_info()),TaskListAssets.__name__).__str__()
            Logger.exception(self,type=sys.exc_info()[0], value = sys.exc_info()[1], tb =sys.exc_info()[2], properties = self.properties)
        finally:
            if istraceenabled:
                self.properties[CustomLog.end_time] = datetime.now(timezone.utc).isoformat()
                Logger.request(self,properties= self.properties)
            return self.response, self.status_code    
  