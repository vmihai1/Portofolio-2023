import openpyxl as xl
def f(file_name,sheet_name):
    data=list()
    wb=xl.load_workbook(str(file_name),data_only='True')
    Sheet=wb[str(sheet_name)]

    for i in range(2, len(Sheet['A'])+1):
         data.append(Sheet.cell(row=i, column=1).value)

    #print(data)
    fileoutput=''
    fo=open(f'script_{sheet_name}.txt','a')
    for item in data:
        fileoutput=fileoutput+'REG NE:NAME="'+item+'";\n'+'LST CELL:;\n'+'LST CAMGTCFG:;\n'+'UNREG NE:NAME="'+item+'";\n'

    fo.write(fileoutput)



f('CAMGTCFG_sites.xlsx','Toronto Sites')
f('CAMGTCFG_sites.xlsx','Montreal')
f('CAMGTCFG_sites.xlsx','Ontario')
f('CAMGTCFG_sites.xlsx','Quebec')