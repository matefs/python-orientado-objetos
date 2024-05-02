import time
import random

class EventManager:
    def __init__(self):
        self.listeners = {}

    def register_event(self, event):
        if event not in self.listeners:
            self.listeners[event] = []

    def register_listener(self, event, listener):
        if event in self.listeners:
            self.listeners[event].append(listener)
        else:
            print(f"O evento '{event}' não está registrado. Registre o evento antes de adicionar ouvintes.")

    def unregister_listener(self, event, listener):
        if event in self.listeners:
            if listener in self.listeners[event]:
                self.listeners[event].remove(listener)
            else:
                print(f"O ouvinte '{listener}' não está registrado para o evento '{event}'.")
        else:
            print(f"O evento '{event}' não está registrado.")

    def emit_event(self, event, data=None):
        if event in self.listeners:
            for listener in self.listeners[event]:
                listener(data)
        else:
            print(f"O evento '{event}' não está registrado. Registre o evento antes de emitir.")

class EventGenerator:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def generate_event(self):
        event_data = {"value": random.randint(1, 100)}
        self.event_manager.emit_event("evento_gerado", event_data)
        print(f"Evento gerado: {event_data}")
        time.sleep(2)

class EventConsumer:
    def __init__(self, event_manager):
        self.event_manager = event_manager

    def process_event(self, data):
        print(f"Evento recebido: {data['value']}")
        # Implemente o processamento do evento conforme necessário

# Exemplo de uso
if __name__ == "__main__":
    event_manager = EventManager()
    event_generator = EventGenerator(event_manager)
    event_consumer = EventConsumer(event_manager)

    event_manager.register_event("evento_gerado")
    event_manager.register_listener("evento_gerado", event_consumer.process_event)

    # Simula a execução contínua do gerador de eventos
    while True:
        event_generator.generate_event()
