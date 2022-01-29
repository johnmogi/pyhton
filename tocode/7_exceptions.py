def illegal_divide_by_zero(num):
    if num / 0 :
        raise Exception (' sub zero fatality ')

try:
    illegal_divide_by_zero(5)
except Exception:
    print('sorry exception')

