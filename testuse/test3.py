import sys
import jsonpath
import os
import logging
import json

''' 
python test3.py
'''

def json_to_dict(file_path):
    if not os.path.isfile(file_path):
        logging.error(f"file {file_path} does not exist or have no permission to access.")
        sys.exit(1)

    with open(file_path) as d:
        dictData = json.load(d)
        return dictData
    
    
def swithVersion(versionstr):
    symbol = "."
    firstIndex = versionstr.find(symbol)
    if firstIndex == -1:
        return -1
    versionPre = versionstr[0:firstIndex+1]
    versionSubfix = versionstr[firstIndex+1:].replace(symbol, "")
    versionNumber = float(versionPre+versionSubfix)
    return versionNumber


if __name__ == '__main__':
    pdu_services = ["Federation-TMO-Traffic", "iam-service-default", "DP-ProfileService-TMO-Traffic" ,"DP-TMO-AA-Traffic" ,"IAM-AA-Adapter"]
    data_dict = json_to_dict("./test_config/consul-kv-export-POL-comp.json")
    version_dict = {}
    for svc in pdu_services:
        baseVersion = "1.0"
        version_dict[svc] = baseVersion
    for data in data_dict:
        split_str = data['key'].split("/")
        if len(split_str) > 6 and split_str[3] in pdu_services and split_str[5] == 'config' and split_str[6] != '.metadata':
            svc = split_str[3]
            version = split_str[4]
            version_split_arr = version.split(".")
            if svc != "iam-service-default" and len(version_split_arr) == 3:
                #is old version, 23.1.0
                continue
            versionNumber = swithVersion(version)
            if versionNumber == -1:
                continue
            currentVersion = version_dict[svc]
            if swithVersion(currentVersion) < versionNumber:
                version_dict[svc] = version
    print("service_version_mapping_on_vm: %s" % version_dict)

            



