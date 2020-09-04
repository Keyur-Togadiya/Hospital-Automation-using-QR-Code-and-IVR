res = {'a': ['ENT', '2020-04-21', '7:30 PM', '8768'], 'b': ['Dental', '2020-04-23', '8:30 PM', '3666'], 'c': ['Dental', '2020-04-23', '8:30 PM', '3666'], 'd': ['Dental', '2020-04-23', '8:30 PM', '3666']}
r=res.values()
r=list(r)
print(r)
    
j= [['Dental', '2020-04-23', '8:30 PM']]
print(" .")
c=[]
for row in r:
  c.append(row[0:3])
  
print(c)  


def is_Sublist(l, s):
	sub_set = False
	if s == []:
		sub_set = True
	elif s == l:
		sub_set = True
	elif len(s) > len(l):
		sub_set = False

	else:
		for i in range(len(l)):
			if l[i] == s[0]:
				n = 1
				while (n < len(s)) and (l[i+n] == s[n]):
					n += 1
				
				if n == len(s):
					sub_set = True

	return sub_set
	
print(is_Sublist(c, j))	