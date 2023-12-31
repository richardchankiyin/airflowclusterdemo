#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.
"""
### Tutorial Documentation
Documentation that goes along with the Airflow tutorial located
[here](https://airflow.apache.org/tutorial.html)
"""
from __future__ import annotations

# [START tutorial]
# [START import_module]
from datetime import datetime, timedelta
from textwrap import dedent

# The DAG object; we'll need this to instantiate a DAG
from airflow import DAG

# Operators; we need this to operate!
from airflow.operators.bash import BashOperator
# python task
from airflow.decorators import task

from analyze import Analysis

# [END import_module]
output="/opt/airflow/taskout"

# [START instantiate_dag]
with DAG(
    "dollar_index_summary",
    # [START default_args]
    # These args will get passed on to each operator
    # You can override them on a per-task basis during operator initialization
    default_args={
        "depends_on_past": False,
        "email": ["airflow@example.com"],
        "email_on_failure": False,
        "email_on_retry": False,
        "retries": 1,
        "retry_delay": timedelta(minutes=5),
        # 'queue': 'bash_queue',
        # 'pool': 'backfill',
        # 'priority_weight': 10,
        # 'end_date': datetime(2016, 1, 1),
        # 'wait_for_downstream': False,
        # 'sla': timedelta(hours=2),
        # 'execution_timeout': timedelta(seconds=300),
        # 'on_failure_callback': some_function, # or list of functions
        # 'on_success_callback': some_other_function, # or list of functions
        # 'on_retry_callback': another_function, # or list of functions
        # 'sla_miss_callback': yet_another_function, # or list of functions
        # 'trigger_rule': 'all_success'
    },
    # [END default_args]
    description="Dollar Index Summary DAG",
    schedule=timedelta(days=1),
    start_date=datetime(2021, 1, 1),
    catchup=False,
    tags=["dollarindex"],
) as dag:
    # [END instantiate_dag]

    # [START basic_task]

    t1 = BashOperator(
        task_id="yahoo_curl_nyicdx",
        depends_on_past=False,
        bash_command="/opt/airflow/dags/yahoo_finance_data.sh ^NYICDX > /opt/airflow/taskout/NYICDX.csv",
        retries=3,
    )

    # [END basic_task]

    @task(task_id="output_nyicdx_summary")
    def print_context(ds=None, **kwargs):
        analyze=Analysis(output)
        nyicdx=analyze.readyahoo("NYICDX")
        lastentry=nyicdx.tail(1)
        time=lastentry.time.values[0]
        value=lastentry.close.values[0]
        result=str(time) + "," + str(value)
        lastentry.to_csv(output + "/NYICDX_summary.csv") 
        return result

    t2 = print_context()

    t1 >> t2
