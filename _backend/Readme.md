This is a django DRF project setup initialized part.
I have organize these following things so that i dnt need do this everytime I start any project.
1. created custom setting folder to manage settings.py manually.
2. customized settings.py into three part such as: base, local, production
3. if debug is true : will run local and if debug is false will production.
4. No 4 is about Django secret key:
   i. as default generated secret key is started with djang-insecure,lets genrate a new secret key.
   ii. lets access python shell : python manage.py shell
   iii. from djang official git repo, we get a build in method get_random_key()
   iv. from djnago.core.management.utils import get_random_secret_key
   v. print(get_random_secret_key())
   vi. now that we have secret key lets select it.
5. lets store everything in env (we are using dotenv)
6. added pytest to test our project before deployment.







# command part:
requirment text:
get: pip freeze > requirements.txt
install: pip install requirements.txt
dotenv: pip install python-dotenv
pytest: pip install pytest
pytest-django: pip install pytest-django

#.gitignore:
venv/
.pytest_cache
**__pycache__/
db.sqlite3
.env
.coverage
.vscode