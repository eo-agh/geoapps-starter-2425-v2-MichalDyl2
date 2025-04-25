from datetime import datetime

class Incident:
    __max_id = 0

    def __init__(self, description, priority, reporter_info, location):
        Incident.__max_id += 1
        self.id = Incident.__max_id
        self.description = description
        self.priority = priority
        self.reported_at = datetime.now()
        self.reporter_info = reporter_info
        self.location = location 

class IncidentManager:
    def __init__(self, ambulances):
        self.ambulances = ambulances

    def compute_distance(self, loc1, loc2):
        return ((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2) ** 0.5

    def assign_ambulance(self, incident):
        available = [a for a in self.ambulances if a.status == "available"]
        if not available:
            print("Brak dostępnych karetek")
            return

        best = min(available, key=lambda a: self.compute_distance(a.location, incident.location))
        best.status = "on mission"
        best.location = incident.location
        print(f"Karetka {best.id} przydzielona do incydentu {incident.id}")
