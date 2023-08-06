from typing import Callable, Dict, Iterable, List, Literal, Optional, Sequence, Set, TypeVar, Union, cast, overload

from ..fmt import Text
from . import inpt, out

T = TypeVar("T")

@overload
def get_bool(text: Union[str, Text], default: bool, inline: Optional[bool] = None) -> bool:
    ...

@overload
def get_bool(text: Union[str, Text], default: Optional[bool] = None, inline: Optional[bool] = None) -> Optional[bool]:
    ...

def get_bool(text: Union[str, Text], default: Optional[bool] = None, inline: Optional[bool] = None) -> Optional[bool]:
    info = "y/n"
    if default is not None:
        info = "Y/n" if default else "y/N"
    out.print_question(Text(text, " [", info, "]"), inline=inline)
    return inpt.select_bool(default)


@overload
def get_str(text: Union[str, Text], verify: Callable[[str], bool], default: str, silent: bool = False, inline: Optional[bool] = None) -> str:
    ...

@overload
def get_str(text: Union[str, Text], verify: Callable[[str], bool] = lambda text: True, default: Optional[str] = None, silent: bool = False, inline: Optional[bool] = None) -> Optional[str]:
    ...

def get_str(text: Union[str, Text], verify: Callable[[str], bool] = lambda text: True, default: Optional[str] = None, silent: bool = False, inline: Optional[bool] = None) -> Optional[str]:
    def_text: Union[str, Text] = ""
    if default is not None:
        def_text = Text(" [", default, "]")
    out.print_question(Text(text, def_text), inline=inline)
    return inpt.select_str(verify, default, silent)


@overload
def get(text: Union[str, Text], convert: Callable[[str], T], default: T, default_str: Optional[Union[str, Text]] = None, allow_empty: bool = False, silent: bool = False, inline: Optional[bool] = None) -> T:
    ...

@overload
def get(text: Union[str, Text], convert: Callable[[str], T], default: Optional[T] = None, default_str: Optional[Union[str, Text]] = None, allow_empty: Literal[False] = False, silent: bool = False, inline: Optional[bool] = None) -> T:
    ...

@overload
def get(text: Union[str, Text], convert: Callable[[str], T], default: Optional[T] = None, default_str: Optional[Union[str, Text]] = None, allow_empty: bool = False, silent: bool = False, inline: Optional[bool] = None) -> Optional[T]:
    ...

def get(text: Union[str, Text], convert: Callable[[str], T], default: Optional[T] = None, default_str: Optional[Union[str, Text]] = None, allow_empty: bool = False, silent: bool = False, inline: Optional[bool] = None) -> Optional[T]:
    def_text: Union[str, Text] = ""
    if default is not None:
        def_text = Text(" [", default_str or str(default), "]")
    out.print_question(Text(text, def_text), inline=inline)
    return inpt.select(convert, default, allow_empty, silent)


import math, re, sys


@overload
def ask_nlist(
    text: str,
    seq_items: Iterable[T],
    allow_range: Literal[False] = False,
    topiced_items: Optional[Union[Dict[str, List[T]], Dict[Optional[str], List[T]], Dict[str, Sequence[T]], Dict[Optional[str], Sequence[T]]]] = None,
    custom_keys: Literal[None] = None,
    custom_all_key: Literal[None] = None,
    default: Optional[T] = None,
    default_index: Optional[int] = None,
    display: Callable[[T], str] = str,
    skip_if_one: bool = False,
) -> T:
    ...


@overload
def ask_nlist(
    text: str,
    seq_items: Iterable[T],
    allow_range: Literal[True],
    topiced_items: Optional[Union[Dict[str, List[T]], Dict[Optional[str], List[T]], Dict[str, Sequence[T]], Dict[Optional[str], Sequence[T]]]] = None,
    custom_keys: Literal[None] = None,
    custom_all_key: Optional[str] = None,
    default: Optional[T] = None,
    default_index: Optional[int] = None,
    display: Callable[[T], str] = str,
    skip_if_one: bool = False,
) -> List[T]:
    ...


@overload
def ask_nlist(
    text: str,
    seq_items: Iterable[T],
    allow_range: Literal[False] = False,
    topiced_items: Optional[Union[Dict[str, List[T]], Dict[Optional[str], List[T]], Dict[str, Sequence[T]], Dict[Optional[str], Sequence[T]]]] = None,
    custom_keys: Optional[Dict[str, str]] = None,
    custom_all_key: Literal[None] = None,
    default: Optional[Union[T, str]] = None,
    default_index: Optional[Union[int, str]] = None,
    display: Callable[[T], str] = str,
    skip_if_one: bool = False,
) -> Union[str, T]:
    ...


@overload
def ask_nlist(
    text: str,
    seq_items: Iterable[T],
    allow_range: Literal[True],
    topiced_items: Optional[Union[Dict[str, List[T]], Dict[Optional[str], List[T]], Dict[str, Sequence[T]], Dict[Optional[str], Sequence[T]]]] = None,
    custom_keys: Optional[Dict[str, str]] = None,
    custom_all_key: Optional[str] = None,
    default: Optional[Union[T, str]] = None,
    default_index: Optional[Union[int, str]] = None,
    display: Callable[[T], str] = str,
    skip_if_one: bool = False,
) -> Union[str, List[T]]:
    ...


@overload
def ask_nlist(
    text: str,
    seq_items: Iterable[T],
    allow_range: bool = False,
    topiced_items: Optional[Union[Dict[str, List[T]], Dict[Optional[str], List[T]], Dict[str, Sequence[T]], Dict[Optional[str], Sequence[T]]]] = None,
    custom_keys: Optional[Dict[str, str]] = None,
    custom_all_key: Optional[str] = None,
    default: Optional[Union[T, str]] = None,
    default_index: Optional[Union[int, str]] = None,
    display: Callable[[T], str] = str,
    skip_if_one: bool = False,
) -> Union[str, T, List[T]]:
    ...


# ask using a list of valid items
# if the index of the selected item is required, enumerate(items) can be passed as arguments
def ask_nlist(
    text: str,
    seq_items: Iterable[T],
    allow_range: bool = False,
    topiced_items: Optional[Union[Dict[str, List[T]], Dict[Optional[str], List[T]], Dict[str, Sequence[T]], Dict[Optional[str], Sequence[T]]]] = None,
    custom_keys: Optional[Dict[str, str]] = None,
    custom_all_key: Optional[str] = None,
    default: Optional[Union[T, str]] = None,
    default_index: Optional[Union[int, str]] = None,
    display: Callable[[T], str] = str,
    skip_if_one: bool = False,
) -> Union[str, T, List[T]]:
    if default is not None and default_index is not None:
        assert False

    if topiced_items is None:
        topiced_items = cast(Union[Dict[str, List[T]], Dict[Optional[str], List[T]]], {})
    items = list(seq_items)
    if None in topiced_items:  # topiced_items key has Optional[str] type
        items += list(topiced_items[None])  # type: ignore[index]  # mypy cannot recognize None as keytype
    topiced_items = {topic: entries for topic, entries in topiced_items.items() if topic is not None}
    if custom_keys:
        for key in custom_keys:
            if re.match(r"^(\d+|\*)$", key):
                if key == "*":
                    if custom_all_key is not None:
                        raise Exception("custom key must not be '*'")
                else:
                    raise Exception("custom key must not be a number")
    else:
        custom_keys = {}

    if custom_all_key is not None:
        custom_keys = {**custom_keys, "*": custom_all_key}

    # sort dicts
    sorted_topiced_items = {topic: topiced_items[topic] for topic in sorted(topiced_items)}
    sorted_custom_keys = {key: custom_keys[key] for key in sorted(custom_keys)}

    result_list: List[T] = []
    for topic_items in sorted_topiced_items.values():
        result_list.extend(topic_items)
    result_list.extend(items)
    entry_count = len(result_list)

    default_str = None
    default_custom_key = None
    if default is not None:
        if default in result_list:  # implies 'default' is of type T
            # mypy cannot recognise implied type
            default_str = str(result_list.index(default))  # type: ignore[arg-type]
            default_custom_key = False
        elif isinstance(default, str) and default in custom_keys.values():
            default_str = {v: k for k, v in custom_keys.items()}[default]
            default_custom_key = True
        else:
            assert False
    elif default_index is not None:
        if isinstance(default_index, int):
            if 1 <= default_index <= entry_count:
                default_str = str(default_index)
                default_custom_key = False
                default = result_list[default_index-1]
            else:
                assert False
        elif default_index in custom_keys:
            default_str = default_index
            default_custom_key = True
            default = custom_keys[default_index]
        else:
            assert False

    if entry_count == 1 and skip_if_one:
        if allow_range:
            return [result_list[0]]
        return result_list[0]

    max_key_length = max(0, int(math.log10(max(entry_count, 1))+1), *[len(key) for key in custom_keys.keys()])

    fmt_str = f" [%{max_key_length}s]: %s"

    def print_choices() -> None:
        print(f">>> {text}", flush=True)
        item_id = 1
        for header, entry_items in sorted_topiced_items.items():
            print(header)
            for item in entry_items:
                print(fmt_str % (item_id, display(item)))
                item_id += 1
            print()
        for item in items:
            print(fmt_str % (item_id, display(item)))
            item_id += 1
        for key, value in sorted_custom_keys.items():
            print(fmt_str % (key, value))

    print_choices()
    from .inpt.selector import select_str
    def vrfy(choice_str: str) -> bool:
        if default is not None and choice_str == "":
            return True

        if custom_all_key is not None and choice_str == "*":
            return True
        if choice_str in sorted_custom_keys:
            return True
        if allow_range:
            choices: Set[int] = set()
            invalid_choices = []

            for range_str in map(str.strip, choice_str.split(",")):
                range_match = re.match(r"^(\d+|(\d+)-(\d+))$", range_str)
                if range_match:  # range / number
                    if range_match.group(2) and range_match.group(3):  # range
                        start = int(range_match.group(2))
                        end = int(range_match.group(3))
                        if 1 <= start <= end <= entry_count:
                            choices.update(range(start, end+1))
                            continue
                    elif 1 <= int(range_match.group(1)) <= entry_count:
                        choices.add(int(range_match.group(1)))
                        continue
                invalid_choices.append(range_str)

            return not invalid_choices

        return choice_str.isdigit() and (int(choice_str) > 0) and (int(choice_str) <= len(result_list))

    print_choices()
    print("> ", end="", flush=True)
    choice_str = select_str(verify=vrfy)

    if default is not None and choice_str == "":
        if allow_range and default_custom_key is False:
            return [default]  # type: ignore[list-item]  # default_custom_key enforces type T
        return default

    if custom_all_key is not None and choice_str == "*":
        return result_list
    if choice_str in custom_keys:
        return choice_str
    if allow_range:
        choices: Set[int] = set()
        invalid_choices = []

        for range_str in map(str.strip, choice_str.split(",")):
            range_match = re.match(r"^(\d+|(\d+)-(\d+))$", range_str)
            if range_match:  # range / number
                if range_match.group(2) and range_match.group(3):  # range
                    start = int(range_match.group(2))
                    end = int(range_match.group(3))
                    if 1 <= start <= end <= entry_count:
                        choices.update(range(start, end+1))
                        continue
                elif 1 <= int(range_match.group(1)) <= entry_count:
                    choices.add(int(range_match.group(1)))
                    continue
            invalid_choices.append(range_str)

        if invalid_choices:
            pass # impossible
        return [result_list[choice-1] for choice in choices]

    if not choice_str.isdigit() or (int(choice_str) < 1) or (int(choice_str) > len(result_list)):
        #print_error("Invalid value \"%s\". Please enter again" % choice_str)
        pass  # impossible

    return result_list[int(choice_str)-1]

