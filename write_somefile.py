string = 'zlxs'
f = open('somefile.txt','a')
f.write((string+'\n')*10)
f.close()

def rp(st):
	return st+'\n'
f = ''
	'''
with open('somefile.txt','w') as f:
	str(f)
	if ']' in f:
		rp(']')
	'''