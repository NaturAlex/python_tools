import yaml
import os

dict = {}

def readPro(file_path):
    """
        0.读取文件
        1.相关处理 ,注释,换行
        2.分割字符串
        3.放到dict
    """
    # file = open(file_path,'Ur')
    with open(file_path,'r+', encoding = "utf-8") as file: 
        lines = file.readlines()
        file.seek(0)
        for line in lines:
            line = line.replace("\n","")
            if line.find('#') > -1:
                line = line[0:line.find('#')]
            if len(line) > 0 and '=' in line:
                k = line.split('=')[0].strip()
                v = line.split('=')[1].strip()
                if k in dict:
                    print('exist repeat key = '+k)
                    raise Exception('exist repeat key: {0} in file: {1}'.format(k,file_path))
                else:
                    dict[k] = v
    

def writeYml(mydict): 
    for k in mydict:
        v = mydict[k]
    stream=open('result_file/generate.yaml',mode='w',encoding='utf-8')
    yaml.dump(mydict,stream,allow_unicode=True)
    stream.close()

file_path = 'before_file'
all_files = os.listdir(file_path)
for file_name in all_files:
    if file_name.endswith('.properties'): 
        print('tranfor properties file :' + file_name)
        readPro(file_path+'/'+file_name)
        writeYml(dict)