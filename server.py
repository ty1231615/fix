from discord.ext import commands
import pickle
import os

guild_folder = "servers"

class Server:
    @classmethod
    def load(cls,id):
        if os.path.exists(id):
            return pickle.loads(open(id,"br").read())
    def __init__(self,id) -> None:
        self.__name = ""
        self.__id = id
    def dump(self):
        pickle.dump(self,open(f"{guild_folder}/{self.__id}","w",encoding="UTF-8"))
    def set_name(self):
        pass