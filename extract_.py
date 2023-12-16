import itertools
import numpy
file=open('journal.csv','r')
file1=open('scimagojr 2017  Subject Category - Electrical and Electronic Engineering.csv','r')
output=open('output2.csv','w')
minerror=100000					#infinite
numbers=list(range(1,10))
for i in range(9):
	l=list(itertools.combinations(numbers,i+1))
	for l1 in l:
		file=open('journal.csv','r')
		f=0
		linear=[0]*len(l1)
		quad=[[0]*len(l1)]*len(l1)
		m2=[0]*(len(l1)+1)
		combo=[]
		for row in file:
			f+=1
			a=row.find(";")
			lis=[]
			for i in range(1,10):
				if i in l1:
					lis.append(row[a+1:a+1+row[a+1:].find(";")])
				a=a+1+row[a+1:].find(";")
			if f==1:
				for i in range(len(l1)):
					combo.append(lis[i])
				continue

			for i in range(len(lis)):
				s=""
				for j in range(len(lis[i])):
					if lis[i][j]!=",":
						s+=lis[i][j]
				linear[i]+=int(s)
				lis[i]=int(s)
			for i in range(len(l1)):
				for j in range(len(l1)):
					quad[i][j]+=lis[i]*lis[j]
			ifactor=row[a+1:a+1+row[a+1:].find(";")]
			m2[0]-=float(ifactor)
			for i in range(len(lis)):
				m2[i+1]-=float(ifactor)*lis[i]
			if f==221:
				break

		linear.append(220)
		m1=[]
		m1.append(linear)
		for i in range(len(l1)):
			m1.append(quad[i]+[linear[i]])
		a=numpy.array(m1)
		b=numpy.array(m2)
		try:
			c=numpy.linalg.solve(a,b)
		except:
			continue
		abserror=0
		squareerror=0
		for row in file:
			f+=1
			a=row.find(";")
			lis=[]
			for i in range(1,10):
				if i in l1:
					lis.append(row[a+1:a+1+row[a+1:].find(";")])
				a=a+1+row[a+1:].find(";")
			x=0
			for i in range(len(l1)):
				s=""
				for j in range(len(lis[i])):
					if lis[i][j]!=",":
						s+=lis[i][j]
				if s!='':
					x+=c[i]*int(s)
					lis[i]=int(s)
			x+=c[len(c)-1]
			ifactor=float(row[a+1:a+1+row[a+1:].find(";")])
			abserror+=abs(ifactor-(-x))
			squareerror+=(ifactor+x)**2
			if f==276:
				break
		meanabserror=abserror/75
		meansquareerror=squareerror/75
		print(combo)
		print('Mean absolute error = '+str(meanabserror/75)+" Mean square error = "+str(meansquareerror/75))
		s=""
		for i in combo:
			s+=i+" "
		output.write(s+"    ")
		output.write('Mean absolute error = '+str(meanabserror/75)+"   Mean square error = "+str(meansquareerror/75))
		output.write("\n")
		if abs(meanabserror/75)<minerror:
			minerror=abs(meanabserror/75)
			mincombo=combo
		file.close()
print("Combination giving least error ")
print(mincombo)
print("with error=")
print(minerror)
output.write("Combination giving least error is ")
s=""
for i in mincombo:
	s+=i+" "
output.write(s)
output.write("   with mean abs error=")
output.write(str(minerror))