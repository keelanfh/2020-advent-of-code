from itertools import count


def transform(subject_number: int, loop_size: int) -> int:
    value = 1
    for x in range(loop_size):
        value *= subject_number
        value %= 20201227

    return value


def decrypt(public_key):
    for x in count(1):
        if transform(7, x) == public_key:
            return x


# a, b = 5764801, 17807724
a, b = 11562782, 18108497
print(transform(a, decrypt(b)))

# for x in (11562782, 18108497):
#     # print(decrypt(x))
#     print(transform(18108497, decrypt(11562782)))
