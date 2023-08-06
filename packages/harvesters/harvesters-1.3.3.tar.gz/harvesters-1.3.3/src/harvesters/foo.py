from .simple import Notepad


notepad = Notepad()
notepad.add('path/to/foo')
notepad.add('path/to/bar')
notepad.update()
entry = notepad.entries[0]
harvester = notepad.create(entry)
harvester.run()
buffer = harvester.fetch()
buffer.queue()
harvester.stop()

