#django-customise-history
========================

**django-customise-history** is customise history feature which is used to show the old and new value of model's change field in history action of admin panel.

------------
Installation
------------

Just use:

::

    pip install django-customise-history

Setup
=====

Add **django_customise_history** to **INSTALLED_APPS** in your settings.py, e.g.:

::

    INSTALLED_APPS = [
    ...
    'django_customise_history',
    ...


Usage
=====

Inherit from **DjangoCustomHistory** to get the custom history feature.

admin.py e.g.:

::

    
    from django.contrib import admin
    from .models import ExampleModel
    from django_customize_history.admin import DjangoCustomHistory
    
    @admin.register(ExampleModel)
    class ExampleModelAdmin(DjangoCustomHistory, admin.ModelAdmin):
        ...

Screenshot
=====
Here is screenshot of django-customize-history

![alt text](https://raw.githubusercontent.com/mayur-softices/djnago-customize-history/main/docs/_static/Change-history-CrudUser-object-5-Django-site-admin.png)