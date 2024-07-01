from marshmallow import Schema, fields

class WeightStatisticsDTO(Schema):
    id = fields.Int(dump_only = True)
    value = fields.Float(required = False)
    date = fields.Date(required = False)
    time = fields.Time(required = False)
