#!/bin/bash

# Update OS
echo "update OS"
apt update && apt upgrade -y

# Reinstall python3 into version 3.11
echo "Install python version 3.10"
apt install python3.10 -y

# Update default python version
update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.10 1
update-alternatives --config python3

# Install pip3 and dependencies package
apt-get install python3-pip -y
pip3 install --no-cache-dir --upgrade -r requirements.txt

# Install Docker Engine
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do apt-get remove $pkg; done

# Add Docker's official GPG key:
apt-get update
apt-get install ca-certificates curl gnupg
install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

# Add the repository to Apt sources:
echo \
  "deb [arch="$(dpkg --print-architecture)" signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  "$(. /etc/os-release && echo "$VERSION_CODENAME")" stable" | \
  tee /etc/apt/sources.list.d/docker.list > /dev/null
apt-get update

apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y

# Run docker compose file
docker compose up -d

sleep 10
python3 -m alembic upgrade head

touch /var/log/activate_scheduler.log
cp scripts/scheduler.sh /

python3 healthcheck_db.py
python3 initialize_db_data.py

chmod 0744 ./crontabs/activate-dumpuser-cron
crontab ./crontabs/activate-dumpuser-cron

touch /var/log/dumpuser_service.log
python3 -m gunicorn main:app --bind 0.0.0.0:8080 -w 6 -k uvicorn.workers.UvicornWorker > /var/log/dumpuser_service.log 2>&1 &
