# -*- encoding: utf-8 -*-
import os, sys, re

f=open('./sol.xml', 'w')
payload="""<?xml version="1.0" encoding="UTF-8"?>
<meal>
	<course>
		<plate>
			<宫保鸡丁>1</宫保鸡丁>
		</plate>
	</course>
</meal>
"""
f.write(payload)
f.close()
os.system("ncat 54.180.154.109 1337 < sol.xml > output.txt")
f=open("./output.txt", 'r')
while True:
	line=f.readline()
	a=re.search(r"XSLT message: (\d{10})[\s\S]*at line 49, column 49\.\)", line)
	if(a):
		k=a.group(1)
		#print(k)
	if not line:
		break
f.close()

flag=True
while (flag):
	f=open('./sol.xml', 'w')
	payload="""<?xml version="1.0" encoding="UTF-8"?>
	<meal>
		<course>
			<plate>
				<paella>"""+str(k)+"""</paella>
			</plate>
			<plate>
				<ラーメン>1</ラーメン>
			</plate>
			<plate>
				<宫保鸡丁>1</宫保鸡丁>
			</plate>
		</course>
	</meal>
	"""
	f.write(payload)
	f.close()
	os.system("ncat 54.180.154.109 1337 < sol.xml > output.txt")
	f=open("./output.txt", 'r')
	while True:
		line=f.readline()
		a=re.search(r"XSLT message: (\d+)[\s\S]*at line 54, column 54\.\)", line)
		if(a):
			#print(a.group(1))
			if(a.group(1)=='0'):
				#print(k)
				first_k=k
				flag=False
				break
		if not line:
			break
	f.close()
	k=k[:-1]


f=open('./sol.xml', 'w')
payload="""<?xml version="1.0" encoding="UTF-8"?>
	<meal>
		<course>
			<plate>
				<paella>"""+first_k+"""</paella>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<宫保鸡丁>1</宫保鸡丁>
			</plate>
		</course>
	</meal>
"""
f.write(payload)
f.close()
os.system("ncat 54.180.154.109 1337 < sol.xml > output.txt")
f=open("./output.txt", 'r')
while True:
	line=f.readline()
	a=re.search(r"XSLT message: (\d{10})[\s\S]*at line 49, column 49\.\)", line)
	if(a):
		k=a.group(1)
		#print(k)
	if not line:
		break
f.close()

flag=True
while (flag):
	f=open('./sol.xml', 'w')
	payload="""<?xml version="1.0" encoding="UTF-8"?>
	<meal>
		<course>
			<plate>
				<paella>"""+first_k+"""</paella>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<paella>"""+k+"""</paella>
			</plate>
			<plate>
				<ラーメン>1</ラーメン>
			</plate>
			<plate>
				<宫保鸡丁>1</宫保鸡丁>
			</plate>
		</course>
	</meal>
	"""
	f.write(payload)
	f.close()
	os.system("ncat 54.180.154.109 1337 < sol.xml > output.txt")
	f=open("./output.txt", 'r')
	while True:
		line=f.readline()
		a=re.search(r"XSLT message: (\d+)[\s\S]*at line 54, column 54\.\)", line)
		if(a):
			#print(a.group(1))
			if(a.group(1)=='0'):
				#print(k)
				second_k=k
				flag=False
				break
		if not line:
			break
	f.close()
	k=k[:-1]


f=open('./sol.xml', 'w')
payload="""<?xml version="1.0" encoding="UTF-8"?>
	<meal>
		<course>
			<plate>
				<paella>"""+second_k+"""</paella>
			</plate>
			<plate>
				<paella>"""+first_k+"""</paella>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<宫保鸡丁>1</宫保鸡丁>
			</plate>
		</course>
	</meal>
"""
f.write(payload)
f.close()
os.system("ncat 54.180.154.109 1337 < sol.xml > output.txt")
f=open("./output.txt", 'r')
while True:
	line=f.readline()
	a=re.search(r"XSLT message: (\d{10})[\s\S]*at line 49, column 49\.\)", line)
	if(a):
		k=a.group(1)
		#print(k)
	if not line:
		break
f.close()


flag=True
while (flag):
	f=open('./sol.xml', 'w')
	payload="""<?xml version="1.0" encoding="UTF-8"?>
		<meal>
			<course>
				<plate>
					<paella>"""+second_k+"""</paella>
				</plate>
				<plate>
					<paella>"""+first_k+"""</paella>
				</plate>
				<plate>
					<Борщ>1</Борщ>
				</plate>
				<plate>
					<Борщ>1</Борщ>
				</plate>
				<plate>
					<paella>"""+k+"""</paella>
				</plate>
				<plate>
					<ラーメン>1</ラーメン>
				</plate>
				<plate>
					<宫保鸡丁>1</宫保鸡丁>
				</plate>
			</course>
		</meal>
	"""
	f.write(payload)
	f.close()
	os.system("ncat 54.180.154.109 1337 < sol.xml > output.txt")
	f=open("./output.txt", 'r')
	while True:
		line=f.readline()
		a=re.search(r"XSLT message: (\d+)[\s\S]*at line 54, column 54\.\)", line)
		if(a):
			#print(a.group(1))
			if(a.group(1)=='0'):
				#print(k)
				third_k=k
				flag=False
				break
		if not line:
			break
	f.close()
	k=k[:-1]


f=open('./sol.xml', 'w')
payload="""<?xml version="1.0" encoding="UTF-8"?>
	<meal>
		<course>
			<plate>
				<paella>"""+third_k+"""</paella>
			</plate>
			<plate>
				<paella>"""+second_k+"""</paella>
			</plate>
			<plate>
				<paella>"""+first_k+"""</paella>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<宫保鸡丁>1</宫保鸡丁>
			</plate>
		</course>
	</meal>
"""
f.write(payload)
f.close()
os.system("ncat 54.180.154.109 1337 < sol.xml > output.txt")
f=open("./output.txt", 'r')
while True:
	line=f.readline()
	a=re.search(r"XSLT message: (\d{10})[\s\S]*at line 49, column 49\.\)", line)
	if(a):
		k=a.group(1)
		#print(k)
	if not line:
		break
f.close()

flag=True
while (flag):
	f=open('./sol.xml', 'w')
	payload="""<?xml version="1.0" encoding="UTF-8"?>
		<meal>
			<course>
				<plate>
					<paella>"""+third_k+"""</paella>
				</plate>
				<plate>
					<paella>"""+second_k+"""</paella>
				</plate>
				<plate>
					<paella>"""+first_k+"""</paella>
				</plate>
				<plate>
					<Борщ>1</Борщ>
				</plate>
				<plate>
					<Борщ>1</Борщ>
				</plate>
				<plate>
					<Борщ>1</Борщ>
				</plate>
				<plate>
					<paella>"""+k+"""</paella>
				</plate>
				<plate>
					<ラーメン>1</ラーメン>
				</plate>
				<plate>
					<宫保鸡丁>1</宫保鸡丁>
				</plate>
			</course>
		</meal>
	"""
	f.write(payload)
	f.close()
	os.system("ncat 54.180.154.109 1337 < sol.xml > output.txt")
	f=open("./output.txt", 'r')
	while True:
		line=f.readline()
		a=re.search(r"XSLT message: (\d+)[\s\S]*at line 54, column 54\.\)", line)
		if(a):
			#print(a.group(1))
			if(a.group(1)=='0'):
				#print(k)
				fourth_k=k
				flag=False
				break
		if not line:
			break
	f.close()
	k=k[:-1]


f=open('./sol.xml', 'w')
payload="""<?xml version="1.0" encoding="UTF-8"?>
	<meal>
		<course>
			<plate>
				<paella>"""+fourth_k+"""</paella>
			</plate>
			<plate>
				<paella>"""+third_k+"""</paella>
			</plate>
			<plate>
				<paella>"""+second_k+"""</paella>
			</plate>
			<plate>
				<paella>"""+first_k+"""</paella>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<宫保鸡丁>1</宫保鸡丁>
			</plate>
		</course>
	</meal>
"""
f.write(payload)
f.close()
os.system("ncat 54.180.154.109 1337 < sol.xml > output.txt")
f=open("./output.txt", 'r')
while True:
	line=f.readline()
	a=re.search(r"XSLT message: (\d{10})[\s\S]*at line 49, column 49\.\)", line)
	if(a):
		k=a.group(1)
		#print(k)
	if not line:
		break
f.close()


flag=True
while (flag):
	f=open('./sol.xml', 'w')
	payload="""<?xml version="1.0" encoding="UTF-8"?>
		<meal>
			<course>
				<plate>
					<宫保鸡丁>1</宫保鸡丁>
				</plate>
				<plate>
					<paella>"""+fourth_k+"""</paella>
				</plate>
				<plate>
					<paella>"""+third_k+"""</paella>
				</plate>
				<plate>
					<paella>"""+second_k+"""</paella>
				</plate>
				<plate>
					<paella>"""+first_k+"""</paella>
				</plate>
				<plate>
					<Борщ>1</Борщ>
				</plate>
				<plate>
					<Борщ>1</Борщ>
				</plate>
				<plate>
					<Борщ>1</Борщ>
				</plate>
				<plate>
					<Борщ>1</Борщ>
				</plate>
				<plate>
					<paella>"""+k+"""</paella>
				</plate>
				<plate>
					<ラーメン>1</ラーメン>
				</plate>
				<plate>
					<宫保鸡丁>1</宫保鸡丁>
				</plate>
			</course>
		</meal>
	"""
	f.write(payload)
	f.close()
	os.system("ncat 54.180.154.109 1337 < sol.xml > output.txt")
	f=open("./output.txt", 'r')
	while True:
		line=f.readline()
		a=re.search(r"XSLT message: (\d+)[\s\S]*at line 54, column 54\.\)", line)
		if(a):
			#print(a.group(1))
			if(a.group(1)=='0'):
				#print(k)
				fifth_k=k
				flag=False
				break
		if not line:
			break
	f.close()
	k=k[:-1]


f=open('./sol.xml', 'w')
payload="""<?xml version="1.0" encoding="UTF-8"?>
	<meal>
		<course>
			<plate>
				<宫保鸡丁>1</宫保鸡丁>
			</plate>
			<plate>
				<paella>"""+fifth_k+"""</paella>
			</plate>
			<plate>
				<paella>"""+fourth_k+"""</paella>
			</plate>
			<plate>
				<paella>"""+third_k+"""</paella>
			</plate>
			<plate>
				<paella>"""+second_k+"""</paella>
			</plate>
			<plate>
				<paella>"""+first_k+"""</paella>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<Борщ>1</Борщ>
			</plate>
			<plate>
				<宫保鸡丁>1</宫保鸡丁>
			</plate>
			<plate>
				<दाल>1</दाल>
			</plate>
		</course>
	</meal>
"""
f.write(payload)
f.close()
os.system("ncat 54.180.154.109 1337 < sol.xml > output.txt")
f=open("./output.txt", 'r')
while True:
	line=f.readline()
	a=re.search(r"XSLT message: (\d{10})[\s\S]*at line 49, column 49\.\)", line)
	if(a):
		k=a.group(1)
		#print(k)
	if not line:
		break
f.close()