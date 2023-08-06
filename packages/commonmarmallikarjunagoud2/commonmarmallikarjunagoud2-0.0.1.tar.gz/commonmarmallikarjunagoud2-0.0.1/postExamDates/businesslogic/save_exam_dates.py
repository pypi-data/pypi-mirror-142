#save_exam_dates.py

import sys
import os
import logging
import pandas as pd
import numpy as np
import azure.functions as func
from common import SqlOperation, Logger, JsonHelper,ValidationHelper,CustomLog, AppStatus, SharedConstants,ErrorResponse,SuccessResponse,SetProperties
from datetime import datetime, timezone
from .validate_request import ValidateRequest
from ..constants.save_exam_dates_constants import SaveExamDatesConstants
from ..schema import ExamDatesRequestSchema
import traceback
from datetime import date 
import json
istraceenabled = os.environ[SharedConstants.trace_enabled]


class SaveExamDates(SetProperties):
    """ SaveExamDates class to  update the planned exam dates"""
    def __init__(self):
        
        self.sql_query = """
                           EXEC [CES].[sp_Save_Tasklist_ExamDts_UI]
                           @Input_JSON = ?, @UserKey = ?
                           """
        self.response = str({})
        self.status_code = AppStatus.ok.value[0]
        SetProperties.__init__(self,CustomLog.save_exam_dates,CustomLog.save_exam_dates_val)
        Logger.__init__( self,name = SaveExamDates.__name__, start_time = datetime.now(timezone.utc))
        self.json_helper = JsonHelper()
    
    
    
    def save_exam_date(self,req: func.HttpRequest)-> func.HttpResponse:
        """
        Function to call Ces database to update the planned exam dates
       
        Args:
            self ([SaveExamDates]): [self instance]
            req: Http Request data (Json data)
        Returns:
            HttpResponse
            statuscode(int)     - 201 Created
                                - 500 Internal Server Error
                                - 400 BadRequest 
        """
        try:
            self.exam_date_req = req.get_json()
            user_key = req.params.get(SaveExamDatesConstants.user_key)
            if user_key is not None:
                is_valid_payload, return_object =  ValidateRequest(ExamDatesRequestSchema()).is_valid_payload(self.exam_date_req)
                if is_valid_payload:
                    self.exam_date_json = self.json_helper.stringify_json(return_object[SaveExamDatesConstants.exam_data])
                    sp_param = self.exam_date_json[1], user_key
                    sp_req_params = SaveExamDatesConstants.sp_input_json + SharedConstants.colon + self.exam_date_json[1] + SharedConstants.comma + SaveExamDatesConstants.user_key + SharedConstants.colon + str(user_key)
                    SetProperties.sprequest_params(self,sp_req_params)
                    SetProperties.sprequest_time(self)
                    json_string = SqlOperation().fetch_one(self.sql_query,sp_param) 
                    SetProperties.sprequestend_time(self)
                    status,message=json_string
                    if status:
                        self.status_code = AppStatus.record_created.value[0]
                        self.response =  SuccessResponse(AppStatus.record_created.value[0],
                                                SaveExamDatesConstants.update_exam_dates_success_msg).__str__()
                        response = func.HttpResponse(body= self.response, status_code= self.status_code, mimetype= SharedConstants.json_mime_type)  
                    else:
                        self.status_code = AppStatus.internal_server_error.value[0]
                        self.response = ErrorResponse(SharedConstants.request_val_failure,SharedConstants.request_header_failure,
                                                    self.status_code, str(message),
                                                    SaveExamDates.__name__).__str__()
                        response = func.HttpResponse(body= self.response, status_code= self.status_code, mimetype= SharedConstants.json_mime_type)  
                else:
                    self.status_code = AppStatus.bad_Request.value[0]
                    self.response = ErrorResponse(SharedConstants.request_val_failure,SharedConstants.request_header_failure,self.status_code, str(return_object),SaveExamDates.__name__).__str__()
                    response = func.HttpResponse(body= self.response, status_code= self.status_code, mimetype= SharedConstants.json_mime_type)    
            else:
                self.status_code = AppStatus.bad_Request.value[0]
                self.response = ErrorResponse(SharedConstants.request_val_failure,SharedConstants.request_header_failure,self.status_code, SaveExamDatesConstants.invalid_user_key,SaveExamDates.__name__).__str__()
                response = func.HttpResponse(body= self.response, status_code=self.status_code, mimetype= SharedConstants.json_mime_type)                                
        except:
            SetProperties.error_messsage(self,str(traceback.format_exc()))
            SetProperties.status(self, False)
            Logger.exception(self,type= sys.exc_info()[0], value = sys.exc_info()[1], tb =sys.exc_info()[2], properties = self._properties )
            self.status_code = AppStatus.internal_server_error.value[0]
            error_response = ErrorResponse(SharedConstants.request_val_failure,SaveExamDates.__name__,
                                              self.status_code, str(sys.exc_info()[1]),
                                              SaveExamDates.__name__,).__str__()
            response = func.HttpResponse(body= error_response, status_code= self.status_code, mimetype= SharedConstants.json_mime_type)
        finally:
            if istraceenabled:
                SetProperties.end_time(self)
                Logger.request(self,properties= self._properties)
            return response 
            
    