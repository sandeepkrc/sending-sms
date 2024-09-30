# sending-sms
# Bulk Email Sender from Excel

This Python script reads email addresses from an Excel file and sends an email to each address using SMTP. It can be useful for sending bulk emails in a simple and automated way.

## Features

- Reads email addresses from an Excel file.
- Sends personalized emails to each recipient.
- Utilizes SMTP for email sending.
- Supports plain text email content.
- Handles exceptions during email sending.

## Requirements

To use this script, you need to install the following Python packages:

- `pandas`: For reading the Excel file.
- `openpyxl`: For handling `.xlsx` files.
- `smtplib`: Standard Python library for sending emails.
- `email`: Standard Python library for constructing email content.

### Install required dependencies

```bash
pip install pandas openpyxl
