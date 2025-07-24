import pandas as pd
import mysql.connector
import os
from dotenv import load_dotenv

def run_etl():
    try:
        print("📦 Reading .env variables...")
        load_dotenv(dotenv_path="/opt/airflow/.env")

        print("📂 Reading CSV...")
        csv_path = '/opt/airflow/data/airlines.csv'
        df = pd.read_csv(csv_path)

        print("🔐 Connecting to MySQL...")
        conn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
            connection_timeout=10
        )
        cursor = conn.cursor()

        print("🛠️ Inserting data into flight_data table...")
        insert_query = """
            INSERT INTO flight_data (
                YEAR, MONTH, DAY, AIRLINE, FLIGHT_NUMBER,
                ORIGIN_AIRPORT, DESTINATION_AIRPORT,
                DEPARTURE_DELAY, ARRIVAL_DELAY, DISTANCE
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        for i, row in df.iterrows():
            try:
                cursor.execute(insert_query, (
                    int(row['YEAR']),
                    int(row['MONTH']),
                    int(row['DAY']),
                    row['AIRLINE'],
                    int(row['FLIGHT_NUMBER']),
                    row['ORIGIN_AIRPORT'],
                    row['DESTINATION_AIRPORT'],
                    float(row['DEPARTURE_DELAY']) if not pd.isna(row['DEPARTURE_DELAY']) else None,
                    float(row['ARRIVAL_DELAY']) if not pd.isna(row['ARRIVAL_DELAY']) else None,
                    int(row['DISTANCE']) if not pd.isna(row['DISTANCE']) else None
                ))
                print(f"✅ Inserted row {i}")
            except Exception as e:
                print(f"⚠️ Failed to insert row {i}: {e}")

        conn.commit()
        print("✅ ETL process complete.")

    except mysql.connector.Error as err:
        print(f"❌ MySQL error: {err}")
    except Exception as e:
        print(f"❌ General ETL error: {e}")
    finally:
        if 'conn' in locals() and conn.is_connected():
            cursor.close()
            conn.close()
            print("🔒 MySQL connection closed.")
