import yaml

#读取yaml文件



#写出yaml文件
def writeYaml():
    map={
        'a' : {
          'c' : 'd',
          'e' : 'f'
        }
    }
    map={
        "a": "b",
        "a.b": "c",
        "a.c": "d"
    }
     # mode=a 追加内容 w覆盖
    stream=open('write.yaml',mode='w',encoding='utf-8')
    yaml.dump(map,stream,allow_unicode=True)
    stream.close()
   




#map操作


def main():
    writeYaml()

if __name__ == "__main__":
    main()


