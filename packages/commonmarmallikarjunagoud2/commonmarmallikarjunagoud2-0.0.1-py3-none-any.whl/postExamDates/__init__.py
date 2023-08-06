import logging
import azure.functions as func
from .businesslogic import SaveExamDates
from common import SharedConstants

def main(req: func.HttpRequest) -> func.HttpResponse:
    """[summary]

    Args:
        req (func.HttpRequest): request parameter to update planned Exam Dates to CES DB

    Returns:
        func.HttpResponse: update Planned Exam Dates to CES DB
        
    """
    
    return SaveExamDates().save_exam_date(req)