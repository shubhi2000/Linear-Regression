file=open('journal2.csv','r')
file1=open('scimagojr 2017  conferences.csv','r')
conference=open('conferencefinal1.csv','w')
f=0
sumofh=0                        #sum of h-indices
sumofi=0                        #sum of impact factors
for row in file:
	f+=1
	if row[:14]=="Title;H index;":
		continue
	a=row.find(";")
	b=a+1+row[a+1:].find(";")
	hindex=row[a+1:b]
	a=b+1+row[b+1:].find(";")
	#b=a+1+row[a+1:].find(";")
	ifactor=row[b+1:a]
	sumofh+=float(hindex)
	sumofi+=float(ifactor)
	if f==221:
		break
meanofh=sumofh/220
meanofi=sumofi/220
xy=0
x2=0
y2=0
for row in file:
	f+=1
	if row[:14]=="Title;H index;":
		continue
	a=row.find(";")
	b=a+1+row[a+1:].find(";")
	hindex=float(row[a+1:b])
	a=b+1+row[b+1:].find(";")
	#b=a+1+row[a+1:].find(";")
	ifactor=float(row[b+1:a])
	xy+=hindex*ifactor
	x2+=(hindex-meanofh)**2
	y2+=(ifactor-meanofi)**2
x2=x2/220
y2=y2/220
sdx=x2**(1/2)
sdy=y2**(1/2)
corcoeff=(xy-meanofh*meanofi*220)/(sdx*sdy*220)
a=corcoeff*sdy/sdx
b=meanofi-a*meanofh
print("Regression coefficient is "+str(a)+" and intercept is "+str(b))

"""Finding error for 20% of data"""
f=0
error=0
file.close()
file=open('journal2.csv','r')
for row in file:
	f+=1
	if f>=221:
		i=row.find(";")
		j=i+1+row[i+1:].find(";")
		hindex=float(row[i+1:j])
		i=j+1+row[j+1:].find(";")
		#b=a+1+row[a+1:].find(";")
		ifactor=float(row[j+1:i])
		p=b-a*(meanofh)
		error+=(ifactor-b)**2
print("Root mean square error is "+str((error/55)**(1/2)))
""" Predicting impact factor for conference"""
flag=0
for row in file1:
	if flag==0:
		conference.write("Title;H Index;Predicted Impact Factor")
		conference.write("\n")
		flag=1
		continue
	a=row.find(";")
	for i in range(6):
		a=a+1+row[a+1:].find(";")
		if i==0:
			title=row[a+1:a+1+row[a+1:].find(";")]
		if i==5:
			hindex=row[a+1:a+1+row[a+1:].find(";")]
	ifactor=b-a*(meanofh)
	conference.write(str(title)+";"+str(hindex)+";"+str(ifactor)+";")
	conference.write("\n")