echo "Install Dev Database"
cat setup_mysql_dev.sql | mysql -hlocalhost -uroot -p

echo "Check if hbnb_dev DB is installed"
echo "SHOW DATABASES;" | mysql -uhbnb_dev -p | grep hbnb_dev_db

echo "Show DB Permissions
echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | mysql -uroot -p