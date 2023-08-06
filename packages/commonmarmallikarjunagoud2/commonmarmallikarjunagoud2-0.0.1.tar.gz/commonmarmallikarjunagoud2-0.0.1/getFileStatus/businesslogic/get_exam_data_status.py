#get_exam_data_status.py

import sys
import os
import logging
import azure.functions as func
from common import SqlOperation, Logger, JsonHelper,CustomLog, AppStatus, SharedConstants,ErrorResponse,SetProperties,SuccessResponse
from datetime import datetime, timezone
from ..constants import ExamDataConstants
from ..schema.file_status_schema import FileStatusSearchSchema
import traceback
from .validate_request import ValidateRequest
import json
istraceenabled = os.environ[SharedConstants.trace_enabled]

class ExamDataStatus(SetProperties):
    def __init__(self):
        self.sql_query = """
                           EXEC [CES].[sp_Get_FileUploadStatus_SearchResult]
                           @Input_JSON = ?
                           """
        self.response = str({})
        self.status_code = AppStatus.ok.value[0]
        self.properties = {ExamDataConstants.get_file_status:ExamDataConstants.get_file_status_val}
        self.properties[CustomLog.start_time] = datetime.now(timezone.utc).isoformat()
        Logger.__init__( self,name = ExamDataStatus.__name__, start_time = datetime.now(timezone.utc))
        self.properties[CustomLog.status] = True
        self.json_helper = JsonHelper()
    
    def exam_data_status(self, file_status_search_req)-> func.HttpResponse:
        """
        Function to call Ces database to get the exam data status
       
        Args:
            self ([ExamDataStatus]): [self instance]
            req: Http Request data (params Data)
        Returns:
            HttpResponse
            status_code(int)    - 200 Success
                                - 500 Internal Server Error
                                - 400 BadRequest 
                                - 204 No Content
        """
        try:
            is_valid_payload, return_object =  ValidateRequest(FileStatusSearchSchema()).is_valid_payload(file_status_search_req)
            if is_valid_payload:
                req_param = self.json_helper.stringify_json(return_object)[1]
                self.properties[CustomLog.sp_req_param] = req_param
                self.properties[CustomLog.sprequest_time] = datetime.now(timezone.utc).isoformat()
                json_string = SqlOperation().fetch_one(self.sql_query,req_param)
                self.properties[CustomLog.sprequestend_time] = datetime.now(timezone.utc).isoformat()
                if json_string is not None:
                    is_valid_response,json_obj = self.json_helper.parse_json(json_string[0])
                    if is_valid_response:
                        self.response = json_string[0]
                    else:
                        self.statusCode = AppStatus.no_content.value[0]
                else:
                    self.statusCode = AppStatus.no_content.value[0]
            else:
                self.status_code = AppStatus.bad_Request.value[0]
                self.response = ErrorResponse(SharedConstants.request_val_failure, SharedConstants.request_header_failure,self.status_code,str(return_object.messages),ExamDataStatus.__name__).__str__() 
        except:
            self.properties[CustomLog.error_messsage] =   str(traceback.format_exc())
            self.properties[CustomLog.status] = False
            self.status_code = AppStatus.internal_server_error.value[0]
            Logger.exception(self,type= sys.exc_info()[0], value = sys.exc_info()[1], tb =sys.exc_info()[2], properties = self._properties )
            self.response = ErrorResponse(sys.exc_info()[0],ExamDataStatus.__name__,self.status_code, str(sys.exc_info()[1]),ExamDataStatus.__name__).__str__()
        finally:
            if istraceenabled:
                self.properties[CustomLog.end_time] = datetime.now(timezone.utc).isoformat()  
                Logger.request(self,properties= self.properties)
            return  self.response, self.status_code