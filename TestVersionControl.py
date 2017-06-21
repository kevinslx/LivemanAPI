import requests
import json
import unittest


class TestVersionControl(unittest.TestCase):
	"""接口名称：版本管理"""
	def setUp(self):
		self.host = 'http://gene.lesports.com'
		self.url = '/api/liveman/version/latest'

	def tearDown(self):
		pass

	def get_version(self, appType, versionCode=None):
		self.params = {'appType':appType}
		self.version = {'versionCode':versionCode}
		r = requests.get(url=self.host+self.url, params=self.params)
		return r

	def test_type1(self):
		"""测试获取appType为1，即安卓app应用更新"""
		r = self.get_version(appType=1)
		self.assertEqual(r.status_code, 200)
		self.assertIn('apk', r.text, '返回非安卓更新安装文件')

	def test_type2(self):
		"""测试获取appType为2，即m1相机固件更新"""
		r = self.get_version(appType=2)
		self.assertEqual(r.status_code, 200)
		self.assertIn('M1', r.text, '返回非m1更新安装文件')

	def test_type3(self):
		"""测试获取appType为3，即C1相机固件更新"""
		r = self.get_version(appType=3)
		self.assertEqual(r.status_code, 200)
		self.assertIn('c1', r.text, '返回非c1更新安装文件')

	def test_type4(self):
		"""测试获取appType为4，即自拍杆固件更新"""
		r = self.get_version(appType=4)
		self.assertEqual(r.status_code, 200)
		self.assertIn('自拍', r.text, '返回非自拍杆更新安装文件')

	def test_type5(self):
		"""测试获取appType为5，即D1相机固件更新"""
		r = self.get_version(appType=5)
		self.assertEqual(r.status_code, 200)
		self.assertIn('D1', r.text, '返回非D1更新安装文件')


	def test_type6(self):
		"""测试获取appType为6，>5时的结果"""
		r = self.get_version(appType=6)
		self.assertEqual(r.status_code, 200)
		self.assertEqual(r.json()['data'], None)

	def test_type0(self):
		"""测试获取appType为0，<1时的结果"""
		r = self.get_version(appType=0)
		self.assertEqual(r.status_code, 200)
		self.assertEqual(r.json()['data'], None)

	def test_type_minus(self):
		"""测试获取appType为负数时的结果"""
		r = self.get_version(appType=-1)
		self.assertEqual(r.status_code, 200)
		self.assertEqual(r.json()['data'], None)

	def test_type_str(self):
		"""测试获取appType为非数字时的结果"""
		r = self.get_version(appType='abc')
		self.assertEqual(r.status_code, 200)
		self.assertEqual(r.json()['data'], None)

	def test_version_minus(self):
		"""测试versionCode为负数时的结果"""
		r = self.get_version(appType=1, versionCode=1)
		self.assertEqual(r.status_code, 200)
		self.assertIn('apk', r.text, '返回非安卓更新安装文件')

	def test_version_str(self):
		"""测试versionCode为字符时的结果"""
		r = self.get_version(appType=1, versionCode='abc')
		self.assertEqual(r.status_code, 200)
		self.assertIn('apk', r.text, '返回非安卓更新安装文件')

if __name__ == '__main__':
	unittest.main()