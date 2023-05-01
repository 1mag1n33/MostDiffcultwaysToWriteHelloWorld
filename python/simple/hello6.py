def print_message(message):
    if len(message) == 1:
        print(message)
    else:
        print_message(message[:-1])
        print(message[-1])

print_message("Hello, World!")
