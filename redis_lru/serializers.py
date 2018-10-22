import json
from typing import *
from io import BytesIO
from abc import ABC, abstractmethod

class AbstractBaseSerializer(ABC):

    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def redis_loads(self, loadable: Union[str, BytesIO])-> Any:
        pass
    
    @abstractmethod
    def redis_dumps(self, dumpable:Any)-> Union[str, BytesIO]:
        pass

