import unittest
import requests
import json


class TestGetFocusList(unittest.TestCase):
	"""接口名称：获取焦点图列表"""
	def setUp(self):
		self.host = 'http://gene.lesports.com'
		self.url = '/api/liveman/user/info'
		self.params = {'access_token':'140XXXQQjm53qt7m5bg3m5ym1qHDlq3xGm5ym1hr2iv5Q3RYv6qy5KvdTNK1S3U4pID5pJlAm1sm2SuwPr3VE738hEvYm1zRfy2co9m1jHO27DLZUm53zMUF5m2ngm4'}

	def tearDown(self):
		pass

	def test_getFocusList(self):
		r = requests.get(url=self.host+self.url, params=self.params)
		print(r.text)



if __name__ == '__main__':
	unittest.main()