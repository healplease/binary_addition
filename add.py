def bit_and(left:int, right:int) -> int:
    '''One-bit AND function.\n\t0, 0 → 0\n\t0, 1 → 0\n\t1, 0 → 0\n\t1, 1 → 1'''
    return 1 if all((int(bool(left)), int(bool(right)))) else 0

def bit_xor(left:int, right:int) -> int:
    '''One-bit XOR function.\n\t0, 0 → 0\n\t0, 1 → 1\n\t1, 0 → 1n\t1, 1 → 0'''
    return 1 if int(bool(left)) != int(bool(right)) else 0

def number_to_binary_array(number: int) -> list:
    return list(map(int, reversed(str(bin(number))[2:])))

def binary_array_to_number(array: list) -> int:
    return int('0b' + ''.join(map(str, reversed(array))), 2)

def half_binary_addition(left:int, right:int) -> [int, int]:
    '''Half binary addition.\n\t0, 0 → 0, 0\n\t0, 1 → 1, 0\n\t1, 0 → 1, 0\n\t1, 1 → 0, 1'''
    units = bit_xor(left, right)
    twos = bit_and(left, right)
    return units, twos

def full_binary_addition(left:int, right:int, overfill:int=0) -> [int, int]:
    '''Half binary addition.\n\t0, 0, 0 → 0, 0\n\t0, 0, 1 → 1, 0\n\t0, 1, 0 → 1, 0\n\t1, 0, 0 → 1, 0\n\t0, 1, 1 → 0, 1\n\t1, 1, 0 → 0, 1\n\t1, 0, 1 → 0, 1\n\t1, 1, 1 → 1, 1'''
    units, twos = half_binary_addition(left, right)
    units, carry = half_binary_addition(units, overfill)
    twos, _ = half_binary_addition(twos, carry)
    return units, twos

def binary_add(left: list, right: list) -> list:
    result = []
    overfill = 0
    for i in range(max(len(left), len(right))):
        left_bit = left[i] if i < len(left) else 0
        right_bit = right[i] if i < len(right) else 0
        addition, overfill = full_binary_addition(left_bit, right_bit, overfill)
        result.append(addition)
    result.append(overfill)
    return result

def add(left:int, right:int) -> int:
    left = number_to_binary_array(left)
    right = number_to_binary_array(right)
    result = binary_add(left, right)
    result = binary_array_to_number(result)
    return result

if __name__ == '__main__':
    x = add(7, 14)
    print(x)
