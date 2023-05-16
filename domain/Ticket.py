class Ticket:
    
    def __init__(self):
        self.id = None
        self.seatId = None
        self.phoneNumber = None
        self.seat = None
    
    def __str__(self):
        return 'Ticket : {' + '\n' \
               + '\t' + 'id : ' + self.id + '\n' \
               + '\t' + 'seatId : ' + self.seatId + '\n' \
               + '\t' + 'phoneNumber : ' + str(self.phoneNumber) + '\n' \
               + '}'

    @staticmethod
    class Builder:

        def id(self, id):
            self.id = id
            return self
        
        def seatId(self, seatId):
            self.seatId = seatId
            return self
        
        def phoneNumber(self, phoneNumber):
            self.phoneNumber = phoneNumber
            return self
        
        def build(self):
            ticket = Ticket()
            ticket.id = self.id
            ticket.seatId = self.seatId
            ticket.phoneNumber = self.phoneNumber
            return ticket