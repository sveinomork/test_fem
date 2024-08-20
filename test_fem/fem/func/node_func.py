from test_fem.fem.fem_base import FEM_BASE
from typing import Self
from test_fem.fem.func.func_template import FUNC_TEMPLATE
from test_fem.fem.cards.gcoord import GCOORD
from shapely.geometry import Point
from shapely.geometry.polygon import Polygon
from vectormath import Vector3
import numpy as np
import math

import logging
logger = logging.getLogger(__name__)



   

class NODE_FUNC(FEM_BASE,FUNC_TEMPLATE):

   def get_node_coordinates(self,node:int)->tuple[float,float,float]:
      return (self.gcoord[node].xcoord,self.gcoord[node].ycoord,self.gcoord[node].zcoord)
      
      


   def translate_nodes(self,trans_vector:Vector3)->None:
      for key,val in self.gcoord.items():
         self.gcoord[key]=GCOORD(val.xcoord+trans_vector.x,val.ycoord+trans_vector.y,val.zcoord+trans_vector.z)

  



      
     
   