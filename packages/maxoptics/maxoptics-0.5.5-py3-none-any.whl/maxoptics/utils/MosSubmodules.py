import weakref

from maxoptics.base.BaseContainer import BaseSearchContainer
from maxoptics.utils.base import error_print


class PublicMaterials(BaseSearchContainer):
    def __init__(self, mos):
        self.mos = mos
        self._cached = []

    def all(self):
        if self._cached:
            return self._cached
        else:
            self._cached = self.mos.post(url="get_public_materials", token=self.mos.token)["result"]["public_materials"]
            return self._cached

    def reload(self):
        self._cached = self.mos.post(url="get_public_materials", token=self.mos.token)["result"]["public_materials"]

    def __getitem__(self, keyval: str):
        return self.all()[self._get_index(keyval=keyval)]

    def __setitem__(self, keyval: str, val):
        raise NotImplementedError("Changing public material is NOT allowed")


class UserMaterials(BaseSearchContainer):
    def __init__(self, mos, project_type):
        self.mos = mos
        self._cached = []
        self.project_type = project_type
        self.deleter = weakref.WeakMethod(mos.delete_material)

    def all(self):
        if self._cached:
            return self._cached
        else:
            self._cached = self.mos.post(url="search_materials", token=self.mos.token, project_type=self.project_type)[
                "result"
            ]["result"]
            return self._cached

    def reload(self):
        self._cached = self.mos.post(url="search_materials", token=self.mos.token, project_type=self.project_type)[
            "result"
        ]["result"]

    def __getitem__(self, keyval: str):
        return self.all()[self._get_index(keyval=keyval)]

    def __setitem__(self, keyval: str, val):
        raise NotImplementedError()


class UserWaveforms(BaseSearchContainer):
    def __init__(self, mos):
        self.mos = mos
        self._cached = []
        self.deleter = weakref.WeakMethod(mos.delete_waveform)

    def all(self):
        if self._cached:
            return self._cached
        else:
            self._cached = self.mos.post(url="search_waveforms", token=self.mos.token)["result"]["result"]
            return self._cached

    def reload(self):
        self._cached = self.mos.post(url="search_waveforms", token=self.mos.token)["result"]["result"]

    def __getitem__(self, keyval: str):
        return self.all()[self._get_index(keyval=keyval)]

    def __setitem__(self, keyval: str, val):
        raise NotImplementedError()
