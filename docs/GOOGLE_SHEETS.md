
# Google Sheets Database Setup Guide

Ensure you have followed the [Google Cloud Setup](/docs/GOOGLE_CLOUD.md) guide, specifically that you have enabled the "Google Sheets API", and have downloaded the service account JSON file into the root directory of this repository and renamed it as "google-credentials.json".

## Document Setup

Create a new Google Sheet document. Note the document identifier, and set it as the `GOOGLE_SHEETS_DOCUMENT_ID` environment variable via the ".env" file (see README). The document identifier is located between the "/d/" and "/edit", like: ".../d/DOCUMENT_ID/edit".

![image of the url bar, with the document id highlighted](/docs/images/google-sheet-document-id.png)

The app will need read and write access to this document. Modify the document's sharing settings to grant "Edit" privileges to the "client email" address specified in the Google API service account credentials JSON file (e.g. "my-serice@my-project.iam.gserviceaccount.com").

![](/docs/images/google-sheet-share-service-account-editor.png)

## Sheets Setup

In the spreadsheet document itself, create two example sheets. One called "products" and the other called "orders".

On the "products" sheet, populate the first row with the following column headers:

  + `id`
  + `name`
  + `description`
  + `price`
  + `url`
  + `created_at`

On the "orders" sheet, populate the first row with the following column headers:

  + `id`
  + `user_email`
  + `product_id`
  + `product_name`
  + `product_price`
  + `created_at`


You will notice there are corresponding "model" classes defined in the "app/models" directory. For any sheet, the fields defined in the corresponding model class need to stay consistent with the column names designated in the sheet, except the sheet will have an additional "id" column first and "created_at" column last. For more information, see the [`gspread_models` package docs](https://github.com/s2t2/gspread-models-py).
