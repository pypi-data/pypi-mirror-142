from os import PathLike
from allocation_language.alloc_lang_data_containers.event_dataclasses import EventData
import allocation_language.lexer as lexer_module
from allocation_language.parser import parser
import random

def _make_contract(text_content: str):
    lexer = lexer_module.make_new_lexer()
    token_stream = lexer.lex(text_content)
    
    contract = parser.parse(token_stream)
    return contract
    
def make_contract_from_file(file_src: PathLike):
    with open(file_src, "r") as src_file:
        return _make_contract(src_file.read())

def make_contract_from_text(text_content: str):
    return _make_contract(text_content)

def make_test_events(n=10):
    for _ in range(n):
        yield EventData(
            data = {
                "type": random.choice(['A', 'B', 'C']),
                "claim": random.randint(1, 5e5),
                "liable": 0,
                "revenue": random.randint(1, 5e5)
            }
        )


""" Testing code, not part of library. """
def _test_contract():
    contract = make_contract_from_file("./src/allocation_language/test_files/test1.txt")
    contract.update("testvar", 1e5)
    events = list(make_test_events(50000))
    events = contract.evaluate_stream(events)
    for event in events:
        print(event)
        
def __main():
    import cProfile
    import pstats

    with cProfile.Profile() as pr:
        _test_contract()

    stats = pstats.Stats(pr)
    stats.sort_stats(pstats.SortKey.TIME)
    # stats.print_stats()
    stats.dump_stats('profiling_test_stats.prof')

if __name__ == "__main__":
    __main()