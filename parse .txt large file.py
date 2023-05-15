#import
class FileParser():
    """parse large text files into smaller files"""
    def __init__(self,file_path_name,number_of_splits):
        self.file_path_name=file_path_name
        self.number_of_splits = number_of_splits


    def Initial_file_open(self):
        fo=open(self.file_path_name,'r')
        content=fo.read().splitlines()
        self.number_of_lines=len(content)
        self.content=content
        print(content)
        return content
        #
    def Create_new_smaller_files(self):

        chunks = [self.content[x:x + int(self.number_of_lines/self.number_of_splits)] for x in range(0, len(self.content), int(self.number_of_lines/self.number_of_splits))]
        for item in range(0,len(chunks)):
            fo1=open('Output'+str(item)+'.txt','w')
            for item1 in chunks[item]:
                fo1.write(item1+'\n')


Object1=FileParser('rollout_northeast_20220209.txt',4)
Object1.Initial_file_open()
print(Object1.number_of_lines)
Object1.Create_new_smaller_files()