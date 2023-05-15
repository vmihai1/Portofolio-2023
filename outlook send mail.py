destination_address='valentin.mihai@vodafone.com;florin.buja1@vodafone.com'

attach_list=[]

def mailsend(dest,attachment_list):
    import win32com.client


    outlook = win32com.client.Dispatch("Outlook.Application")
    namespace = outlook.GetNamespace("MAPI")


    Msg = outlook.CreateItem(0)
    Msg.To = dest
    print(type(Msg.To))
    #Msg.CC = dest
    #Msg.BCC = "valentin.mihai@vodafone.com"

    Msg.Subject = "The subject of your mail"
    Msg.Body = "The main body text of you mail"
    for item in attachment_list:
        Msg.Attachments.Add(item)


    Msg.Send()


mailsend(destination_address,attach_list)