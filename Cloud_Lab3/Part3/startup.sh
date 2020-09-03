#!/bin/sh
yum -y install httpd
sudo systemctl enable httpd
sudo systemctl start httpd.service
usermod -a -G apache ec2-user
chown -R ec2-user:apache /var/www
chmod 2775 /var/www

wget -P /var/www/html https://achalbuck2.s3.us-east-2.amazonaws.com/index.html
wget -P /var/www/html https://achalbuck2.s3.us-east-2.amazonaws.com/second.html
wget -P /var/www/html https://achalbuck2.s3.us-east-2.amazonaws.com/style.css