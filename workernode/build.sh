
rm -fR dags
mkdir dags
PROJ_FOLDER=$(grep ^AIRFLOW_PROJ_DIR env_var | cut -d'=' -f2)
DAGS_FOLDER=${PROJ_FOLDER}/dags
cp -r ${DAGS_FOLDER}/* dags
docker compose --env-file env_var build
