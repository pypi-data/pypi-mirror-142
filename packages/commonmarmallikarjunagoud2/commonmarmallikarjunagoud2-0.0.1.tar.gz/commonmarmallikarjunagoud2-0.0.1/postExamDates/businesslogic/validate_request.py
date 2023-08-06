#validate_request.py

import sys
import os
import ast
import json
import pandas as pd
import numpy as np
import azure.functions as func
from common import JsonHelper
from ..constants import SaveExamDatesConstants

__all__ = [SaveExamDatesConstants.validate_request]
class ValidateRequest:

    """ ValidateRequest class to validate the request json """ 
    def __init__(self, exam_dates_schema):
        self.exam_dates_schema = exam_dates_schema
        self.json_helper = JsonHelper()

    def is_valid_payload(self, exam_date_req):
        """ To validate incoming request

        Args:
            self ([ValidateRequest]): [self instance]
            exam_date_req: json
        Returns:
            [tuple]: [boo represent the schema validation was successful or not and error message for validation failure scenario]

        """
        try:
            load_schema =  self.exam_dates_schema.loads(self.json_helper.stringify_json({SaveExamDatesConstants.exam_data: exam_date_req})[1])
            return_object =  self.exam_dates_schema.dump(load_schema)
            return True, return_object
        except:
            (excepclass, errormessage, trackback) = sys.exc_info()
            return False, errormessage
        
           
       
       

        



