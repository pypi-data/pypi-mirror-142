#validate_request.py

import sys
import os
import ast
import json
import pandas as pd
import numpy as np
import azure.functions as func
from common import JsonHelper
from ..constants import TaskListStatusConstants

__all__ = [TaskListStatusConstants.validate_request]
class ValidateRequest:

    """ ValidateRequest class to validate the request json """ 
    def __init__(self, task_schema):
        self.task_schema = task_schema
        self.json_helper = JsonHelper()

    def is_valid_payload(self, http_task_req):
        """ To validate incoming request

        Args:
            self ([ValidateRequest]): [self instance]
            http_task_req: json
        Returns:
            [tuple]: [boo represent the schema validation was successful or not and error message for validation failure scenario]

        """
        try:
            return_object =  self.task_schema.loads(self.json_helper.stringify_json({TaskListStatusConstants.task_data: http_task_req})[1], partial=True)
            return True, return_object
        except:
            (excepclass, errormessage, trackback) = sys.exc_info()
            return False, errormessage
        
           
       
       

        



