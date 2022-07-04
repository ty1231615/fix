import types
import discord

class Command:
    def __init__(self,func:types.FunctionType,id:int,**opt) -> None:
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

class Handler(object):
    INSTANCE = {}
    def __init__(self) -> None:
        self.__id = self.__hash__()
        self.__cmds = []
        Handler.INSTANCE.update(
            {
                self.__id:self
            }
        )
    @classmethod
    def getInstance(cls,id):
        return Handler.INSTANCE.get(id,None)
    def __del__(self):
        Handler.INSTANCE.pop(self.__id)
    def attach(self,cmd:Command):
        self.__cmds.append(cmd)
    def getId(self):
        return self.__id
