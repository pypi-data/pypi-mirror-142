from maxoptics.utils.base import error_print


class BaseSearchContainer:
    @property
    def names(self):
        return list(map(lambda _: _["name"], list(self.all())))

    @property
    def ids(self):
        return list(map(lambda _: _["id"], list(self.all())))

    def _get_index(self, keyval: str):
        names = list(map(lambda _: _["name"], list(self.all())))

        def __get_index(_names, _keyval):
            for i, v in enumerate(_names):
                if _keyval == v:
                    yield i

        indexes = list(__get_index(_names=names, _keyval=keyval))
        if len(indexes) == 0:
            # Not Found
            print(f"The {keyval} is not found, please select from one of these:")
            for name in names:
                print("\t", name)
            raise KeyError
        elif len(indexes) == 1:
            return indexes[0]
        else:
            num = len(indexes)
            error_print(f"You got {num} material with same name {keyval}")
            while True:
                answer = input("Delete all of them?(y/n):\n").strip()
                if answer in ["y", "Y"]:
                    deleter = self.deleter()
                    for ind in indexes:
                        deleter(self.all()[ind]["id"])
                    print("\nDeleted. Please rerun.")
                    break
                elif answer in ["n", "N"]:
                    print("\nCanceled. Please check materials before rerun.")
                    break
                else:
                    print("\nPlease input 'y' or 'n'.")
            exit(1)
