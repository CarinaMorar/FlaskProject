from flask import Blueprint, request, jsonify
from marshmallow import ValidationError
from application.service.WeightStatisticsService import WeightStatisticsService

weightStatisticsController = Blueprint('weightStatisticsController', __name__, url_prefix='/weightStatistics')

@weightStatisticsController.route('/addWeightStatistics', methods=['POST'])
def addWeightStatistics():
    data = request.get_json()
    try:
        fs = WeightStatisticsService.createWeightStatistics(**data)
        return jsonify(fs.repr()), 201
    except ValidationError as err:
        return jsonify(err.messages), 400
    
@weightStatisticsController.route('/updateWeightStatistics/<int:id>', methods=['PUT'])
def updateWeightStatistics(id):
    data = request.get_json()
    fs = WeightStatisticsService.updateWeightStatistics(id, data)
    if fs:
        return jsonify(fs.repr()), 200
    return jsonify({'message': 'Error - weight statistics not found'}), 404

@weightStatisticsController.route('/deleteWeightStatistics/<int:id>', methods=['DELETE'])
def deleteWeightStatistics(id):
    fs = WeightStatisticsService.deleteWeightStatistics(id)
    if fs:
        return jsonify(fs.repr()), 200
    return jsonify({'message': 'Error - weight statistics not found'}), 404

@weightStatisticsController.route('/getWeightStatisticsById/<int:id>', methods=['GET'])
def getWeightStatisticsById(id):
    fs = WeightStatisticsService.findWeightStatisticsById(id)
    if fs:
        return jsonify(fs.repr()), 200
    return jsonify({'message': 'Error - weight statistics not found'}), 404

@weightStatisticsController.route('/getAllWeightStatistics', methods=['GET'])
def getAllWeightStatistics():
    fs = WeightStatisticsService.findAllWeightStatistics()
    repr_list = [fsi.repr() for fsi in fs]  # Convert each WeightStatisticsModel object to its representation
    return jsonify(repr_list), 200