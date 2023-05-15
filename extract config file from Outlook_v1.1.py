


Outlook_Config_Subfolder='CR'
# should be a folder in C:\
C_saving_folder='\\CR\\'
last_how_many_days = 100
my_email_address='valentin.mihai@vodafone.com'

import win32com.client
import os
import time
import datetime as dt
#import zipfile

outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")
root_folder=''
try:
    root_folder1 = namespace.Folders.Item(1) # example:  valentin.mihai@vodafone.com
    root_folder2 = namespace.Folders.Item(2)
    if root_folder1.Name==my_email_address:
        root_folder=root_folder1
    else:
        root_folder=root_folder2
except:
    pass
print(f'OUTLOOK Root folder name: {root_folder.Name}')

subfolder = root_folder.Folders['Inbox'].Folders[Outlook_Config_Subfolder]
print(f'OUTLOOK saving folder name: {subfolder.Name}')
local_folder='C:'+C_saving_folder
print(f'Local Folder for saved configs {local_folder}')
messages = subfolder.Items
messages.Sort("[ReceivedTime]", True)

# print(messages)
# print(count_messages)
# print(dir(messages))


print(f'Time now: {dt.datetime.now()}')

lastHourDateTime_14 = dt.datetime.now() - dt.timedelta(hours=24*last_how_many_days)
last2weeksMessages = messages.Restrict("[ReceivedTime] >= '" +lastHourDateTime_14.strftime('%m/%d/%Y %H:%M %p')+"'")
count_messages=last2weeksMessages.count

print(f'Time since configs are received: {lastHourDateTime_14}')

#files already existing in the config file folder
arr = os.listdir('C:'+C_saving_folder)
#print(arr)

if count_messages > 0:
        for i in range(0,count_messages):
            message = messages[i]
            #print(str(message.Sender))
            atch=message.Attachments
            nbrOfAttachmentInMessage=atch.Count
            x = 1
            while x <= nbrOfAttachmentInMessage:
                    attachment = atch.item(x)
                    file_name=str(attachment).split('.')[0]
                    extension=str(attachment).split('.')[1]
                    # try:
                    #     #if extension in ['zip', '7Z', 'XML', 'xml', 'ZIP', '7z', 'rar','RAR','.zip']:
                    #     if extension in ['xlsx','xls']:
                    #         extension=str(attachment).split('.')[1]
                    #     if '..' in str(attachment):
                    #         extension=str(attachment).split('.')[2]

                    # except :
                    #     #print(attachment)
                    #     pass
                    #         #extension = str(attachment).split('.')[2]

                    extension = str(attachment).split('.')[1]
                    # if  (str(attachment) not in arr)  and '[fisier pregatire integrare]' not in str(attachment) and ('CME' in str(attachment)) or ('XL' in str(attachment)) or ('B2' in str(attachment)) or ('XU' in str(attachment)) or ('.xml' in str(attachment)) or ('.XML' in str(attachment)) or ('.zip' in str(attachment)):
                    #
                    #     try:
                    #         if 'CME_' in str(file_name):
                    #             save_path='C:\\'+str(C_saving_folder)+'\\'  + str(file_name)[4::]+'_'+str(message.Sender).split(',')[0]+'_'+str(message.Sender).split(',')[1]+'.'+str(extension)
                    #             attachment.SaveAsFile(save_path)
                    #         else:
                    #             save_path='C:\\' +str(C_saving_folder)+'\\'+ str(file_name) + '_' + str(message.Sender).split(',')[0] + '_' +str(message.Sender).split(',')[1]  + '.'+str(extension)
                    #             attachment.SaveAsFile(save_path)
                    #
                    #     except:
                    #         if str(message.Sender)=='Mail Delivery System':
                    #             pass
                    #         else:
                    #             pass
                    save_path = 'C:\\' + str(C_saving_folder) + '\\' + str(file_name)[0::] + '_' + str(message.Sender).split(',')[0] + '_' + str(message.Sender).split(',')[1] + '.' + str(extension)
                    attachment.SaveAsFile(save_path)
                        #attachment.SaveAsFile('C:\\Z\\' + str(attachment))
                    x=x+1


