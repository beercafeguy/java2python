

def validate_string(input_string):
    tmp_stack = []
    for s in input_string:
        if s == '{' or s == '[' or s == '(':
            tmp_stack.append(s)
        elif s == '}':
            if len(tmp_stack) == 0 or tmp_stack.pop() != '{':
                return False
        elif s == ']':
            if len(tmp_stack) == 0 or tmp_stack.pop() != '[':
                return False
        elif s == ')':
            if len(tmp_stack) == 0 or tmp_stack.pop() != '(':
                return False
        else:
            continue

    if len(tmp_stack) !=0:
        return False
    else:
        return True


print(validate_string('{[]}'))

validate_string('Hem')