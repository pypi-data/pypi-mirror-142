from typing import Callable, Tuple, Any
import numpy as np

class Data:
    def __init__(self,t:list) -> None:
        self.t = np.array(t)

    def __str__(self) -> str:
        return self.t.__str__()

    def value(self) -> np.array:
        return self.t

    def getArray(self, func:Callable[[np.array],Any]) -> list:
        return np.array(list(map(func,self.t)))

    def getSet(self, func:Callable[[np.array],Any]) -> set:
        l = set()
        for line in self.t:
            l.add(func(line))
        return l

    def toCsv(self, path:str) -> None:
        np.savetxt(path, self.t, delimiter=",", fmt='%s')

    def row(self, row:int) -> np.array:
        return self.t[row]

    def col(self, col:int) -> np.array:
        return self.t[:,col]

    def head(self, row:int):
        return Data(self.t[:row])
    
    def tail(self, row:int):
        return Data(self.t[-row:])