class Seat:

    def __init__(self):
        self.id = None
        self.scheduleId = None
        self.seatNumber = None
        self.reserveYn = None
    
    def __str__(self):
        return 'Seat : {' + '\n' \
               + '\t' + 'id : ' + self.id + '\n' \
               + '\t' + 'scheduleId : ' + self.scheduleId + '\n' \
               + '\t' + 'seatNumber : ' + str(self.seatNumber) + '\n' \
               + '\t' + 'reserveYn : ' + self.reserveYn + '\n' \
               + '}'

    @staticmethod
    class Builder:

        def id(self, id):
            self.id = id
            return self
        
        def scheduleId(self, scheduleId):
            self.scheduleId = scheduleId
            return self
        
        def seatNumber(self, seatNumber):
            self.seatNumber = seatNumber
            return self
        
        def reserveYn(self, reserveYn):
            self.reserveYn = reserveYn
            return self
        
        def build(self):
            seat = Seat()
            seat.id = self.id
            seat.scheduleId = self.scheduleId
            seat.seatNumber = self.seatNumber 
            seat.reserveYn = self.reserveYn 
            return seat