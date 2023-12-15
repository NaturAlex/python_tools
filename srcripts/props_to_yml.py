import sys
import os
import yaml

'''
    global variable
'''

#restrore day1 key
keys = []
#restore config.yaml
config_dict = {}

keys_file = 'keys.txt'
# if true only transfor config key in keys.txt
findKeys = False

service_name = 'aa'
generate_path = './cn_config/'
source_files = './iam_config/eric-idm-cm-<service name>.config.properties'

default_key = 'defaultValue'
desc_key= 'description'
desc_val = ""
type_key = 'type'
type_val = 'java.lang.String'
default_yaml_prefix = 'metadata'

#restore metadata.yaml not useful
metadata_dict = {}
metadata_dict[default_yaml_prefix] = {}

print("init global variable success")

def list_pros(file_path):
    """
        list properties file in dir
    """
    files = os.listdir(file_path)
    file_list = []
    for file_name in files:
        if file_name.endswith('.properties'): 
            file_list.append(file_name)
    return file_list

def init_dict_data():
    """
       read yml file and get config dict and meadata dict init them to global variable
    """
    init_config_dict = {}
    init_metadata = {}
    global config_dict
    global metadata_dict
    if os.path.exists(config_files) and os.path.exists(metadata_files):
        file = open(config_files,'r',encoding='utf-8')
        init_config_dict = yaml.safe_load(file)
        file.close
        file = open(metadata_files,'r',encoding='utf-8')
        init_metadata = yaml.safe_load(file)
        file.close
        if init_config_dict:
            if len(init_config_dict) > 0:
                config_dict = init_config_dict
                metadata_dict = init_metadata

def generate_meta(k,v):
    """
       generate a pair of metadata of single config  
    """
    meta = {}
    meta[default_key] = v
    meta[desc_key] = desc_val
    meta[type_key] = type_val
    return meta

def readpros(file_path):
    """
       read properties file and get config dict and meadata dict and return them
    """
    print("read files {0}".format(file_path))
    mydict = {}
    mymetadata = {}
    result_dict = {}
    with open(file_path,'r+',encoding='utf-8') as file:
        for line in file:
            line = line.replace("\n","")
            if line.find('#') > -1:
                line = line[0:line.find('#')]
            if len(line) > 0 and '=' in line:
                k = line.split('=')[0].strip()
                v = str(line.split('=')[1].strip())
                mydict[k] = v
                # {'dv':'xx','desc':'yy'}
                meta_dict = generate_meta(k,v)
                #{'k':{'dv':'xx','desc':'yy'}}
                mymetadata[k] = meta_dict
        result_dict['config'] = mydict
        result_dict['metadata'] = mymetadata
        return result_dict


def append_config(mydict,new_file_name):
    """
       put dict as yaml and append to config.yml 
       mydict: {'k','v'}
    """
    if not os.path.exists(generate_path):
        os.mkdir(generate_path)
    stream=open(new_file_name,mode='a',encoding='utf-8')
    yaml.dump(mydict,stream,allow_unicode=True)
    stream.close()

def append_metadata(my_metadata,new_file_name):
    """
       put dict as yaml and append to metadata.yml
       my_metadata: {'k':{'defaultValue':'xx',}}
    """
    before_metadata_dict = {}
    if os.path.exists(new_file_name):
        file = open(new_file_name, 'r+', encoding="utf-8")
        before_metadata_dict = yaml.safe_load(file)
        file.close()
    if not bool(before_metadata_dict):
        before_metadata_dict = {}
        before_metadata_dict[default_yaml_prefix] = {}
    before_metadata_dict[default_yaml_prefix].update(my_metadata)
    stream=open(new_file_name,mode='w+',encoding='utf-8')
    yaml.dump(before_metadata_dict,stream,allow_unicode=True)
    stream.close()

def check_and_push_config(result_dict):
    """
        check key repeat 
        check whether day1 config and return it
        push all config to global variable
    """
    result_config = result_dict['config']
    # {'k':{..}}
    result_metadata = result_dict['metadata']
    need_write_config = {}
    need_write_metadata = {}
    need_write_config.update(result_config)
    need_write_metadata = {}
    need_write_metadata.update(result_metadata)
    global keys;
    # 检查是否重复key
    # key是否属于day1
    # 放到global
    for k in result_config:
        v = result_config[k]
        check_repeat_push_config(k,v)
        if findKeys:
            if k in keys:
                keys.remove(k)
            else:
                del need_write_config[k]
                del need_write_metadata[k]
    push_global_dict(result_config,result_metadata)
    result_config = {}
    result_config['config'] = need_write_config
    result_config['metadata'] = need_write_metadata
    return result_config

def push_global_dict(result_config,result_metadata):
    config_dict.update(result_config)
    metadata_dict[default_yaml_prefix].update(result_metadata)

def check_repeat_push_config(k,v):
    if findKeys:
        if not k in keys:
            return
    if k in config_dict:
        raise Exception("-----------error--------------: repeat key: {}".format(k))
        
def ready_keys(keys_file):
    """
        read pros find day1 keys and restroe them in 'keys'
    """
    global keys
    with open(keys_file,'r+',encoding='utf-8') as file:
        lines = file.readlines()
        for line in lines:
            if line.find('#') > 0:
                line = line[0:line.find('#')]
                # line has colon or equal sign
            split_index = line.find('=')
            colon_index = line.find(':')
            if split_index < 0 and colon_index < 0:
                continue
            if split_index < 0 or (colon_index > 0 and colon_index < split_index):
                split_index = colon_index
            k = line[0:split_index]
            k = k.replace('_','.')
            keys.append(k)

def append_config_from_props(generate_path,source_file):
    if source_file.endswith('.properties'):
        result_dict = readpros(source_file)
        # findKeys & exits keys & check repeat  & push config in global 
        result_dict = check_and_push_config(result_dict)
        if len(result_dict['config']) > 0:
            # append_config
            append_config(result_dict['config'],config_files)
            append_metadata(result_dict['metadata'],metadata_files)

def check_not_found_keys():
    if len(keys) > 0:
        print('-----------warn-------------- not find keys: {0}'.format(keys))

def main(generate_path,source_files):
    init_dict_data()
    # for
    if os.path.exists(source_files):
        if os.path.isdir(source_files):
            for sf in os.listdir(source_files):
                if not source_files.endswith('/'):
                    source_files = source_files+'/'
                source_file = source_files+sf
                append_config_from_props(generate_path,source_file)
            check_not_found_keys()
        else:
            append_config_from_props(generate_path,source_files)
    else:
        help()
        raise Exception("-----------error--------------: error source file,can't can't find properties file on {}".format(source_files))

def help():
    helpmsg = """
    -------------------------------help---------------------------
        funcation:
            generate some yml files from properties file
            or
            transfer properties to yml and append it to config.xml and metadata.yml
            yml files will be generate on <dist_dir>/eric-idm-ca-<service_name>.config.yml',<dist_dir>/eric-idm-ca-<service_name>.metadata.yml'

        usage:
            props_to_yml.py <service-name> <source_file> <dist_dir> <keys_file> \n
            <service-name> (required): such as, aa \n
            <source_files> (option)  : dir or file, default: './iam_config/eric-idm-cm-<service name>.config.properties' if is dir will find all properties files on this dir and file must be properties file and only transfor it. \n
            <dist_dir>     (option)  : is dir,default: './cn_config/' generate config.yml and metadata.yml ' s directory. \n
            <keys_file>    (option)  : is file,default './keys.txt', if source_file is dir,this files must be exists.will filter keys from it as day1 key and only these key will be transfor. \n

        example:
            gernerate init some yml files from properties file:
              python props_to_yml.py aa ./iam_config/
              python props_to_yml.py aa ./iam_config/ ./iam_config/ ./cn_config/ ./iam_config/keys.txt
            transfer one properties file and append yml file:
              python props_to_ym.py aa
              python props_to_ym.py aa ./iam_config/eric-idm-cm-aa.config.properties
              python props_to_ym.py aa ./iam_config/eric-idm-cm-aa.config.properties ./iam_config/eric-idm-cm-<service-name>.config.properties
    -------------------------------help---------------------------
    """
    print(helpmsg)

def init_param(svc, config_path):
    global service_name
    service_name = svc
    global source_files
    source_files = config_path
    global config_files
    config_files = generate_path + 'eric-idm-ca-'+service_name+'.config.yml'
    global metadata_files
    metadata_files = generate_path + 'eric-idm-ca-'+service_name+'.metadata.yml'


if __name__ == '__main__':
    if len(sys.argv) < 2:
       help()
       raise Exception("-----------error--------------: service name is required")
    service_name = sys.argv[1]
    source_files = source_files.replace("<service name>",service_name)
    if len(sys.argv) > 2 :
        source_files = sys.argv[2].strip()
    if len(sys.argv) > 3 :
        generate_path = sys.argv[3].strip() 
        if os.path.isfile(generate_path):
            help()
            raise Exception("-----------error--------------: yaml genernate path must be diretory") 
    if len(sys.argv) > 4 :
        keys_file = sys.argv[4].strip()
        if not os.path.exists(keys_file):
            raise Exception("-----------error--------------: keys file:{} not exists, yaml genernate,keys file is required".format(keys_file)) 
    if os.path.isdir(source_files):
        if not os.path.exists(keys_file):
            help()
            raise Exception("-----------error--------------: keys file:{} not exists, yaml genernate,keys file is required".format(keys_file)) 
        else:
            findKeys = True
            ready_keys(keys_file)
    if not os.path.exists(generate_path):
            os.makedirs(generate_path)
    config_files = generate_path + 'eric-idm-ca-'+service_name+'.config.yml'
    metadata_files = generate_path + 'eric-idm-ca-'+service_name+'.metadata.yml'
    main(generate_path,source_files)




