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
Example DAG for demonstrating behavior of Datasets feature.

Notes on usage:

Turn on all the dags.

DAG dataset_produces_1 should run because it's on a schedule.

After dataset_produces_1 runs, dataset_consumes_1 should be triggered immediately
because its only dataset dependency is managed by dataset_produces_1.

No other dags should be triggered.  Note that even though dataset_consumes_1_and_2 depends on
the dataset in dataset_produces_1, it will not be triggered until dataset_produces_2 runs
(and dataset_produces_2 is left with no schedule so that we can trigger it manually).

Next, trigger dataset_produces_2.  After dataset_produces_2 finishes,
dataset_consumes_1_and_2 should run.

Dags dataset_consumes_1_never_scheduled and dataset_consumes_unknown_never_scheduled should not run because
they depend on datasets that never get updated.
"""
from __future__ import annotations

import pendulum

from airflow import DAG, Dataset
from airflow.operators.bash import BashOperator

# [START dataset_def]
usindexsourcing_dataset = Dataset("file:///opt/airflow/taskout/usindexsourcing.txt", extra={"hi": "bye"})
# [END dataset_def]

# python task
from airflow.decorators import task

from analyze import Analysis

output="/opt/airflow/taskout"

with DAG(
    dag_id="usindexsourcing",
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule="@daily",
    tags=["produces", "usindex"],
) as dagsourcing:
    # [START task_outlet]

    tixic = BashOperator(
        task_id="yahoo_curl_ixic",
        depends_on_past=False,
        bash_command="/opt/airflow/dags/yahoo_finance_data.sh ^IXIC > /opt/airflow/taskout/IXIC.csv",
        retries=3,
    )

    tdji = BashOperator(
        task_id="yahoo_curl_dji",
        depends_on_past=False,
        bash_command="/opt/airflow/dags/yahoo_finance_data.sh ^DJI > /opt/airflow/taskout/DJI.csv",
        retries=3,
    )

    tspx = BashOperator(
        task_id="yahoo_curl_spx",
        depends_on_past=False,
        bash_command="/opt/airflow/dags/yahoo_finance_data.sh ^GSPC > /opt/airflow/taskout/SPX.csv",
        retries=3,
    )

    t = BashOperator(
        outlets=[usindexsourcing_dataset],
        task_id="print_date",
        bash_command="date +%Y%m%d > /opt/airflow/taskout/usindexsourcing.txt",
    )

    [tixic,tdji,tspx] >> t
    # [END task_outlet]

# [START dag_dep]
with DAG(
    dag_id="usindexconsuming",
    catchup=False,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    schedule=[usindexsourcing_dataset],
    tags=["consumes", "usindex"],
) as dagconsuming:
    # [END dag_dep]

    @task(task_id="output_dji_summary")
    def print_dji_context(ds=None, **kwargs):
        analyze=Analysis(output)
        sym=analyze.readyahoo("DJI")
        lastentry=sym.tail(1)
        time=lastentry.time.values[0]
        value=lastentry.close.values[0]
        result=str(time) + "," + str(value)
        lastentry.to_csv(output + "/DJI_summary.csv") 
        return result
    
    tdji=print_dji_context()

    @task(task_id="output_ixic_summary")
    def print_ixic_context(ds=None, **kwargs):
        analyze=Analysis(output)
        sym=analyze.readyahoo("IXIC")
        lastentry=sym.tail(1)
        time=lastentry.time.values[0]
        value=lastentry.close.values[0]
        result=str(time) + "," + str(value)
        lastentry.to_csv(output + "/IXIC_summary.csv") 
        return result

    tixic=print_ixic_context() 

    @task(task_id="output_spx_summary")
    def print_spx_context(ds=None, **kwargs):
        analyze=Analysis(output)
        sym=analyze.readyahoo("SPX")
        lastentry=sym.tail(1)
        time=lastentry.time.values[0]
        value=lastentry.close.values[0]
        result=str(time) + "," + str(value)
        lastentry.to_csv(output + "/SPX_summary.csv") 
        return result

    tspx=print_spx_context()

    t = BashOperator(
        task_id="print_date",
        bash_command="date +%Y%m%d > /opt/airflow/taskout/usindexconsuming.txt",
    )

    [tixic,tdji,tspx] >> t
