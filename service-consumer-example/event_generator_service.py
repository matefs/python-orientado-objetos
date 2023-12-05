
class EventManager: 
    def __init__(self):
        self.listenners = {}

    def register_event(self,event):
        if event not in self.listenners:
            self.listenners[event] = '';
    

event_manager = EventManager()
event_manager.register_event('primeiro evento')

print(event_manager.listenners)

