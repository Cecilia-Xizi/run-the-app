# Google Cloud Setup Guide

We will use the Google Cloud platform for user login purposes, and to interface with Google Sheets and other Google services.

After creating a project, we will configure an OAuth Client to handle user logins, and a Service Account to programmatically interface with Google Sheets and other services on our behalf.

## Project Setup

Visit the [Google Cloud Console](https://console.cloud.google.com). Create a new project, and name it.

![](/docs/images/google-cloud-project-create.png)

After it is created, select it as necessary, for example using the project selection dropdown menu at the top left.

![](/docs/images/google-cloud-project-select.png)

## OAuth Client

Visit the [API Credentials](https://console.cloud.google.com/apis/credentials) page for your Google Cloud project. Click the button with the plus icon to "Create Credentials", and choose "Create OAuth Client Id". Before moving forward, we will be prompted to set up a consent screen.

Click to "Configure Consent Screen". Choose "external" by default. Give your app a name (users might see this when they log in). Leave the domain info blank for now, and leave the defaults / skip lots of the setup for now.

![](/docs/images/oauth-consent-screen.png)


Return to actually creating the "OAuth Client Id" from the Credentials page. Choose a "Web application" type, give it a name, and set the following "Authorized Redirect URIs":

  + http://localhost:5000/auth/google/callback
  + http://127.0.0.1:5000/auth/google/callback

![](/docs/images/oauth-client-redirect-uris.png)

> FORESHADOWING: after you deploy the app to a hosted site, you will need to return here to configure an additional redirect URL pointing to your hosted site.


After the OAuth Client is created, note the `GOOGLE_CLIENT_ID` and `GOOGLE_CLIENT_SECRET`, and set them as environment variables via the ".env" file (see README).

![](/docs/images/oauth-client-secrets.png)

## Service Account Credentials

To fetch data from the Google Sheets database (and use other Google APIs), the app will need access to a local "service account" credentials file.

From the [Google API Credentials](https://console.cloud.google.com/apis/credentials) page, create a new service account, and give it "Editor" role access to your Google API project.

Find the service account you just created in the "Service Accounts" section of the Credentials page, and click on it. For the selected service account, visit the "Keys" menu to create a new JSON credentials file.

![](/docs/images/service-account-json.png)

Then download the resulting JSON key file into the root directory of this repo, and rename it to "google-credentials.json".

> NOTE: it is important to have this file in the root directory of the repository, specifically called "google-credentials.json". This file has been ignored from version control for security reasons (see ".gitignore" file), and therefore should NOT be tracked in version control or uploaded to GitHub.

## Enabling APIs

In the Google APIs project console, from the "Enabled APIs and Services" page, search for and enable the "Google Sheets API".

![](/docs/images/google-cloud-enable-apis-services.png)

If you would like to use additional APIs in the future (for example Google Calendar API for a calendar integration), you will need to come back and enable them separately.
