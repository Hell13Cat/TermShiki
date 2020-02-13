import pprint
def top(api):
	req_get_data = api.animes.GET(page=1, limit=10)
	pprint(req_get_data[0])