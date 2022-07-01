import types
import discord
from traitlets import Int

class Handler:
    def __init__(self) -> None:
        pass
    

class Command:
    def __init__(self,func:types.FunctionType,id:Int,**opt) -> None:
        self.__func = func
        self.__id = id
        self.__option = opt
    def _ATTACH_OPTION(self,atach:dict,opt:dict):
        atached = {}
        for atc in atach:
            if atach[atc][0]:
                for o in opt:
                    if atc == o:
                        atached.update(
                            {
                                atach[atc][1]:opt[o]
                            }
                        )
        return atached
    def run(self,atach):
        atach_data = self._ATTACH_OPTION(self.__option,atach)
        self.__func(**atach_data)
    def getId(self):
        return self.__id
    @classmethod
    def recv(cls,msg=(True,"msg")):
        def deco(func):
            return Command(func,1,**{"msg":msg})
        return deco
