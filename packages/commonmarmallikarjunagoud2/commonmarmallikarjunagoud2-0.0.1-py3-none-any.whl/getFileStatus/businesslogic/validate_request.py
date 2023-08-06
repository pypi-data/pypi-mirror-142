#validate_request.py
import sys
import os
import json

#validate_request.py

__all__ = ['ValidateRequest']
class ValidateRequest:

    def __init__(self, file_status_schema):
        self.file_status_schema = file_status_schema

    def is_valid_payload(self, payload)-> (bool, dict):
        try: 
            return True, self.file_status_schema.dump(self.file_status_schema.loads(payload))
        except:
            return False, sys.exc_info()[1]

        



