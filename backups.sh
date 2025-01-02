#!/bin/sh
# written by: atholcomb
# Shell script creates backups for the 8thpath.net Wordpress blog

echo "Backing up wp-content"
zip -q -r files/zips/wp-content.zip /var/www/html/8thpath
sudo chown andrew:andrew files/zips/wp-content.zip

echo "Backing up SQL database"
mysqldump --defaults-file=/home/andrew/.my.cnf -u root wordpress > files/sql/wordpress.sql

echo "Backing up wp-config.php"
cp /var/www/html/8thpath/wp-config.php files/configs/wp-config.php
