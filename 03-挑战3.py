#!/usr/bin/env python3
#-*-coding:utf-8-*-
import sys
import csv
from collections import namedtuple
income_quick_list = namedtuple('income_quick_list',
	['start_point','tax_rate','quick_sub'])
INCOME_QUICK_LIST = [
income_quick_list(80000,0.45,13505),
income_quick_list(55000,0.35,5505),
income_quick_list(35000,0.30,2755),
income_quick_list(9000,0.25,1005),
income_quick_list(4500,0.2,555),
income_quick_list(1500,0.1,105),
income_quick_list(0,0.03,0),
]
class Args(object):
	def __init__(self):
		self.args = sys.argv[1:]
	def _find_path(self,path):
		index =self.args.index(path)
		return self.args[index + 1]
	@property
	def config_path(self):
		return self._find_path('-c')
	@property
	def userdata_path(self):
		return self._find_path('-d')
	@property
	def output_path(self):
		return self._find_path('-o')
args =Args()

class Config(object):
	def __init__(self):
		self.config = self._read_config()
	def _read_config(self):
		config = {}
		config_path = args.config_path
		with open(config_path) as f:
			for line in f.readlines():
				key,value = line.strip().split(' = ')
				config[key]=float(value)
		return config
	def _get_config(self,key):
		return self.config[key]
	@property
	def print_config(self):
		return self.config
	@property 
	def social_high(self):
		return self._get_config('JiShuH')
	@property 
	def social_low(self):
		return self._get_config('JiShuL')
	@property 
	def social_sum(self):
		return sum([
					self._get_config('YangLao'),
					self._get_config('YiLiao'),
					self._get_config('ShiYe'),
					self._get_config('GongShang'),
					self._get_config('ShengYu'),
					self._get_config('GongJiJin'),
			])
config = Config()

class User_data:
	def __init__(self):
		self.userdata = self._read_userdata()
	def _read_userdata(self):
		userdata = []
		userdata_path = args.userdata_path
		with open(userdata_path) as f:
			for line in f.readlines():
				num,income = line.strip().split(',')
				try:
					income = int(income)
				except:
					print('error79')
					exit()
				userdata.append((num,income))
		return userdata
	def __iter__(self):
		return iter(self.userdata)


class Calculator:
	def __init__(self,userdata):
		self.userdata = userdata
	@staticmethod
	def social_calculator(income):
		if income > config.social_high:
			return config.social_high * config.social_sum
		elif income < config.social_low:
			return config.social_low * config.social_sum
		else:
			return income * config.social_sum
	@classmethod
	def tax_remain_calculator(cls,income):
		social_money = cls.social_calculator(income)
		real_income = income - social_money
		tax_part = real_income - 3500
		if tax_part <= 0:
			return '0.00','{:.2f}'.format(real_income)
		
		for item in INCOME_QUICK_LIST:
			if tax_part > item.start_point:
				tax = tax_part * item.tax_rate - item.quick_sub
				return '{:.2f}'.format(tax),'{:.2f}'.format(real_income - tax)
				
	def all_calculator(self):
		data = []
		for num,income in self.userdata:
			data1 =[num,income]
			social_money = '{:.2f}'.format(self.social_calculator(income))
			tax,remain = self.tax_remain_calculator(income)
			data1 = data1 + [social_money,tax,remain]
			data.append(data1)
		return data
	def output(self,default='csv'):
		result = self.all_calculator()
		with open(args.output_path,'w',newline='') as f:
			writer = csv.writer(f)
			writer.writerows(result)

if __name__ == '__main__':
	calculator = Calculator(User_data())
	calculator.output()
