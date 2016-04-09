
def rotate(bina,rot):
	string=bin(bina)[2:]
	
	while rot > 0 :
		y=''
		a=''
		string=list(string)
		b=string.pop()
		string=y.join(string)
		string=b+string
		rot=rot-1
	return int(string,2)


def padder(ip):
	word=list()
	index=0
        if len (ip) > 512 :
        	print "Errr"
        	return False 
	ip=ip.ljust(512,'0')
	while index<512 :
		string=ip[index:index+32]
		index=index+32
		a=''
		a=a.join(string) 
		word.append([a])
		
		 
	print type(word)	
	return word 
	      
        
        
        
def digest(string):
	var=''	
	for letter in string:
		num=ord(letter)
		bina=str(bin(num))[2:]
		var=var+bina
	
	return str(var)


def sha_custom(words):
	


	h1=0b10101010011010101
	h2=0b10100101010101010
	h3=0b1010101010101010011
	h4=0b1010101111101110111
	h5=0b11110101111010110101
	

	index=0
	while index<16 :
		a=h1
		b=h2
		c=h3
		d=h4
		e=h5
		word=words.pop()
		if index in xrange(0,4) : 
			f = (b & c) | ((b) & d )
			k=0b1100101001010
		if index in xrange(4,8) : 
			f = b^c^d
			k=0b1111100111011101
		if index in xrange(8,12) : 
			f = (b & c) | (( b) & d )
			k=0b10100110100100101010
		if index in xrange(12,16) : 
			f = b^c^d
			k=0b111110111011101110
		index=index+1 
		
		a_rot=rotate(a,5)
		b_rot=rotate(b,30)
	        word=word.pop()
	        temp = f + a_rot + e + k + int(word,2) 
	        
	        e=d 
	        d=c
	        c=b_rot 
	        b=a
	        a=temp 
	        
	        
	        h1 = h1+ a 
	        h2 = h2+ b 
	        h3 = h3+ c 
	        h4 = h4+ d 
	        h5 = h5+ e 
	        
	        	
	has = hex(h1)[2:]+hex(h2)[2:]+hex(h3)[2:]+hex(h4)[2:]+hex(h5)[2:]
	return has
		
	
s=digest("hi")
padd=padder(s)
a=sha_custom(padd)


s=digest("hi!")
padd=padder(s)
b=sha_custom(padd)	

if a==b :
	print "YAAAY!"
else :
	print "BOOO!"

	
