import os

# def test(): 
str = '#123'
index = str.find('#')
print(index)
if index > -1:
    str = str[0:index]
    print(str)
str = 'a.b = c.d'
list=str.split('=')
k = list[0].strip()
v = list[1].strip()
print(k)
print(v)
dict = {}
dict[k] = v
print(dict)
k1=k
# k1 = 'a.a'
exist = k1 in dict
if exist:
    print('exists')
else:
    print('not exists')
print('123'+str)

file_path = './iam_config/'
all_files = os.listdir(file_path)
for file_name in all_files:
    if file_name.endswith('.properties'): 
        print(file_name)

dict = {'metadata':[{'iam.aa.passwordHistoryCheck': {'defaultValue': 'true', 'description': '""', "type": 'java.lang.String'}}]}
dict.update
print(dict)

mydict = {}
mydict.update(dict)
dict['metadata'] = '1'
print(mydict)
dict2 = {'ab':'cd'}
mydict.update(dict2)
print(mydict)
list = ['a','b']
list2 = ['c','d']
list.extend(list2)
exists = 'ab' in dict2
print(exists)
print(len(mydict))
str = ''
if str:
    print('blank str true')
else:
    print('blank str false')

file_path = './before_file'
if os.path.exists(file_path):
    print('{} is exist'.format(file_path))
else:
    print('{} is not exist'.format(file_path))

if os.path.isdir(file_path):
    print('{} is dir'.format(file_path))
else:
    print('{} is file'.format(file_path))

path = './iam_config/'
list_file = os.listdir(path)
print(type(list_file))
dict = {}

str='111.txt'
open(str,'w+')

keys=[]
line = 'iam_env_sdg_sms_url: "https://sms.sdg.msg.t-mobile.com/oneapi/sms/1/outbound/<senderAddress>/requests/"'
if line.find('=') > 0:
    k = line.split('=')[0].strip()
    k = k.replace('_','.')
    keys.append(k)
elif line.find(':') > 0: 
    k = line.split(':')[0].strip()
    print("k = {}".format(k))
    k = k.replace('_','.')
    keys.append(k)
print(keys)
# def main():
#     test()

# if __name__ == "__main__":
#     main()
abc = '123'
if not abc.endswith('/'):
    abc = abc+'/'
print(abc)

