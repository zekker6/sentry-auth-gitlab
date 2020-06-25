
.. image:: https://badge.fury.io/py/sentry-auth-gitlab-v2.svg
    :target: https://badge.fury.io/py/sentry-auth-gitlab-v2


Disclaimer 1
============
Thats a second level for of this library. This fork was made in order to prepare PyPi package and make installation process easier via supported plugins install flow.
Original fork disclamer is below.

Disclaimer 2
============
I am NOT a python developer. I just changed what was necessary to make it work. This repository can be used directly or be an inspiration to others to enable Gitlab SSO with Sentry 10. These files can be installed from local folder only as no updated package is available in pip repository.

How to
======

Main problem
------------

Django has been updated in Sentry 10 and previous scripts don't work anymore.

Install
-------

Add `sentry-auth-gitlab-v2` to list of plugins at `sentry/requirements.txt`.

Setup Gitlab Auth configuration for Sentry as mentioned in original documentation bellow

Stop, rebuild and restart your Sentry docker containers to accept new configuration and plugins

.. code-block:: bash

  docker-compose down
  docker-compose build
  docker-compose up -d


It **should** work.
Tested with sentry 20.6.0 and official sentry/onpremise installation.

GitLab Auth for Sentry
======================
v0.1.0

An SSO provider for Sentry which enables GitLab Login

Changes made for Gitlab 9.x
----------
Following configuration has been changed

.. code-block:: python

  # You can specify scope to "api" in Gitlab's OAuth Application page
  # If you failed to do that, set GITLAB_AUTH_SCOPE = "read_user"
  GITLAB_AUTH_SCOPE = "api"
  # If your gitlab does not support v4 api, set GITLAB_API_VERSION = 3
  GITLAB_API_VERSION = 4


Install
-------

::

    pip install sentry-auth-gitlab-v2

Setup
-----

Create a new application under your GitLab.
Enter the **Callback URL** as the prefix to your Sentry installation:

::

    http(s?)://sentry.example.com/auth/sso/


Once done, grab your API keys and drop them in your ``sentry.conf.py:

.. code-block:: python

    GITLAB_APP_ID = "APP-ID"
    GITLAB_APP_SECRET = "APP-SECRET"
    GITLAB_BASE_DOMAIN = "git.example.com"


Optionally you may also specify the api version, scheme, and scope:

.. code-block:: python

    GITLAB_API_VERSION = 4
    GITLAB_AUTH_SCOPE = "api"
    GITLAB_HTTP_SCHEME = "https"


Notice
------

If your gitlab is deployed in a private network (probably).
You need to alter sentry's default ip black list to make oauth flow work.

Put following config in your **sentry.conf.py** and delete conflit ones

.. code-block:: python

    SENTRY_DISALLOWED_IPS = (
        '0.0.0.0/8',
        '10.0.0.0/8',
        '100.64.0.0/10',
        '127.0.0.0/8',
        '169.254.0.0/16',
        '172.16.0.0/12',
        '192.0.0.0/29',
        '192.0.2.0/24',
        '192.88.99.0/24',
        '192.168.0.0/16',
        '198.18.0.0/15',
        '198.51.100.0/24',
        '224.0.0.0/4',
        '240.0.0.0/4',
        '255.255.255.255/32'
    )
