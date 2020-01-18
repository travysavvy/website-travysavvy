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
Enable debugging by changing `DEBUG=True` in `travysavvy/settings.py`. Static files will not be served in local deployment if debugging is disabled.
```
python3 manage.py runserver
```
