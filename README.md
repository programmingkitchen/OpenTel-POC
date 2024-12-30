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

# GROCERY STORE
