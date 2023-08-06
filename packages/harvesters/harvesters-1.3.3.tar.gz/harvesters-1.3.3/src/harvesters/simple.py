class Buffer:
    def __init__(self):
        pass

    def queue(self):
        pass


class Harvester:
    def __init__(self, entry):
        self._entry = entry

    def fetch(self):
        return Buffer()

    def run(self):
        pass

    def stop(self):
        pass


class Notepad:
    def __init__(self):
        self._entries = []

    def add(self, path: str):
        self._entries.append(path)

    def update(self):
        pass

    @property
    def entries(self):
        return self._entries

    def create(self, entry) -> Harvester:
        return Harvester(entry)