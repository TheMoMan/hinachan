import json
import os
from app.services import textService, dateTimeService
from discord.ext import tasks, commands

class LoopHandler():
    def __init__(self, client: commands.Bot):
        self.textService = textService.TextService()
        self.dateTimeService = dateTimeService.DateTimeService()
        self.client = client

    @tasks.loop(hours=1)
    async def steamMaintenanceLoop(self):
        if not self.dateTimeService.steamMaintenanceImminent():
            return

        message = self.textService.getSteamMaintenanceAlert()

        for channelId in json.loads(os.environ['STEAM_MAINTENANCE_CHANNELS']):
            channel = self.client.get_channel(channelId)

            try:
                await channel.send(message)

            except:
                print('Unknown channel id {}'.format(str(channelId)))
                continue

    def startLoops(self):
        print('Initialising loops')
        self.steamMaintenanceLoop.start()
