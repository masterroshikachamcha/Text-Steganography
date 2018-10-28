from tkinter import *

from_email='regestration.university121@gmail.com'
from_pwd="Bennett123"


root=Tk()
root.title('Text Steganography')

Label(root, font=('arial',18,'bold'), text='Text Steganography',width=50,height=3).grid(row=0,columnspan=2)
Label(root, text='Secret Message: ').grid(row=1,column=0,sticky=W)
secret_msgV=StringVar()
Entry(root, textvariable=secret_msgV,width=60).grid(row=1,column=1,sticky=W)

Label(root, text='Text: ').grid(row=2,column=0,sticky=W)
textV=StringVar()
Entry(root, textvariable=textV,width=60).grid(row=2,column=1,sticky=W)

Label(root).grid()

def submit_btn():
    
    n=textV.get().lower()
    S=secret_msgV.get().lower()
    
    s=S.split(",")
    delD=[]
    d=0
    j=0
    max_len=len(n)
    for x in range (len(s)):
        while j<max_len:
            if n[j]==s[x]:
                deld=j+1-d
                d=j+1
                j=j+1
                delD.append(deld)
                break
            else:
                j=j+1

    r=[]
    e=[]
    for i in range(len(delD)):
        dele=delD[i]//26
        e.append(dele)
        delr=delD[i]
        r.append(delr)  
  
    encoded_version={}
    r=[3,2,6,1,1,1,2,2,11,21,1,1,1,7,5,3,13,2,1,1]
    dictionary=[]
    lst=[]
    for i in range(1,27):
        lst.append(i)
        encoded_version[i]=lst
        lst=[]

    val_dict=list(encoded_version.values())
    key_dict=list(encoded_version.keys())
    n=len(r)
    p=[]
    rprime=[]
    for j in range(n):
        c=r[j]
        p.append(c)
        if p in val_dict:    
            pass
        else:
            p1=list(p[:-1])
            rprime.append(key_dict[val_dict.index(p1)])
            encoded_version[len(list(encoded_version.keys()))+1]=p
            val_dict=list(encoded_version.values())
            key_dict=list(encoded_version.keys())
            p=[]
            p.append(c) 
    bitstream=[]
    for v in rprime:
        six_bits=format(v,'06b')
        bitstream.append(six_bits)
  
    new_bitstream=" ".join(bitstream)
    bitstream=new_bitstream.replace(" ","")

    if len(bitstream)%26!=0:
        bitstream=bitstream+("0"*(12-len(bitstream)%26))

    x=[]
    y=[]
    z=[]
    
    for i in range(0,len(bitstream),12):
        mst=""
        lstt=""
        vst=""
        for j in range(i,i+9):
            mst=mst+bitstream[j]
    
  
        for v in range(i+9,i+12):
            vst=vst+bitstream[v]

        new=int(mst,2)
        x1=new//26
        y1=new%26
        z1=int(vst,2)
        x.append(x1)
        y.append(y1)
        z.append(z1)

    lst=[]
    x_lst=65
    while x_lst<=90:
        lst1_lst=[""]
        for i in range(0,26):
            y_lst=x_lst
            t_lst=y_lst+i
            if t_lst<=90:
                lst1_lst.append(chr(t_lst))
            if (t_lst)>90:
                t_lst=t_lst-90
            
                lst1_lst.append(chr(t_lst+64))
        lst.append(lst1_lst)
        x_lst+=1

    var_string=[]
    for access in range(len(x)):
        var_string.append((lst[access][x[access]+1] + lst[access][y[access]+1]).lower())

    keys=["@hotmail.com","@gmail.com","@yahoo.com","@msn.com","@windowslive.com","@mail.com","@myspace.com","@mynet.com"]

    import random, string

    def randomword(length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))

    rand_list=[]   
    for i in range(len(x)):
        rand_word=randomword(4)
        rand_list.append(rand_word)

    empty_string=""
    emp_strg=[]
    for i in range(len(x)):
        empty_string=var_string[i]+rand_list[i]
        emp_strg.append(empty_string)

    key_empty_strg=[]

    for i in range(len(z)):
        key_empty_strg.append(emp_strg[i]+keys[z[i]])

####################################################################
    root.destroy()
    r=Tk()
    r.title('Send Message')

    str1=''
    for i in key_empty_strg:
        str1+=i+', '

    Label(r).grid()
    Label(r,font=('arial',13,'bold'),text='To: ').grid(row=1,column=0,sticky=W)
    toV=StringVar()
    Entry(r,textvariable=toV,width=50).grid(row=1,column=1,sticky=W)

    Label(r).grid(row=2)

    Label(r,font=('arial',13,'bold'),text='CC: ').grid(row=3,column=0,sticky=W)
    cc=StringVar()
    Label(r,text=str1).grid(row=3,column=1,sticky=W)

    Label(r).grid(row=4)

    Label(r,font=('arial',13,'bold'),text='Subject: ').grid(row=5,column=0,sticky=W)
    subject=StringVar()
    Entry(r, textvariable=subject,width=50).grid(row=5,column=1,sticky=W)

    Label(r).grid()

    Label(r,font=('arial',13,'bold'),text='Message Box: ').grid(row=7,sticky=W)
    Label(r,text=textV.get()).grid(row=8,column=1,sticky=W)

    Label(r).grid(row=9,column=0)
    def send():
        import smtplib
        to=toV.get()
        cc=key_empty_strg
        content=textV.get().lower()

        message='From: %s\r\n' % from_email + 'To: %s\r\n' % to + 'CC: %s\r\n' % cc + 'Subject: %s\r\n' % subject.get() +'\r\n'+ content

        
        mail = smtplib.SMTP("smtp.gmail.com",587) 
        mail.ehlo()
        mail.starttls()
        mail.login(from_email , from_pwd)
        mail.sendmail(from_email, [to]+cc , message)
        mail.close()
        

    Button(r,text='Send',command=send).grid(row=10,columnspan=2)
    Label(r).grid()

    r.mainloop()

Button(root, text='Submit',command=submit_btn).grid(row=4,columnspan=2)
Label(root).grid()

root.mainloop()
