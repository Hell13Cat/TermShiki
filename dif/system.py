import pickle
import json
import time
def load_info(key):
	file = open("./dif/config.bin", "rb")
	res = pickle.load(file)
	return res[key]

def load_setting():
	file = open("./dif/setting.pkl", "rb")
	res = pickle.load(file)
	return res

def save_setting(setting):
	file = open("./dif/setting.pkl", "wb")
	pickle.dump(setting, file)

def load_code():
	file = open("./dif/code.pkl", "rb")
	res = pickle.load(file)
	return res

def save_code(code):
	file = open("./dif/code.pkl", "wb")
	pickle.dump(code, file)

def default_setting():
	setting = {"last_time_token" : -666, "check_update" : 0}
	file = open("./dif/setting.pkl", "wb")
	pickle.dump(setting, file)

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

def check_time():
	time_last_token = load_setting()["last_time_token"]
	if time.clock() - time_last_token >= 72000:
		return 0
	else:
		return 1

def re_time():
	#setting_my = load_setting()
	setting_my = {}
	setting_my["last_time_token"] = time.clock()
	save_setting(setting_my)


def logo_print():
	print("""╔╗───────────╔═╗╔╗─╔╗╔╗─╔╗
║╚╗╔═╗╔╦╗╔══╗║═╣║╚╗╠╣║╠╗╠╣
║╔╣║╩╣║╔╝║║║║╠═║║║║║║║═╣║║
╚═╝╚═╝╚╝─╚╩╩╝╚═╝╚╩╝╚╝╚╩╝╚╝""")