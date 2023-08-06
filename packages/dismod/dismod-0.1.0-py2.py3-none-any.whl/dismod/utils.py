import fnmatch
import os
from typing import Any
from typing import Generator
from typing import List
from typing import Tuple


def collect_files_in_module(filepath: str) -> List[str]:
    """ """
    matches = []
    for root, _, filenames in os.walk(filepath):
        for filename in fnmatch.filter(filenames, "*.py"):
            matches.append(os.path.join(root, filename))

    return matches


def neighborhood(
    iterable: List[Any],
) -> Generator[Any, Any, Any]:
    """ """
    if not iterable:
        return iterable

    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)


def search_key_in_iterable(
    key: str,
    value: str,
    iterable: List[Any],
) -> Tuple[Any, ...]:
    """ """
    return tuple(
        next(
            (
                (index, thing)
                for index, thing in enumerate(iterable)
                if thing[key] == value
            ),
            (None, None),
        ),
    )
