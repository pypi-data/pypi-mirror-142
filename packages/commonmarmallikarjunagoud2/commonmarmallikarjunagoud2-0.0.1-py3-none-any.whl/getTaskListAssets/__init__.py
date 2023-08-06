#__init__.py

"""main method."""
import azure.functions as func
from getTaskListAssets.businesslogic import get_task_list_assets as bu
from .businesslogic.get_task_list_assets import TaskListAssets
from common import AppStatus,SharedConstants,ErrorResponse, CustomMessage
from .constants.get_task_list_assets import GetTaskListAssetsConstants

def main(req: func.HttpRequest) -> func.HttpResponse:
    """[summary]
    Args:
        req (func.HttpRequest): To get task list assets from CES DB

    Returns:
        func.HttpResponse: Return json data based on filters values from CES database.
    """
  
    is_supplier_search_param = GetTaskListAssetsConstants.is_supplier_search
    task_list_filter = GetTaskListAssetsConstants.task_list_filter
    if is_supplier_search_param not in req.params:
       message = ErrorResponse(SharedConstants.request_val_failure,SharedConstants.request_header_failure,
                                              AppStatus.bad_Request.value,CustomMessage.bad_request, TaskListAssets.__name__).__str__()
       status_code = AppStatus.bad_Request.value[0]

    elif task_list_filter not in req.headers:
       message = ErrorResponse(SharedConstants.request_val_failure,SharedConstants.request_header_failure,
                                              AppStatus.bad_Request.value,CustomMessage.bad_request, TaskListAssets.__name__).__str__()
       status_code = AppStatus.bad_Request.value[0]
    else:
       asset_filter = req.headers[task_list_filter]
       is_supplier_search_param_value = req.params[is_supplier_search_param]
       obj = bu.TaskListAssets()
       message, status_code = obj.get_task_list_assets(asset_filter,is_supplier_search_param_value)
         
    return func.HttpResponse(body=message, status_code= status_code, mimetype=SharedConstants.json_mime_type)

if __name__ == SharedConstants.main:
    main(func.HttpRequest)
