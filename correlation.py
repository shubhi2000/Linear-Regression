file=open('journal2.csv','r')
sumofh=0                        #sum of h-indices
sumofi=0                        #sum of impact factors
for row in file:
	if row.find(";")>=2:
		if row[:14]=="Title;H index;":
			continue
		a=row.find(";")
		b=a+1+row[a+1:].find(";")
		hindex=float(row[a+1:b])
		a=b+1+row[b+1:].find(";")
		#b=a+1+row[a+1:].find(";")
		ifactor=float(row[b+1:a])
		sumofh+=hindex
		sumofi+=ifactor
meanofh=sumofh/275
meanofi=sumofi/275
xy=0
x2=0
y2=0
file.close()
file=open('journal2.csv','r')
for row in file:
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
x2=x2/275
y2=y2/275
sdx=x2**(1/2)
sdy=y2**(1/2)
corcoeff=(xy-meanofh*meanofi*275)/(sdx*sdy*275)
print("Correlation coefficient is "+str(corcoeff))
