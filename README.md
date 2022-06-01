# Financial email automation

The purpose of this project is to automatically generate an HTML template with finanacial information and send it by email to a list of contacts.

## Before you start

### Prerequisites

* Installed python
* Basic knowledge of Unix/Linux Shell commands

### Local configuration

1. Clone repository
```sh
git clone git@github.com:benjaminlozanow/financial_email_bot.git
```

2. Install requirements
```sh
pip install -r requirements.txt
```

3. Log into [Yahoo Finance API](https://www.yahoofinanceapi.com/) and get you API key and copy it to a file with environmental variables.

4. The same file with environmental variables must contain the sender email address and the list of recievers email addresses.

5. Enable your gmail account to send emails though python with the following [guide](https://developers.google.com/gmail/api/quickstart/python).

## Files
- [generate_email.py](https://github.com/benjaminlozanow/financial_email_bot/blob/main/generate_email.py) is a script that consumes the [Yahoo Finance API](https://www.yahoofinanceapi.com/) extracting information about stock, indexes and cryptocurrencies. This data is used to edit the template HTML file [base_email.html](https://github.com/benjaminlozanow/financial_email_bot/blob/main/base_email.html).

- [email_bot.py](https://github.com/benjaminlozanow/financial_email_bot/blob/main/email_bot.py) is a script that sends an email containing the previously generated HTML ([out_email.html](https://github.com/benjaminlozanow/financial_email_bot/blob/main/out_email.html)) to a list of contacts.

## Usage

Run following shell commands in your local repository:
```
python generate_email.py  
```
```
python email_bot.py  
```

## Contribution

Feel free to optimize/modify the code to have better or different results.
