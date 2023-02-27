
def readPro(file_path):
    """
        0.读取文件
        1.相关处理 ,注释,换行
        2.分割字符串
        3.放到dict
    """
    dict = {}
    file = open(file_path,'Ur')
    for line in file:
        line = line.replace("\n","")
        if line.find('#') > -1:
            line = line[0:line.find('#')]
        if len(line) > 0 and '=' in line:
            k = line.split('=')[0].strip()
            v = line.split('=')[1].strip()
            if k in dict:
                print('repeat key'+k)
            else:
                dict[k] = v
    
    print(dict)

if __name__ == '__main__':
    file_path = 'before_file/1.properties'
    readPro(file_path)
    

            



