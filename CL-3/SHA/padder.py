x=int(raw_input("Number?"))

l=x.bit_length()

while l<512 :
        s=str(x)
        s=s+'0'
        x=s 
        x=int(s)
        
        l=x.bit_length()
print(x)
