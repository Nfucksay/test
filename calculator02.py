#!/usr/bin/env python3
from collections import namedtuple

taxStart = 3500
taxQuick = namedtuple('taxquick',['payable','taxRate','quickSub',])
taxList = [
taxQuick(80000,0.45,13505),
taxQuick(55000,0.35,5505),
taxQuick(35000,0.30,2755),
taxQuick(9000,0.25,1005),
taxQuick(4500,0.2,555),
taxQuick(1500,0.1,105),
taxQuick(0,0.03,0),
]

def cal(income1):
	incomePayable = income1 * 0.835 - 3500
	if incomePayable <= 0:
		return '{:.2f}'.format(income1 * 0.835)
		exit()
	for item in taxList:
		if incomePayable > item.payable:
			tax = incomePayable * item.taxRate - item.quickSub
			money = 0.835 * income1 -tax
			return "{:.2f}".format(money)
def main():
	import sys
	for item in sys.argv[1:]:
		num,income = item.split(':')
		try:
			income1 = int(income)
		except:
			print('Parameter Error')
			exit()
		print(num+':'+str(cal(income1)))

if __name__ == '__main__':
	main()
