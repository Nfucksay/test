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

IncomeTaxQuickLookupItem = namedtuple(
	'IncomeTaxQuickLookupItem',
	['start_point',
	'tax_rate',
	'quick_subtractor']
	)
INCOME_TAX_START_POINT = 3500
INCOME_TAX_QUICK_LOOKUP_TABLE = [
IncomeTaxQuickLookupItem(80000,0.45,13505),
IncomeTaxQuickLookupItem(55000,0.35,5505),
IncomeTaxQuickLookupItem(35000,0.30,2755),
IncomeTaxQuickLookupItem(9000,0.25,1005),
IncomeTaxQuickLookupItem(4500,0.2,555),
IncomeTaxQuickLookupItem(1500,0.1,105),
IncomeTaxQuickLookupItem(0,0.03,0),
]
q_user = Queue()
q_result = Queue()

class Args(object):
	def __init__(self):
		options,_ = getopt(sys.argv[1:],'C:c:d:o:')
		self.options = dict(options)

	def _value_afer_option(self,option):
		value = self.options.get(option)
		if value is None and option != '-C':
			print('error 01')
			exit()
		return value