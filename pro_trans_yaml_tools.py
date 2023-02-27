import os
import yaml

keys_file = 'keys.txt'
service_name = 'aa'
generate_path = 'result_file'
config_files = generate_path + '/eric-idm-ca-'+service_name+'.config.yml'
metadata_files = generate_path + '/eric-idm-ca-'+service_name+'.metadata.yml'
file_path = 'before_file'
newconfig_files = 'new_config_files/config.properties'

keys = []
dict = {}

default_key = 'defaultValue'
desc_key= 'description'
desc_val = ""
type_key = 'type'
type_val = 'java.lang.String'
default_yaml_prefix = 'metadata'

metadata_dict = {default_yaml_prefix:[]}

def ready_keys(keys_file):
    """
        read pros find day1 keys and restroe them in 'keys'
    """
    with open(keys_file,'r+',encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.find('#') > -1:
                line = line[0:line.find('#')]
            if len(line) > 0:
                #必须先判断=号,因为存在xx=http://xxx
                if line.find('=') > 0:
                    k = line.split('=')[0].strip()
                    k = k.replace('_','.')
                    keys.append(k)
                elif line.find(':') > 0: 
                    k = line.split(':')[0].strip()
                    k = k.replace('_','.')
                    keys.append(k)

def generate_meta(k,v):
    """
       generate a pair of metadata of single config  
    """
    meta = {}
    meta[default_key] = v
    meta[desc_key] = desc_val
    meta[type_key] = type_val
    key_meta = {}
    key_meta[k] = meta
    return key_meta
   


def readpro(file_path):
    """
       read properties file and get config dict and meadata dict and put them in global 
    """
    print("read files {0}".format(file_path))
   
    with open(file_path,'r+',encoding='utf-8') as file:
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
                    if k in keys:
                        keys.remove(k)
                        dict[k] = v
                        key_meta_dict = generate_meta(k,v)
                        metadata_dict[default_yaml_prefix].append(key_meta_dict)

def get_dict_from_readpros(file_path):
    """
       read properties file and get config dict and meadata dict and return them
    """

    print("read files {0}".format(file_path))
    mydict = {}
    mymetadata = []
    result_dict = {}
    with open(file_path,'r+',encoding='utf-8') as file:
        for line in file:
            line = line.replace("\n","")
            if line.find('#') > -1:
                line = line[0:line.find('#')]
            if len(line) > 0 and '=' in line:
                k = line.split('=')[0].strip()
                v = line.split('=')[1].strip()
                mydict[k] = v
                keyMetaDict = generate_meta(k,v)
                mymetadata.append(keyMetaDict)
        result_dict['config'] = mydict
        result_dict['metadata'] = mymetadata
        return result_dict


# {'metadata':['k':{'defaultValue':'',...}]}
def write_yml_fromdict(mydict,new_file_name): 
    """
       put dict as yaml and write to config.yml or metadata.yml
    """
    stream=open(new_file_name,mode='w',encoding='utf-8')
    yaml.dump(mydict,stream,allow_unicode=True)
    stream.close()

def check_repeat_keys(mydict,new_file_name):
    """
        check mydict exists file keys
    """
    file = open(new_file_name, 'r', encoding="utf-8")
    old_metadata_dict = yaml.safe_load(file)
    for key in mydict:
        if key in old_metadata_dict:
            raise Exception("-----------error--------------: repeat key: {}".format(key))
    file.close()
    
    


def append_config(mydict,new_file_name): 
    """
       put dict as yaml and append to config.yml 
    """
    print("-----------debug-------------- check repeat pass")
    stream=open(new_file_name,mode='a',encoding='utf-8')
    yaml.dump(mydict,stream,allow_unicode=True)
    stream.close()

def append_metadata(myMetadata,new_file_name): 
    """
       put dict as yaml and append to metadata.yml
    """
    file = open(new_file_name, 'r+', encoding="utf-8")
    new_metadata_dict = yaml.safe_load(file)
    file.close()
    new_metadata_dict[default_yaml_prefix].extend(myMetadata)
    stream=open(new_file_name,mode='w+',encoding='utf-8')
    yaml.dump(new_metadata_dict,stream,allow_unicode=True)
    stream.close()

ready_keys(file_path+'/'+keys_file)
files = os.listdir(file_path)
for file_name in files:
    if file_name.endswith('.properties'): 
        readpro(file_path + '/' + file_name)
print('-----------warn-------------- not find keys: {0}'.format(keys))
write_yml_fromdict(dict,config_files)
write_yml_fromdict(metadata_dict,metadata_files)

result_dict = get_dict_from_readpros(newconfig_files)
append_config(result_dict['config'],config_files)
append_metadata(result_dict['metadata'],metadata_files)
                



