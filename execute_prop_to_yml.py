import props_to_yml
import os

service_name='aa'
config_path='./iam_config/configuration/'
generate_path='./cn_config/'
keys_file='./keys.txt'
other_keys=[]

new_props_file='./'

if not os.path.exists('keys.txt'):
    raise Exception("keys file not exist!")
props_to_yml.init_param(service_name,config_path)
props_to_yml.findKeys = True
props_to_yml.ready_keys(keys_file)
if len(other_keys) > 0:
    props_to_yml.keys.extend(other_keys)
props_to_yml.main(generate_path,config_path)