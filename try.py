import requests

host = [
	'http://gene.lesports.com/api',
	'http://gene.lesports.com/api',
	'http://gene.lesports.com/api',
	'http://gene.lesports.com/api'
	]

url = [
	'/liveman/version/latest',
	'/liveman/photo/focuspic',
	'/liveman/user/569dee74e4b041f5e53fe1d8/follow',
	'/liveman/user/569dee74e4b041f5e53fe1d8/unfollow'
	]

method = ['GET', 'GET', 'POST', 'POST']

request_data = [{'appType':'2'},
                {},
                {"access_token":"140XXXQQjm53qt7m5bg3m5ym1qHDlq3xGm5ym1hr2iv5Q3RYv6qy5KvdTNK1S3U4pID5pJlAm1sm2SuwPr3VE738hEvYm1zRfy2co9m1jHO27DLZUm53zMUF5m2ngm4"},
				{"access_token":"140XXXQQjm53qt7m5bg3m5ym1qHDlq3xGm5ym1hr2iv5Q3RYv6qy5KvdTNK1S3U4pID5pJlAm1sm2SuwPr3VE738hEvYm1zRfy2co9m1jHO27DLZUm53zMUF5m2ngm4"}
			]

headers = {
	'cache-control': "no-cache",
	'postman-token': "3235f79c-1f4b-1919-4e92-8a7354d4f29c"
	}

for i in range(len(method)):
	r = requests.request(method=method[i], url=host[i]+url[i], params=request_data[i])
	print(i+1)
	print(r.status_code)
	print(r.text)


