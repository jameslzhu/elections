HKNlib
=========

Scripts for running HKN automated account related operations. 


### Getting API credentials
The API key is available on lastpass as `hknlib` as a JSON file called `hknlib.key`. Place this file into `secret/`.


### Recommended: Creating a Virtual Environment (venv)
If `conda` is not already available, install [conda](https://docs.conda.io/projects/conda/en/stable/user-guide/install/index.html). If you're installing `conda` for the first time, we recommend `Miniconda` over `Anaconda`. If you want to keep your default version of python, run `conda config --set auto_activate_base false`.

```bash
conda create --name hknlib python=3.7
conda activate hknlib
pip install -r requirements.txt
```


### Scripts
The two scripts `new_members.py` and `new_officers.py` should now work, using these credentials and the hknlib/election module. Use `hknlib/config/settings.json` to control which sheets they read off of.

There are various standalone scripts in the `standalone_scripts` folder that run by itself. See file comments for specific instructions. Currently, there is one for LastPass provisioning and one for the HKN Rails website automating the approval accounts process.


### Relevant docs
- HTTP methods: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- Google Sheets API (v4): https://developers.google.com/sheets/api/
- Google Admin API: https://developers.google.com/admin-sdk/directory/
- Gmail API: https://developers.google.com/gmail/api/
