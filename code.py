import mysql.connector as m
while 1==True:
menu=int(input('''
*CareWell Hospital OP*
------------------------
1.Search patient
2.Doctor list
3.New Patient
4.Update appointment
5.Update Renewal date
------------------------
Choose the number: '''))
con=m.connect(host='localhost',user='root',password='ISHANIbk@9648',database='hos
p', charset='utf8')
cur=con.cursor()
def patient_details(op):
c='select * from patient where op_id={}'.format(op)
cur.execute(c)
f=cur.fetchone()
l=[]
if f is None:
return l
else:
for x in f:
l.append(x)
return l
def doc_details():
c='select * from doctor'
cur.execute(c)
d_data=cur.fetchall()
import tabulate as t
x=[['Name','D code','Dept','Gender', 'Age','Working time','Available']]
for y in d_data:
x.append(list(y))
print(t.tabulate(x))
#searching patient

if menu==1:
d=input('op/ph ')
if d in 'OPop':
op=int(input('Enter op id '))
p=patient_details(op)
if p==[]:
print('OP id not registered')
else:
print("op id",p[0])
print("Name",p[1])
print("Age",p[2])
print("Gender",p[3])
print("Doctor code",p[4])
print("Appointment Date",p[5])
print("Appointment time",p[6])
print("Ph no",p[7])
print('Last renewed',p[8])
elif d in 'phPH':
ph=input('Enter phone number: ')
c1="select * from patient where phone='{}'".format(ph)
cur.execute(c1)
f=cur.fetchone()
if f is None:
print('Sorry not match')
else:
print("op id",f[0])
print("Name",f[1])
print("Age",f[2])
print("Gender",f[3])
print("Doctor code",f[4])
print("Appointment Date",f[5])
print("Appointment time",f[6])
print("Ph no",f[7])
print('Last renewed',p[8])
else:
print('Enter valid content')

#viewing or updating doc slots
elif menu==2:
doc_details()
doc=input('Choose doctor with d_code: ')
try:
cur.execute('select * from {}'.format(doc))
app=cur.fetchall()
except:
print('Code not match')
import tabulate as t
try:
slots=[]
for x in range(1,len(app)):
slots.append('Slot',x)
tab=[slots]
for y in app:
tab.append(list(y))
print(t.tabulate(tab))
key1=input('Do you want to update a slot?(y/n)')
if key1 in 'Yy':
d=input('Enter date')
s=input('Enter slot number (Slot x) ')
n=input('Enter new number of patients')
cur.execute('update {} set {}={} where date="{}"'.format(doc,'Slot_'+s,n,d))
con.commit()
print(‘Slot updated’)
else:
continue
except:
print(‘’check format’’)
#adding new patient
elif menu==3:
op=int(input('Enter op id '))
if patient_details(op)==[]:
na=input('Enter name: ')
age=int(input('Enter age: '))
g=input('M/F: ')
doc_details()
dc=input('Enter doctor code: ')

cur.execute('select * from {}'.format(dc))
s=cur.fetchall()
slots=[]
import tabulate as t
for x in s:
l=[]
for y in range(1,len(x)-1):
l.append('slot'+str(y)+'='+str(x[y-1]))
l.append(x[-1])
slots.append(l)
print(t.tabulate(slots))
app_date=input('Enter appointment date(YYYY/MM/DD): ')
app_time=input('Enter appointment time(HH:MM:SS): ')
ph=input('Enter phone number ')
cur.execute("insert into patient values ({},'{}',{},'{}','{}','{}','{}','{}','{}')".
format(op,na,age,g,dc,app_date,app_time,ph,app_date))
con.commit()
print('Patient added')
else:
print('Op already exists')
#updating appointment
elif menu==4:
try:
op=int(input('Enter op id '))
l=patient_details(op)
if l==[]:
continue
else:
cur.execute('select month(reg_date),year(reg_date) from patient where
op_id={}'.format(op))
od=cur.fetchall() #stores old dates
d=input('Enter new date: ')
t=input('Enter new time: ')
if int(d[0:4:1])>int(od[0][1]) and int(d[5:7:])>int(od[0][0]):
print('Time to renew card')
elif int(d[0:4:])>(int(od[0][1]))+1:
print('Time to renew card')
else:
pass

c4_1="update patient set app_date='{}' where op_id={}".format(d,l[0])
cur.execute(c4_1)
con.commit()
c4_2="update patient set app_time='{}' where op_id={}".format(t,l[0])
cur.execute(c4_2)
con.commit()
print('Appointment updated')
except:
print('Use correct format')
#updating registration date
elif menu==5:
op=int(input('Enter op id'))
d=input('Enter renewal date')
cur.execute('update patient set reg_date="{}" where op_id={}'.format(d,op))
con.commit()
print('Registration renewed')
#preventing undefined numbers
else:
print('Please enter correct function number')