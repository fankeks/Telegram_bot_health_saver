from abc import ABC, abstractmethod


class IControlPoints(ABC):
    @abstractmethod
    def __init__(self, path):
        '''
        Инициализатор
        :param path: Путь к файлу с видео
        '''
        pass

    @abstractmethod
    def get_report(self) -> bool:
        '''
        Перезаписывает файл с видео (С указанием контрольных точек)
        :return: True - Если удалось, иначе False
        '''
        pass