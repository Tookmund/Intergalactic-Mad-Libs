#!/usr/bin/python3
import json
fs = input("File Name:")
fp = open(fs)

js = json.load(open(fs))

i = ord('A') - 1
q = {}
result = ""

for k,v in js.items():
	if v == '':
		result += k+"\n"

	else:
		i += 1
		q[chr(i)] = input(k)
		result += v.format(**q)+"\n"
		if i == 90:
			i += 7
		elif i == 122:
			print("ERROR: Too many variables")
			break;

print(result)
