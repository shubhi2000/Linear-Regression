file=open('scimagojr 2017  Subject Category - Electrical and Electronic Engineering.csv','r')
journal=open('journal2.csv','w')
file1=open('impactf.txt','r')
def func(title):
	file1=open('impactf.txt','r')
	for row in file1:
		if row.upper().find(title.upper())!=-1:
			a=row.find("\t")
			a=a+len("\t")+row[a+len("\t"):].find("\t")
			a=a+len("\t")+row[a+len("\t"):].find("\t")			
			pr=(row[a+len("\t"):a+len("\t")+row[a+len("\t"):].find("\t")])
			return pr
for row in file:
	a=row.find(";")
	for i in range(6):
		a=a+1+row[a+1:].find(";")
		if i==0:
			title=row[a+1:a+1+row[a+1:].find(";")]
		if i==5:
			hindex=row[a+1:a+1+row[a+1:].find(";")]
	ifactor=func(title[1:len(title)-1])
	file1.close()
	if ifactor!=None:
		info=title+";"+str(hindex)+";"+str(ifactor)+";"
		journal.write(info)
		journal.write("\n")