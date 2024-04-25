# Deployment Guide

This document provides instructions for how to host this application on a user-facing production server provided by the Render platform.

References:

  + https://render.com/docs/deploy-flask

## Repo Setup

Ensure the `gunicorn` package is listed in the "requirements.txt" file and commit and push before moving forward. This step has been done already.

## Google Sheet Setup, Revisited

You may want to create a separate copy of the Google Sheet database to use in production. If you do, specify the production document's identifier as the `GOOGLE_SHEETS_DOCUMENT_ID` environment variable when configuring the server (see below). This will allow you to keep user data separate from development and test data.


## Render Setup

Login to [Render](https://dashboard.render.com), perhaps using your GitHub account. Once logged in, visit the dashboard.

Create a New Web Service using the button at the top right. Specify the GitHub repo URL via "Public Git repository" option at the bottom.

Specify the following start command:

```sh
gunicorn "web_app:create_app()"
```

Choose instance type of "Free".

Set environment variables (omitting the quotes), including two new variables for the production server:

```sh
GOOGLE_CLIENT_ID="______.apps.googleusercontent.com"
GOOGLE_CLIENT_SECRET="______"
GOOGLE_SHEETS_DOCUMENT_ID="___________"

#
# production server specific variables:
#

# use this exact path (see secret config file setup below):
GOOGLE_CREDENTIALS_FILEPATH="/etc/secrets/google-credentials.json"

# use your own random string password (for encrypting user data stored in the session)
SECRET_KEY="___________"
```

Set a [secret configuration file](https://community.render.com/t/using-google-application-credentials-json/6885) called "google-credentials.json", and paste the contents from your google service account credentials JSON file. Make sure there isn't an extra space or new line at the end! The render web service will then have access to the file as "/etc/secrets/google-credentials.json" (as designated by the `GOOGLE_CREDENTIALS_FILEPATH` environment variable set on the server).

Click "Create web service" and wait a few moments as your code is deployed. Then visit the hosted site at the designated URL.

> FYI: the free tier can take a few moments to spin up after periods of inactivity. It is possible to upgrade server tiers later to remove this limitation.

## Google Cloud Setup, Revisited

To make the login functionality work, revisit the OAuth Client setup (see Google Cloud Setup Guide), and configure a new redirect URL pointing to the render server (like "https://YOUR_RENDER_APP.onrender.com/auth/google/callback"), and save the changes.

FYI - while the OAuth Client is still in test mode, you may need to allow certain individuals to use the hosted app, by specifing a number of email addresses as "Test Users" in the OAuth Consent Screen. Once your app is out of test mode, anyone with a Google Account should be able to login to the hosted app.
