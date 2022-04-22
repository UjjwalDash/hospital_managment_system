import os
from tkinter import*
from tkinter import ttk
import random
import time
import tempfile
import datetime
import  tkinter.messagebox
import sqlite3

root=Tk()
root.title("Hospital Management System")
root.geometry("1350x750+0+0")
root.configure(background='Light Green')


cmbNameTablets=StringVar()
Ref=StringVar()
Dose=StringVar()
NumberTablets=StringVar()
Lot=StringVar()
IssuedDate=StringVar()
ExpDate=StringVar()
ExpDateS=StringVar()
DailyDose=StringVar()
PossibleSideEffects=StringVar()
FurtherInformation=StringVar()
StorageAdvice=StringVar()
DrivingUsingMachines=StringVar()
HowtoUseMedication=StringVar()
PatientID=StringVar()
PatientPhoneNo=StringVar()
PatientName=StringVar()
DateofBirth=StringVar()
DatesofBirth=StringVar()
DateofBirths=StringVar()
PatientAddress=StringVar()
Prescription=StringVar()
Ref.set(random.randint(100000,9999999))
IssuedDate.set(time.strftime("%d/%m/%y"))

cost=StringVar()
#--------------------------------------------------------------Function declaration-----------------------------------------------------------------------------------------------------------------------------

def search():
    if PatientName.get()!='':
        e=PatientName.get().lower()
        rd=Tk()
        rd.geometry('550x550')
        rd.title("Patient's Details")
        rd.configure(bg='Light Green')
        ou8=Text(rd,width=20,height=5,font=('none 16 bold'))
        ou8.grid(row=8,column=1)
        nam1=Label(rd,text='Patient Name',font=('arial 15 bold'),bg='Light Green')
        nam1.grid(row=0,column=0,sticky=W)
        ou7=Text(rd,width=20,height=1,font=('none 16 bold'))
        ou7.grid(row=0,column=1)
        ou7.insert(END,e)
        nam2=Label(rd,text='Reference No:',font=('arial 15 bold'),bg='Light Green')
        nam2.grid(row=1,column=0,sticky=W)
        nam3=Label(rd,text='Phone No.',font=('arial 15 bold'),bg='Light Green')
        nam3.grid(row=2,column=0,sticky=W)
        nam4=Label(rd,text='Address:',font=('arial 15 bold'),bg='Light Green')
        nam4.grid(row=3,column=0,sticky=W)
        nam5=Label(rd,text='Name of tablet',font=('arial 15 bold'),bg='Light Green')
        nam5.grid(row=4,column=0,sticky=W)
        nam6=Label(rd,text='Issued Date',font=('arial 15 bold'),bg='Light Green')
        nam6.grid(row=5,column=0,sticky=W)
        nam7=Label(rd,text='Patient ID',font=('arial 15 bold'),bg='Light Green')
        nam7.grid(row=6,column=0,sticky=W)
        nam8=Label(rd,text='Daily Dose',font=('arial 15 bold'),bg='Light Green')
        nam8.grid(row=7,column=0,sticky=W)
        
        def clk():
            crr=sqlite3.connect('recipt.db')
            c=crr.cursor()
            c.execute('select* from recipt')
            l=c.fetchall()
            d={}
            for row in l:
                d[row[0]]=row[1],row[2],row[3],row[4],row[5],row[6],row[7]
                
            try:
                b=d[e]
                
                Ref=b[0]
                PatientPhoneNo=b[1]
                PatientAddress=b[2]
                cmbtabletname=b[3]
                IssuedDate=b[4]
                PatientID=b[5]
                DailyDose=b[6]
                if (PatientName.get()==""):
                    k="Name not found"
                else:
                    k='Name found'
                ou8.insert(END,k)
                ou.insert(0.0,Ref)
                ou1.insert(0.0,PatientPhoneNo)
                ou2.insert(0.0,PatientAddress)
                ou3.insert(0.0,cmbtabletname)
                ou4.insert(0.0,IssuedDate)
                ou5.insert(0.0,PatientID)
                ou6.insert(0.0,DailyDose)
                
            except:
                hi='No Such Name Found'
                ou8.insert(END,hi)
                tkinter.messagebox.showinfo('program','No Such Name Found')
                rd.destroy()
        ou=Text(rd,width=20,height=1,font=('none 16 bold'))
        ou.grid(row=1,column=1)
        ou1=Text(rd,width=20,height=1,font=('none 16 bold'))
        ou1.grid(row=2,column=1)
        ou2=Text(rd,width=20,height=1,font=('none 16 bold'))
        ou2.grid(row=3,column=1)
        ou3=Text(rd,width=20,height=1,font=('none 16 bold'))
        ou3.grid(row=4,column=1)
        ou4=Text(rd,width=20,height=1,font=('none 16 bold'))
        ou4.grid(row=5,column=1)
        ou5=Text(rd,width=20,height=1,font=('none 16 bold'))
        ou5.grid(row=6,column=1)
        ou6=Text(rd,width=20,height=1,font=('none 16 bold'))
        ou6.grid(row=7,column=1)
        
        
        clk()
        rd.mainloop()
    else:
        tkinter.messagebox.showinfo('program','please enter the name')
def iExist():
    
    iExist=tkinter.messagebox.askyesno("Hospital Management Systems","Confirm if you want to exit")
    if iExist >0:
        root.destroy()
        
        return
def icost():
    if(cmbNameTablets.get()=='Quninine'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    if(cmbNameTablets.get()=='Paracetomal'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    
    if(cmbNameTablets.get()=='Tonact'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    
    if(cmbNameTablets.get()=='"Losar-50'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    
    if(cmbNameTablets.get()=='Glasiphase'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    if(cmbNameTablets.get()=='Quninine'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    if(cmbNameTablets.get()=='Acilok'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    if(cmbNameTablets.get()=='Eltroxin'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    if(cmbNameTablets.get()=='Metronidazole'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    if(cmbNameTablets.get()=='Calpol'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    if(cmbNameTablets.get()=='Aspirin'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    if(cmbNameTablets.get()=='Bcosul'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    if(cmbNameTablets.get()=='Zentac'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    if(cmbNameTablets.get()=='Losar-50'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
    if(cmbNameTablets.get()=='Adrenalin'):
        if(Dose.get()=='1'):
            q=float (NumberTablets.get())
            price=float(5*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='2'):
            q=float (NumberTablets.get())
            price=float(7*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='3'):
            q=float (NumberTablets.get())
            price=float(9*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='4'):
            q=float (NumberTablets.get())
            price=float(11*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='5'):
            q=float (NumberTablets.get())
            price=float(13*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='6'):
            q=float (NumberTablets.get())
            price=float(15*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='7'):
            q=float (NumberTablets.get())
            price=float(17*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='8'):
            q=float (NumberTablets.get())
            price=float(19*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='9'):
            q=float (NumberTablets.get())
            price=float(21*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='10'):
            q=float (NumberTablets.get())
            price=float(23*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='11'):
            q=float (NumberTablets.get())
            price=float(25*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='12'):
            q=float (NumberTablets.get())
            price=float(27*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='13'):
            q=float (NumberTablets.get())
            price=float(29*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='14'):
            q=float (NumberTablets.get())
            price=float(31*q)
            t='Rs'+str(price)
            cost.set(t)
        if(Dose.get()=='15'):
            q=float (NumberTablets.get())
            price=float(33*q)
            t='Rs'+str(price)
            cost.set(t)
def iPrescription (): 
    txtPresciption.insert(END,'Name of Tablets:  \t\t\t\t' +  cmbNameTablets.get()   +  "\n")
    txtPresciption.insert(END,'Reference No:  \t\t\t\t' +  Ref.get()   +  "\n")
    txtPresciption.insert(END,'Dose:  \t\t\t\t' +  Dose.get()   +  "\n")
    txtPresciption.insert(END,'Number of Tablets:  \t\t\t\t' +  NumberTablets.get()   +  "\n")
    txtPresciption.insert(END,'Lot:  \t\t\t\t' +  Lot.get()   +  "\n")
    txtPresciption.insert(END,'Issued Date:  \t\t\t\t'   +  IssuedDate.get()   +  "\n")
    txtPresciption.insert(END,'Exp.Date:  \t\t\t\t' +  ExpDate.get() + ExpDateS .get()   +  "\n")
    txtPresciption.insert(END,'DailyDose:  \t\t\t\t' + DailyDose.get()   +  "\n")
    txtPresciption.insert(END,'Possible Side Effects:  \t\t\t\t' +  PossibleSideEffects.get()   +  "\n")
    txtPresciption.insert(END,'Further Information:  \t\t\t\t' + FurtherInformation.get()   +  "\n")
    txtPresciption.insert(END,'Storing Advice:  \t\t\t\t' +  StorageAdvice.get()   +  "\n")
    txtPresciption.insert(END,'Driving or Using Machines:  \t\t\t\t' +DrivingUsingMachines .get()   +  "\n")
    txtPresciption.insert(END,'How to use medication:  \t\t\t\t' + HowtoUseMedication .get()   +  "\n")
    txtPresciption.insert(END,'Patient ID:  \t\t\t\t' +  PatientID.get()   +  "\n")
    txtPresciption.insert(END,'Phone No:  \t\t\t\t' + PatientPhoneNo.get()   +  "\n")
    txtPresciption.insert(END,'Patient Name:  \t\t\t\t' + PatientName.get()   +  "\n")
    txtPresciption.insert(END,'Date of Birth:  \t\t\t\t' + DatesofBirth.get()+ DateofBirth.get() + DateofBirths.get()   +  "\n")
    txtPresciption.insert(END,'PatientAddress:  \t\t\t\t' +PatientAddress.get()   +  "\n")
    txtPresciption.insert(END,'Total Cost:  \t\t\t\t' +cost .get()   +  "\n")
    if(PatientPhoneNo.get()==""):
        tkinter.messagebox.showinfo("program","Please enter patient phone no.")
        txtPresciption.delete("1.0",END)
    if(len(PatientPhoneNo.get())>0):
        h=PatientPhoneNo.get()
        for i in range(len(h)):            
            if(h[i].isalpha()):                
                tkinter.messagebox.showinfo("program","Please enter patient phone no. in number")
                txtPresciption.delete("1.0",END)
                break
            else:
                continue
    if((len(PatientPhoneNo.get())<=9) and (len(PatientPhoneNo.get())>0)):
        tkinter.messagebox.showinfo("program","Please enter correct phone number")
        txtPresciption.delete("1.0",END)
    if(len(PatientPhoneNo.get())>=11):
        tkinter.messagebox.showinfo("program","Please enter correct phone number")
        txtPresciption.delete("1.0",END)
    if(PatientAddress.get()==""):
        tkinter.messagebox.showinfo("program","Please enter Patient Address ")
        txtPresciption.delete("1.0",END)
    if(PatientID.get()==""):
        tkinter.messagebox.showinfo("program","Please enter Patient ID")
        txtPresciption.delete("1.0",END)
    if (len(PatientName.get())>0):
        a=PatientName.get()
        for i in range(len(a)):
            if(a[i].isdigit()):
                tkinter.messagebox.showinfo("program","Please enter correct name")
                txtPresciption.delete("1.0",END)
            else:
                continue
    if (len(PatientName.get())==""):
        tkinter.messagebox.showinfo("program","Please enter patient's name")
        txtPresciption.delete("1.0",END)
    if (len(PatientName.get())>0):
        a=PatientName.get()
        if (a[0].islower()):
            tkinter.messagebox.showinfo("program","Please enter first letter of patient's name in capital")
            txtPresciption.delete("1.0",END)
        else:
            True
    if (len(Lot.get())>0):
        d=Lot.get()
        for i in range(len(d)):
            if (d[i].isalpha()):
                tkinter.messagebox.showinfo("program","Please enter Lot in number ")
                txtPresciption.delete("1.0",END)
                break
            else:
                continue
    if(len(PatientID.get())>0):
        b=PatientID.get()
        for j in range(len(b)):
            if(b[j].isalpha()):
                if(b[j].islower()):
                    tkinter.messagebox.showinfo("program","Please enter Patient's ID in capital")
                    txtPresciption.delete("1.0",END)
                    break
                else:
                    continue
            else:
                continue
    if((DateofBirth.get()=="Feb") and (DatesofBirth.get()=="30") ):
        tkinter.messagebox.showinfo("program","Please enter correct date of birth")
        txtPresciption.delete("1.0",END)
    if((DateofBirth.get()=="Feb") and  (DatesofBirth.get()=="31")):
        tkinter.messagebox.showinfo("program","Please enter correct date of birth")
        txtPresciption.delete("1.0",END)
    if((DateofBirth.get()=="April") and (DatesofBirth.get()=="31")):         
        tkinter.messagebox.showinfo("program","Please enter correct date of birth")
        txtPresciption.delete("1.0",END)    
    if((DateofBirth.get()=="June") and (DatesofBirth.get()=="31" )):        
        tkinter.messagebox.showinfo("program","Please enter correct date of birth")
        txtPresciption.delete("1.0",END)
    if((DateofBirth.get()=="Sept") and(DatesofBirth.get()=="31")):        
        tkinter.messagebox.showinfo("program","Please enter correct date of birth")
        txtPresciption.delete("1.0",END)
    if((DateofBirth.get()=="Nov") and (DatesofBirth.get()=="31")):        
        tkinter.messagebox.showinfo("program","Please enter correct date of birth")
        txtPresciption.delete("1.0",END)
    if(PatientName.get()==""):
        tkinter.messagebox.showinfo("program","Please enter patient's name")
        txtPresciption.delete("1.0",END)
            
    a=str(PatientName.get().lower())
    b=str(PatientPhoneNo.get())
    c=str(PatientAddress.get())
    d=str(cmbNameTablets.get())
    x=str(Ref.get())
    y=str(IssuedDate.get())
    e=str(PatientID.get())
    f=str(DailyDose.get())
    
    q="insert into recipt values"+'('+'"'+a+'"'+','+'"'+x+'"'+','+'"'+b+'"'+','+'"'+c+'"'+','+'"'+d+'"'+','+'"'+y+'"'+','+'"'+e+'"'+','+'"'+f+'"'+')'
    
    crr=sqlite3.connect('recipt.db')
    c=crr.cursor()
    #c.execute("create table recipt(Name TEXT,SlipNO TEXT,PhoneNo TEXT,Adress TEXT,TotalCost TEXT,DateofOrder TEXT,Patient id TEXT,dAILY dOSE TEXT)")
    c.execute(q)
    crr.commit()
    c.close()
    
    return

def iPresciptionData():
    if cost .get()!='':
        root1=Tk()
        root1.maxsize(500,800)
        root1.minsize(500,800)
        txtFrameDetail=Text(font=('aerial',12,'bold'),width=141,height=4,padx=2,pady=4)
        
        def code():
            
            q=txtFrameDetail.get('1.0','end-1c')
            filename=tempfile.mktemp('.txt')
            open(filename,'w').write(q)
            os.startfile(filename)
        #txtFrameDetail.insert(END, cmbNameTablets.get()+"\t\t"+Ref.get+"\t"+Dose.get()+"\t\t"
        #+NumberTablets.get()+"\t"+Lot.get()+"\t"+IssuedDate.get()+"\t\t"+ExpDate.get()+"\t"
        #+DailyDose.get()+"\t\t"+StorageAdvice.get()+"\t"+PatientPhoneNo.get()+"\t\t"
        #+PatientName.get()+"\t\t"+DateOfBirth.get()+"\t\t"+PatientAdress.get()+'\n')
        txtFrameDetail.insert(END,'Patient ID:  \t\t\t\t' +  PatientID.get()   +  "\n")
        txtFrameDetail.insert(END,'Patient Name:  \t\t\t\t' + PatientName.get()   +  "\n")
        txtFrameDetail.insert(END,'PatientAddress:  \t\t\t\t' +PatientAddress .get()   +  "\n")
        txtFrameDetail.insert(END,'Phone No:  \t\t\t\t' + PatientPhoneNo.get()   +  "\n")   
        txtFrameDetail.insert(END,'Date of Birth:  \t\t\t\t' + DatesofBirth.get() + DateofBirth.get() + DateofBirths.get()   +  "\n")
        txtFrameDetail.insert(END,'Reference No:  \t\t\t\t' +  Ref.get()+"\t\t")
        txtFrameDetail.insert(END,'Issued Date:  \t\t'   +  IssuedDate.get()   +  "\n")
        txtFrameDetail.insert(END,'Name of Tablets:  \t\t\t\t' +  cmbNameTablets.get()   +  "\n")
        txtFrameDetail.insert(END,'Number of Tablets:  \t\t\t' +  NumberTablets.get()   +  "\n")
        txtFrameDetail.insert(END,'Dose:  \t\t\t\t\t' +  Dose.get()   +  "\n")
        txtFrameDetail.insert(END,'DailyDose:  \t\t\t\t' + DailyDose.get()   +  "\n")
        txtFrameDetail.insert(END,'Lot:  \t\t\t\t\t' +  Lot.get()   +  "\n")
        txtFrameDetail.insert(END,'Exp.Date:  \t\t\t\t' +  ExpDate.get() + ExpDateS.get()   +  "\n")    
        txtFrameDetail.insert(END,'Possible Side Effects:\t\t\t' +PossibleSideEffects.get()   +  "\n")
        txtFrameDetail.insert(END,'Further Information:\t\t\t\t'+FurtherInformation.get()   +  "\n")
        txtFrameDetail.insert(END,'Storing Advice:  \t\t\t\t'+StorageAdvice.get()   +  "\n")
        txtFrameDetail.insert(END,'Driving or Using Machines:\t\t\t'+DrivingUsingMachines .get()   +  "\n")
        txtFrameDetail.insert(END,'How to use medication:\t\t\t'+HowtoUseMedication .get()   +  "\n")    
        txtFrameDetail.insert(END,'----------------------------------------------------------------------------------------------------------------------------------------'  +  "\n")
        txtFrameDetail.insert(END,'Total Cost including GST:  \t\t\t\t' +cost .get()   +  "\n")
        txtFrameDetail.insert(END,'-----------------------------------------------------------------------------------------------------------------------------------------'  +  "\n")
        #=============================
        code()
        root1.destroy()
        root1.mainloop()
    else:
        tkinter.messagebox.showinfo("program","Please enter the total  cost")
        
def iDelete():

    cmbNameTablets.set("")
    cboNameTablet.current(0)
    Ref.set(random.randint(100000,9999999))
    #Ref.set("")
    Dose.set("")
    NumberTablets.set("")
    Lot.set("")
    IssuedDate.set(time.strftime("%d/%m/%y"))
    #IssuedDate.set("")
    ExpDate.set("")
    ExpDateS.set("")
    DailyDose.set("")
    PossibleSideEffects.set("")
    FurtherInformation.set("")
    StorageAdvice.set("")
    DrivingUsingMachines.set("")
    HowtoUseMedication.set("")
    PatientID.set("")
    PatientPhoneNo.set("")
    PatientName.set("")
    DateofBirth.set("")
    DatesofBirth.set("")
    DateofBirths.set("")
    PatientAddress.set("")
    txtPresciption.delete("1.0",END)
    txtFrameDetail.delete("1.0",END)
    
    return

def iReset():
    
    cmbNameTablets.set("")
    cboNameTablet.current(0)
    Ref.set(random.randint(100000,9999999))
    Dose.set("")
    NumberTablets.set("")
    Lot.set("")
    IssuedDate.set(time.strftime("%d/%m/%y"))
    #IssuedDate.set("")
    ExpDate.set("")
    ExpDateS.set("")
    DailyDose.set("")
    PossibleSideEffects.set("")
    FurtherInformation.set("")
    StorageAdvice.set("")
    DrivingUsingMachines.set("")
    HowtoUseMedication.set("")
    PatientID.set("")
    PatientPhoneNo.set("")
    PatientName.set("")    
    DateofBirth.set("")
    DateofBirths.set("")
    DatesofBirth.set("")
    PatientAddress.set("")
    txtPresciption.delete("1.0",END)
    txtFrameDetail.delete("1.0",END)
    cost.set('')
    return

#--------------------------------------------------------------Frame----------------------------------------------------------------------------------------------------------------------------------
     
MainFrame =Frame(bg ="maroon")
MainFrame.grid()

TitleFrame =Frame(MainFrame, bd=20, width=1350, padx=20, relief=RIDGE,bg='maroon')
TitleFrame.pack(side=TOP)

lblTitle =Label(TitleFrame, font=("Algerian",40,"bold"), text="\tHospital Management System\t", padx=2,bg='Misty Rose')
lblTitle.grid()

FrameDetail =Frame(MainFrame, bd=20, width=1350, height=400, padx=20, relief=RIDGE,bg='Misty Rose')
FrameDetail.pack(side=BOTTOM)

ButtonFrame =Frame(MainFrame, bd=20, width=1350, height=50, padx=20, relief=RIDGE,bg='Misty Rose')
ButtonFrame.pack(side=BOTTOM)

DataFrame =Frame(MainFrame, bd=20, width=1350, height=400, padx=20, relief=RIDGE,bg='Misty Rose')
DataFrame.pack(side=BOTTOM)

DataFrameLEFT=Frame(DataFrame, bd=10, width=1350, height=400, padx=20, relief=RIDGE,bg='Misty Rose')
DataFrameLEFT.pack(side=LEFT)

DataFrameRIGHT =Frame(DataFrame, bd=10, width= 1350, height=400, padx=20, relief=RIDGE,bg='Misty Rose')
DataFrameRIGHT.pack(side=RIGHT)

#------------------------------------------------------------DataFrameLEFT------------------------------------------------------------------------------------------------------------------------------------------------

lblNameTablet =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Name of Tablets :", padx=2, pady=2,bg='Misty Rose')
lblNameTablet.grid(row=0, column=0, sticky=W)

cboNameTablet=tkinter.ttk.Combobox(DataFrameLEFT, textvariable=cmbNameTablets, state='readonly', font=('arial',12,'bold'), width =23)
cboNameTablet.grid(row=0, column=1)
cboNameTablet['value']=("","Quninine","Paracetomal","Tonact","Losar-50","Acilok","Glasiphase","Eltroxin","Metronidazole","Calpol","Aspirin","Bcosul","Zentac","Adrenalin")
cboNameTablet.current(0)

lblFurtherInfo =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Further Information :", padx=2, pady=2,bg='Misty Rose')
lblFurtherInfo.grid(row=0, column=2, sticky=W)
txtFurtherInfo=Entry(DataFrameLEFT, font=("arial",12,"bold"), text="Further Information :",  textvariable=FurtherInformation, width= 25)
txtFurtherInfo.grid(row=0, column=3)

lblRef =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Reference No. :", padx=2, pady=2,bg='Misty Rose')
lblRef.grid(row=1, column=0, sticky=W)
txtRef=Entry(DataFrameLEFT, font=("arial",12,"bold"), text="Reference No. :",  textvariable=Ref, width= 25,state=DISABLED)
txtRef.grid(row=1, column=1)

lblStorage =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Storage Advice :", padx=2, pady=2,bg='Misty Rose')
lblStorage.grid(row=1, column=2, sticky=W)

cboStorage=tkinter.ttk.Combobox(DataFrameLEFT, textvariable=StorageAdvice, state='readonly', font=('arial',12,'bold'), width =23)
cboStorage.grid(row=1, column=3)
cboStorage['value']=("","Cool and dry place","On its container only")
cboStorage.current(0)

lblDose =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Dose :", padx=2, pady=2,bg='Misty Rose')
lblDose.grid(row=2, column=0, sticky=W)

cboDose=tkinter.ttk.Combobox(DataFrameLEFT, textvariable=Dose, state='readonly', font=('arial',12,'bold'), width =23)
cboDose.grid(row=2, column=1)
cboDose['value']=("","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15")
cboDose.current(0)

DUseMachine =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Driving Machines :", padx=2, pady=2,bg='Misty Rose')
DUseMachine.grid(row=2, column=2, sticky=W)
txtDUseMachine=Entry(DataFrameLEFT, font=("arial",12,"bold"), text="Driving Machines",  textvariable=DrivingUsingMachines, width= 25)
txtDUseMachine.grid(row=2, column=3)

lblNumberTablet =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Number Tablet :", padx=2, pady=2,bg='Misty Rose')
lblNumberTablet.grid(row=3, column=0, sticky=W)

cboNumberTablets=tkinter.ttk.Combobox(DataFrameLEFT, textvariable=NumberTablets, state='readonly', font=('arial',12,'bold'), width =23)
cboNumberTablets.grid(row=3, column=1)
cboNumberTablets['value']=("",5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
cboNumberTablets.current(0)

lblUseMedication =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Medication", padx=2, pady=2,bg='Misty Rose')
lblUseMedication.grid(row=3, column=2, sticky=W)
txtUseMedication=Entry(DataFrameLEFT, font=("arial",12,"bold"), text="Medication",  textvariable=HowtoUseMedication,width= 25)
txtUseMedication.grid(row=3, column=3)

lblLot =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Lot", padx=2, pady=2,bg='Misty Rose')
lblLot.grid(row=4, column=0, sticky=W)
txtLot=Entry(DataFrameLEFT, font=("arial",12,"bold"), text="Lot",  textvariable=Lot, width= 25)
txtLot.grid(row=4, column=1)

lblPatientID =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Patient ID", padx=2, pady=2,bg='Misty Rose')
lblPatientID.grid(row=4, column=2, sticky=W)
txtPatientID=Entry(DataFrameLEFT, font=("arial",12,"bold"), text="Patient ID",  textvariable=PatientID, width= 25)
txtPatientID.grid(row=4, column=3)

lblIssuedDate =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Issued Date", padx=2, pady=2,bg='Misty Rose')
lblIssuedDate.grid(row=5, column=0, sticky=W)
txtIssuedDate=Entry(DataFrameLEFT, font=("arial",12,"bold"), text="Issued Date",  textvariable=IssuedDate, width= 25,state=DISABLED)
txtIssuedDate.grid(row=5, column=1)

lblPatientPhoneNo =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Phone No.", padx=2, pady=2,bg='Misty Rose')
lblPatientPhoneNo.grid(row=5, column=2, sticky=W)
txtPatientPhoneNo=Entry(DataFrameLEFT, font=("arial",12,"bold"), text="Phone No.", textvariable=PatientPhoneNo, width= 25)
txtPatientPhoneNo.grid(row=5, column=3)

lblExpDate =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Exp Date", padx=2, pady=2,bg='Misty Rose')
lblExpDate.grid(row=6, column=0, sticky=W)
#txtExpDate=Entry(DataFrameLEFT, font=("arial",12,"bold"), textvariable=ExpDate, width= 15)
#txtExpDate.grid(row=6, column=1)

cboExpDate=tkinter.ttk.Combobox(DataFrameLEFT, textvariable=ExpDate, state='readonly', font=('arial',9,'bold'), width =14)
cboExpDate.place(x=141,y=165)
cboExpDate['value']=("","Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec")
cboExpDate.current(0)

cboExpDate=tkinter.ttk.Combobox(DataFrameLEFT, textvariable=ExpDateS, state='readonly', font=('arial',9,'bold'), width =13)
cboExpDate.place(x=257,y=165)
cboExpDate['value']=("","2022","2023","2024","2025","2026")
cboExpDate.current(0)


lblPatientName =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Patient Name", padx=2, pady=2,bg='Misty Rose')
lblPatientName.grid(row=6, column=2, sticky=W)
txtPatientName=Entry(DataFrameLEFT, font=("arial",12,"bold"), text="Patient Name",  textvariable=PatientName, width= 25)
txtPatientName.grid(row=6, column=3)

lblDailyDose =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Daily Dose", padx=2, pady=2,bg='Misty Rose')
lblDailyDose.grid(row=7, column=0, sticky=W)

cboDailyDose=tkinter.ttk.Combobox(DataFrameLEFT, textvariable=DailyDose, state='readonly', font=('arial',12,'bold'), width =23)
cboDailyDose.grid(row=7, column=1)
cboDailyDose['value']=("", 1,2, 3, 4, 5)
cboDailyDose.current(0)


lblDob =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Date of Birth", padx=2, pady=2,bg='Misty Rose')
lblDob.grid(row=7, column=2, sticky=W)
#txtDob=Entry(DataFrameLEFT, font=("arial",12,"bold"), text="Date of Birth",  textvariable=DateofBirth, width= 25)
#txtDob.grid(row=7, column=3)

cboDob=tkinter.ttk.Combobox(DataFrameLEFT, textvariable=DateofBirth, state='readonly', font=('arial',9,'bold'), width =9)
cboDob.place(x=600,y=193)
cboDob['value']=("","Jan","Feb","March","April","May","June","July","Aug","Sept","Oct","Nov","Dec")
cboDob.current(0)

cboDob=tkinter.ttk.Combobox(DataFrameLEFT, textvariable=DatesofBirth, state='readonly', font=('arial',9,'bold'), width =6)
cboDob.place(x=535,y=193)
cboDob['value']=("",1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31)
cboDob.current(0)

cboDob=tkinter.ttk.Combobox(DataFrameLEFT, textvariable=DateofBirths, state='readonly', font=('arial',9,'bold'), width =8)
cboDob.place(x=684,y=193)
cboDob['value']=("",1920,1921,1922,1923,1924,1925,1926,1927,1928,1930.1931,1932,1933,1934,1935,1936,1937,1938,1939,1940,1941,1942,1943,1945,1946,1947,1948,1949,1950,1951,1952,1953,1954,1955,1956,1957,1958,1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969,1970,1971,1972,1973,1974,1975,1976,1977,1978,1979,1980.1981,1982,1983,1984,1985,1986,1987,1988,1989,1990,1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019,2020)
cboDob.current(0)



lblSideEffects =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Side Effects", padx=2, pady=2,bg='Misty Rose')
lblSideEffects.grid(row=8, column=0, sticky=W)
txtSideEffects=Entry(DataFrameLEFT, font=("arial",12,"bold"),  textvariable=PossibleSideEffects, width= 25)
txtSideEffects.grid(row=8, column=1)

lblPatientAddress =Label(DataFrameLEFT, font=("arial",12,"bold"), text="Patient Address", padx=2, pady=2,bg='Misty Rose')
lblPatientAddress.grid(row=8, column=2, sticky=W)
txtPatientAddress=Entry(DataFrameLEFT, font=("arial",12,"bold"), text="Patient Address", textvariable=PatientAddress, width= 25)
txtPatientAddress.grid(row=8, column=3)

lblcost=Label(DataFrameLEFT, font=("arial",12,"bold"), text="Total Cost", padx=2, pady=2,bg='Misty Rose')
lblcost.grid(row=9, column=0, sticky=W)
txtcost=Entry(DataFrameLEFT, font=("arial",12,"bold"),textvariable=cost, width= 25,state=DISABLED)
txtcost.grid(row=9, column=1)


#--------------------------------------------------------------Data Frame Right--------------------------------------------------------------------------------------------------------------------------------------------

txtPresciption=Text(DataFrameRIGHT, font=('arial', 12, 'bold'), width = 43, height =14, padx=2, pady=4)
txtPresciption.grid(row=0, column=0)

#---------------------------------------------------------------ButtonFrame------------------------------------------------------------------------------------------------------------------------------------------------------
btncost=Button(ButtonFrame, text= "Total", font=('Forte', 15), width=18, bd=4, command=icost,bg='Purple')
btncost.grid(row=0, column=0)


btnPrescription=Button(ButtonFrame, text= "Prescription", font=('Forte', 15), width=18, bd=4, command=iPrescription,bg='light blue')
btnPrescription.grid(row=0, column=1)

btnPresciptionData =Button(ButtonFrame, text= "Presciption Data", font=('Forte', 15), width=18, bd=4, command=iPresciptionData,bg='Orange')
btnPresciptionData.grid(row=0, column=2)

btnSea=Button(ButtonFrame, text= "Search", font=('Forte', 15), width=18, bd=4, command=search,bg='Pink')
btnSea.grid(row=0, column=3)

btnReset=Button(ButtonFrame, text= "Reset", font=('Forte', 12), width=18, bd=4, command=iReset,bg='Brown')
btnReset.grid(row=0, column=4)

btnExist=Button(ButtonFrame, text= "Exit", font=('Forte', 17), width=18, bd=4, command=iExist,bg='Red')
btnExist.grid(row=0, column=5)


#------------------------------------------------------------FrameDetail----------------------------------------------------------------------------------------------------------------------------------------------------------------

lblLabel =Label(FrameDetail, font=("arial",10,"bold"), pady=8)
text = ('Name of Tablets  Reference no.  Doseage  No.of Tablets  Lot  Issued Date  Exp. Date  Daily Dose  Storage Adv.  PhoneNo.  Patient Name DOB  Address')

lblLabel.pack(side=BOTTOM)

                          
txtFrameDetail=Text(FrameDetail, font=('arial', 12, 'bold'), width= 141, height=4, padx=2, pady=4)
txtFrameDetail.pack(side=BOTTOM)
#txtFrameDetail.insert(END,text+'\n')

photo1=PhotoImage(file='1.png')
photo_label=Label(FrameDetail,image=photo1)
photo_label.pack(side=BOTTOM,fill=BOTH)


root.mainloop()


    
    
        
        
        

    
        
