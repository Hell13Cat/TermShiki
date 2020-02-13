import pickle
import json
def load_info(key):
	file = open("./dif/config.bin", "rb")
	res = pickle.load(file)
	return res[key]


def token_file_saver(token):
	with open('./dif/login.json', 'w') as f:
		json.dump(token, f)

def token_file_load():
	with open('./dif/login.json') as f:
		token = json.load(f)
	return token

def check_token():
	try:
		file = open("./dif/login.json", "r")
		return 1
	except:
		return 0

def logo_print():
	print("""╔════╗╔═══╗╔═══╗╔═╗╔═╗╔═══╗╔╗─╔╗╔══╗╔╗╔═╗╔══╗
║╔╗╔╗║║╔══╝║╔═╗║║║╚╝║║║╔═╗║║║─║║╚╣─╝║║║╔╝╚╣─╝
╚╝║║╚╝║╚══╗║╚═╝║║╔╗╔╗║║╚══╗║╚═╝║─║║─║╚╝╝──║║─
──║║──║╔══╝║╔╗╔╝║║║║║║╚══╗║║╔═╗║─║║─║╔╗║──║║─
──║║──║╚══╗║║║╚╗║║║║║║║╚═╝║║║─║║╔╣─╗║║║╚╗╔╣─╗
──╚╝──╚═══╝╚╝╚═╝╚╝╚╝╚╝╚═══╝╚╝─╚╝╚══╝╚╝╚═╝╚══╝""")