[![PyPI version](https://badge.fury.io/py/sentry-auth-gitlab-v2.svg)](https://badge.fury.io/py/sentry-auth-gitlab-v2)

## Disclaimer 1
Thats a second level for of this library. This fork was made in order to prepare PyPi package and make installation process easier via supported plugins install flow.
Original fork disclamer is below.

## Disclaimer 2
I am NOT a python developer. I just changed what was necessary to make it work. This repository can be used directly or be an inspiration to others to enable Gitlab SSO with Sentry 10. These files can be installed from local folder only as no updated package is available in pip repository.

## How to install

### Install via `pip`

Use `enhance-image.sh` script to build new image with this plugin.
Create a new file `sentry/enhance-image.sh` if it is missing.
```shell
cp sentry/enhance-image.example.sh sentry/enhance-image.sh
```

Add the following line to `sentry/enhance-image.sh` file:
```shell
pip install sentry-auth-gitlab-v2
```

Then run `./install.sh` script to build new image with this plugin.

### Install from sources

Create plugins folder in `sentry` and clone this repo:
```shell
mkdir sentry/plugins
cd sentry/plugins
git clone https://github.com/zekker6/sentry-auth-gitlab.git
```

Use `enhance-image.sh` script to build new image with this plugin.
Create a new file `sentry/enhance-image.sh` if it is missing.
```shell
cp sentry/enhance-image.example.sh sentry/enhance-image.sh
```

Add the following line to `sentry/enhance-image.sh` file:
```shell
pip install /usr/src/sentry/plugins/sentry-auth-gitlab
```

### Gitlab configuration

Tested with an official [sentry/self-hosted](https://github.com/getsentry/self-hosted) installation:
- Sentry 24.1.0
- Gitlab 17.1

Create a new application under your GitLab.
Enter the **Callback URL** as the prefix to your Sentry installation:
```
http(s?)://sentry.example.com/auth/sso/
```

Once done, grab your API keys and drop them in your `sentry.conf.py`:

```python
GITLAB_APP_ID = "APP-ID"
GITLAB_APP_SECRET = "APP-SECRET"
GITLAB_BASE_DOMAIN = "git.example.com"
```

Optionally you may also specify the api version, scheme, and scope:

```python
GITLAB_API_VERSION = 4
GITLAB_AUTH_SCOPE = "api"
```

### Notice

If your gitlab is deployed in a private network (probably).
You need to alter sentry's default ip black list to make oauth flow work.

Put following config in your **sentry.conf.py** and delete conflict ones


```python
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
```
