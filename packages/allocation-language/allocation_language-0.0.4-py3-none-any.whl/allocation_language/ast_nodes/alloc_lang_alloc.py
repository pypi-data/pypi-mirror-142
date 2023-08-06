from statistics import quantiles
from allocation_language.alloc_lang_data_containers.event_dataclasses import EventData
from allocation_language.ast_nodes.alloc_lang_primitives import Node, Field, Percent

class Alloc(Node):
    def __init__(
        self, source: Field, value_node: Node, target: Field
    ):
        self.source = source
        self.value_node = value_node
        self.target = target

        self.is_percent = isinstance(self.value_node, Percent)

    def get_live_nodes(self, found=None):
        if (found is None):
            found = []
        return found + self.value_node.get_live_nodes()

    def update(self, name: str, value: float):
        self.value_node.update(name, value)
    
    def evaluate(self, event_data: EventData) -> dict:
        if (not event_data.scope_flag):
            return event_data

        source_value = self.source.evaluate(event_data)
        target_value = self.target.evaluate(event_data)
        alloc_value = self.value_node.evaluate(event_data)

        if self.is_percent:
            quantity = alloc_value * source_value
        else:
            quantity = min(source_value, alloc_value)
        
        event_data.data[self.source.name] = source_value - quantity
        event_data.data[self.target.name] = target_value + quantity

        return event_data