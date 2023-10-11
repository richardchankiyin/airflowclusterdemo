# airflowclusterdemo workernode

Steps to setup
-------------
1. Prepare env_var file and put this under the parent folder. For detail you can refer to env_var_example.txt 
2. run **./build.sh** command to build
```
richard@richard-mx:
$ ./build.sh 
[+] Building 60.3s (16/16) FINISHED                                                                                                                                                                  docker:default
 => [airflow-init internal] load build definition from Dockerfile                                                                                                                                              0.3s
 => => transferring dockerfile: 209B                                                                                                                                                                           0.0s
 => [airflow-init internal] load .dockerignore                                                                                                                                                                 0.5s
 => => transferring context: 2B                                                                                                                                                                                0.0s
 => [airflow-worker internal] load metadata for docker.io/apache/airflow:2.7.1                                                                                                                                 0.0s
 => [airflow-worker 1/4] FROM docker.io/apache/airflow:2.7.1                                                                                                                                                  12.3s
 => [airflow-init internal] load build context                                                                                                                                                                 0.3s
 => => transferring context: 17.86kB                                                                                                                                                                           0.0s
 => [airflow-init 2/4] COPY requirements.txt /                                                                                                                                                                 1.2s
 => [airflow-init 3/4] COPY dags/* /opt/airflow/dags/                                                                                                                                                          1.2s
 => [airflow-init 4/4] RUN pip install --no-cache-dir "apache-airflow==2.7.1" -r /requirements.txt                                                                                                            19.2s
 => [airflow-init] exporting to image                                                                                                                                                                          1.4s 
 => => exporting layers                                                                                                                                                                                        1.2s 
 => => writing image sha256:e9c745645dc6ba26c59b54dd41e99f1296133d9b284c7ec8587b6c907188d37c                                                                                                                   0.0s 
 => => naming to docker.io/apache/airflow:2.7.1                                                                                                                                                                0.1s 
 => [airflow-worker internal] load .dockerignore                                                                                                                                                               1.0s 
 => => transferring context: 2B                                                                                                                                                                                0.0s 
 => [airflow-worker internal] load build definition from Dockerfile                                                                                                                                            0.6s
 => => transferring dockerfile: 209B                                                                                                                                                                           0.0s
 => [airflow-worker internal] load build context                                                                                                                                                               0.3s
 => => transferring context: 461B                                                                                                                                                                              0.0s
 => [airflow-worker 2/4] COPY requirements.txt /                                                                                                                                                               1.0s
 => [airflow-worker 3/4] COPY dags/* /opt/airflow/dags/                                                                                                                                                        1.1s
 => [airflow-worker 4/4] RUN pip install --no-cache-dir "apache-airflow==2.7.1" -r /requirements.txt                                                                                                          17.9s
 => [airflow-worker] exporting to image                                                                                                                                                                        1.3s 
 => => exporting layers                                                                                                                                                                                        1.1s 
 => => writing image sha256:9a10cf73c8f02363b2ec07e5b1a845a7f2ae8eea13542015647f6a217ee192e6                                                                                                                   0.0s 
 => => naming to docker.io/apache/airflow:2.7.1                        
```
