
USER=airflow
PASSWORD=airflow
PORT=18080

curl --user ${USER}:${PASSWORD} http://localhost:${PORT}/health
