
def split_and_join(line):
    # write your code here
    list1 = line.split(" ")
    return '-'.join(list1)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
