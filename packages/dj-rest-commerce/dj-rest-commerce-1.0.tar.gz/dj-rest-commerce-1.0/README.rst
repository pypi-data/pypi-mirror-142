=================
dj-rest-commerce
=================

Django rest framework E-commerce package which has simple beautiful eCommerce features.

Features:
==========
1. Below some features::
    1) Product Management.
    2) Category, Brand, Model, Brand, Serial number Management.
    3) Semi-multi vendor (for the beta version).
    4) Easy order Management system.

Quick start
============

1. Add `commerce` app in your `INSTALLED_APPS` settings like this::

    INSTALLED_APPS = [
        ...
        'commerce',
        'rest_framework',
    ]

2. Include the app URLconf in your project urls.py like this::
    path('api/v1/commerce/', include('commerce.urls')),

3. Migrations file from your application then again run migration in the app::
    1) python manage.py makemigrations commerce
    2) python manage.py migrate commerce
    3) python manage.py migrate (optional if have already migrate not need to run the command again.)

API endpoint:
==============
1. Root API: ``api/v1/commerce/``
Download the postman collection from here: http://surl.li/bocru
