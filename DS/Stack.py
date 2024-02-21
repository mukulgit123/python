def createStack():
    stack = []
    return stack


def push(stack, item):
    length = len(stack)
    stack += [item]
    return stack


def pop(stack):
    if not(isEmpty(stack)):
        length = len(stack)
        item = stack[length - 1]
        stack = stack[:-1]
        return stack
    else:
        print("Stack is empty")
        exit()


def isEmpty(stack):
    return len(stack) == 0


def peek(stack):
    print(stack[len(stack) - 1])


if __name__ == '__main__':
    stack = createStack()
    stack = push(stack, str("first"))
    stack = push(stack, str("second"))
    stack = push(stack, str("third"))
    stack = push(stack, str("fourth"))
    peek(stack)
    stack = pop(stack)
    peek(stack)
    print("stack after popping an element: " + str(stack))
    stack = pop(stack)
    stack = pop(stack)
    print("stack after popping an element: " + str(stack))
    stack = pop(stack)
    print("stack after popping an element: " + str(stack))
    stack = pop(stack)
    stack = pop(stack)
