
if [ $# -lt 1 ]; then echo "run_dag.sh <dag_id>"; exit -1; fi 

USER=airflow
PASSWORD=airflow
PORT=18080
DAG=$1
RUNID=${DAG}_$(date +%Y%m%d%H%M%s)

curl -H "Content-Type: application/json" -X POST --user ${USER}:${PASSWORD} http://localhost:${PORT}/api/v1/dags/${DAG}/dagRuns -d "{\"dag_run_id\":\"${RUNID}\", \"conf\":{}}"
