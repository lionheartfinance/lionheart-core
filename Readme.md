# Lionheart-Core Internal Documentation

Lionheart-Core is the main repository that houses the Lionheart web application. 
Please follow these standard practices when working on the Lionheart repository. 

## Installation

This repo connects directly to our Heroku dyno. Be VERY careful when pushing updates to the master branch, especially anything affecting the following files:
- views.py
- urls.py
- settings.py


## Documentation

> Table of Contents
> 1. [Application Structure](##)
> 2. [Settings.py](##)
> 3. [Creating New Pages](##)
> 4. [Linking Static Content](##)
> 5. [Deploying to Heroku](##)

### Application Structure
---
The lionheart-core web application is structured as follows: 
```bash
├── Procfile
├── dash
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── landing_page
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   ├── fonts
│   │   ├── img
│   │   └── js
│   ├── templates
│   │   └── landing_page
|   |       ├── index.html
|   |       ├── plans.html
|   |       └── register.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── lionheart
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── settings.cpython-37.pyc
│   │   ├── urls.cpython-37.pyc
│   │   └── wsgi.cpython-37.pyc
│   ├── settings.py
│   ├── static
│   │   └── staticgoeshere.txt
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── templates
│   └── registration
│       ├── login.html
│       └── signin.html


```
### Settings.py
---
### Creating New Pages
---
### Linking Static Content
---
### Deploying to Heroku
---

 
## Contributing

Create separate branch for all edits, test in a local dev environment, push to lionheart-core.

Heroku will automatically (not set up yet) pull the update from GitHub and load to the staging (dev) server located at:

>[Lionheart Dev Server](lionheart-core-dev.herokuapp.com)





