list = [1,4,3,'popeye', [1,4], True, None]
sentence = 'I am a good python enthusiast life is great!'
words = sentence.split()

# for index, l in enumerate(list):
#     print(f'list: {l}, index: {index}')

# rebuild list !
int_list = [l for l in list if type(l) == int]
lentghs = [len(t) for t in words]
print(lentghs)

print(sum([1,2,3,4,5,10]))

squares = [n * n for n in range(1,101) ]
print(sum(squares))