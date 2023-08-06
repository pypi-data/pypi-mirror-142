import logging

import azure.functions as func
from .businesslogic import TaskListStatus
from .constants.task_list_status_constants import TaskListStatusConstants

def main(req: func.HttpRequest) -> func.HttpResponse:
    """[summary]

    Args:
        req (func.HttpRequest): request parameter to update task status to CES DB

    Returns:
        func.HttpResponse: update task status 
        
    """
    
    return TaskListStatus().save_task_list_status(req)
