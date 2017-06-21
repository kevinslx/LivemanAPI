import requests


def get_version(host, url, appType, versionCode=None):
	params = {'appType': appType}
	version = {'versionCode': versionCode}
	r = requests.get(url=host + url, params=params)
	return r