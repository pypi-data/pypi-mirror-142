# job_number_details.py

import sys
import os
from common import SqlOperation, Logger, JsonHelper,CustomLog, AppStatus, SharedConstants,ErrorResponse
from datetime import datetime, timezone
from ..constants.job_number_constants import JobNumberConstants
from jobNumber.business_logic.job_numbers_validate_request import ValidateRequest
import traceback
import json

istraceenabled = os.environ[SharedConstants.trace_enabled]

class JobNumberDetails:
  
    """ JobNumberDetails class to get and post task list job numbers information """ 

    def __init__(self):
        self.response = str({})
        self.statusCode = AppStatus.ok.value[0]
        self.properties = {JobNumberConstants.job_number_func : JobNumberConstants.job_number_func_val}
        self.properties[CustomLog.start_time] = datetime.now(timezone.utc).isoformat()
        self.properties[CustomLog.status] = True
        Logger.__init__( self,name = self.__class__.__name__, start_time = datetime.now(timezone.utc))
        self.json_helper = JsonHelper()
        self.validation = ValidateRequest()
        
    def get_job_number_info(self, exam_key:str):
        """
        Function to call Ces database to get task list job numbers information.
       
        Args:
            exam_key (str)

        Returns:
            json(str) 
            statuscode(int)     - 204 No Content
                                - 200 Success
                                - 400 Bad Request
                                - 500 Internal Server Error 
                                
        """
        try:
            self.properties[CustomLog.sp_req_param] = JobNumberConstants.exam_key_param + SharedConstants.colon + exam_key
            self.properties[CustomLog.sprequest_time] = datetime.now(timezone.utc).isoformat()
            job_number = SqlOperation().fetch_one(JobNumberConstants.get_sql_query, exam_key)
            self.properties[CustomLog.sprequestend_time] = datetime.now(timezone.utc).isoformat()
            if job_number is not None:
                is_valid_response,json_obj = self.json_helper.parse_json(job_number[0])
                if is_valid_response:
                    self.response = job_number[0]
                else:
                    self.statusCode = AppStatus.no_content.value[0]  
            else:
                self.statusCode = AppStatus.no_content.value[0]

        except:
            self.properties[CustomLog.error_messsage] = str(traceback.format_exc())
            self.properties[CustomLog.status] = False
            self.statusCode = AppStatus.internal_server_error.value[0]
            self.response = ErrorResponse(str(sys.exc_info()[0]), JobNumberDetails.__name__,AppStatus.internal_server_error.value[0], str(sys.exc_info()),JobNumberDetails.__name__).__str__()
            Logger.exception(self,type= sys.exc_info()[0], value = sys.exc_info()[1], tb =sys.exc_info()[2], properties = self.properties )
        
        finally:
            if istraceenabled:
                self.properties[CustomLog.end_time] = datetime.now(timezone.utc).isoformat()
                Logger.request(self,properties= self.properties)
            return self.response, self.statusCode 

    def post_job_number_info(self, job_number_details_json):

        """
        Function to call Ces database to setjob number information json.
       
        Args:
        Returns:
            json(str) 
            statuscode(int)     - 204 No Content
                                - 201 Created
                                - 500 Internal Server Error 
                                - 400 Bad Request
        """
        try:
            is_valid,res = self.validation.is_valid_payload(json.dumps(job_number_details_json))
            if(is_valid):
                req_param = self.json_helper.stringify_json(res)[1]
                self.properties[CustomLog.sp_req_param] = JobNumberConstants.input_json + SharedConstants.colon + req_param
                self.properties[CustomLog.sprequest_time] = datetime.now(timezone.utc).isoformat()
                _json_string = SqlOperation().fetch_one(JobNumberConstants.post_sql_query,req_param)
                self.properties[CustomLog.sprequestend_time] = datetime.now(timezone.utc).isoformat()
                if _json_string is not None:
                    is_valid_response,json_obj = self.json_helper.parse_json(_json_string[0])
                    if is_valid_response:
                        self.statusCode = AppStatus.record_created.value[0]
                        self.response = _json_string[0]
                        if json.loads(self.response)['save_status'] == 0:
                            self.statusCode = 200
                    else:
                        self.statusCode = AppStatus.no_content.value[0]
                else:
                    self.statusCode = AppStatus.no_content.value[0]
            else:
                self.response = ErrorResponse(SharedConstants.request_val_failure, SharedConstants.request_header_failure, AppStatus.bad_Request.value[0], str(res), self.__class__.__name__).__str__()
                self.statusCode = AppStatus.bad_Request.value[0]
                self.properties[CustomLog.error_messsage] =  str(res)    
        except:
            self.properties[CustomLog.error_messsage] =   str(traceback.format_exc())
            self.properties[CustomLog.status] = False
            self.statusCode = AppStatus.internal_server_error.value[0]
            self.response = ErrorResponse(str(sys.exc_info()[0]), JobNumberDetails.__name__,AppStatus.internal_server_error.value[0], str(sys.exc_info()),JobNumberDetails.__name__).__str__()
            Logger.exception(self,type= sys.exc_info()[0], value = sys.exc_info()[1], tb =sys.exc_info()[2], properties = self.properties )
        finally:
            if istraceenabled:
                self.properties[CustomLog.end_time] = datetime.now(timezone.utc).isoformat()
                Logger.request(self,properties= self.properties)
            return self.response, self.statusCode