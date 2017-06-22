import unittest
import requests
import json


class TestGetFocusList(unittest.TestCase):
	"""接口名称：获取焦点图列表"""
	def setUp(self):
		self.host = 'http://gene.lesports.com'
		self.url = '/api/liveman/photo/focuspic'

	def tearDown(self):
		pass

	def test_getFocusList(self):
		"""测试正确获取焦点图列表"""
		r = requests.get(url=self.host+self.url)
		self.assertIn('直播公约', r.text, '返回的检点图列表错误，未含有直播公约项')
		self.assertEqual(r.status_code, 200)
		print(r.text)

	def test_getFocusList_WithParam(self):
		"""测试带参数时获取焦点图列表"""
		r = requests.get(url=self.host + self.url, params={'p': 1})
		self.assertEqual(r.status_code, 200)
		self.assertIn('直播公约', r.text, '返回的检点图列表错误，未含有直播公约项')
		print(r.text)


if __name__ == '__main__':
	unittest.main()
