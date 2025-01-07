
- This library seems to have gone under changes.  Problems with imports.  

opentelemetry.sdk._logs.export

BatchLogProcessor vs. BatchLogRecordProcessor

ImportError: cannot import name 'BatchLogProcessor' from 'opentelemetry.sdk._logs.export' (/home/ubuntu/.opentel/lib/python3.8/site-packages/opentelemetry/sdk/_logs/export/__init__.py)

ImportError: cannot import name 'LogEmitterProvider' from 'opentelemetry.sdk._logs' (/home/ubuntu/.opentel/lib/python3.8/site-packages/opentelemetry/sdk/_logs/__init__.py)





(.opentel) ubuntu@OpenTel-vm-01:~/OpenTel-POC/mycode$ cd ~/OpenTel-POC/mycode; python metrics-02.py 
Traceback (most recent call last):
  File "metrics-02.py", line 22, in <module>
    configure_meter_provider()
  File "metrics-02.py", line 13, in configure_meter_provider
    reader = PrometheusMetricReader(prefix="MetricExampleRJG")
TypeError: __init__() got an unexpected keyword argument 'prefix'
(.opentel) ubuntu@OpenTel-vm-01:~/OpenTel-POC/mycode$ 


def configure_meter_provider():
    start_http_server(port=8000, addr="localhost")
    reader = PrometheusMetricReader(prefix="MetricExampleRJG")


