from database.dao import Dao

class Model:
    def __init__(self):
        # E' utile avere una lista di trips e stations
        self._list_trips = []
        self._list_stations = []

        # Quando il model viene creato, lui si va a leggere ciò che serve dal DB (tabelle trip e station)
        # e memorizza tutto in quelle liste
        self.get_trips()
        self.get_stations()

        # Per comodità di accesso per chiave/id mi creo anche i dizionari
        self._dict_trips = {}
        self._dict_stations = {}

        # Potrei scandire tutte le mie trip, e al posto di lasciare solo gli id delle station, potrei
        # memorizzare in esse anche il riferimento all'oggetto station corrispondente

        # Inizializzo i dizionari prendendo i dati dalle liste
        for station in self._list_stations:
            self._dict_stations[station.station_id] = station

        # Quando costruisco la lista di trip, al posto di memorizzare gli id delle trip vado ad
        # inserire direttamente i riferimenti agli oggetti corrispondenti
        for trip in self._list_trips:
            self._dict_trips[trip.trip_id] = trip
            trip.start_station = self._dict_stations[trip.start_station_id]
            trip.end_station = self._dict_stations[trip.end_station_id]

        print(f"#Trips: {len(self._list_trips)}")
        print(f"#Stations: {len(self._list_stations)}")


    # Funzione che è incaricata di fornire le trip
    def get_trips(self):
        print("Getting trips ...")
        dao = Dao()

        # Prima di andare a leggere le trip dal database tramite il Dao, verifico che questa operazione
        # non sia per caso già stata fatta. Se ho già la lista di trip, faccio che restituire quella
        if len(self._list_trips) == 0:
            self._list_trips = dao.read_trips_from_db()
        else:
            pass
        return self._list_trips

    def get_selected_trips(self, letter):
        print("Getting selected trips ...")
        #dao = Dao()
        #return dao.read_selected_trips_from_db(letter)

        result = []
        """
        for trip in self._list_trips:
            for station in self._list_stations:
                if trip.start_station_id == station.station_id and station.name.startswith(letter):
                    result.append(station)
        """

        # In alternativa, se ho usato il pattern ORM e, nella trip, ho non l'id della station
        # ma la station vera e propria (ovvero un riferimento all'oggetto che la rappresenta),
        # posso accedere direttamente all'oggetto e, da quello, prendere direttamente .name
        for trip in self._list_trips:
            if trip.start_station.name.startswith(letter):
                result.append(trip)

        return result

    def get_stations(self):
        print("Getting stations ...")
        dao = Dao()
        if len(self._list_stations) == 0:
            self._list_stations = dao.read_stations_from_db()
        else:
            pass
        return self._list_stations

