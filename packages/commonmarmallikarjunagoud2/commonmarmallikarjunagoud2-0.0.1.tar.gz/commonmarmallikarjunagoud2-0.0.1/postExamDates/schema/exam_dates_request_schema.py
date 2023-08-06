#exam_dates_request_schema.py

from marshmallow import fields, validate,Schema
from ..constants.save_exam_dates_constants import SaveExamDatesConstants
from common import SharedConstants

__all__ =[SaveExamDatesConstants.exam_dates_request_schema]
class ExamSchema(Schema):
    examkey = fields.Int(required=True)
    actualExamDate = fields.Date(required=False,format=SharedConstants.date_format, allow_none=True)  
    plannedExamDate = fields.Date(required=False,format=SharedConstants.date_format, allow_none=True)  
    otherSupplierComment = fields.String(required=False,validate=validate.Length(max=1000),allow_none=True,default=None)
    crId = fields.String(required=False,allow_none=True,default=None)

class ExamDatesRequestSchema(Schema):
    examData = fields.List(fields.Nested(ExamSchema), required=True)
    
    


