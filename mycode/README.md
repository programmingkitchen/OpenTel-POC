# My Code Repository

## Virtual Environment
source ~/.opentel/bin/activate
pip list
pip freeze | grep opentelemetry

## Distributed Tracing
pip install flask requests
pip install opentelemetry-api opentelemetry-sdk

pip freeze | grep opentelemetry
opentelemetry-api==1.29.0
opentelemetry-sdk==1.29.0
opentelemetry-semantic-conventions==0.50b0


# Logging


pip install opentelemetry-api opentelemetry-sdk
pip install opentelemetry-propagator-b3
pip install opentelemetry-instrumentation-wsgi

(.opentel) ubuntu@OpenTel-vm-01:~/OpenTel-POC/mycode$ pip freeze | grep opentelemetry
opentelemetry-api==1.29.0
opentelemetry-instrumentation==0.50b0
opentelemetry-instrumentation-wsgi==0.50b0
opentelemetry-propagator-b3==1.29.0
opentelemetry-sdk==1.29.0
opentelemetry-semantic-conventions==0.50b0
opentelemetry-util-http==0.50b0


(.opentel) ubuntu@OpenTel-vm-01:~/OpenTel-POC/mycode$ pip list
Package                            Version   
---------------------------------- ----------
blinker                            1.8.2     
certifi                            2024.12.14
charset-normalizer                 3.4.1     
click                              8.1.8     
Deprecated                         1.2.15    
flask                              3.0.3     
idna                               3.10      
importlib-metadata                 8.5.0     
itsdangerous                       2.2.0     
jinja2                             3.1.5     
MarkupSafe                         2.1.5     
opentelemetry-api                  1.29.0    
opentelemetry-instrumentation      0.50b0    
opentelemetry-instrumentation-wsgi 0.50b0    
opentelemetry-propagator-b3        1.29.0    
opentelemetry-sdk                  1.29.0    
opentelemetry-semantic-conventions 0.50b0    
opentelemetry-util-http            0.50b0    
packaging                          24.2      
pip                                20.0.2    
pkg-resources                      0.0.0     
requests                           2.32.3    
setuptools                         44.0.0    
typing-extensions                  4.12.2    
urllib3                            2.2.3     
werkzeug                           3.0.6     
wrapt                              1.17.0    
zipp                               3.20.2    


# Metrics

pip install opentelemetry-exporter-prometheus


(.opentel) ubuntu@OpenTel-vm-01:~/OpenTel-POC$ pip list | grep opentelemetry
opentelemetry-api                  1.29.0    
opentelemetry-exporter-prometheus  0.50b0    
opentelemetry-instrumentation      0.50b0    
opentelemetry-instrumentation-wsgi 0.50b0    
opentelemetry-propagator-b3        1.29.0    
opentelemetry-sdk                  1.29.0    
opentelemetry-semantic-conventions 0.50b0    
opentelemetry-util-http            0.50b0   


## Prometheus
ubuntu@OpenTel-vm-01:~$ netstat -an | grep 8000
tcp        0      0 127.0.0.1:8000          0.0.0.0:*               LISTEN     

## NOTE:  we have a problem with this:

```
prometheus_reader = PrometheusMetricReader(prefix="MetricExampleRJG")
```

## Prometheus Results

ubuntu@OpenTel-vm-01:~$ curl localhost:8000
# HELP python_gc_objects_collected_total Objects collected during gc
# TYPE python_gc_objects_collected_total counter
python_gc_objects_collected_total{generation="0"} 91.0
python_gc_objects_collected_total{generation="1"} 264.0
python_gc_objects_collected_total{generation="2"} 0.0
# HELP python_gc_objects_uncollectable_total Uncollectable objects found during GC
# TYPE python_gc_objects_uncollectable_total counter
python_gc_objects_uncollectable_total{generation="0"} 0.0
python_gc_objects_uncollectable_total{generation="1"} 0.0
python_gc_objects_uncollectable_total{generation="2"} 0.0
# HELP python_gc_collections_total Number of times this generation was collected
# TYPE python_gc_collections_total counter
python_gc_collections_total{generation="0"} 61.0
python_gc_collections_total{generation="1"} 5.0
python_gc_collections_total{generation="2"} 0.0
# HELP python_info Python platform information
# TYPE python_info gauge
python_info{implementation="CPython",major="3",minor="8",patchlevel="10",version="3.8.10"} 1.0
# HELP process_virtual_memory_bytes Virtual memory size in bytes.
# TYPE process_virtual_memory_bytes gauge
process_virtual_memory_bytes 1.84147968e+08
# HELP process_resident_memory_bytes Resident memory size in bytes.
# TYPE process_resident_memory_bytes gauge
process_resident_memory_bytes 2.5411584e+07
# HELP process_start_time_seconds Start time of the process since unix epoch in seconds.
# TYPE process_start_time_seconds gauge
process_start_time_seconds 1.73628665457e+09
# HELP process_cpu_seconds_total Total user and system CPU time spent in seconds.
# TYPE process_cpu_seconds_total counter
process_cpu_seconds_total 0.14
# HELP process_open_fds Number of open file descriptors.
# TYPE process_open_fds gauge
process_open_fds 6.0
# HELP process_max_fds Maximum number of open file descriptors.
# TYPE process_max_fds gauge
process_max_fds 1024.0
ubuntu@OpenTel-vm-01:~$ 



## Produce load


