from typing import List, Callable
from DataProcX.data import Data

class Parser:
    def __init__(self) -> None:
        self.preprocess:Callable[[str],str] = lambda x: x.strip()
        self.postprocess:Callable[[list],list] = lambda x: x

    def parse(self, lines:List[str], offset:int, delimiter:str=' ') -> Data:
        return Data(list(map(lambda x: self.postprocess(self.preprocess(x).split(delimiter)), lines[offset:])))

    def loadFile(self, path:str, offset:int, delimiter:str) -> Data:
        with open(path) as f:
            return self.parse(f.readlines(), offset, delimiter)

    def loadCsv(self, path:str) -> Data:
        return self.parse(path,0,',')
