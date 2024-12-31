# OPEN TELEMETRY POC


# NON-AUTOMOTED STUFF

## Git Hub Repo

```
echo "# OpenTel-POC" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:programmingkitchen/OpenTel-POC.git
git push -u origin main

git config --global user.email "programmingkitchen@gmail.com"
git config --global user.name "PK VM #1"
git config --global user.name "PK VM #2"
git config --global user.name "PK VM #3"

git clone git@github.com:programmingkitchen/OpenTel-POC.git

$ cat config
Host 10.*
        StrictHostKeyChecking no
        UserKnownHostsFile=/dev/null
Host github.com
  HostName github.com
  IdentitiesOnly yes
  IdentityFile ~/.ssh/id_rsa_github
  user git
```

## /etc/hosts file

10.111.2.5 front
10.111.2.4 back
10.111.2.6 store 

## User Account Configuration 
 
 - Docker

ubuntu@OpenTel-vm-02:~$ grep docker /etc/group
docker:x:998:ubuntu

- For other users like "elk"

ubuntu@OpenTel-vm-02:~$ grep elk /etc/passwd
elk:x:1001:1001:Elk,,,:/home/elk:/bin/bash

ubuntu@OpenTel-vm-02:~$ grep elk /etc/group
sudo:x:27:ubuntu,elk
elk:x:1001:

### Sudo configuration 

```
/etc/sudoers.d/90-cloud-init-users

root@OpenTel-vm-02:/etc/sudoers.d# grep sudo /etc/group
sudo:x:27:ubuntu,elk

# User rules for ubuntu
ubuntu ALL=(ALL) NOPASSWD:ALL

# User rules for elk 
elk ALL=(ALL) NOPASSWD:ALL
```


## Python virtual environment

python --version 
python3 --version 

ubuntu@OpenTel-vm-03:~/OpenTel-POC$ python3 --version 
Python 3.8.10

- Make the directory for the virtual environment
mkdir .opentel

- Install the python virtual environment

sudo apt install python3.8-venv

python3 -m venv .opentel 

source ~/.opentel/bin/activate \r

ubuntu@OpenTel-vm-02:~$ source ~/.opentel/bin/activate 
(.opentel) ubuntu@OpenTel-vm-02:~$ pip list
Package       Version
------------- -------
pip           20.0.2 
pkg-resources 0.0.0  
setuptools    44.0.0 

deactivate \r




## Open Tel Packages

pip install flask requests

(.opentel) ubuntu@OpenTel-vm-01:~$ pip list
Package            Version   
------------------ ----------
blinker            1.8.2     
certifi            2024.12.14
charset-normalizer 3.4.1     
click              8.1.8     
flask              3.0.3     
idna               3.10      
importlib-metadata 8.5.0     
itsdangerous       2.2.0     
jinja2             3.1.5     
MarkupSafe         2.1.5     
pip                20.0.2    
pkg-resources      0.0.0     
requests           2.32.3    
setuptools         44.0.0    
urllib3            2.2.3     
werkzeug           3.0.6     
zipp               3.20.2    
(.opentel) ubuntu@OpenTel-vm-01:~$ 



pip install opentelemetry-api opentelemetry-sdk


pip freeze | grep opentelemetry

(.opentel) ubuntu@OpenTel-vm-01:~$ pip freeze | grep opentelemetry
opentelemetry-api==1.29.0
opentelemetry-sdk==1.29.0
opentelemetry-semantic-conventions==0.50b0
(.opentel) ubuntu@OpenTel-vm-01:~$ 


## Test Run

(.opentel) ubuntu@OpenTel-vm-01:~/OpenTel-POC/mycode$ python3 test.py 
(.opentel) ubuntu@OpenTel-vm-01:~/OpenTel-POC/mycode$ 






# GROCERY STORE

## Docker compose commands

Need to cd into Chapter 2

~/OpenTel-POC/Cloud-Native-Observability/chapter02

docker compose help


ubuntu@OpenTel-vm-03:~/OpenTel-POC/Cloud-Native-Observability/chapter02$ docker compose up
WARN[0000] /home/ubuntu/OpenTel-POC/Cloud-Native-Observability/chapter02/docker-compose.yml: the attribute `version` is obsolete, it will be ignored, please remove it to avoid potential confusion 
[+] Running 10/10
 ✔ Network chapter02_cloud-native-observability  Created                                                                                       0.2s 
 ✔ Container prometheus                          Created                                                                                       1.7s 
 ✔ Container opentelemetry-collector             Created                                                                                       1.5s 
 ✔ Container jaeger                              Created                                                                                       1.7s 
 ✔ Container loki                                Created                                                                                       1.6s 
 ✔ Container grafana                             Created                                                                                       1.6s 
 ✔ Container promtail                            Created                                                                                       1.6s 
 ✔ Container inventory                           Created                                                                                       0.7s 
 ✔ Container grocery-store                       Created                                                                                       0.7s 
 ✔ Container shopper                             Created                                                                                       0.5s 
Attaching to grafana, grocery-store, inventory, jaeger, loki, opentelemetry-collector, prometheus, promtail, shopper




ubuntu@OpenTel-vm-03:~$ docker compose ls
NAME                STATUS              CONFIG FILES
chapter02           running(9)          /home/ubuntu/OpenTel-POC/Cloud-Native-Observability/chapter02/docker-compose.yml



docker compose stats

CONTAINER ID   NAME                      CPU %     MEM USAGE / LIMIT    MEM %     NET I/O           BLOCK I/O        PIDS
1bafa7d87c36   shopper                   0.86%     35.65MiB / 3.33GiB   1.05%     272kB / 605kB     20.3MB / 0B      8
55533000d7db   grocery-store             3.88%     76.26MiB / 80MiB     95.32%    509kB / 783kB     24.5MB / 0B      17
838a9340fe25   inventory                 3.48%     72.33MiB / 80MiB     90.42%    299kB / 468kB     33.2MB / 0B      17
186f9eaaabcd   prometheus                0.00%     26.93MiB / 3.33GiB   0.79%     273kB / 58.2kB    59.2MB / 115kB   8
586763016d43   jaeger                    0.09%     25.49MiB / 3.33GiB   0.75%     952kB / 2.96MB    31.8MB / 0B      6
1cd01e77a426   grafana                   0.02%     35.51MiB / 3.33GiB   1.04%     12.7kB / 3.77kB   68.4MB / 365kB   11
86117f7d5bac   promtail                  0.26%     23.43MiB / 3.33GiB   0.69%     8.47kB / 208kB    54.5MB / 156kB   8
126cc2a77e22   loki                      0.12%     32.37MiB / 3.33GiB   0.95%     388kB / 36.7kB    51.7MB / 115kB   9
d176718809b1   opentelemetry-collector   0.19%     35.69MiB / 3.33GiB   1.05%     1.07MB / 1.43MB   85.9MB / 0B      7

docker compse logs


opentelemetry-collector  | Value: 0.009000
opentelemetry-collector  | 
opentelemetry-collector  | 2024-12-30T23:23:20.004Z     INFO    loggingexporter/logging_exporter.go:54  MetricsExporter {"#metrics": 1}
opentelemetry-collector  | 2024-12-30T23:23:20.005Z     DEBUG   loggingexporter/logging_exporter.go:64  ResourceMetrics #0
opentelemetry-collector  | Resource SchemaURL: 
opentelemetry-collector  | Resource labels:
opentelemetry-collector  |      -> telemetry.sdk.language: STRING(python)
opentelemetry-collector  |      -> telemetry.sdk.name: STRING(opentelemetry)
opentelemetry-collector  |      -> telemetry.sdk.version: STRING(1.9.1)
opentelemetry-collector  |      -> net.host.name: STRING(1bafa7d87c36)
opentelemetry-collector  |      -> net.host.ip: STRING(172.18.0.10)
opentelemetry-collector  |      -> service.name: STRING(shopper)






## Jaeger
http://grocerystore.programmingkitchen.com:16686/search