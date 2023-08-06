#__init__.py

import sys
import azure.functions as func
from common import SharedConstants, ErrorResponse, AppStatus
from .constants.job_number_constants import JobNumberConstants
from .business_logic.job_number_details import JobNumberDetails
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    """[summary]

    Args:
        req (func.HttpRequest): To Get/Post task list job numbers from/to CES DB

    Returns:
        func.HttpResponse: task list job numbers json for get operation and save task list job number details to CES DB
    """
    try:
        if req.method == SharedConstants.method_type_get:
            exam_key = req.params.get(JobNumberConstants.exam_key)
            if exam_key is not None :
                message, statuscode = JobNumberDetails().get_job_number_info(exam_key)
            else:
                statuscode = AppStatus.bad_Request.value[0]
                message = ErrorResponse(SharedConstants.request_val_failure, SharedConstants.request_header_failure, statuscode, JobNumberConstants.param_failure, JobNumberDetails().__class__.__name__).__str__()
        else:
            job_number_post = req.get_json()
            message, statuscode  = JobNumberDetails().post_job_number_info(job_number_post)
                         
    except:
        message = ErrorResponse(str(sys.exc_info()[0]), JobNumberDetails().__class__.__name__, AppStatus.internal_server_error.value, str(sys.exc_info()[1]), JobNumberDetails().__class__.__name__).__str__()
        statuscode = AppStatus.internal_server_error.value[0]

    finally:
        return func.HttpResponse(body=message, status_code= statuscode, mimetype= SharedConstants.json_mime_type)

if __name__ == SharedConstants.main:
    main(func.HttpRequest)                                  