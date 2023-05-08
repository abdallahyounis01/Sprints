def isBalanced(expr):
    stack = []

    for char in expr:
        if char in ["(", "{", "["]:
            stack.append(char)
        else:
            if not stack:
                return False
            curr_char = stack.pop()
            if curr_char == '(':
                if char != ')':
                    return False
            if curr_char == '{':
                if char != '}':
                    return False
            if curr_char == '[':
                if char != ']':
                    return False
    if not stack:
        print("YES")
        return True
    else:
        print("NO")
        return False


user_input = input("Please Enter The Expr.")
isBalanced(user_input)
