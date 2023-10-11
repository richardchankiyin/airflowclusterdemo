# airflowclusterdemo
To demonstrate the setup of cluster of airflow master and worker nodes with some simple data sourcing and analysis jobs

Folder Structure
---------
- masternode: docker configuration to setup master node (including internal worker to take up jobs)
- workernode: docker configuration to setup remote worker node

Prerequsites:
------------
- docker ce engine
- share drive that is with read and write access for master and worker nodes
