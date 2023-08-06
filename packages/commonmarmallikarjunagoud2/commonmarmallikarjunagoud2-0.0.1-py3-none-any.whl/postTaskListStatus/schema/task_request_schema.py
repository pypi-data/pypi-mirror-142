#task_request_schema.py

from marshmallow import fields, validate,Schema
from ..constants.task_list_status_constants import TaskListStatusConstants
from common import SharedConstants

__all__ =[TaskListStatusConstants.task_request_schema]
class TaskSchema(Schema):
    exam_sr_key = fields.Integer(required=True)
    task_list_id = fields.Integer(required=True)
    task_list_stat  = fields.Integer(required=False)
   

class TaskRequestSchema(Schema):
    taskData = fields.List(fields.Nested(TaskSchema), required=True)
    
    


