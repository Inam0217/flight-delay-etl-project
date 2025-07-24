import mysql.connector
conn = mysql.connector.connect(
    host="mysql",  # or same as in your .env
    user="root",
    password="kashar0217",
    database="flights_db"
)
cursor = conn.cursor()
cursor.execute("INSERT INTO flight_data (YEAR, MONTH, DAY, AIRLINE, FLIGHT_NUMBER, ORIGIN_AIRPORT, DESTINATION_AIRPORT, DEPARTURE_DELAY, ARRIVAL_DELAY, DISTANCE) VALUES (2025, 7, 22, 'XY', 123, 'JED', 'RUH', 10, 15, 850)")
conn.commit()
cursor.close()
conn.close()
