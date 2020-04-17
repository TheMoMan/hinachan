import discord
import os

class MasterService():
    def __init__(self):
        self.userId = int(os.environ['USER_ID'])
        self.ownerId = int(os.environ['OWNER_ID'])

    async def foo(self):
        print('bar')
