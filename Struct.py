def struct_value(string):
    """
    Return converted value

    When you put string, you should put the string shape of only one value.
    For example, "1, 2, 3, 4, 5" is the wrong input shape. Instead, use "[1, 2, 3, 4, 5]"

    :param string: string shape of a vlue
    """
    if has_wrong_syntax(string):
        raise SyntaxError(f"{string}\n\nSyntaxError: Unmatched parenthesis or invalid values")
    interpreted_value = ''
    return_type = None
    c = string[0]
    if c == "[":
        if string[1] == "]":
            return []
        return_type = list
        interpreted_value = []
        for item in separate_by_comma(string[1:-1]):
            interpreted_value.append(struct_value(item))
    elif c == "(":
        if string[1] == ")":
            return tuple()
        return_type = tuple
        interpreted_value = []
        for item in separate_by_comma(string[1:-1]):
            interpreted_value.append(struct_value(item))
    elif c == "{":
        if string[1] == "}":
            return dict()
        return_type = dict
        interpreted_value = dict()
        # TODO declare how to convert str to dict
        pass
    elif c.isdigit():
        if '.' in string:
            return_type = float
        else:
            return_type = int
        interpreted_value = string
    elif c == '"' or c == "'":
        return_type = str
        interpreted_value = string[1:-1]
    elif string.lower() == 't' or string.lower() == 'f':
        return_type = bool
        interpreted_value = True if string.lower() == 't' else False
    else:  # Unknown initial character
        raise SyntaxError(f"Unknown character {c}.\nIf you want 'str', use a pair of quotations.")
        pass
    return return_type(interpreted_value)


def separate_by_comma(string) -> list:
    """
    Separate string based on comma.

    :param string:
    :return: split string
    """
    quot = ''
    sequence = []
    escape = 0
    string_buffer = ''
    value_list = []
    for c in string:
        if escape:
            escape = False
            if c == 'n':
                string_buffer += '\n'
                continue
            elif c == 't':
                string_buffer += '\t'
                continue
            elif c == 'b':
                string_buffer += '\b'
                continue
            elif c == '\\' or c == '"' or c == "'":
                pass
            else:
                raise SyntaxError("EzTest only supports \\, \", and \' escape characters.")
        elif (c == '"' or c == "'") and not sequence:
            if quot == '':
                quot = c
            elif quot == c:
                quot = ''
        elif quot:  # In string section
            if c == '\\':
                escape = True
                print("ESCAPE")
                continue
        elif c in ['[', '(', '{']:  # Not in string part, but in sequence part
            sequence.append(c)
        elif sequence:
            if (sequence[-1], c) in (('[', ']'), ('(', ')'), ('{', '}')):
                sequence.pop(-1)
        elif c == ' ':  # Redundant white space
            continue
        elif c == ',':
            value_list.append(string_buffer)
            string_buffer = ''
            continue
        string_buffer += c

    value_list.append(string_buffer)
    return value_list


def has_wrong_syntax(string) -> bool:
    """
    Check the pair and the sequence of parenthesis & quotations.

    :param string: target
    :return: true when wrong syntax detected
    """
    # TODO simply check pair of those two... SKIP!
    return False