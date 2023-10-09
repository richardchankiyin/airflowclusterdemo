FROM apache/airflow:2.7.1
COPY requirements.txt /
COPY dags/* /opt/airflow/dags/
RUN pip install --no-cache-dir "apache-airflow==${AIRFLOW_VERSION}" -r /requirements.txt
