# Open Telemetry POC

## Git Hub Repo

# Test from VM #2 
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

