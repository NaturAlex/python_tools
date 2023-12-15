''' 
python define_clz.py
'''

class DefineClz:
    clz_var_count = 0
    
    def __init__(self, name):
        self.name = name
    
    def instance_method(self):
        print(self.name)
        
    @classmethod
    def clz_method(cls):
        cls.clz_var_count += 1
        print(cls.clz_var_count)
    
    @staticmethod
    def static_method():
        print('static')
        
    def nothing():
        pass

if __name__ == "__main__":
    obj = DefineClz("ddd")
    obj.instance_method()
    DefineClz.clz_method()
    DefineClz.static_method()