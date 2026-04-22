import io

class StringIO:
    def __init__(self, initial_value: str | None = "", newline: str | None = "\n"):
        self._sio=io.StringIO(initial_value, newline)

    def getvalue(self):
        pass