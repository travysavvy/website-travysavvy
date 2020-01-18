# Travel Guide Website - travysavvy.com

Local development, implementation and deployment of <a href="http://travysavvy.com/" target="_blank">travysavvy.com</a>
## Local Development

Python version 3.5.3 is recommended but anything higher should also work.
### Setup
Clone the repository and `cd` into the directory. Use the following commands to build the virtual environment.
```
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
<!-- Update `SECRET_KEY` and `EMAIL_HOST_PASSWORD` in `travysavvy/settings.py` with proper values. Also update other variables (such as `EMAIL_HOST`, `STATIC_URL`, `MEDIA_URL`) if necessary. -->
### DB Migrations
```
python3 manage.py makemigrations
python3 manage.py migrate
```
### Collect Static Files
```
python3 manage.py collectstatic
```
`STATIC_ROOT` in `travysavvy/settings.py` will store the static files to deploy in the static server. The URL can be configured in `STATIC_URL` of `settings.py`.

### Create Superuser
```
python3 manage.py createsuperuser
```
If necessary, create a super user to log into the admin panel.

### Start Server
Enable debugging by changing `DEBUG=True` in `travysavvy/settings.py`
```
python3 manage.py runserver
```

## Production Deployment

### Prerequisites
- Apache2 and mod_wsgi module for Apache. 

The mod_wsgi module can be installed by `sudo apt-get install libapache2-mod-wsgi-py3`
Make sure to stop the Apache2 server and create a backup of `db.sqlite3` before deploying the latest changes.

### Setup
Build the virtual environment.
```
rm -rf venv
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```
<!-- Update `SECRET_KEY` and `EMAIL_HOST_PASSWORD` in `travysavvy/settings.py` with proper values. Also update other variables (such as `EMAIL_HOST`, `STATIC_URL`, `MEDIA_URL`) if necessary. -->

### DB Migrations
```
python3 manage.py makemigrations
python3 manage.py migrate
```
### Create Superuser
This step is not necessary if reusing an existing DB.
```
python3 manage.py createsuperuser
```
Create a super user to log into the admin panel. 
<!-- Application server emails will be sent to the mail address configured for the super user. -->

### Provide write permission for Apache
Change ownership of the website folder and DB. Change permission only if multiple users needs to write into the folder.
```
sudo chown www-data:www-data .
sudo chown www-data:www-data db.sqlite3
sudo chmod 775 .
sudo chmod 775 db.sqlite3
```
Restart the Apache application server with `sudo systemctl restart apache2.service`

## DevOps
Static file server can be configured to run along with the application server in `/etc/apache2/sites-available/<host>.conf`. The static files url should match the one in `STATIC_URL` in `travysavvy/settings.py`.
```
        ServerAdmin admin@abijith.net
        DocumentRoot /var/www/<host>

        Alias /static /var/www/<host>/staticfiles
        <Directory /var/www/<host>/staticfiles>
                Options -Indexes
        </Directory>

	    <Directory /var/www/<host>/travysavvy>
                <Files wsgi.py>
                        Require all granted
                </Files>
        </Directory>

        WSGIDaemonProcess travysavvy python-path=/var/www/<host> python-home=/var/www/<host>/venv processes=4 threads=4
        WSGIProcessGroup travysavvy  
        WSGIScriptAlias / /var/www/<host>/travysavvy/wsgi.py

```
Restart the server after adding the host `a2ensite <host>`
