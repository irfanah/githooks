This repository sets up a simple Flask server to receive [Bitbucket](https://bitbucket.com) webhooks and notifies you via Mac OS X Notification Center

# Requirements

- Mac OS X 10.8+
- Python
- Pip
- virtualenv (optional)

# Installation

- `pip install -r REQUIREMENTS.txt`
- Edit `.env` for a ngrok subdomain of your choosing
- `honcho start` to start the ngrok tunnel and Flask server (`python listener.py` to start without ngrok)
- Configure your webhook (default: http://bbwebhook.ngrok.io/webhook) on your repo in Bitbucket

# Access

- Access locally on http://localhost:5000
- Access remotely on http://bbwebhook.ngrok.io (subdomain is set in `.env`)
- Access ngrok interface on http://localhost:4040

# Thanks

This repo uses:

- Microframework: [Flask](http://flask.pocoo.org/)
- Python Foreman clone: [Honcho](https://github.com/nickstenning/honcho)
- Python wrapper for Mac OS 10.8 Notification Center: [pync](https://github.com/setem/pync/)

# License

The MIT License (MIT)

Copyright (c) 2015 Atlassian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
