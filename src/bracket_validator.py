def is_valid_bracket(string: str) -> bool:
    brackets_open = "([{"
    brackets_close = ")]}"

    stack = []

    for char in string:
        if char in brackets_open:
            stack.append(char)
        elif not stack or stack.pop() != brackets_open[brackets_close.index(char)]:
            return False

    return len(stack) == 0
