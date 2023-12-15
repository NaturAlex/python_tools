#!/usr/bin/python
'''
Created on Jun 28, 2018

@author: ezhonho

python2 python2/GenerateJ2.py iam_config/eric-idm-ca-idv.config.yml
'''
from optparse import OptionParser
import os
import shutil
import yaml
from string import Template

class FileUtil():
    
    @staticmethod    
    def get_file_list(path):
        file_list = []
        path_list=path.split(';')
        for file_path in path_list:
            if os.path.exists(file_path) and os.path.isfile(file_path):
                file_list.append(file_path)
        return file_list

    @staticmethod
    def is_config_file(file_name):
        if file_name.endswith('.yml'):
            return True
        return False

    @staticmethod
    def is_constraint_file(file_name):
        if file_name.endswith('constraint.yml'):
            return True
        return False

class FileHandler():
    def __init__(self,base_file,customized_file,constraint_file,target_file):
        self.base_file=base_file
        self.customized_file=customized_file
        self.constraint_file=constraint_file
        self.target_file=target_file
        self.default_conf_files = []
        self.customized_conf_files = []
        self.constrained_conf_files = []

 
    def _generate_jijia_config_files(self):
        print "Generating target file to: %s" % (self.target_file)
        print "Default files are : "+ self.base_file
        print "Customized files are : " + self.customized_file
        print "constraint files are : "+ self.constraint_file
        
        for file_path in FileUtil.get_file_list(self.base_file):
            print self.base_file
            if FileUtil.is_config_file(file_path):
                self.default_conf_files.append(file_path)
            
        for file_path in FileUtil.get_file_list(self.customized_file):
            if FileUtil.is_config_file(file_path):
                self.customized_conf_files.append(file_path)
                
        for file_path in FileUtil.get_file_list(self.constraint_file):
            if FileUtil.is_constraint_file(file_path):
                self.constrained_conf_files.append(file_path)

        self._merge_files_to_jijia_file(self.target_file)

        print "\nTarget config files generated in file %s \n\n" % self.target_file
     
    def _cleanup_and_init_file(self,filename):
        if os.path.exists(filename):
            os.remove(filename)
        else:
            dirname=os.path.dirname(filename)
            if not os.path.exists(dirname):
                os.mkdir(dirname)

    
    def _read_config_file(self, file_path):
        with open(file_path, "r") as file_read_default:
            data = yaml.load(file_read_default)
            return data 
                
    def _merge_files_to_jijia_file(self, target_file):       
        data = {}
        constraint_data={}
        for file_path in self.default_conf_files:
            print file_path
            file_data = self._read_config_file(file_path)
            if file_data:
                data.update(file_data)                         
        for file_path in self.customized_conf_files:
            file_data = self._read_config_file(file_path)
            if file_data:
                for key, value in file_data.items():
                    if key not in data:
                        print "  - New customized key: %s = %s" % (key, value)
                    elif value != data[key]:
                        print "  - Updated customized key: %s = from %s to %s" % (key, data[key], value)
                    data[key] = value
                              
        for file_path in self.constrained_conf_files:
            file_data = self._read_config_file(file_path)            
            if file_data:
                for key, value in file_data.items():
                    constraint_data.update(file_data) 
                    print '  constraint_data key: %s = %s' % (key, value)  
                    
        print '  - Generate J2 config file: %s' % target_file
        self._write_data_to_jijia_file(data, constraint_data,target_file)
        
        
    def _write_data_to_jijia_file(self,data, constraint_data,target_file):    
        self._cleanup_and_init_file(target_file)
        jijia_data={}

        for key, value in data.items():
            if key in constraint_data and constraint_data[key]=='mandatory':
                jijia_data[key]="'{{ %s | mandatory }}'" % key.replace(".", "_").replace("-", "")
            if key in constraint_data and constraint_data[key]=='removed':
                print '  - Removed customized key: %s' % key
            elif key in constraint_data and constraint_data[key]=='non_configurable':
                if type(value)==str and "\n" in value: 
                    value_str="|\n"
                    lines=value.splitlines()
                    for line in lines:
                        value_str=value_str+"  "+line
                        if lines.index(line) != len(lines)-1:
                            value_str=value_str+"\n"
                    jijia_data[key]=value_str
                else:
                    if type(value) == str:
                        value = value.replace("'", "\\'")
                    jijia_data[key]="'%s'" % value
            else:
                if type(value)==str and "\n" in value:
                    value = value.replace("\\\\","\\\\\\\\")
                    value = value.replace("'", "\\'")
                    value_str="{{ %s | default('|\n" % key.replace(".", "_").replace("-", "")
                    lines=value.splitlines()
                    for line in lines:
                        value_str=value_str+"  "+line
                        if lines.index(line) != len(lines)-1:
                            value_str=value_str+"\n"  
                    value_str=value_str+"') }}"
                    jijia_data[key]=value_str
                else:
                    if type(value) == str:
                        value = value.replace("\\\\","\\\\\\\\")
                        value = value.replace("'", "\\'")
                    jijia_data[key]="'{{ %s | default('%s') }}'" % (key.replace(".", "_").replace("-", ""),value) 
                  
        with open(target_file, "w") as file_write:
            for key, value in jijia_data.items():
                file_write.write(key+": "+value+"\n")
        file_write.close()
        
        
    
if __name__ == '__main__':
    usage = "usage: %prog [options]" 
    parser = OptionParser(usage=usage)
    parser.add_option('-b', '--base-file',
                               help='Default config files.'
                                    'Mandatory',
                               dest='base_file', default='', action='store')
    parser.add_option('-c', '--customized-file',
                               help='Customized config files.'
                                    'Optional.',
                               dest='customized_file', default='', action='store')
    parser.add_option('-n', '--constraint-file',
                               help='Constraint config files.'
                                    'Optional.',
                               dest='constraint_file', default='', action='store')
    parser.add_option('-t', '--target-file',
                               help='Target config files.'
                                    'Mandatory',
                               dest='target_file', default='', action='store')

    (options, args) = parser.parse_args()
    
    
    if not options.base_file:
        parser.error("options --base-file are required!")      
    if not options.target_file:
        parser.error("options --target-file are required!")

    
    file_handler=FileHandler(options.base_file,options.customized_file,options.constraint_file,options.target_file)
    file_handler._generate_jijia_config_files()
        
        
        
        
    
    


