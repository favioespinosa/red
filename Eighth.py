from array import *
class Red:
	def __init__(self,numero):
		self.next=[None for i in range(numero)]
		self.numero=None
		self.peso=[0 for i in range(numero)]
		self.flag=[False for i in range(numero)]
def Lector(linea):
	lagar=0#Inicio
	lagar2=0#entre
	lagar3=1#entre
	lagar4=1#fin
	trozo=""
	arr=array('i',[])
	lagarnum=0
	num1=0
	num2=0
	for i in range(len(linea)):
		if linea[i]=='[':
			if lagar==0 and lagar3==1:#Si es al principio
				lagar=1
			elif lagar2==0 and lagar==1:#Si es entre
				lagar2=1
				lagar3=1
			else:
				print("Ingreso mal los datos: "+linea[i])
		elif linea[i]==']':
			if lagar3==1 and lagar2==1:#Si es que es entre
				arr.append(int(trozo))
				trozo=""
				lagar3=0
				lagar2=0
			elif lagar4==1 and lagar3==0:#Si es que es al final
				break
			else:
				print("Ingreso mal los datos1: "+linea[i])
				break
		elif linea[i]==',' and lagar==1 and lagar2==1 and lagar3==1 and lagar4==1 and lagarnum==1:
			arr.append(int(trozo))
			trozo=""
		elif ord(linea[i])>=ord('0') and ord(linea[i])<=ord('9'):
			lagarnum=1
			trozo=trozo+linea[i]
		else:
			print("",end='')
			#print(i)
	return arr
def Perito(arr):
	largo=maximo(arr)
	flag=0
	for i in range(largo):
		flag=0
		for j in range(len(arr)):
			if i==arr[j] and (i+1)%3!=0:
				flag=1
		if flag==0:
			print("Esta mal construido el Red")
			return False
	return True
def maximo(arr):
	may=0
	for i in range(len(arr)):
		if arr[i]>may and (i+1)%3!=0:
			may=arr[i]
	return may
def base_de_datos(arr):
	base=[Red(maximo(arr)+1) for i in range(maximo(arr)+1)]
	for i in range(maximo(arr)+1):
		base[i]=Red(maximo(arr)+1)
		base[i].numero=i
	return base
def Construccion(base,arr):
	for i in range(len(arr)):
		if i%3==0:
			base[arr[i]].next[arr[i+1]]=base[arr[i+1]]
			base[arr[i]].peso[arr[i+1]]=arr[i+2]
			base[arr[i+1]].peso[arr[i]]=arr[i+2]
			base[arr[i+1]].next[arr[i]]=base[arr[i]]
def todo_visitado(visitado,vertices):
	for i in range(vertices):
		if visitado[i]==False:
			return True
	return False
def minimo_pesos(pesos):
	mini=pesos[0]
	inice=0
	for i in range(len(pesos)):
		if mini>pesos[i]:
			mini=pesos[i]
			inice=i
	return inice
def rutas(base,vertices):
	for i in range(vertices):
		for j in range(verices):
			if  base[i].next[j]==None:
				base[i].flag[j]=True
def despeje(base,vertices):
	for i in range(vertices):
		for j in range(vertices):
			if  base[i].next[j]==None:
				base[i].flag[j]=True
			elif base[i].next[j]!=None:
				base[i].flag[j]=False
def rutas_visitadas(base,vertices):#Que todas las rutas estan todas visitadas
	for i in range(vertices):
		for j in range(vertices):
			if base[i].flag[j]==False:
				return True
	return False
def fin_de_cola(base,vertices,numero):
	for i in range(vertices):
		if  base[numero].flag[i]==False:
			return False
	return True
def exist(num,head):
	for i in range(len(head)):
		if head[i]==num:
			return True
	return False
def Senal(inicio,fin,base,vertices):
	head=array('i',[])
	llegados=["" for i in range(vertices*10)]
	pesos=array('i',[])
	j=0
	peso=0
	r=-1
	k=inicio-1
	despeje(base,vertices)
	head.append(inicio-1)
	j=1
	while rutas_visitadas(base,vertices):
		if fin_de_cola(base,vertices,k) and k!=fin-1:
			if j==0:
				j=1
				k=head[j-1]
			else:
				peso=peso-base[k].peso[i]
				k=head[j-1]
				if len(head)-1!=0:
					head.pop(len(head)-1)
				j-=1
		for i in range(0,vertices):
			if k==fin-1:
				r+=1
				llegados[r]=""
				for p in range(len(head)):
					llegados[r]=llegados[r]+'->'+chr(head[p]+48)
				head=array('i',[inicio-1])
				pesos.append(peso)
				k=inicio
				j=1
				head.append(inicio-1)
				return peso
			if base[k].next[i]!=None and base[k].flag[i]!=True:
				peso=peso+base[k].peso[i]
				j+=1
				head.append(base[i].numero)
				base[k].flag[i]=True
				base[i].flag[k]=True
				k=i
				if k==inicio-1:
					head=array('i',[inicio-1])
					k=inicio-1
					j=0
				i=0
	return -1
linea=input()
arr=Lector(linea)
base=base_de_datos(arr)
print(arr)
Construccion(base,arr)
print("The inicial point?")
inicio=input()
print("The end point")
fin=input()
print(maximo(arr)+1)
print("The signal is: ",end='')
print(Senal(int(inicio)+1,int(fin)+1,base,maximo(arr)+1))
