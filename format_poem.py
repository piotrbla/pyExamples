from unittest.test.test_case import Test


def format_poem(poem):
    if poem[-1:] == ".":
        return ".\n".join(x.strip() for x in str.split(poem, '.'))
    else:
        return ".\n".join(x.strip() for x in str.split(poem, '.'))[:-1] + poem[-1:]

x=[1, 2, 3]
a = sum(x)/len(x)
print(format_poem('Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated?'))
    # 'Beautiful is better than ugly.\nExplicit is better than implicit.\nSimple is better than complex.\nComplex is better than complicated.')