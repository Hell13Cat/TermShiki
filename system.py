import pickle
import json
def load_info(key):
	file = open("config.bin", "rb")
	res = pickle.load(file)
	return res[key]


def token_file_saver(token):
	with open('login.json', 'w') as f:
		json.dump(token, f)

def token_file_load():
	with open('login.json') as f:
		token = json.load(f)
	return token

def check_token():
	try:
		file = open("login.json", "r")
		return 1
	except:
		return 0