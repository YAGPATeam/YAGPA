'''
Created on 15 juin 2016

@author: kicyfroth
'''
class game:
    def __init__(self, name):
        self.name = name
    
class player:
    def __init__(self, name):
        self.name = name
    
class system:    
    def __init__(self, name):
        self.name = name
        
class mac_mahon(metaclass=system):
    def __init__(self, name):
        self.name = name
            
class swiss(metaclass=system):
    def __init__(self, name):
        self.name = name
         
class Tounament:    
    def __init__(self, name):
        self.name = name
    