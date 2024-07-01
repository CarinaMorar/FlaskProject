from application.model.models import FoodScheduleModel
from application.repository.FoodScheduleRepository import FoodScheduleRepository
from application.dto.FoodScheduleDTO import FoodScheduleDTO

class FoodScheduleService:
    @staticmethod
    def createFoodSchedule(**data):
        food_schedule_dto = FoodScheduleDTO()
        food_schedule_data = food_schedule_dto.load(data)

        new_food_schedule = FoodScheduleModel(
            schedule_name = food_schedule_data.get('schedule_name'),
            number_meals = food_schedule_data.get('number_meals'),
            meal_1 = food_schedule_data.get('meal_1'),
            meal_2 = food_schedule_data.get('meal_2'),
            meal_3 = food_schedule_data.get('meal_3'),
            meal_4 = food_schedule_data.get('meal_4'),
            meal_5 = food_schedule_data.get('meal_5'),
            meal_6 = food_schedule_data.get('meal_6'),
            stepper_rotations = food_schedule_data.get('stepper_rotations')
        )

        return FoodScheduleRepository.addFoodSchedule(new_food_schedule)
        
    @staticmethod
    def findFoodScheduleById(id):
        return FoodScheduleRepository.findFoodScheduleById(id)
    
    @staticmethod
    def findAllFoodSchedule():
        return FoodScheduleRepository.findAllFoodSchedule()
    
    @staticmethod
    def findFoodScheduleByName(name):
        return FoodScheduleRepository.findFoodScheduleByName(name)
    
    @staticmethod
    def findFoodScheduleByNumberOfMeals(number):
        return FoodScheduleRepository.findFoodScheduleByNumberOfMeals(number)
    
    @staticmethod
    def updateFoodSchedule(id, data):
        return FoodScheduleRepository.updateFoodSchedule(id, data)
    
    @staticmethod
    def deleteFoodSchedule(id):
        return FoodScheduleRepository.deleteFoodSchedule(id)