from dataclasses import dataclass

@dataclass
class Trip:
    trip_id : int
    bike_id : int
    start_station_id : int
    end_station_id : int
    start_time : str
    end_time : str
    duration_seconds : int
    user_type : str

    #start_station : None # Station
    #end_station : None # Station

    def __str__(self):
        return f"Trip {self.trip_id}"

    def __eq__(self, other):
        return self.trip_id == other.trip_id

    def __hash__(self):
        return hash(self.trip_id)