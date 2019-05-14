# DevOpsProCamp
Script collects CPU and memory metrics from your OS to console.

Installation
=
Make sure to install python 3.6+, pip3 and psutils:
```
sudo apt-get update && sudo apt-get install python3
sudo apt-get install gcc python-pip
pip3 install psutil
```

Usage
=
```python3 metrics.py cpu``` - CPU metrics  
```python3 metrics.py mem``` - Memory metrics

If you need to run in a **Docker** container:
```
docker build -t metrics .

docker run --rm metrics python3 metrics.py cpu
docker run --rm metrics python3 metrics.py mem
```
