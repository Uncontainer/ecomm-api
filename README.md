Converse ECOMM REST API Provider
================================

- Using python, flask, peewee ORM.
- Run inside a virtualenv with gunicorn.

Requirements:
------------
1. python 2.7
2. apache2
3. Working Magento ECOMM system

Install:
--------
1. sudo easy_install pip
2. sudo pip install virtualenv
3. virtualenv ecomm-api
4. cd ecomm-api && source bin/activate
5. git checkout master
6. pip install -r requirements.txt
7. Edit mysql connection information at the top of model.py
8. Edit the api_base_url at the top of app.py if different
9. Edit gunicorn.sh to change USER, GROUP, and APPDIR as needed
9. Edit deploy/gunicorn-ecomm-api.conf to change the path to gunicorn.sh.
10. sudo deploy/gunicorn-ecomm-api.conf /etc/init/
11. sudo service gunicorn-ecomm-api start
12. Edit deploy/apache-ecomm-api.conf to your likings, and copy it to apache config. 
13. Restart apache and test

Usage:
------
- API documentation is online at / or /doc of your URL (ex: server.com/api/doc or api.server.com/doc)
- Requests require a header named "token". The token is found in the Magento ECOMM system api_user table (ex: token=akjdhfkjashdgasd7fau9duyfio)