from marshmallow import Schema,fields,validate # type: ignore


class EmployeeSchema(Schema):
    id=fields.Int(required=True)
    name=fields.Str(required=True,validate=validate.Length(min=1))
    age = fields.Int(required=True)
    dept=fields.Str(required=True,validate=validate.Length(min=1))
