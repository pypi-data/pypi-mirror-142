# job_number_schema.py

from marshmallow import fields,Schema

class JobNumberSchema(Schema):
    examkey = fields.Int(required=True)
    jobnumber = fields.Str(required=True)
    current_user_key =  fields.Str(required=True)