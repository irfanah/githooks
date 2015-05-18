import os

from pync import Notifier

from flask import Flask  
from flask import request  
app = Flask(__name__)

# check for ngrok subdomain
ngrok = ''
if 'NGROK_SUBDOMAIN' in os.environ:
    ngrok = os.environ['NGROK_SUBDOMAIN']

html_message = 'Webhook server online! Go to <a href="https://bitbucket.com">Bitbucket</a> to configure your repository webhook for your <a href="http://%s.ngrok.io/webhook">http://%s.ngrok.io/webhook</a> <br />\
            You can access ngrok\'s web interface via <a href="http://localhost:4040">http://localhost:4040</a>' % (ngrok,ngrok)

def displayIntro():
    if ngrok:
        print 'You can access this webhook publicly via at http://%s.ngrok.io/webhook' % ngrok
    print 'You can access ngrok\'s web interface via http://localhost:4040'

@app.route('/', methods=['GET'])
def index():  
    if ngrok:
        return html_message
    else:
        print 'Webhook server online! Go to Bitbucket to configure you webhook'

@app.route('/webhook', methods=['GET', 'POST'])
def tracking():  
    if request.method == 'POST':
        data = request.get_json()
        commit_author = data['actor']['username']
        commit_hash = data['push']['changes'][0]['new']['commit']['hash'][:7]
        commit_url = data['push']['changes'][0]['new']['commit']['links']['html']['href']
        Notifier.notify('%s committed %s\nClick to view in Bitbucket' % (commit_author, commit_hash), title='Webhook received!', open=commit_url)
        return 'OK'
    else:
        if ngrok:
            return html_message
        else:
            print 'Webhook server online! Go to Bitbucket to configure you webhook'

if __name__ == '__main__':
    displayIntro()
    app.run(host='0.0.0.0', port=5000, debug=True)