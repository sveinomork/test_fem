
from vectormath import Vector3
class FUNC_TEMPLATE:
    def get_node_coordinates(self,node:int)->tuple[float,float,float]:
        ...

    def translate_nodes(self,trans_vector:Vector3)->None:
        ...
    