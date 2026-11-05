from dataclasses import dataclass

@dataclass
class Station:
    station_id : int
    name : str
    latitude : float
    longitude : float

    def __str__(self):
        return f"{self.station_id} {self.name} {self.latitude:.2f} {self.longitude:.2f}"