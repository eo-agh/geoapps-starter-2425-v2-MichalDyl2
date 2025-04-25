class Station:
    __max_id = 0

    def __init__(self, location, ambulance, driver, employee):
        Station.__max_id += 1
        self.id = Station.__max_id
        self.location = location
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee

    def is_ambulance_at_station(self):
        return self.ambulance.location == self.location
 