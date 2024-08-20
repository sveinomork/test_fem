from test_fem.fem.cards_import import *
from collections import OrderedDict

from dataclasses import dataclass,field
@dataclass
class FEM_BASE():
    
    cards:list[str]=field(default_factory=list)
   
    gcoord: OrderedDict[int,GCOORD]= field(default_factory=OrderedDict)
    gnode: OrderedDict[int,GNODE] = field(default_factory=OrderedDict)
    
    gelmnt1: OrderedDict[int,GELMNT1] = field(default_factory=OrderedDict)
   

    
   
  
    
   
    


    