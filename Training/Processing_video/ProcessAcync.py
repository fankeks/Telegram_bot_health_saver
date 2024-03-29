import asyncio
import multiprocessing as mp


from Training.Processing_video.ControlPoints import ControlPointsCPU


class ProcessAsync:
    @staticmethod
    def f(path):
        c = ControlPointsCPU(path)
        c.get_report()

    def __init__(self, path):
        self.__p = mp.Process(target=self.f, args=(path,))

    async def start(self):
        self.__p.start()

    async def join(self):
        while self.__p.is_alive():
            await asyncio.sleep(0)