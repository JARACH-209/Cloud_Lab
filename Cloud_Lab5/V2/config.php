<?php
/* Database credentials. Assuming you are running MySQL
server with default setting (user 'root' with no password) */
define('DB_SERVER', 'lab5.coddw0p8k4sn.us-east-2.rds.amazonaws.com');
define('DB_USERNAME', 'boto3_user');
define('DB_PASSWORD', 'boto3_password');
define('DB_NAME', 'lab5_portal');
 
/* Attempt to connect to MySQL database */
$link = mysqli_connect(DB_SERVER, DB_USERNAME, DB_PASSWORD, DB_NAME);
 
// Check connection
if($link === false){
    die("ERROR: Could not connect. " . mysqli_connect_error());
}
?>