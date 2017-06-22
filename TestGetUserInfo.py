import unittest
import requests
import json


class TestGetUserInfo(unittest.TestCase):
	"""接口名称：获取当前用户信息"""
	def setUp(self):
		self.host = 'http://gene.lesports.com'
		self.url = '/api/liveman/user/info'
		self.token = '140XXXQQjm53qt7m5bg3m5ym1qHDlq3xGm5ym1hr2iv5Q3RYv6qy5KvdTNK1S3U4pID5pJlAm1sm2SuwPr3VE738hEvYm1zRfy2co9m1jHO27DLZUm53zMUF5m2ngm4'

	def tearDown(self):
		pass

	def test_getUserinfo(self):
		"""正确获取当前用户信息"""
		r = requests.get(url=self.host+self.url, params={'access_token': self.token})
		self.assertEqual(r.status_code, 200)
		self.assertIn('13701334231', r.text, '返回用户信息错误')
		print(r.text)

	def test_getUserinfoWithoutToken(self):
		"""没带token时获取当前用户信息"""
		r = requests.get(url=self.host + self.url)
		self.assertEqual(r.status_code, 200)
		self.assertEqual(r.json()['data'], None)

	def test_getUserinfoWithWrongToken(self):
		"""带有错误的token时获取当前用户信息"""
		r = requests.get(url=self.host + self.url, params={'access_token': 'wrongtoken'})
		self.assertEqual(r.status_code, 200)
		self.assertEqual(r.json()['data'], None)


if __name__ == '__main__':
	unittest.main()