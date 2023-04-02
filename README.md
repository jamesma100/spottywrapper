# spottywrapper

Flask-based wrapper around Spotify's Client API.

## Setup
```bash
$ git clone git@github.com:jamesma100/spottywrapper.git
$ cd spottywrapper
$ python3 -m venv venv
$ source ./venv/bin/activate
$ (venv) pip install flask os requests base64 argparse
$ (venv) python3 app.py --id <your client id> --secret <your client secret>
```

Then login with your Spotify account at `http://127.0.0.1:5000/login` 🚀
