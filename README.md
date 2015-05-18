# Requirements

- OS X
- Python
- Pip
- virtualenv (optional)

# Installation

- `pip install -r REQUIREMENTS.txt`
- Edit `.env` for a ngrok subdomain to your choosing
- `honcho start`
- Configure your webhook on your repo in Bitbucket

- Access locally on http://localhost:5000
- Access remotely on http://bbwebhook.ngrok.io (set subdomain in `.env`)
- Access ngrok interface on http://localhost:4040