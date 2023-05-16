from repository.BaseRepository import BaseRepository
from repository.SeatRepository import SeatRepository

class TicketRepository(BaseRepository):

    def isValidated(self, cls):
        seatRepository = SeatRepository()
        seat = seatRepository.findById(cls.seatId)
        if not seat:
            print('해당하는 좌석이 없습니다.')
            return False
        return True