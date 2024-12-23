# Open Telemetry POC

## Git Hub Repo

echo "# OpenTel-POC" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:programmingkitchen/OpenTel-POC.git
git push -u origin main


$ cat config
Host 10.*
        StrictHostKeyChecking no
        UserKnownHostsFile=/dev/null
Host github.com
  HostName github.com
  IdentitiesOnly yes
  IdentityFile ~/.ssh/id_rsa_github
  user git

