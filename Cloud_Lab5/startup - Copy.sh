#!/bin/sh
sudo yum -y install httpd
sudo yum install -y httpd24 php56 php56-mysqlnd
sudo systemctl enable httpd
sudo systemctl start httpd.service
sudo service httpd start
sudo chkconfig httpd on
sudo groupadd www  
sudo usermod -a -G apache ec2-user
sudo chown -R ec2-user:apache /var/www
sudo chgrp -R www /var/www 
sudo chmod 2775 /var/www
find /var/www -type d -exec sudo chmod 2775 {} +     
find /var/www -type f -exec sudo chmod 0664 {} +



cd /var/www
mkdir inc

wget -P /var/www/inc https://achalbuck2.s3.us-east-2.amazonaws.com/dbinfo.inc

wget -P /var/www/html https://achalbuck2.s3.us-east-2.amazonaws.com/welcome.php
wget -P /var/www/html https://achalbuck2.s3.us-east-2.amazonaws.com/index.php
wget -P /var/www/html https://achalbuck2.s3.us-east-2.amazonaws.com/logout.php
wget -P /var/www/html https://achalbuck2.s3.us-east-2.amazonaws.com/reset-password.php
wget -P /var/www/html https://achalbuck2.s3.us-east-2.amazonaws.com/register.php
wget -P /var/www/html https://achalbuck2.s3.us-east-2.amazonaws.com/config.php