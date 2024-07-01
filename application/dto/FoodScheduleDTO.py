from marshmallow import Schema, fields

class FoodScheduleDTO(Schema):
    id = fields.Int(dump_only = True)
    schedule_name = fields.Str(required=True)
    number_meals = fields.Int(requierd = True)
    meal_1 = fields.Time(required = True)
    meal_2 = fields.Time(required = True)
    meal_3 = fields.Time(required = True)
    meal_4 = fields.Time(required = True)
    meal_5 = fields.Time(required = True)
    meal_6 = fields.Time(required = True)
    stepper_rotations = fields.Int(requierd = True)

