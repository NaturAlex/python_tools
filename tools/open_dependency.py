import os
import re

File_PATH = 'conf\dependency.txt'
""" 
python tools/open_dependency.py
"""


    
def main():
    with open(File_PATH,'r',encoding='utf-8') as f:
        data = f.readlines()
        str = 'C:/repository'
        for line in data:
            line = line.replace('\n','')
            line = line.replace(' ','')
            if 'version' in line:
                line = re.sub('<\w*>','',line)
                line = re.sub('</\w*>','',line)
                str += line
                break
            else:
                line = re.sub('<\w*>','',line)
                line = re.sub('</\w*>','',line)
                line = line.replace('.','/')
                str += line+'/'
            # print('line:{}'.format(line))
        print('str:{}'.format(str))
        os.system('start '+str)

if __name__ == '__main__':
    main()
    