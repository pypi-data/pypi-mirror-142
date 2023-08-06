import json

ALL_CAPTION = "<ALL>"
NONE_CAPTION = "<NONE>"
WTF_CAPTION = "<???>"
NO_YES_OPTIONS = ["No", "Yes"]


def get_ords(chs: str) -> dict:
    res = {}

    for x in chs:
        if x.isalpha():
            res[x] = { ord(x), ord(x.upper()) }

        else:
            res[x] = { ord(x) }

    return res


def assign_diff(obj1, obj2, attr: str, type_conv = None) -> bool:
    if isinstance(obj1, dict):
        v1 = obj1[attr]
    else:
        v1 = getattr(obj1, attr)

    if isinstance(obj2, dict):
        v2 = obj2[attr]
    else:
        v2 = getattr(obj2, attr)

    if type_conv:
        if type_conv == dict:
            if v1 and not isinstance(v1, dict):
                v1 = json.loads(v1)

            if v2 and not isinstance(v2, dict):
                v2 = json.loads(v2)
        else:
            if v1 is not None:
                v1 = type_conv(v1)

            if v2 is not None:
                v2 = type_conv(v2)

    if v1 == v2:
        return False

    if isinstance(obj1, dict):
        obj1[attr] = v2
    else:
        setattr(obj1, attr, v2)

    return True


def validator_alpha() -> str:
    return "^[a-zA-Z]*$"


def validator_numeric() -> str:
    return "^[0-9]*$"


def validator_json(value: str) -> bool:
    if not value:
        return True

    try:
        json.loads(value)
    except Exception:
        return False

    return True


def couplet_to_dropdown(cplt: dict, add_all: bool = True, add_none: bool = False) -> list:
    res = []

    if add_all:
        res.append((ALL_CAPTION, None))
    elif add_none:
        res.append((NONE_CAPTION, None))

    keys = list(cplt.keys())
    keys.sort()

    for key in keys:
        res.append((cplt[key], key))

    return res


def pop_exception(screen, ex: Exception) -> str:
    from asciimatics import widgets

    text = f'!! ERROR !!\n\n{ex}'
    return widgets.PopUpDialog(screen, text, ["OK"], has_shadow=True)
