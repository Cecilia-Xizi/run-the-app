
# GitHub Actions Setup Guide

This repository uses GitHub Actions to run tests automatically when new code is pushed up to GitHub. The configuration file for this CI build is found at ".github/workflows/python-app.yml".


To make the build pass, you'll need to first set a few repository secrets (via the "Secrets and variables" > "Actions" menu in the GitHub repo settings). Use the same environment variables and values as in your local ".env" file (except omit the quotes).


Add a repository secret called `GOOGLE_API_CREDENTIALS`, and paste the JSON content from the "google-credentials.json" file. Make sure there isn't an extra space or new line at the end!

Also add a repository secret called `GOOGLE_SHEETS_TEST_DOCUMENT_ID` and set it (see "Testing" section in README).

![](/docs/images/repository-secrets.png)
