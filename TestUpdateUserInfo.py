import unittest
import requests
import json


class TestUpdataUserInfo(unittest.TestCase):
	"""接口名称：更新当前用户信息"""
	def setUp(self):
		self.host = 'http://gene.lesports.com'
		self.url = '/api/liveman/user/update'
		self.geturl = '/api/liveman/user/info'
		self.token = '140XXXQQjm53qt7m5bg3m5ym1qHDlq3xGm5ym1hr2iv5Q3RYv6qy5KvdTNK1S3U4pID5pJlAm1sm2SuwPr3VE738hEvYm1zRfy2co9m1jHO27DLZUm53zMUF5m2ngm4'
		self.desc = '新用户名'
		self.headImageUrl = 'https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=1260021239,3145541481&fm=58'
		self.nickName = '新昵称'

	def tearDown(self):
		pass

	def test_getUserinfo(self):
		"""正确更新当前用户信息"""
		r = requests.post(url=self.host+self.url, data={'access_token': self.token, 'desc': self.desc, 'headImageUrl': self.headImageUrl, 'nickName': self.nickName})
		self.assertEqual(r.status_code, 200)
		print(r.text)
		newr = requests.get(url=self.host+self.geturl, params={'access_token': self.token})
		print(newr.text)
		self.assertEqual(newr.json()['data']['desc'], '新用户名')
		self.assertEqual(newr.json()['data'][ 'headImageUrl'], 'https://ss2.baidu.com/6ONYsjip0QIZ8tyhnq/it/u=1260021239,3145541481&fm=58')
		self.assertEqual(newr.json()['data']['nickName'], '新昵称')


if __name__ == '__main__':
	unittest.main()