elections
=========

Scripts for running HKN elections.

## Usage

### Getting API credentials

You will first need the API key for OAuth. Specifically, you will need the
**service account key** from the [Google Developers console](https://console.developers.google.com/),
with the **hkn-ops** login.

12/12/2019 UPDATE: service account and scope have been temporarily migrated. Please contact
anthony.ding@hkn.mu for the service account credentials.

Download this service account key, which should be in a JSON file `hknlib.json`.
Place this file into `secret/`.

### Installing dependencies

This script won't work unless you install the dependencies:

```
pip install -r requirements.txt
```

If you followed the setup instructions from the [hknweb wiki](https://github.com/compserv/hknweb/wiki/Setup), you can install with pipenv:

```
pipenv install -r requirements.txt
```

### Scripts

The three scripts `new_members.py`, `new_officers.py`, and `old_officers.py`
should now work, using these credentials and the hknlib/election module.

## Development

Relevant docs:
- HTTP methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- Google Sheets API (v4): https://developers.google.com/sheets/api/
- Google Admin API: https://developers.google.com/admin-sdk/directory/
- Gmail API: https://developers.google.com/gmail/api/

Tasks:

- [x] Login with the right access permissions
- [x] Grab data from the spreadsheet
- [x] Hunt through the Admin API to find out how to make a new user
  - If the username is taken (you should probably check before making a user), complain (print the problematic people)
  - Ask people for a backup (which might also be taken)
- [x] Find out how to add a user to a Google Group (email list)
  - If they're an elected officer, add them to <comm>-officers@
  - If they're an assistant officer, same thing
  - If they're a 'committee member', i.e. they're on another committee but want to be added, add them to <comm>-cmembers@
- [x] Make it work
- [x] Bonus! Make it work for the member signup too, but only for cmembers + jobs + alumni
