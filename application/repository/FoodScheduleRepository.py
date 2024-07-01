from application import db
from application.model.models import FoodScheduleModel

class FoodScheduleRepository:
    @staticmethod
    def findFoodScheduleById(id):
        return FoodScheduleModel.query.get(id)
    
    @staticmethod
    def findAllFoodSchedule():
        return FoodScheduleModel.query.all()

    @staticmethod
    def findFoodScheduleByName(name):
        return FoodScheduleModel.query.filter_by(schedule_name = name).first()
    
    @staticmethod
    def findFoodScheduleByNumberOfMeals(number):
        return FoodScheduleModel.query.filter_by(number_meals = number)
    
    @staticmethod
    def addFoodSchedule(food_schedule):
        db.session.add(food_schedule)
        db.session.commit()
        return food_schedule
    
    @staticmethod
    def updateFoodSchedule(id, data):
        food_schedule = FoodScheduleModel.query.get(id)
        if food_schedule:
            food_schedule.schedule_name = data.get('schedule_name', food_schedule.schedule_name)
            food_schedule.number_meals = data.get('number_meals', food_schedule.number_meals)
            food_schedule.meal_1 = data.get('meal_1', food_schedule.meal_1)
            food_schedule.meal_2 = data.get('meal_2', food_schedule.meal_2)
            food_schedule.meal_3 = data.get('meal_3', food_schedule.meal_3)
            food_schedule.meal_4 = data.get('meal_4', food_schedule.meal_4)
            food_schedule.meal_5 = data.get('meal_5', food_schedule.meal_5)
            food_schedule.meal_6 = data.get('meal_6', food_schedule.meal_6)
            food_schedule.stepper_rotations = data.get('stepper_rotations', food_schedule.stepper_rotations)
            db.session.commit()
        return food_schedule
    
    @staticmethod
    def deleteFoodSchedule(id):
        food_schedule = FoodScheduleModel.query.get(id)
        if food_schedule:
            db.session.delete(food_schedule)
            db.session.commit()
        return None