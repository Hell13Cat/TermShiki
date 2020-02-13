print("TermSiki v 0.0.2a")
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

print("[i]Проверка авторизации...")
if system.check_token()==0:
	api = API(app_name, client_id, client_secret, token_update_callback=system.token_file_saver)
	#api = API(app_name, client_id, client_secret)
	avtorizurl = api.authorization_url
	print("[i]Сейчас ссылка для авторизации откроется в браузере. Пожалуйста разрешите доступ и ввседите полученный код сюда.")
	webbrowser.open(avtorizurl, new=0, autoraise=True)
	code = input("Код: ")
	print(api.fetch_token(code))
else:
	api = API(app_name, client_id, client_secret, system.token_file_load())
	print("[i]Авторизация была совершена ранее")
clearShell()
system.logo_print()

print("[i]help - для помощи")
exit = "0"
while exit == "0":
	cmd_full = input(">")
	cmd_split = cmd_full.split(" ")
	cmd_root = cmd_split[0]
	if cmd_root == "exit":
		print("[i]Выход из приложения...")
		exit = "1"
	elif cmd_root == "unlogin":
		print("[i]Выход из аккаунта и приложения...")
		path = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'login.json')
		os.remove(path)
		exit = "1"
	elif cmd_root == "cls":
		os.system("cls")
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
	elif cmd_root == "help":
		print("""Команды:
top [страница] -  Топ аниме на шики
bug - Оставить информацию о баге
unlogin - Выйти из аккаунта
exit - Выйти из приложения""")
	else:
		print("Команда \"" + cmd_root + "\" не существует")