import pickle
from dataclasses import dataclass


#from fem_base import FEM_BASE
from test_fem.fem.read import READ
from test_fem.fem.func.func_template import FUNC_TEMPLATE

@dataclass(frozen=False)
class FEM(READ,FUNC_TEMPLATE):


    def save_obj(self,name:str)->None:
        with open(f'{name}', 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)
    
def load_obj(name)->FEM:   
    with open(f'{name}', 'rb') as f:
        return pickle.load(f) 

