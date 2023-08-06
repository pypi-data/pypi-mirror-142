from abc import abstractmethod, ABC

import matplotlib.pyplot as plt

from maxoptics.models import MosProject
from maxoptics.plot.PolygonLike import compromised_transform


class Device(ABC):
    """_summary_
        @params:
        xy: Device coordinates of the center point
    Args:
        meteaclass (_type_, optional): _description_. Defaults to ABCMeta.
    """

    def __init__(self, xy=(0, 0)) -> None:
        self._xy = xy
        self._height = 0.22

    def __str__(self) -> str:
        return str(self.__dict__)

    def visuilize(self, project: MosProject, xysize=(10, 10)):
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.set_xlim((-xysize[0], xysize[0]))
        ax.set_ylim((-xysize[1], xysize[1]))

        for _ in project.__dict__["polygons"]:
            item = compromised_transform(_)
            ax.add_patch(item.__plot__())
        plt.show()

    @abstractmethod
    def build(self):
        pass
