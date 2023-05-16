from repository.BaseRepository import BaseRepository
from repository.ScheduleRepository import ScheduleRepository

class SeatRepository(BaseRepository):

    def isValidated(self, cls):
        scheduleRepository = ScheduleRepository()
        schedule = scheduleRepository.findById(cls.scheduleId)
        if not schedule:
            print('해당하는 스케줄이 없습니다.')
            return False
        return True