from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from application.service.FoodScheduleService import FoodScheduleService

foodScheduleController = Blueprint('foodScheduleController', __name__, url_prefix='/foodSchedule')

@foodScheduleController.route('/addFoodSchedule', methods=['POST'])
def addFoodSchedule():
    data = request.get_json()
    print(data)
    try:
        fs = FoodScheduleService.createFoodSchedule(**data)
        return jsonify(fs.repr()), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    
@foodScheduleController.route('/updateFoodSchedule/<int:id>', methods=['PUT'])
def updateFoodSchedule(id):
    data = request.get_json()
    fs = FoodScheduleService.updateFoodSchedule(id, data)
    if fs:
        return jsonify(fs.repr()), 200
    return jsonify({'message': 'Error - food schedule not found'}), 404

@foodScheduleController.route('/deleteFoodSchedule/<int:id>', methods=['DELETE'])
def deleteFoodSchedule(id):
    fs = FoodScheduleService.deleteFoodSchedule(id)
    if fs:
        return jsonify(fs.repr()), 200
    return jsonify({'message': 'Error - food schedule not found'}), 404

@foodScheduleController.route('/getFoodScheduleById/<int:id>', methods=['GET'])
def getFoodScheduleById(id):
    fs = FoodScheduleService.findFoodScheduleById(id)
    if fs:
        return jsonify(fs.repr()), 200
    return jsonify({'message': 'Error - food schedule not found'}), 404

@foodScheduleController.route('/getFoodScheduleByName/<string:name>', methods=['GET'])
def getFoodScheduleByName(name):
    fs = FoodScheduleService.findFoodScheduleByName(name)
    if fs:
        return jsonify(fs.repr()), 200
    return jsonify({'message': 'Error - food schedule not found'}), 404

@foodScheduleController.route('/getFoodScheduleByNumberOfMeals/<int:number>', methods=['GET'])
def getFoodScheduleByNumberOfMeals(number):
    fs = FoodScheduleService.findFoodScheduleByNumberOfMeals(number)
    if fs:
        repr_list = [fsi.repr() for fsi in fs]  # Convert each WeightStatisticsModel object to its representation
        return jsonify(repr_list), 200
    return jsonify({'message': 'Error - food schedule not found'}), 404

@foodScheduleController.route('/getAllFoodSchedule', methods=['GET'])
def getAllFoodSchedule():
    fs = FoodScheduleService.findAllFoodSchedule()
    repr_list = [fsi.repr() for fsi in fs]  # Convert each WeightStatisticsModel object to its representation
    return jsonify(repr_list), 200