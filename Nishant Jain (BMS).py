"'For staff directory, I have used CSV file.'"

import csv                                             #In order to use csv files, csv module is imported.
L=[]                                                         #Initialising an empty list.
ans='y'        
f=open('Staff_details.csv','w',newline='')                 # Opening the file in write only mode.
w=csv.writer(f)                             #Creating a writer object.
w.writerow(['Emplyee id','Name','Phone number','Emailid','Qualifications','Salary'])                        
while ans=='y' or ans=='Y':
     i=int(input('Employee id :'))
     n=input('Name :')
     pn=int(input('Phone number(of 10 digits) :'))
     e=input('Email id :')
     q=input('Qualifications :')
     s=float(input('Salary(in rupees) :'))
     l=[i,n,pn,e,q,s]                        #Creating a list.
     L.append(l)                             #Appending the created list in the empty list.
     ans=input('Want to enter more?(y/n)')                 #Asking the user.
w.writerows(L)                      #Writing the data onto the writer object.
f.close()                                   #Closing the file.
"'For Stock Management, I have used text files.'"

h=open('Purchased_Stock.txt','w')         #Opening file in write only mode.
a=int(input('Stock puchased :'))
h.write('January :'+str(a)+'\n')
h.close()

#For opening the file in append mode, following function is defined.

def ap(m,s):
     f=open('Purchased_Stock.txt','a')
     f.write(m+str(s)+'\n')
     f.close()
     return                             #Returning from function.

ap('February :',200)             #Function call statement
ap('March :',150)
ap('April :',200)
ap('May :',350)
ap('June :',200)

h=open('Stock_Sold.txt','w')         #Opening file in write only mode.
a=int(input('Stock sold :'))
h.write('January :'+str(a)+'\n')
h.close()

#For opening the file in append mode, following function is defined.

def ap(m,s):
     f=open('Stock_Sold.txt','a')
     f.write(m+str(s)+'\n')
     f.close()
     return                             #Returning from function.

ap('February :',150)                #Function call statement
ap('March :',130)
ap('April :',190)
ap('May :',300)
ap('June :',180)

"'For calculating stock left.'"

D=[]
E=[]
g=open('Purchased_stock.txt','r')              #Opening file in read only mode.
i=open('Stock_Sold.txt')            #The default mode is read only.
for j in g:
    b=j.split(':')
    a=int(b[1])
    D.append(a)
print(D)
print('\n')

for k in i:
    c=k.split(':')
    d=int(c[1])
    E.append(d)
print(E)
print('\n')

for x in range(6):
    y=D[x]-E[x]
    print(y)            #Displaying the stock remaining.
g.close()
i.close()

'"For calculating Profit Percentage."'

def tp(a,b):           #Function for total price.
    return a*b

def pp(m,n):            #Function for profit percentage.
    return (m*100)/n

H=[]
G=[]
L=[]
T=[]
w=open('Purchased_stock.txt','r')
z=open('Stock_Sold.txt')
x=float(input('Cost price of 1 product :'))
y=float(input('Selling price of 1 product :'))
print('\n')

for i in w:
    A=i.split(':')
    t=A[0]
    T.append(t)              #List of months
    C=int(A[1])
    h=tp(x,C)                #Function call statement
    H.append(h)             #List of total cost price per month
print(H)
print('\n')

for e in z:


    B=e.split(':')
    E=int(B[1])
    g=tp(y,E)                  #Function call statement
    G.append(g)                  #List of total selling price per month
print(G)
print('\n')

for f in range(6):
    p=G[f]-H[f]
    q=pp(p,H[f])                #Function call statement
    L.append(q)             #List of profit percentage per month
print(L)

"'For plotting profit percentage graph.'"

from matplotlib import pyplot   #Using pyplot module of matplotlib for plotting graph
pyplot.bar(T,L)               #Plotting bar graph
pyplot.xlabel('Months')         #Labelling x-axis of the graph
pyplot.ylabel('Profit percentage')         #Labelling y-axis of the graph
pyplot.show()            #Showing graph
