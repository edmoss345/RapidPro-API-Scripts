# Update Contact Group Script

This repository contains a Python script, `update_group.py`, that updates contact groups in [RapidPro](https://rapidpro.io/) based on contact UUIDs listed in an Excel file. It uses the RapidPro API via the `temba-client` library.

## 📋 Features

- Reads contact UUIDs from an Excel file
- Retrieves existing contact groups from RapidPro
- Adds a specified group to contacts (if not already present)
- Skips a specified "problem group" that should not be modified
- Loads API credentials securely from a JSON file (`api_credentials.json`)

---

## 🔧 Requirements

- Python 3.8+
- Virtual environment (`.venv`) recommended
- Excel file with a sheet containing a `UUID` column

---

## 🔐 Setup Credentials

Create a file named `api_credentials.json` in the root of the project with the following structure:

```json
{
  "api_url": "https://app.rapidpro.io/",
  "api_token": "your-rapidpro-api-token"
}
```

⚠️ **Do not share this file or commit it to version control.**

---

## 📦 Installation

Setup

1. Clone or fork the repo to a local folder
1. Install Python >= 3.8
1. Create a Python virtual environment `python -m venv .venv`
1. Activate the environment:
    - Linux: `source .venv/bin/activate`
    - Windows: `.venv/Scripts/activate`
1. Upgrade pip `pip install --upgrade pip`
1. Install project Python dependencies `pip install -r requirements.txt`

## 🚀 Usage

Update the Excel file path and group name inside `update_group.py` as needed, then run:

```bash
python update_group.py
```

Make sure your Excel file contains a sheet (e.g., `test group`) with a column labeled `UUID`.

---

## ✅ Best Practices

- Always activate the `.venv` environment before running the script
- Store sensitive data (like API tokens) **only** in `api_credentials.json`
- Never commit credentials to version control
- Consider logging output to a file for record-keeping

---

## 🧹 Troubleshooting

- Ensure the UUID column is correctly labeled and populated
- Make sure your API token has the correct permissions
- Check that the contact exists in RapidPro before updating

---

## 📄 License

This project is for internal use. Contact the maintainer before redistribution or reuse.
