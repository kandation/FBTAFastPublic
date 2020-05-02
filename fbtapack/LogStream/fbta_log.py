
def log(*args):
    text = ''
    for i, t in enumerate(args):
        text += str(t) + str('\t' if i != len(args) - 1 else '')
    print(text)
