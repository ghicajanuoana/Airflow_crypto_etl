Automated Bitcoin ETL Pipeline (Docker + Airflow)

In acest proiect am integrat pipeline-ul ETL intr-o platforma de orchestrare folosind Apache Airflow, rulat in containere Docker.
Airflow preia, transforma si incarca automat datele la un interval de timp definit (eu am definit la fiecare 5 minute).

1. DAG
Am definit un workflow format din 3 task-uri:
Task 1: extract_task → extrage date din API
Task 2: transform_task → transforma si valideaza datele
Task 3: load_task → incarca datele in MySQL
DAG-ul ruleaza automat la fiecare 5 minute (schedule_interval="*/5 * * * *")

2. Docker Compose
Airflow ruleaza in containere Docker:
Webserver
Scheduler
Triggerer
Postgres (Airflow Metadata DB)
Totul este orchestrat cu docker-compose.yaml.

3. Integrarea cu proiectul ETL
Airflow importa functiile ETL:
extract_data()
transform_data()
load_data()

Tehnologii utilizate:

* Apache Airflow 2.x
* Docker & Docker Compose
* Postgres (metadate Airflow)
* Python Operators
* Scheduler profesional
* UI Airflow pentru monitorizare

Obiective atinse:

* orchestrarea unui pipeline ETL real
* automatizarea completa a procesarii datelor
* utilizarea unui scheduler enterprise
* monitorizarea executiilor in UI (Succeeded/Failed)
* comunicare intre containere si servicii externe
* integrarea unei baze de date MySQL din exterior
