from flask import Flask, redirect, request
import requests
import base64
import argparse

app = Flask(__name__)

CLIENT_ID=""
CLIENT_SECRET=""
AUTHORIZE_URI="https://accounts.spotify.com/authorize"
TOKEN_URI="https://accounts.spotify.com/api/token"
REDIR_URI="http://localhost:5000/callback"

def init_client():
	parser = argparse.ArgumentParser(description="Parse client data")
	parser.add_argument("--id", type=str, help="Client id")
	parser.add_argument("--secret", type=str, help="Client secret")
	args = parser.parse_args()
	CLIENT_ID, CLIENT_SECRET = args.id, args.secret

def base64encode(s):
	s_in_bytes = s.encode("ascii")
	s_in_b64_bytes = base64.b64encode(s_in_bytes)
	s_b64_str = s_in_b64_bytes.decode("ascii")
	return s_b64_str

@app.route("/")
def hello_world():
	return "<p>Hello world!</p>"

@app.route("/error")
def error():
	return "<p>Encountered generic error</p>"

@app.route("/login")
def login():
	payload = {
		"client_id": CLIENT_ID,
		"response_type": "code",
		"redirect_uri": REDIR_URI
	}
	r = requests.get(AUTHORIZE_URI, params=payload)
	print("Authorize status: ", r.status_code)
	return redirect(r.url)

@app.route("/callback")
def callback():
	code = request.args.get("code")
	state = request.args.get("state")

	secret_str = CLIENT_ID + ":" + CLIENT_SECRET
	secret_str_encoded = base64encode(secret_str)

	payload = {
		"code": code,
		"redirect_uri": REDIR_URI,
		"grant_type": "authorization_code"
	}
	headers = {
		"Authorization": "Basic " + secret_str_encoded,
		"Accept": "application/json"
	}
	r = requests.post(TOKEN_URI, data=payload, headers=headers)
	print("Token fetch status: ",r.status_code)
	print(r.json())
	return "<p>Entered callback route</p>"

if __name__ == "__main__":
	init_client()
	app.run(debug=True)
