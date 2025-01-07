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



## Produce load


