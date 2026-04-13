def uppercase_str(text: str) -> str:
    if not text:
        return text
    return text.upper()


def lowercase_str(text: str) -> str:
    if not text:
        return text
    return text.lower()


def str_to_bool(text: str) -> bool:
    if not text:
        return False
    elif text == "Y" or text.lower() == "Yes".lower():
        return True
    else:
        return False
