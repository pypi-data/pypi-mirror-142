"""
Automatically Checks for updates every 5 minutes and reboots the bot if there is a new version.

`bot.load_extension('dis_taipan.updater')`

"""
import asyncio
import subprocess
import sys
from dis_snek import Snake, listen, Scale

from dis_snek.models.snek.tasks import Task, triggers


class Updater(Scale):
    def __init__(self, bot: Snake) -> None:
        self.bot = bot
        self.commit_id = (
            subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
        )
        self.branch = (
            subprocess.check_output(["git", "rev-parse", "--abbrev-ref", "HEAD"])
            .strip()
            .decode()
        )
        try:
            upstream = (
                subprocess.check_output(["git", "rev-parse", f"origin/{self.branch}"])
                .decode()
                .strip()
            )
            if upstream == self.commit_id:
                print(f"Currently running {self.commit_id} on {self.branch}")

        except subprocess.CalledProcessError as e:
            print(e)
            pass

    @listen()
    async def on_startup(self):
        try:
            self.update.start()
        except Exception as e:
            print(e)

    @Task.create(triggers.IntervalTrigger(minutes=5))
    async def update(self) -> None:
        loop = asyncio.get_running_loop()
        reboot = loop.run_in_executor(None, self.check_for_update)
        if reboot.result():
            await self.bot.stop()

    def check_for_update(self) -> bool:
        try:
            subprocess.check_output(["git", "fetch"]).decode()
        except subprocess.CalledProcessError:
            return
        commit_id = (
            subprocess.check_output(["git", "rev-parse", f"origin/{self.branch}"])
            .decode()
            .strip()
        )
        if commit_id != self.commit_id:
            print(f"origin/{self.branch} at {commit_id}")
            print("Update found, shutting down")
            subprocess.check_output(["git", "pull"]).decode()
            try:
                subprocess.check_output(["pipenv", "sync"]).decode()
            except Exception as c:
                print(c)
            return True
        return False


def setup(bot: Snake) -> None:
    Updater(bot)
