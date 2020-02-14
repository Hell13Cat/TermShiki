#pylint:disable=E1111
print("TermSiki v 0.0.3a")
print("[i]Загрузка модулей...")
import os
import json
import webbrowser
import pickle
from pprint import pprint
try:
	import requests
except:
	print("[e]requests не установлен\n[i]Установка модуля requests...")
	os.system("pip install requests")
	print("[i]Готово")
try:
	from prettytable import PrettyTable
except:
	print("[e]requests не установлен\n[i]Установка модуля prettytable...")
	os.system("pip install prettytable")
	print("[i]Готово")
try:
	from pyshikiapi import API
except:
	print("[e]pyshikiapi не установлен\n[i]Установка модуля prettytable...")
	os.system("pip install pyshikiapi")
	print("[i]Готово")
import dif.system as system
from dif.git import ver_control
print("[i]Успешно")

app_name = system.load_info("app_name")
client_id = system.load_info("client_id")
client_secret = system.load_info("client_secret")

def clearShell():
	os.system(['clear', 'cls'][os.name == os.sys.platform])

def request_top(api, page):
	req_get_data = api.animes.GET(page=page, limit=10)
	x = PrettyTable()
	x.field_names = ["Рейтинг", "Называние"]
	for req_get_one in req_get_data:
		x.add_row([req_get_one["score"] ,req_get_one["russian"]])
	print(x)

def request_profile_print(jsn):
	pass
#	x = PrettyTable()
#	x.field_names = ["Рейтинг", "Называние"]
#	for req_get_one in req_get_data:
#		x.add_row([req_get_one["score"] ,req_get_one["russian"]])
	
def request_profile(api, id):
	try:
		temp = int(id)
		type = "id"
	except:
		type = "nick"
	if type == "id":
		req_get_data = api.users(id).GET()
		del req_get_data["about_html"]
		del req_get_data["about"]
		del req_get_data["image"]
		del req_get_data["stats"]["activity"]
		pprint(req_get_data)
	else:
		print("[e]Нужен id пользователя")

def request_profile_me(api):
	req_get_data = api.users("whoami").GET()
	return req_get_data

if system.load_setting()["last_time_token"] == -666:
	cont = 0
	while cont == 0:
		print("[q]Проверять обновления при запуске?")
		check_update_input = input(">")
		if check_update_input == "y":
			setting_start = system.load_setting()
			setting_start["check_update"] = 1
			system.save_setting(setting_start)
			cont = 1
		elif check_update_input == "n":
			setting_start = system.load_setting()
			setting_start["check_update"] = 0
			system.save_setting(setting_start)
			cont = 1
		else:
			pass

print("[i]Проверка авторизации...")
if system.check_token()==0:
	api = API(app_name, client_id, client_secret, token_update_callback=system.token_file_saver)
	avtorizurl = api.authorization_url
	print("[i]Сейчас ссылка для авторизации откроется в браузере. Пожалуйста разрешите доступ и введите полученный код сюда.")
	webbrowser.open(avtorizurl, new=0, autoraise=True)
	code = input(">")
	system.save_code(code)
	system.re_time()
	api.fetch_token(code)
else:
	if system.check_time() == 0:
		api = API(app_name, client_id, client_secret, token_update_callback=system.token_file_saver)
		system.re_time()
		api.fetch_token(system.load_code())
	else:
		api = API(app_name, client_id, client_secret, system.token_file_load())
		print("[i]Авторизация была совершена ранее")

clearShell()
system.logo_print()
ver_control("0.0.3a")

print("[i]help - для помощи")
exit = "0"
while exit == "0":
	cmd_full = input(">")
	cmd_split = cmd_full.split(" ")
	cmd_root = cmd_split[0]
	if cmd_root == "exit":
		print("[i]Выход из приложения...")
		exit = "1"
	elif cmd_root == "default":
		print("[i]Сброс приложения до изначального состояния и выход...")
		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), './dif/login.json')
		system.save_code("no")
		system.default_setting()
		os.remove(path)
		exit = "1"
	elif cmd_root == "cls":
		clearShell()
	elif cmd_root == "bug":
		print("[i]Отрываем браузер...")
		url_issues = "https://github.com/Hell13Cat/TermShiki/issues"
		webbrowser.open(url_issues, new=0, autoraise=True)
	elif cmd_root == "top":
		try:
			aaa = int(cmd_split[1])
			request_top(api, aaa)
		except:
			request_top(api, 1)
	elif cmd_root == "profile":
		try:
			id_prof = cmd_split[1]
			request_profile(api, id_prof)
		except:
			request_profile(api, request_profile_me(api)["id"])
	elif cmd_root == "help":
		print("""Команды:
top [страница] -  Топ аниме на шики
bug - Оставить информацию о баге
profile - Мой профиль
profile <id или ник> - Чужой профиль
cls - Очистить дисплей
default - Сброс приложения до изначального состояния
exit - Выйти из приложения""")
	else:
		print("Команда \"" + cmd_root + "\" не существует")