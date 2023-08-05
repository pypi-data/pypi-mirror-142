
def code_in_combo(code: str, combo: str) -> bool:
    matches = combo.replace(',', '|').split('|')
    for match in matches:
        if code == match:
            return True
        # This match is a range: split the range and check each limit
        elif '-' in match:
            start, end = (x.strip() for x in match.split('-'))
            if start <= code <= end:
                return True
    return False
