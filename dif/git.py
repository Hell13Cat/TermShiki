import requests, json

def ver_control(my_ver):
	print("""╔═════════╗
║""" + my_ver + """
╚═════════╝""")
	url_get_last_ver = "https://api.github.com/repos/Hell13Cat/TermShiki/releases/latest"
	content = requests.get(url_get_last_ver)
	content_json = content.json()
	my_ver_pars = my_ver.replace("a", "").split(".")
	last_ver_pars = content_json["tag_name"].replace("a","").split(".")
	up_ch = 0
	if my_ver_pars[0] < last_ver_pars[1]:
		up_ch = 1
	if my_ver_pars[1] < last_ver_pars[1]:
		up_ch = 1
	if my_ver_pars[2] < last_ver_pars[2]:
		up_ch = 1
	if up_ch == 1:
		print("[!]Новая версия(" + content_json["tag_name"] + ")")