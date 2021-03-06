'''
Created on May 3, 2013

@author: jonathan
'''

from game import get_game


class ComponentManager(object):

    def __init__(self):
        self.components = {}
        
    def register_component(self, name, component):
        self.components[name] = component
        
    def add(self, name, entity):
        self.components[name].add(entity)
        
    def remove(self, name, entity):
        self.components[name].remove(entity)
        
        
class ExampleComponent(object):
    
    def add(self, entity):
        entity.register_handler('update', self.handle_update)
        get_game().register_for_updates(entity)
    
    def remove(self, entity):
        entity.unregister_handler('update', self.handle_update)
    
    def handle_update(self, entity, dt):
        print '%f seconds have elapsed!' % (dt,)