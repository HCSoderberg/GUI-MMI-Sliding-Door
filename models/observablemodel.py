class ObservableModel:
    event_listeners = {}
    def __init__(self):
        print("Observable Model initiated")

    def add_event_listener(self, event, fn):
        self.event_listeners[event]=fn
        return lambda: self.event_listeners.pop(event)

    def trigger_event(self, event):
        if event not in self.event_listeners.keys():
            print("event_listener not working")
            return
        self.event_listeners[event]()
    