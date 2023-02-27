import yaml
import os
import requests
import urllib3
import re
import sys

chart_address = "https://pdg.ei.seli.gic.ericsson.se/yum_repo/tmo/NSI_IAM_TMO_PROMOTED/cloud-native/charts/"
images_address = "https://pdg.ei.seli.gic.ericsson.se/yum_repo/tmo/NSI_IAM_TMO_PROMOTED/cloud-native/images/"

download_chart_path=sys.argv[1]
download_image_path=sys.argv[2]
deploy_config_file=sys.argv[3]

urllib3.disable_warnings()

def download(url,filename,download_path):
    r = requests.get(url,stream=True,verify=False)
    if r.status_code == 200:
        with open(download_path+filename, 'b+w') as f:
            for chunk  in r.iter_content(chunk_size=1024):
                f.write(chunk)

# 读取yml文件内容 ,拿到service列表
file=open(deploy_config_file,'r',encoding='utf-8')
dict=yaml.safe_load(file)
for svc in dict:
    attr_dic=dict[svc]
    enable = attr_dic['enabled']
    if enable:
        version2 = attr_dic['chart'][svc]
        chart_name = svc+'-'+version2
        print(chart_name)
        download(chart_address+chart_name+".tgz",chart_name+".tgz",download_chart_path)
#下载chart文件



#下载image文件

r = requests.get(images_address,verify=False)
content = r.text

for line in content.split('\n'):
    if 'href' in line:
        pattern='<a href="(.*)"'
        ret = re.findall(pattern,line)
        fileuri = ret[0]
        #not directory
        if not fileuri[len(fileuri)-1] == '/' :
            print(fileuri)
            index = fileuri.rfind("/")
            filename = fileuri[index+1:]
            print(filename)
            download(images_address+filename,filename,download_image_path)





