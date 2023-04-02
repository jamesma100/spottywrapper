import os
import requests

def get_client_id():
	parser = argparse.ArgumentParser(description="Parse client data")
	parser.add_argument("--id", type=str, help="Client id")
	args = parser.parse_args()
	return args.id

def main():
	uri = "https://accounts.spotify.com/authorize"
	redir = "http://localhost:8080"
	payload = {
		"client_id": get_client_id(),
		"response_type": "code",
		"redirect_uri": redir
	}
	r = requests.get(uri, params=payload)
	print("Status: ", r.status_code)
	for resp in r.history:
		print(resp.status_code, resp.url)
	return 0

if __name__ == "__main__":
	main()
