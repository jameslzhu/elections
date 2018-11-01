elections
=========

Scripts for running HKN elections.

Relevant docs:
- HTTP methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- Google Sheets API (v4): https://developers.google.com/sheets/api/
- Google Admin API: https://developers.google.com/admin-sdk/directory/

Tasks:

- [x] Login with the right access permissions
- [x] Grab data from the spreadsheet
- [ ] Hunt through the Admin API to find out how to make a new user
  - If the username is taken (you should probably check before making a user), complain (print the problematic people)
  - Ask people for a backup (which might also be taken)
- [ ] Find out how to add a user to a Google Group (email list)
  - If they're an elected officer, add them to <comm>-officers@
  - If they're an assistant officer, same thing
  - If they're a 'committee member', i.e. they're on another committee but want to be added, add them to <comm>-cmembers@
- [ ] Make it work
  
Bonus! Make it work for the member signup too, but only for cmembers + jobs + alumni

This script won't work unless you install the dependencies:

```
pip install -r requirements.txt
```

If you followed the setup instructions from the [hknweb wiki](https://github.com/compserv/hknweb/wiki/Setup), you can install with pipenv:

```
pipenv install -r requirements.txt
```
