from flask import Flask, jsonify
from flask_cognito_extended import (
    CognitoManager, login_handler,
    callback_handler, get_jwt_identity
)

app = Flask(__name__)

# Setup the flask-cognito-extended extention
app.config['COGNITO_SCOPE'] = "aws.cognito.signin.user.admin+email+openid+profile"
app.config['COGNITO_REGION'] = "us-east-1"
app.config['COGNITO_USER_POOL_ID'] = "us-east-1_xxxxxxx"
app.config['COGNITO_CLIENT_ID'] = "xxxxxxxxxxxxxxxxxxxxxxxxxx"
app.config['COGNITO_DOMAIN'] = "https://yourdomainhere.com"
app.config['COGNITO_REDIRECT_URI'] = "https://yourdomainhere/callback"
app.config['COGNITO_SIGNOUT_URI'] = "https://yourdomainhere/logout-redirect"

cognito = CognitoManager(app)


# Use @login_handler decorator on your login route
@app.route('/login', methods=['POST'])
@login_handler
def login():
    return jsonify(msg="User already signed in."), 200


# Use @callback_handler decorator on your callback route
@app.route('/callback', methods=['GET'])
@callback_handler
def callback():
    # fetch the unique 'sub' property of the User
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == '__main__':
    app.run(debug=True)
