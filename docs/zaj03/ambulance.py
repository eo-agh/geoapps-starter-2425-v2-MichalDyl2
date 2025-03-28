class Ambulance:
    __max_id = 0

    def __init__(self, type, status, location, equipment):
        Ambulance.__max_id += 1
        self.id = Ambulance.__max_id
        self.type = type
        self.status = status
        self.location = location
        self.equipment = equipment
 