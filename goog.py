from flask import Flask, redirect, url_for, session
from flask_oauth import OAuth
from flask.ext.pymongo import PyMongo
GOOGLE_CLIENT_ID = '634374800667-vjdg0usk2tu32rpca7gl31pi0456gq3c.apps.googleusercontent.com'
GOOGLE_CLIENT_SECRET = 'oi5wtlGtwEnLKQcl0T_vo9av'
REDIRECT_URI = '/oauth2callback'
 
SECRET_KEY = 'development key'
DEBUG = True
 
app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
oauth = OAuth()
 
google = oauth.remote_app('google',
                          base_url='https://www.google.com/accounts/',
                          authorize_url='https://accounts.google.com/o/oauth2/auth',
                          request_token_url=None,
                          request_token_params={'scope': 'https://www.googleapis.com/auth/userinfo.email',
                                                'response_type': 'code'},
                          access_token_url='https://accounts.google.com/o/oauth2/token',
                          access_token_method='POST',
                          access_token_params={'grant_type': 'authorization_code'},
                          consumer_key=GOOGLE_CLIENT_ID,
                          consumer_secret=GOOGLE_CLIENT_SECRET)
app.config['MONGO_DBNAME'] = 'userdb'
app.config['MONGO_URI'] = 'mongodb://127.0.0.1:27017/userdb'
mongo = PyMongo(app)
 
@app.route('/lol')
def index():
    import json
    access_token = session.get('access_token')
    if access_token is None:
        return redirect(url_for('login'))
 
    access_token = access_token[0]
    from urllib2 import Request, urlopen, URLError
 
    headers = {'Authorization': 'OAuth '+access_token}
    req = Request('https://www.googleapis.com/oauth2/v1/userinfo',
                  None, headers)
    try:
        res = urlopen(req)
    except URLError, e:
        if e.code == 401:
            session.pop('access_token', None)
            return redirect(url_for('login'))
        tmp= res.read()
 
    tmp=json.loads(res.read())
    users = mongo.db.users
    login_user = users.find_one({'email' : str(tmp['email'])})
    if login_user is None:
        users.insert({'name' :str(tmp['name']), 'email':str(tmp['email'])})
    return 'lolo'
 
 
@app.route('/login')
def login():
    callback=url_for('authorized', _external=True)
    return google.authorize(callback=callback)
 
 
 
@app.route(REDIRECT_URI)
@google.authorized_handler
def authorized(resp):
    access_token = resp['access_token']
    session['access_token'] = access_token, ''
    return redirect(url_for('index'))
 
 
@google.tokengetter
def get_access_token():
    return session.get('access_token')
 
 
def main():
    app.run()
 
 
if __name__ == '__main__':
    main()
