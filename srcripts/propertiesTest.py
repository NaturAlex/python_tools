#读取properties内容
class Properties:
    filename = ''
    def __init__(self,filename):
        self.filename = filename
        self.props = {}
    def getPros(self):
        # U 为换行模式, 会有warning
        file = open(self.filename,'Ur')
        for line in file:
            # 期望读取内容转成  {'a':['b','c']}
            # print(line)
            # 处理行 注释,换行符处理
            line=line.replace('\n','')
            if line.find('#')>0:
                line = line[0:line.find('#')]
                line = line.replace(" ","")
                key=line[0:line.find('=')]
                print('key='+key)
                val = []
                val.append(line[line.find('=')+1])
                print ("val = %s" %(val))
                self.props[key] = val
        file.close()
        return self.props

    #a.b=c -> {'a': {'b':'c'}}  a.c.d -> {'a': {'c':'d'}}  --> {'a':[ {'b':'c'},{'c':'d'}]}
    #a.b.c=e -> {'a': [ {'b':'c'},{'c':'d'},]}
    def appendKey(self,key,val):
        if key.find('.') == -1:
            return
        arr = key.split('.')
        i = 0
        while i <= len(arr):
            currentKey = arr[i]
            existVal = self.getPros[currentKey]
            if existVal:
                if i == (len(arr)-1):
                    print("error,重复配置")
                elif:

                    appendKey()
            elif:
              if i == (len(arr-1)):
                  self[key[i]]=val
              elif:
                  newMap = {}
                  currentKeyArr = []
                  currentKeyArr[0] = key[i+1]
                  self[key[i]] = currentKeyArr
            i++
        return 0
        #判断key有无.
        #判断key是否存在
        #查前缀是否存在

def main():
    props=Properties('1.properties').getPros()
    print(props)

if __name__ == "__main__":
    main()
    