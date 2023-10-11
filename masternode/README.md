# airflowclusterdemo masternode

Steps to setup
-------------
1. Prepare env_var file and put this under the parent folder. For detail you can refer to env_var_example.txt 
2. Init project dir, please run ./init_project_dir.sh and you will be able to see the following folders created
```
richard@richard-linux:$ ls -l /mnt/airflow/cluster1/
total 0
drwxr-xr-x 2 root root 0 Oct 10 21:22 config
drwxr-xr-x 2 root root 0 Oct 10 21:27 dags
drwxr-xr-x 2 root root 0 Oct 10 21:31 logs
drwxr-xr-x 2 root root 0 Oct 10 21:22 plugins
drwxr-xr-x 2 root root 0 Oct 10 21:31 taskout
```
3. Build docker images for master node and deploy dags. Images will be built and dags required files will be copied to <shared_drive>/dags
```
Building airflow-init
[+] Building 15.7s (8/8) FINISHED                                                                                                                                                                      docker:default
 => [internal] load .dockerignore                                                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                                                  0.0s
 => [internal] load build definition from Dockerfile                                                                                                                                                             0.0s
 => => transferring dockerfile: 178B                                                                                                                                                                             0.0s
 => [internal] load metadata for docker.io/apache/airflow:2.7.1                                                                                                                                                  0.0s
 => [internal] load build context                                                                                                                                                                                0.0s
 => => transferring context: 37B                                                                                                                                                                                 0.0s
 => [1/3] FROM docker.io/apache/airflow:2.7.1                                                                                                                                                                    0.2s
 => [2/3] COPY requirements.txt /                                                                                                                                                                                0.0s
 => [3/3] RUN pip install --no-cache-dir "apache-airflow==2.7.1" -r /requirements.txt                                                                                                                           15.3s
 => exporting to image                                                                                                                                                                                           0.1s
 => => exporting layers                                                                                                                                                                                          0.0s
 => => writing image sha256:ebee3fb8908ee11e2794cd5e5bf45c56ca2fda69bdbaf039ed098ada26ff16a7                                                                                                                     0.0s
 => => naming to docker.io/apache/airflow:2.7.1                                                                                                                                                                  0.0s
Building airflow-triggerer                                                                                                                                                                                            
[+] Building 15.8s (8/8) FINISHED                                                                                                                                                                      docker:default 
 => [internal] load build definition from Dockerfile                                                                                                                                                             0.0s
 => => transferring dockerfile: 178B                                                                                                                                                                             0.0s
 => [internal] load .dockerignore                                                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                                                  0.0s
 => [internal] load metadata for docker.io/apache/airflow:2.7.1                                                                                                                                                  0.0s
 => [internal] load build context                                                                                                                                                                                0.0s
 => => transferring context: 37B                                                                                                                                                                                 0.0s
 => [1/3] FROM docker.io/apache/airflow:2.7.1                                                                                                                                                                    0.2s
 => [2/3] COPY requirements.txt /                                                                                                                                                                                0.1s
 => [3/3] RUN pip install --no-cache-dir "apache-airflow==2.7.1" -r /requirements.txt                                                                                                                           15.4s
 => exporting to image                                                                                                                                                                                           0.1s 
 => => exporting layers                                                                                                                                                                                          0.0s 
 => => writing image sha256:0fa4d9f6a7d3278f668649efc960fc9dc319c185a5ea207dac112320362a7887                                                                                                                     0.0s 
 => => naming to docker.io/apache/airflow:2.7.1                                                                                                                                                                  0.0s 
Building airflow-worker2                                                                                                                                                                                              
[+] Building 13.2s (8/8) FINISHED                                                                                                                                                                      docker:default 
 => [internal] load .dockerignore                                                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                                                  0.0s
 => [internal] load build definition from Dockerfile                                                                                                                                                             0.0s
 => => transferring dockerfile: 178B                                                                                                                                                                             0.0s
 => [internal] load metadata for docker.io/apache/airflow:2.7.1                                                                                                                                                  0.0s
 => [internal] load build context                                                                                                                                                                                0.0s
 => => transferring context: 37B                                                                                                                                                                                 0.0s
 => [1/3] FROM docker.io/apache/airflow:2.7.1                                                                                                                                                                    0.2s
 => [2/3] COPY requirements.txt /                                                                                                                                                                                0.0s
 => [3/3] RUN pip install --no-cache-dir "apache-airflow==2.7.1" -r /requirements.txt                                                                                                                           12.9s
 => exporting to image                                                                                                                                                                                           0.0s 
 => => exporting layers                                                                                                                                                                                          0.0s 
 => => writing image sha256:db2118478fdf1c3fe02f00934cfae852829bed13064bbe7233eec0728fcdb9da                                                                                                                     0.0s 
 => => naming to docker.io/apache/airflow:2.7.1                                                                                                                                                                  0.0s 
Building airflow-worker                                                                                                                                                                                               
[+] Building 14.3s (8/8) FINISHED                                                                                                                                                                      docker:default 
 => [internal] load .dockerignore                                                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                                                  0.0s
 => [internal] load build definition from Dockerfile                                                                                                                                                             0.0s
 => => transferring dockerfile: 178B                                                                                                                                                                             0.0s
 => [internal] load metadata for docker.io/apache/airflow:2.7.1                                                                                                                                                  0.0s
 => [internal] load build context                                                                                                                                                                                0.0s
 => => transferring context: 37B                                                                                                                                                                                 0.0s
 => [1/3] FROM docker.io/apache/airflow:2.7.1                                                                                                                                                                    0.2s
 => [2/3] COPY requirements.txt /                                                                                                                                                                                0.0s
 => [3/3] RUN pip install --no-cache-dir "apache-airflow==2.7.1" -r /requirements.txt                                                                                                                           14.0s
 => exporting to image                                                                                                                                                                                           0.1s
 => => exporting layers                                                                                                                                                                                          0.0s
 => => writing image sha256:e068ca6bec9eeb290f80e7b790ae8940f5c09f2c3731a2e339b81d87baeb5229                                                                                                                     0.0s
 => => naming to docker.io/apache/airflow:2.7.1                                                                                                                                                                  0.0s
Building airflow-scheduler                                                                                                                                                                                            
[+] Building 15.1s (8/8) FINISHED                                                                                                                                                                      docker:default 
 => [internal] load build definition from Dockerfile                                                                                                                                                             0.0s
 => => transferring dockerfile: 178B                                                                                                                                                                             0.0s
 => [internal] load .dockerignore                                                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                                                  0.0s
 => [internal] load metadata for docker.io/apache/airflow:2.7.1                                                                                                                                                  0.0s
 => [internal] load build context                                                                                                                                                                                0.0s
 => => transferring context: 37B                                                                                                                                                                                 0.0s
 => [1/3] FROM docker.io/apache/airflow:2.7.1                                                                                                                                                                    0.2s
 => [2/3] COPY requirements.txt /                                                                                                                                                                                0.0s
 => [3/3] RUN pip install --no-cache-dir "apache-airflow==2.7.1" -r /requirements.txt                                                                                                                           14.7s
 => exporting to image                                                                                                                                                                                           0.0s
 => => exporting layers                                                                                                                                                                                          0.0s
 => => writing image sha256:acc0049afe116fcaf88629eac79f1005b28329fb830447aef1ae2c35fcf8f05c                                                                                                                     0.0s 
 => => naming to docker.io/apache/airflow:2.7.1                                                                                                                                                                  0.0s 
Building airflow-webserver                                                                                                                                                                                            
[+] Building 19.3s (8/8) FINISHED                                                                                                                                                                      docker:default 
 => [internal] load build definition from Dockerfile                                                                                                                                                             0.0s
 => => transferring dockerfile: 178B                                                                                                                                                                             0.0s
 => [internal] load .dockerignore                                                                                                                                                                                0.0s
 => => transferring context: 2B                                                                                                                                                                                  0.0s
 => [internal] load metadata for docker.io/apache/airflow:2.7.1                                                                                                                                                  0.0s
 => [internal] load build context                                                                                                                                                                                0.0s
 => => transferring context: 37B                                                                                                                                                                                 0.0s
 => [1/3] FROM docker.io/apache/airflow:2.7.1                                                                                                                                                                    0.2s
 => [2/3] COPY requirements.txt /                                                                                                                                                                                0.0s
 => [3/3] RUN pip install --no-cache-dir "apache-airflow==2.7.1" -r /requirements.txt                                                                                                                           14.7s
 => exporting to image                                                                                                                                                                                           0.1s
 => => exporting layers                                                                                                                                                                                          0.0s
 => => writing image sha256:84ec9cf9b1603e55a6c07bd5fc0aa3877a390ad2e66c4dea96bf1abb187f729a                                                                                                                     0.0s
 => => naming to docker.io/apache/airflow:2.7.1
```

```
richard@richard-linux:$ ls -l /mnt/shared_doc/document/J2EE/airflow/cluster1/dags
total 20
-rwxr-xr-x 1 root root  699 Oct 11 13:45 analyze.py
-rwxr-xr-x 1 root root 3383 Oct 11 13:45 dollarindexsummary.py
-rwxr-xr-x 1 root root 4819 Oct 11 13:45 usindexsummary.py
-rwxr-xr-x 1 root root 2387 Oct 11 13:45 yahoo_finance_data.sh
```
