#!/usr/bin/env python3
#-*-coding:utf-8-*-
import sys 
import csv
import queue
import configparser
from getopt import getopt
from datetime import datetime
from multiprocessing import Process,queue
from collections import namedtuple

IncomeTaxQuickLookItem = namedtuple(
'IncomeTaxQuickLookItem',
['start_point','tax_rate','quick_subtractor']
	)
INCOME_TAX_START_POINT = 3500
INCOME_TAX_QUICK_LOOKUP_TABLE = [
IncomeTaxQuickLookItem(80000,0.45,13505),
IncomeTaxQuickLookItem(55000,0.35,5505),
IncomeTaxQuickLookItem(35000,0.30,2755),
IncomeTaxQuickLookItem(9000,0.25,1005),
IncomeTaxQuickLookItem(4500,0.2,555),
IncomeTaxQuickLookItem(1500,0.1,105),
IncomeTaxQuickLookItem(0,0.03,0),
]
q_user = Queue()
q_result = Queue()

class Args(object):
	def __init__(self):
		options, _ getopt(sys.argv[1:],'C:c:d:o:')
		self.options = dict(options)

	def _value_after_option(self,option):
		value = self.options.get(option)
		if value is None and option != '-C':
			print('error01')
			exit()
		return value

		@property
		def city(self):
			return self._value_after_option('-C')

		@property 
		def config_path(self):
			return self._value_after_option('-c')
		@property 
		def userdata_path(self):
			return self._value_after_option('-d')
		@property 
		def export_path(self):
			return self._value_after_option('-o')

args = Args()

class Config(object):
	def __init(self):
		self.config = self._read_config()
	def _read_config(self):
		config = configparser.ConfigParser()
		config.read(args.config_path)
		if args.city and args.city.upper() in config.sections():
			return config[args.city.upper()]
		else:
			return config['DEFAULT']
	def _get_config(self,name):
		try:
			return float(self.config[name])