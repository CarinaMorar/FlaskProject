from application.model.models import WeightStatisticsModel
from application.repository.WeightStatisticsRepository import WeightStatisticsRepository
from application.dto.WeightStatisticsDTO import WeightStatisticsDTO

class WeightStatisticsService:

    @staticmethod
    def createWeightStatistics(**data):
        statistics_dto = WeightStatisticsDTO()
        statistics_data = statistics_dto.load(data)

        new_statistics = WeightStatisticsModel(
            value = statistics_data.get('value'),
            date = statistics_data.get('date'),
            time = statistics_data.get('time')
        )
        print("service")
        return WeightStatisticsRepository.addWeightStatistics(new_statistics)
    
    @staticmethod
    def findWeightStatisticsById(id):
        return WeightStatisticsRepository.findWeightStatisticsById(id)

    @staticmethod
    def findAllWeightStatistics():
        return WeightStatisticsRepository.findAllWeightStatistics()
    
    @staticmethod
    def updateWeightStatistics(id, data):
        return WeightStatisticsRepository.updateWeightStatistics(id, data)
    
    @staticmethod
    def deleteWeightStatistics(id):
        return WeightStatisticsRepository.deleteWeightStatistics(id)