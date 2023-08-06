from typing import Iterable, List
from allocation_language.alloc_lang_data_containers.event_dataclasses import EventData
from allocation_language.ast_nodes.alloc_lang_primitives import Node

class Statement(Node):
    def __init__(self, expr: Node):
        self.expr = expr

    def get_live_nodes(self, found: List[str] | None = None):
        if (found is None):
            return self.expr.get_live_nodes()
        else:
            return found + self.expr.get_live_nodes()

    def update(self, name: str, value: float):
        self.expr.update(name, value)

    def evaluate_stream(self, event_stream: Iterable[EventData]) -> Iterable[EventData]:
        yield from self.expr.evaluate_stream(event_stream)

    def evaluate(self, event_data: EventData) -> dict:
        return self.expr.evaluate(event_data)


class Block(Node):
    def __init__(self, statements: Iterable[Statement]):
        self.statements = statements

    def get_live_nodes(self, found: List[str] | None = None) -> List[str]:
        if (found is None):
            found = []

        for statement in self.statements:
            found += statement.get_live_nodes()
        return found

    def update(self, name: str, value: float):
        for statement in self.statements:
            statement.update(name, value)

    def evaluate_stream(self, event_stream: Iterable[EventData]) -> Iterable[EventData]:
        events = list(event_stream)
        for statement in self.statements:
            events = list(statement.evaluate_stream(events))
        yield from events
        
    def evaluate(self, event_data: EventData) -> dict:
        for statement in self.statements:
            # print(event_data)
            event_data = statement.evaluate(event_data)
        return event_data