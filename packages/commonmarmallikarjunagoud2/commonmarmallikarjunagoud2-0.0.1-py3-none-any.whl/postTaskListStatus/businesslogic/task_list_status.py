#task_list_status.py

import sys
import os
import logging
import azure.functions as func
from common import SqlOperation, Logger, JsonHelper,ValidationHelper,CustomLog, AppStatus, SharedConstants,ErrorResponse,SuccessResponse,SetProperties
from datetime import datetime, timezone
from .validate_request import ValidateRequest
from ..constants import TaskListStatusConstants,TaskSuccessResponse
from ..schema import TaskRequestSchema
import traceback
from datetime import date 
import json
istraceenabled = os.environ[SharedConstants.trace_enabled]


class TaskListStatus(SetProperties):
    """ TaskListStatus class to update the task list status  """
    def __init__(self):
        
        self.sql_query = """
                           EXEC [CES].[sp_Save_TasklistStatus]
                           @Input_JSON = ?, @Role_Name = ?, @User_Key = ?
                           """
        self.response = str({})
        self.status_code = AppStatus.ok.value[0]
        SetProperties.__init__(self,CustomLog.task_list_status,CustomLog.task_list_status_val)
        Logger.__init__( self,name = TaskListStatus.__name__, start_time = datetime.now(timezone.utc))

        self.json_helper = JsonHelper()
        self.supplier_response='null'
        self.pdf_response='null'
    
    def save_task_list_status(self,req: func.HttpRequest)-> func.HttpResponse:
        """
        Function to call Ces database to update the task status
       
        Args:
            self ([TaskListStatus]): [self instance]
            req: Http Request data (Json Data)
        Returns:
            HttpResponse
            statuscode(int)     - 201 Created
                                - 500 Internal Server Error
                                - 400 BadRequest 
        """
        try:
            user_key = req.params.get(TaskListStatusConstants.user_key)
            role_name = req.params.get(TaskListStatusConstants.role_name)
            if user_key is not None and role_name is not None:
                self.task_status_req = req.get_json()
                is_valid_payload, return_object =  ValidateRequest(TaskRequestSchema()).is_valid_payload(self.task_status_req)
                if is_valid_payload:
                    task_status_req_json = self.json_helper.stringify_json(self.task_status_req)[1]
                    sp_req_params = TaskListStatusConstants.sp_input_json + SharedConstants.colon + task_status_req_json + SharedConstants.comma + TaskListStatusConstants.user_key + SharedConstants.colon + str(user_key) + SharedConstants.comma + TaskListStatusConstants.role_name + SharedConstants.colon + str(role_name)
                    sp_param = task_status_req_json, role_name, user_key
                    SetProperties.sprequest_params(self,sp_req_params)
                    SetProperties.sprequest_time(self)
                    json_string = SqlOperation().fetch_one(self.sql_query,sp_param) 
                    SetProperties.sprequestend_time(self)
                    status,message,*args = json_string
                    if status:
                        supplierjson_sucess, supplier_json_obj = self.json_helper.parse_json(args[0] if args[0] else None)
                        if supplierjson_sucess:
                            if len(supplier_json_obj) > 0: self.supplier_response = supplier_json_obj
                        
                        pdfjson_sucess, pdf_json_obj = self.json_helper.parse_json(args[1] if args[1] else None)
                        if pdfjson_sucess:
                            if len(pdf_json_obj) > 0: self.pdf_response = pdf_json_obj
                        self.status_code = AppStatus.record_created.value[0]
                        self.response =   TaskSuccessResponse(self.status_code,self.supplier_response,self.pdf_response,TaskListStatusConstants.update_task_success_msg).__str__() 
                        
                        response = func.HttpResponse(body= self.response, status_code= self.status_code, mimetype= SharedConstants.json_mime_type)  
                    else:
                        self.status_code = AppStatus.internal_server_error.value[0]
                        self.response = ErrorResponse(SharedConstants.request_val_failure,SharedConstants.request_header_failure,self.status_code, str(message),TaskListStatus.__name__).__str__()
                        response = func.HttpResponse(body= self.response, status_code= self.status_code, mimetype= SharedConstants.json_mime_type)  
                else:
                    self.status_code = AppStatus.bad_Request.value[0]
                    self.response = ErrorResponse(SharedConstants.request_val_failure,SharedConstants.request_header_failure,self.status_code, str(return_object),TaskListStatus.__name__).__str__()
                    response = func.HttpResponse(body= self.response, status_code= self.status_code, mimetype= SharedConstants.json_mime_type)   
            else:
                self.status_code = AppStatus.bad_Request.value[0]
                self.response = ErrorResponse(SharedConstants.request_val_failure, SharedConstants.request_header_failure, self.status_code, TaskListStatusConstants.param_failure, TaskListStatus.__name__).__str__()
                response = func.HttpResponse(body= self.response, status_code= self.status_code, mimetype= SharedConstants.json_mime_type) 
        except:
            SetProperties.error_messsage(self,str(traceback.format_exc()))
            SetProperties.status(self, False)
            Logger.exception(self,type= sys.exc_info()[0], value = sys.exc_info()[1], tb =sys.exc_info()[2], properties = self._properties )
            self.status_code = AppStatus.internal_server_error.value[0]
            error_response = ErrorResponse(SharedConstants.request_val_failure,TaskListStatus.__name__,self.status_code, str(sys.exc_info()[1]),TaskListStatus.__name__,).__str__()
            response = func.HttpResponse(body= error_response, status_code= self.status_code, mimetype= SharedConstants.json_mime_type)
        finally:
            if istraceenabled:
                SetProperties.end_time(self)
                Logger.request(self,properties= self._properties)
            return response 