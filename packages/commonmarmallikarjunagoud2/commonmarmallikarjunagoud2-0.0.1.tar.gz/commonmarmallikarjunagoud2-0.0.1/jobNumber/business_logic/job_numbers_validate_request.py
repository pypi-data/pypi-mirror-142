# job_numbers_validate_request.py

import sys
from ..schema import JobNumberSchema

class ValidateRequest:

    """ ValidateRequest class to validate the request json """ 
    def __init__(self):
        self.job_number_schema = JobNumberSchema()

    def is_valid_payload(self, payload):
        """
        Method to validate the request against schema

        Args:
            payload(json)

        Returns:
            bool:represents validation is successful or not | dict:validated json response 
        """
        try:
            return True, self.job_number_schema.dump(self.job_number_schema.loads(payload))
        except:
            return False, sys.exc_info()