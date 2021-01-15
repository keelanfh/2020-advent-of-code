from itertools import count
import math


# def transform(subject_number: int, loop_size: int) -> int:
#     value = 1
#     for x in range(loop_size):
#         value *= subject_number
#         value %= 20201227

#     return value

def transform(subject_number: int, loop_size: int) -> int:
    print(subject_number, loop_size)
    return (subject_number ** loop_size) % 20201227


# def decrypt(public_key):
#     while True:
#         i *= 7
#         loop_size = math.log(public_key + i * 20201227, 7)
#         if int(loop_size) == loop_size:
#             return int(loop_size)

def decrypt(public_key):
    p7 = 7
    power = 1
    while True:
        p7a = p7 - public_key
        if not p7a % 20201227:
            return power
        p7 *= 7
        power += 1


a, b = 5764801, 17807724
# a, b = 11562782, 18108497
print(transform(a, decrypt(b)))

# for x in (11562782, 18108497):
#     # print(decrypt(x))
#     print(transform(18108497, decrypt(11562782)))
