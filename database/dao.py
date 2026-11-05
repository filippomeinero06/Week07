from database.db_connect import DB_Connect
from model.station import Station
from model.trip import Trip


# Classe che si occupa di parlare con il database
class Dao:
    def __init__(self):
        pass

    # Funzione incaricata di leggere le trip dal database con SQL
    def read_trips_from_db(self):
        db = DB_Connect()
        cnx = db.get_connection()
        if cnx is not None:
            print("Connection established")

            #query ="SELECT * FROM trip"
            query ="SELECT trip_id, bike_id, start_station_id, end_station_id, start_time, end_time, duration_seconds, user_type FROM trip"
            cursor = cnx.cursor()
            cursor.execute(query)
            # Leggo tutto dal cursore in una variabile results
            # result = cursor.fetchall()
            result = []
            for row in cursor:
                trip = Trip(*row)
                result.append(trip)

            cursor.close()
            cnx.close()
            return result



    def read_selected_trips_from_db(self, letter):
        db = DB_Connect()
        cnx = db.get_connection()
        if cnx is not None:
            print("Connection established")

            query = f"""SELECT t.*
                       FROM trip t, station s
                       WHERE t.start_station_id = s.station_id 
                       AND s.name LIKE '{letter}%'
                    """
            cursor = cnx.cursor()
            cursor.execute(query)
            result = []
            for row in cursor:
                trip = Trip(*row)
                result.append(trip)

            cursor.close()
            cnx.close()
            return result

            # Funzione incaricata di leggere le trip dal database con SQL
    def read_stations_from_db(self):
        db = DB_Connect()
        cnx = db.get_connection()
        if cnx is not None:
            print("Connection established")

            # query ="SELECT * FROM trip"
            query = "SELECT station_id, name, latitude, longitude FROM station"
            cursor = cnx.cursor()
            cursor.execute(query)
            # Leggo tutto dal cursore in una variabile results
            # result = cursor.fetchall()
            result = []
            for row in cursor:
                station = Station(*row)
                result.append(station)

            cursor.close()
            cnx.close()
            return result






            """
            row["trip_id"],
                            row["bike_id"],
                            row["start_station_id"],
                            row["end_station_id"],
                            row["start_time"],
                            row["end_time"],
                            row["duration_seconds"],
                            row["user_type"]"""