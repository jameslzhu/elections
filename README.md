HKNlib
=========

Scripts for running HKN automated account related stuff. (Formerly, HKN elections)

## Usage

### Getting API credentials

You will first need the API key for OAuth. Specifically, you will need the
**service account key** from the [Google Developers console](https://console.developers.google.com/),
with the **hkn-ops** login.

12/12/2019 UPDATE: service account and scope have been temporarily migrated. Please contact
anthony.ding@hkn.mu for the service account credentials.

Download this service account key, which should be in a JSON file `hknlib.json`.
Place this file into `secret/`.

### Recommended: Creating a Virtual Environment (venv)

This script won't work unless you install the dependencies

Before installing dependencies, please create a Virtual Environment since we do lock our dependencies to certain versions

First, `cd` your terminal to the hknlib folder and it's content

Next, run the following based on your OS to create a venv Virtual Environment:
* On Linux / Mac: `python3 -m venv .venv`
* On Windows: `py -m venv .venv`

Finally activate the venv by:
* On Linux / Mac: `source .venv/bin/activate`
* On Windows: `.\.venv\Scripts\activate`

### Installing dependencies

This script won't work unless you install the dependencies:

To install with `pip`, run the following inside the hknlib folder (Recommended: Read **Creating a Virtual Environment (venv)**):
```
pip install -r requirements.txt
```

### Scripts

The three scripts `new_members.py`, `new_officers.py`, and `infosession_mailing.py`
should now work, using these credentials and the hknlib/election module.

We do not use `old_officers.py` anymore and is no longer supported and maintained.

There are various standalone scripts in the `standalone_scripts` folder that run by itself. See file comments for specific instructions. Currently, there is one for LastPass provisioning and one for the HKN Rails website automating the approval accounts process.

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
