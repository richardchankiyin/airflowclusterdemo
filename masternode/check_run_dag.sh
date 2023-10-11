if [ $# -lt 2 ]; then echo "check_run_dag.sh <dag_id> <run_id>"; exit -1; fi 

USER=airflow
PASSWORD=airflow
PORT=18080
DAG=$1
RUNID=$2


curl --user ${USER}:${PASSWORD} http://localhost:${PORT}/api/v1/dags/${DAG}/dagRuns/${RUNID}
