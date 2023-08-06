#__init__.py

import logging

import azure.functions as func
from .businesslogic import ExamDataStatus
from common import AppStatus, SharedConstants, ErrorResponse
from .constants.exam_data import ExamDataConstants

def main(req: func.HttpRequest) -> func.HttpResponse:
    """[summary]

    Args:
        req (func.HttpRequest): Calling ExamDataStatus class to get the http response

    Returns:
        func.HttpResponse: status of exam data from CES DB
        
    """
    if ExamDataConstants.file_status_filter in req.headers and req.headers[ExamDataConstants.file_status_filter]:
        response, statusCode = ExamDataStatus().exam_data_status(req.headers[ExamDataConstants.file_status_filter])
    else:
        statusCode = AppStatus.bad_Request.value[0]
        response = ErrorResponse(SharedConstants.request_val_failure, SharedConstants.request_header_failure, statusCode, ExamDataConstants.param_failure, ExamDataStatus().__class__.__name__).__str__()
    return func.HttpResponse(body = response,status_code = statusCode, mimetype= SharedConstants.json_mime_type)

 
if __name__ == SharedConstants.main:
    main(func.HttpRequest)
