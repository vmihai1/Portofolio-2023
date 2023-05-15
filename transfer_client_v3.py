from tkinter import *
import smtplib
import mimetypes
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from tkinter import filedialog
import zipfile
import os

def closewindow():
    window.destroy()
try:
    fo=open("user.txt",'r')
    content=fo.read().splitlines()
    #emailfrom ="valentin.mihai@vodafone.com"
    emailfrom = content[0]
    emailto = content[1]
    server_addr=content[2]
    #port=content[3]
except:
    print("Please create the user.txt file with correct content.")

#global variables
# server_addr = "10.50.169.99"
#server_addr = '10.1.4.15' #old - no longer used
#server_addr='10.0.72.45'
#server_addr='10.217.150.12' #new, can be used also

filelist=()
filelist1=()
filelist_string='Hint: save sender/receiver in <user.txt>\n1st row: opcowin user, 2nd row VDF email address.\n\n'

#Create GUI window
window = Tk()
# Set window title
window.title('Email File Transfer v3.0')
# Set window size
window.geometry("800x550")
# Set window background color
window.config(background="white")
#
# Create a File Explorer label
label_file_explorer = Label(window, text="Select options", width=21, height=1, fg="blue",)
#button_exit = Button(window, text="Exit", command=closewindow,width=20)
label_file_explorer.grid(column=1, row=2,sticky="W")
#button_exit.grid(column=1, row=5,sticky="W")

def select_files():
    global filelist,filelist1
    global filelist_string
    filelist=filedialog.askopenfilenames(initialdir="/C:/", title="Select a File")
    #print(type(filelist))
    #print(filelist)
    lst=list(filelist)
    for item in filelist:
        filelist_string=filelist_string+item+'\n'
    print(filelist_string)
    zipMe = zipfile.ZipFile('CitrixTransfer.zip', 'w')

    for file in filelist:
        zipMe.write(file, arcname=file.split("/")[-1], compress_type=zipfile.ZIP_DEFLATED)
    lst.append('CitrixTransfer.zip')
    filelist1=tuple(['CitrixTransfer.zip'])
    print(filelist1)
    #T = Text(window, height=20, width=80)
    Label(window, text='Files', fg='Black', bg='white', font='Calibri 10 bold').place(x=150, y=150)
    T=Frame(window)
    T.place(x=200,y=150)
    #T.grid(column=2, row=5)
    e0=Text(T,width=80, height=20, font=('Helvetica', 9), wrap=WORD)
    e0.insert(END, filelist_string)
    e0.pack(side=TOP, fill=Y)

Label(window, text='Subject', fg='Black',bg='white', font='Calibri 10 bold').place(x=150, y=0)
frame1 = Frame(window)
frame1.place(x=200, y=0)
e1 = Text(frame1, width=80, height=10, font=('Helvetica', 9), wrap=WORD)
e1.insert(INSERT,"")
e1.pack(side=TOP, fill=Y)
def retrieve_input1():
    if e1.get('1.0', 'end-1c') != '':
        return e1.get('1.0', 'end-1c')
    else:
        return "EMAIL FILE TRANSFER"
    #print(e.get('1.0', 'end-1c'))

Label(window, text='Body', fg='Black',bg='white', font='Calibri 10 bold').place(x=150, y=40)
frame2 = Frame(window)
frame2.place(x=200, y=30)
e2 = Text(frame2, width=80, height=10, font=('Helvetica', 9), wrap=WORD)
e2.insert(INSERT,"")
e2.pack(side=BOTTOM, fill=Y)
def retrieve_input2():
    if e2.get('1.0', 'end-1c')!='':
        return e2.get('1.0', 'end-1c')
    else:
        return "."
    #print(e.get('1.0', 'end-1c'))

def send_email(send_type):
    global emailto, emailfrom, server_addr,filelist, filelist1
    #print(filelist1)
    msg = MIMEMultipart()
    msg["From"] = emailfrom
    msg["To"] = emailto
    msg["Subject"] = retrieve_input1()
    body = retrieve_input2()
    msg.attach(MIMEText(body))

    #msg.preamble = "YOUR EMAIL SUBJECT"
    #zipMe=zipfile.ZipFile('CitrixTransfer.zip', 'w')
    #print(zipMe.filename)
    if send_type=='unzipped':
        fileList=filelist
    if send_type=='zipped':
        fileList=filelist1
    for file in fileList:
        #print(file)
        ctype, encoding = mimetypes.guess_type(file)
        #print("ctype, encoding",ctype, encoding)
        if ctype is None or encoding is not None:
            ctype = "application/octet-stream"

        maintype, subtype = ctype.split("/", 1)
        #print("maintype, subtype",maintype, subtype)
        fp = open(file, "rb")
        attachment = MIMEBase(maintype, subtype)
        attachment.set_payload(fp.read())
        fp.close()
        encoders.encode_base64(attachment)
        attachment.add_header("Content-Disposition", "attachment", filename=file.split("/")[-1])
        msg.attach(attachment)
        #zipMe.write(file, compress_type=zipfile.ZIP_DEFLATED)
        #zipMe.write(file, arcname=file.split("/")[-1],compress_type=zipfile.ZIP_DEFLATED)

    #attachment.add_header("Content-Disposition", "attachment", filename='CitrixTransfer.zip'.split("/")[-1])
    #msg.attach(attachment)
    # print(zipMe.filename[0])
    # ctype, encoding = mimetypes.guess_type(file)
    # # print("ctype, encoding",ctype, encoding)
    ctype, encoding = mimetypes.guess_type('CitrixTransfer.zip')
    #print(ctype, encoding)
    if ctype is None or encoding is not None:
        ctype = "application/octet-stream"

    maintype, subtype = ctype.split("/", 1)
    #print(maintype, subtype)
    #fp = open('CitrixTransfer.zip', "rb")
    with open('CitrixTransfer.zip','rb') as fp:
        #attachment1 = MIMEBase("application/x-zip-compressed", 'octet-stream')
        attachment1 = MIMEBase(maintype, "zip")
        attachment1.set_payload(fp.read())
        #fp.close()
        encoders.encode_base64(attachment1)
        #attachment1.add_header("Content-Disposition", "attachment; filename=\"%s.zip\"", filename='CitrixTransfer.zip')
        #attachment1.add_header('Content-Disposition', 'filename="%s"' % os.path.basename('CitrixTransfer.zip') ,filename='CitrixTransfer.zip')
        #attachment1.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename('CitrixTransfer.zip'))
        attachment1.add_header('Content-Disposition', 'attachment; filename="CitrixTransfer.zip"')
        #attachment1.add_header('Content-Transfer-Encoding', encoding)


        #print(attachment1)
        #msg.attach(attachment1)
    # smtp_server = "smtp.mailtrap.io"
    # login = "929c6843c43769"
    # password = "6b213451468e9b"
    # server_addr = '10.1.4.15' #old - no longer used
    #server_addr = '10.0.72.45' #new
    # server_addr='10.217.150.12' #new, can be used also

    server = smtplib.SMTP(server_addr,25,timeout=120)

    #server.connect(host='localhost',port=25,source_address=None)
    #server.login(login, password)
    server.set_debuglevel(0)
    server.sendmail(emailfrom, emailto, msg.as_string())
    filelist_string = 'The email was sent successfully.' + '\n'
    server.quit()
    print('The email was sent successfully.')
    window.destroy()


button_select_files=Button(window, text="File select", command=select_files,width=20).grid(column=1,row=2,sticky="W")

button_send = Button(window, text='Send', command=lambda :send_email("unzipped"),width=20)
button_send.grid(column=1, row=3,sticky="W")
button_send_zipped = Button(window, text='Send ZIP', command=lambda:send_email("zipped"),width=20)
button_send_zipped.grid(column=1, row=4,sticky="W")
Label(window, text='© 2021-2022 Valentin Mihai', fg='DarkGoldenrod4', font='Calibri 10 bold').place(x=25, y=530)

#print(lambda:print(e.get('1.0','end-1c')))
#print(retrieve_input())

window.mainloop()

try:
    #print(os.getcwd()+'/CitrixTransfer.zip')
    os.remove(os.getcwd()+'/CitrixTransfer.zip')
except:
    print("exception")
    pass
# Bellow syntax for sending email from Local machine, using Outlook server
# sender = 'valentin.mihai@vodafone.com'
# sender1 = 'vmihai1@nmcgate.mmo.de'
# # receivers = ['valentin.mihai@vodafone.com','mihai_valentin100@yahoo.com','cristinamihaelanecsoiu@gmail.com']
#
# receivers = 'valentin.mihai@vodafone.com'
# message = """From: Valentin Mihai <vmihai1@nmcgate.mmo.de>
# To: <valentin.mihai@vodafone.com>
# Subject: SMTP e-mail test
#
# This is a test e-mail message.
# """
# try:
#     smtpObj_windows = smtplib.SMTP('10.50.169.99')
#     smtpObj_windows.sendmail(sender, receivers, message)
#     # smtpObj_MAE = smtplib.SMTP('10.0.72.45')
#     # smtpObj_MAE = smtplib.SMTP('10.1.4.15')
#     # smtpObj_MAE.login()
#     # smtpObj_MAE.sendmail(sender1, receivers, message)
#     print("Successfully sent email")
# except:
#     print("Error: unable to send email")

print(input("Press any key.."))
