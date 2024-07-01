from application import db
from application.model.models import WeightStatisticsModel

class WeightStatisticsRepository:
    @staticmethod
    def findWeightStatisticsById(id):
        return WeightStatisticsModel.query.get(id)
    
    @staticmethod
    def findAllWeightStatistics():
        return WeightStatisticsModel.query.all()

    @staticmethod
    def addWeightStatistics(weight_statistics):
        db.session.add(weight_statistics)
        db.session.commit()
        return weight_statistics
    
    @staticmethod
    def updateWeightStatistics(id, data):
        statistics = WeightStatisticsModel.query.get(id)
        if statistics:
            statistics.value = data.get('value', statistics.value)
            statistics.date = data.get('date', statistics.date)
            statistics.time = data.get('time', statistics.time)
            db.session.commit()
        return statistics

    @staticmethod
    def deleteWeightStatistics(id):
        statistics = WeightStatisticsModel.query.get(id)
        if statistics:
            db.session.delete(statistics)
            db.session.commit()

        return None