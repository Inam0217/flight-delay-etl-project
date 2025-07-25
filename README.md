# ✈️ Flight Delay ETL Project

A complete end-to-end ETL pipeline built using **Apache Airflow**, **Python**, and **MySQL**, containerized with **Docker**.

This project simulates a real-world data engineering workflow for processing flight delay data — from extraction and transformation to loading it into a relational database.  
Flight delays affect both airlines and passengers, making this data valuable for improving scheduling efficiency, resource allocation, and customer satisfaction.

---

## 🧰 Tech Stack

- **Apache Airflow** – Workflow orchestration  
- **Python** – Data processing  
- **Pandas** – Data cleaning  
- **MySQL** – Data storage  
- **Docker** – Containerization  

---

## 📁 Folder Structure

flight_etl_project/
├── airflow/
│ ├── dags/
│ │ └── flights_etl_dag.py
│ ├── scripts/
│ │ └── flight_etl_script.py
│ ├── data/
│ │ └── airlines.csv
│ ├── docker-compose.yaml
│ └── requirements.txt
├── .env
├── README.md

---

## ⚙️ How to Run the Project

1. **Clone the repository:**

git clone https://github.com/Inam0217/flight-delay-etl-project.git
cd flight-delay-etl-project

---

2. **Set up environment variables**

Make sure the .env file exists and contains:
MYSQL_ROOT_PASSWORD=yourpassword
MYSQL_DATABASE=flights_db
POSTGRES_USER=airflow
POSTGRES_PASSWORD=airflow
POSTGRES_DB=airflow
 <!-- Replace yourpassword with a strong root password of your choice. -->

---

3. **Start services using Docker Compose:**

docker-compose up

---

4. **Access the Airflow UI:**

- Go to: http://localhost:8080
- Trigger the DAG named: flights_etl_dag

---

## 🗂️ Airflow DAG Overview

The Airflow DAG flights_etl_dag.py includes:

- Extract Task: Reads raw flight data from a CSV file
- Transform Task: Cleans and preprocesses data using Pandas
- Load Task: Inserts cleaned data into a MySQL database (flights_db)
- Schedule: Can be triggered manually or set to run daily
- Retries: Configured with 1 retry (delay: 5 minutes)

## 📦 Sample Output (MySQL Table)

| year | month | day | airline | flight_number | origin | destination | dep_delay | arr_delay | distance |
|------|-------|-----|---------|----------------|--------|-------------|-----------|-----------|----------|
| 2015 | 1     | 1   | AS      | 98             | ANC    | SEA         | -11       | -22       | 1448     |
| 2015 | 1     | 1   | AA      | 2336           | LAX    | PBI         | -8        | -9        | 2330     |

> This is the final cleaned structure inside the `flight_data` table stored in MySQL.
> Additional fields like `TAIL_NUMBER`, `CANCELLED`, etc. were excluded for simplification and focus.

---

## 🔁 ETL Workflow Diagram

graph TD
    A[CSV File] --> B[Python Cleaning Script]
    B --> C[Airflow DAG]
    C --> D[MySQL Database]

This diagram represents the flow of data from raw CSV to final storage using the ETL pipeline.

---

## 🚀 Future Improvements

- Connect to real-time flight delay APIs (e.g., FAA, OpenSky)
- Add validation and testing logic in data transformation
- Use Apache Spark for large-scale flight datasets

---

## 📬 Contact

Inam Ul Hassan
📧 inamaitazaz1998@gmail.com
🔗 GitHub: Inam0217
