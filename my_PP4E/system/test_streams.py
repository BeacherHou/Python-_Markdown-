"read numbers till eof and show squares"


def interact():
    "与用户交互计算平方"
    print('Hello, stream world!')
    while True:
        try: reply_str = input('Enter a number >>> ')
        except EOFError: break
        else:
            if reply_str == 'exit': break
            reply_int = int(reply_str)
            print('%s squared is %d' % (reply_str, reply_int ** 2))
    print(':) Bye')
    

if __name__ == '__main__':
    interact()
