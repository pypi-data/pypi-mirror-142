import asyncio
import importlib.metadata
import time
from typing import Dict, Optional, Type, Tuple
from arclet.letoderea import EventSystem
from .context import edoves_instance
from .network import NetworkStatus
from .module import BaseModule
from .config import TemplateConfig
from .server_docker import BaseServerDocker
from .exceptions import DataMissing, ValidationFailed
from .utilles.logger import Logger, replace_traceback
from .utilles.security import check_name
from .monomer import Monomer, MonoMetaComponent
from .scene import EdovesScene

AE_LOGO = "\n".join(
    (
        "             ▦▦                                 ",
        "▦▦▦▦▦       ▦                                 ",
        " ▦  ▦        ▦                                  ",
        " ▦       ▦▦▦▦   ▦▦▦   ▦▦  ▦▦   ▦▦     ▦▦  ",
        " ▦▦▦   ▦    ▦  ▦    ▦   ▦  ▦   ▦   ▦  ▦     ",
        " ▦     ▦     ▦  ▦    ▦   ▦  ▦   ▦▦▦▦   ▦▦  ",
        " ▦  ▦  ▦   ▦▦  ▦    ▦     ▦     ▦          ▦ ",
        "▦▦▦▦▦  ▦▦ ▦▦   ▦▦▦      ▦      ▦▦▦   ▦▦  ",
        ""
    )
)


class Edoves:
    __instance: bool = False
    event_system: EventSystem
    logger: Logger.logger
    __scene_list: Dict[str, EdovesScene] = {}

    def __init__(
            self,
            *,
            configs: Dict[str, Tuple[Type[TemplateConfig], Dict]],
            event_system: Optional[EventSystem] = None,
            is_chat_log: bool = True,
            debug: bool = False
    ):
        if self.__instance:
            return
        self.event_system: EventSystem = event_system or EventSystem()
        self.logger = Logger(level='DEBUG' if debug else 'INFO').logger
        replace_traceback(self.event_system.loop)
        from ..builtin.chatlog import ChatLogModule
        for name, t_config in configs.items():
            try:
                check_name(name)
                cur_scene = EdovesScene(name, self, t_config[0].parse_obj(t_config[1]))
                self.__scene_list.setdefault(
                    name,
                    cur_scene
                )
            except ValidationFailed as e:
                self.logger.error(e)
            except ValueError as e:
                self.logger.critical(f"{e}: {name}")
                exit()
            else:
                if is_chat_log:
                    cur_scene.require_module(ChatLogModule)
        self.__instance = True

    @classmethod
    def current(cls) -> 'Edoves':
        return edoves_instance.get()

    @classmethod
    def get_scene(cls, name: str) -> EdovesScene:
        return cls.__scene_list.get(name)

    async def launch_task(self):
        self.logger.opt(colors=True, raw=True).info("=--------------------------------------------------------=\n")
        self.logger.opt(colors=True, raw=True).info(f"<cyan>{AE_LOGO}</>")
        official = []
        for dist in importlib.metadata.distributions():
            name: str = dist.metadata["Name"]
            version: str = dist.version
            if name.startswith("arclet-"):
                official.append((" ".join(name.split("-")[1:]).title(), version))

        for name, version in official:
            self.logger.opt(colors=True, raw=True).info(
                f"<magenta>{name}</> version: <yellow>{version}</>\n"
            )
        self.logger.opt(colors=True, raw=True).info("=--------------------------------------------------------=\n")
        start_time = time.time()
        self.logger.info("Edoves Application Start...")
        start_task = []
        for name, cur_scene in self.__scene_list.items():
            running_task = self.event_system.loop.create_task(
                cur_scene.start_running(),
                name=f"Edoves_{name}_Start_Task"
            )
            start_task.append(running_task)
        await asyncio.gather(*start_task)
        self.logger.info(f"Edoves Application Started with {time.time() - start_time:.2}s")

    async def daemon_task(self):
        self.logger.info("Edoves Application Running...")
        update_task = []
        for name, cur_scene in self.__scene_list.items():
            running_task = self.event_system.loop.create_task(
                cur_scene.update(),
                name=f"Edoves_{name}_Stop_Task"
            )
            update_task.append(running_task)
        await asyncio.gather(*update_task)
        # await self.quit_task()

    async def quit_task(self):
        self.logger.info("Edoves Application Stop...")
        start_task = []
        for name, cur_scene in self.__scene_list.items():
            running_task = self.event_system.loop.create_task(
                cur_scene.stop_running(),
                name=f"Edoves_{name}_Stop_Task"
            )
            start_task.append(running_task)
        await asyncio.gather(*start_task)
        self.logger.info("Edoves shutdown. Have a nice day!")

    def run(self):
        try:
            self.event_system.loop.run_until_complete(self.start())
        except KeyboardInterrupt:
            self.logger.warning("Interrupt detected, Edoves stopping ...")
            self.event_system.loop.run_until_complete(self.quit_task())

    async def start(self):
        await self.launch_task()
        await self.daemon_task()

    def __getitem__(self, item: str) -> EdovesScene:
        return self.__scene_list.get(item)

    def __getattr__(self, item):
        if item in self.__scene_list:
            return self.__getitem__(item)
        raise ValueError
