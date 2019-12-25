
def get_2350():
    f = open('./2350.txt')

    h_list = []

    while True:
        line = f.readline().splitlines()
        if not line: break
        h_list.append(line[0])
    f.close()

    return h_list
