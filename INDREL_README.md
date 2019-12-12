indrel
======

Scripts for sending infosession emails out to companies.

## Usage

### Getting API credentials

You will first need the API key for OAuth. Specifically, you will need the
**service account key** from the [Google Developers console](https://console.developers.google.com/),
with the **hkn-ops** login.

12/12/2019 UPDATE: service account and scope have been temporarily migrated. Please contact
anthony.ding@hkn.eecs.berkeley.edu for the service account credentials.

Download this service account key, which should be in a JSON file `hknlib.json`.
Place this file into `secret/`.

### Installing dependencies

This script won't work unless you install the dependencies:

```
pip install -r requirements.txt
```

### Updating settings

Go into `hknlib/indrel/settings.py` to update the fields.

### Scripts
The main script to run is `indrel.py`, which also takes in an optional command-line argument
givenby the `--file` flag if you would like to attach a file to the email. Example usage:

```
python3 indrel.py --file ./indrel.pdf
```
