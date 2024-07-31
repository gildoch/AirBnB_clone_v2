echo "SHOW GRANTS FOR 'hbnb_dev'@'localhost';" | mysql -uroot -p
echo "SHOW DATABASES;" | mysql -uhbnb_test -p | grep hbnb_test_db
echo "SHOW GRANTS FOR 'hbnb_test'@'localhost';" | mysql -uroot -p