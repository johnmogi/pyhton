elements = { "element": "Earth", "position":"first"}

elements['new item'] = 'added'

try:
    del(elements['position2'])
except KeyError:
    print('KeyError : this element does not exist... ')
print(elements)

if 'element' in elements:
    print('yes element')

try:
    del(elements['position'])
except:
    print('allready deleted...')

# interpreter : dir({}) // help({}.get)

# for key, value in elements.items():
#     print(f'key:{key}, value: {value}')

# for key in elements.keys():
#     print(key)
# for value in elements.values():
#     print(value)

# build a new dictionary (comprehension)

elements_guide = {
    key: len(val)
    for key, val in elements.items()
}
# spread operations **
a = {"1":"a","3":"b"}
b = {"3":"a","4":"b"}
c = {**a, **b}
print(c)
