# airflowclusterdemo
To demonstrate the setup of cluster of airflow master and worker nodes with some simple data sourcing and analysis jobs

Folder Structure
---------
- masternode: docker configuration to setup master node (including internal worker to take up jobs)
- workernode: docker configuration to setup remote worker node
- testcases: illustrate the tests were done when setting up the cluster 

Prerequisites
------------
- docker ce engine
- share drive that is with read and write access for master and worker nodes

Sample Jobs
-----------
1. dollar_index_summary - This is a single job with no dependency and will first get dollar index from yahoo finance and download as CSV file. Then the job will analyze the file and generate summary 
2. usindexproducing - This is a upstream job will no dependency and will first get DJI, IXIC and SPX from yahoo finance and download them as CSV files. Once complete another job called usindexconsuming will be triggered 
3. usindexconsuming - This is a downstream job depends on usindexproducing to generate summary files of DJI, IXIC and SPX

Explanation of output
------------
```
richard@richard-linux:$ ls -l /mnt/airflow/cluster1/taskout
total 1788
-rwxr-xr-x 1 root root 488025 Oct 11 12:40 DJI.csv
-rwxr-xr-x 1 root root    222 Oct 11 12:40 DJI_summary.csv
-rwxr-xr-x 1 root root 473928 Oct 11 12:40 IXIC.csv
-rwxr-xr-x 1 root root    231 Oct 11 12:40 IXIC_summary.csv
-rwxr-xr-x 1 root root 366190 Oct 11 12:34 NYICDX.csv
-rwxr-xr-x 1 root root    212 Oct 11 12:34 NYICDX_summary.csv
-rwxr-xr-x 1 root root 467243 Oct 11 12:40 SPX.csv
-rwxr-xr-x 1 root root    226 Oct 11 12:40 SPX_summary.csv
-rwxr-xr-x 1 root root      9 Oct 11 12:40 usindexconsuming.txt
-rwxr-xr-x 1 root root      9 Oct 11 12:40 usindexsourcing.txt
```

NYICDX.csv - yahoo finance file of DXY 
```
Date,Open,High,Low,Close,Adj Close,Volume
2001-01-02,109.330002,109.650002,108.639999,108.769997,108.769997,0
2001-01-03,108.589996,110.339996,108.089996,110.169998,110.169998,0
2001-01-04,110.300003,110.400002,108.510002,108.809998,108.809998,0
2001-01-05,108.639999,109.309998,108.260002,108.419998,108.419998,0
2001-01-08,108.330002,109.190002,108.230003,108.860001,108.860001,0
2001-01-09,109.190002,109.959999,109.080002,109.519997,109.519997,0
2001-01-10,109.599998,109.959999,109.260002,109.860001,109.860001,0
2001-01-11,110.089996,110.099998,108.730003,109.010002,109.010002,0
...
```
NYICDX_summary.csv - summary file of NYICDX illustrating the current date information 
```
time,time,open,high,low,close,adjclose,volume,sma10,sma20,sma50
2023-10-11 08:59:59,2023-10-11 08:59:59,105.752197,105.798798,105.658699,105.764198,105.764198,0,106.31342090000001,105.96321074999999,104.52588402
```
DJI.csv - yahoo finance file of DJI  
DJI_summary.csv - summary file of DJI illustrating the current date information  
IXIC.csv - yahoo finance file of IXIC  
IXIC_summary.csv - summary file of IXIC illustrating the current date information  
SPX.csv - yahoo finance file of SPX  
SPX_summary.csv - summary file of SPX illustrating the current date information  

usindexsourcing.txt - file generated once usindexsourcing job completed with date run. Airflow will be able to detect the update of this file to trigger usindexconsuming job      
usindexconsuming.txt - file generated once usindexconsuming job completed with date run
```
richard@richard-linux:$ cat /mnt/airflow/cluster1/taskout/usindexsourcing.txt 
20231011
richard@richard-linux:$ cat /mnt/airflow/cluster1/taskout/usindexconsuming.txt 
20231011

```
