import json
from typing import *
from io import BytesIO
from abc import ABC, abstractmethod

class AbstractBaseSerializer(ABC):

    def __init__(self):
        super().__init__()
    
    @abstractmethod
    def loads(self, loadable: Union[str, BytesIO])-> Any:
        pass
    
    @abstractmethod
    def dumps(self, dumpable:Any)-> Union[str, BytesIO]:
        pass

class JSONSerializer(AbstractBaseSerializer):
    def __init__(self):
        pass

    def loads(self, loadable):
        return json.loads(loadable)

    def dumps(self, dumpable):
        return json.dumps(dumpable)