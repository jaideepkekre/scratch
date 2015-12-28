import pickle
import sys
def addtopickle():

	lista = list()
	lista = [1,2,3,4,5,6,7,8,9]
	print(lista)
	print(type(lista))
	
	
	File=open('/home/admin/abc.p','wb+')
	pickle.dump(lista,File)
	File.close()

	File=open('/home/admin/abc.p','wb+')
	pickle.dump(lista,File)
	File.close()

	File=open('/home/admin/abc.p','wb+')
	pickle.dump(lista,File)
	File.close()

	File=open('/home/admin/abc.p','wb+')
	pickle.dump(lista,File)
	File.close()

	File=open('/home/admin/abc.p','wb+')
	pickle.dump(lista,File)
	File.close()

	File=open('/home/admin/abc.p','wb+')
	pickle.dump(lista,File)
	File.close()

	File=open('/home/admin/abc.p','wb+')
	pickle.dump(0,File)
	File.close()




if __name__ == '__main__':
	addtopickle()