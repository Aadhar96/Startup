def kmeans(a,b):
	import numpy.random as r
	try:
		del a['Date']
	except:
		pass
	s=r.randint(1,a.shape[0]-1)
	tmp=((((a-a.loc[0])**2).sum(axis=1))**0.5).to_frame().join(((((a-a.loc[s])**2).sum(axis=1))**0.5).to_frame(),rsuffix=1)
	c={1:set(),2:set()}
	for i in range(tmp.shape[0]):
		if(tmp.loc[i]['0']<tmp.loc[i]['01']):
			c[1].add(i)
		else:
			c[2].add(i)
	while True:
		n=[]
		for i in c:
			sum=0
			for j in c[i]:
				sum+=a.loc[j]
			try:
				n.append(sum/len(c[i]))
			except:
				n.append(0)
		tmp=((((a-n[0])**2).sum(axis=1))**0.5).to_frame().join(((((a-n[1])**2).sum(axis=1))**0.5).to_frame(),rsuffix=1)
		d={1:set(),2:set()}
		for i in range(tmp.shape[0]):
			if(tmp.loc[i]['0']<tmp.loc[i]['01']):
				d[1].add(i)
			else:
				d[2].add(i)
		if(c==d):
			return c
			break
		else:
			c=d.copy()

        return c
