# print('hello')
#
# for i in range(5):
#     print(i)

# let's create an error:

str = 'this is a string'
int = 0

def concat(*args):
    str = args[0]
    int = args[1]
    result = int + str
    return result


if __name__ == '__main__':
    result = concat(str, int)

    with result as e:
        try:
            print(result)
        except:
            print('error: ', e)