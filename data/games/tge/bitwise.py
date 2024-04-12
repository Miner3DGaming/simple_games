


def b_lshift(a, b):
    """
    Performs a bitwise left shift operation on the given byte 'a'.
    
    Args:
        a (int): The byte value to be left-shifted.
        b (int): The number of positions to shift 'a' to the left.
        
    Returns:
        int: The result of left-shifting 'a' by 'b' positions.
    """
    return a << b


def b_rshift(a, b):
    """
    Perform bitwise right shift operation on the given byte 'a'.

    Args:
        a (int): The byte value to be bitwise right shifted.
        b (int): The number of positions to right shift 'a' by.

    Returns:
        int: The result of the bitwise right shift operation on 'a' by 'b' positions.
    """
    return a >> b


def b_and(a, b):
    """
    Performs a bitwise AND operation between two bytes.

    This function takes two byte inputs, 'a' and 'b', and performs a bitwise AND
    operation on them. The bitwise AND operation returns a new byte where each
    bit is the result of the AND operation performed on the corresponding bits of 'a'
    and 'b'. In other words, each bit in the output is set to 1 only if the
    corresponding bits in both 'a' and 'b' are also set to 1; otherwise, it is set to 0.

    Args:
        a (int): The first byte operand.
        b (int): The second byte operand.

    Returns:
        int: The result of the bitwise AND operation between 'a' and 'b'.
    """
    return a & b


def b_or(a, b):
    """
    Perform a bitwise OR operation between two bytes.

    This function takes two byte inputs, 'a' and 'b', and returns the result
    of applying the bitwise OR operation between them. In a bitwise OR operation,
    each bit in the output is set to 1 if at least one of the corresponding bits
    in the input bytes is 1.

    Args:
    a (int): The first input byte.
    b (int): The second input byte.

    Returns:
    int: The result of the bitwise OR operation between 'a' and 'b'.
    """
    return a | b


def b_xor(a, b):
    """
    Perform a bitwise XOR (exclusive OR) operation between two bytes.
    
    This function takes two byte values, 'a' and 'b', and applies the bitwise XOR operation
    to their binary representations. It returns an byte representing the result of the XOR operation.
    
    Parameters:
    a (int): The first byte operand for the XOR operation.
    b (int): The second byte operand for the XOR operation.
    
    Returns:
    int: The result of the bitwise XOR operation between 'a' and 'b'.
    """
    return a ^ b


def b_not(a):
    """
    Perform bitwise NOT operation on the given byte 'a'.

    This function calculates the bitwise NOT operation on the input byte 'a', which inverts
    each bit of the binary representation of 'a'. It returns the result of this operation.

    Args:
    a (int): The byte value on which the bitwise NOT operation will be applied.

    Returns:
    int: The result of the bitwise NOT operation, which is the byte with inverted bits.
    """
    return ~a


def b_nand(a, b):
    """
    Computes the bitwise NAND (NOT AND) operation between two binary inputs.

    The bitwise NAND of two binary digits is calculated by performing the bitwise AND
    operation on the inputs and then negating (flipping) the result.

    Args:
        a (int): The first binary input (0 or 1).
        b (int): The second binary input (0 or 1).

    Returns:
        int: The result of the bitwise NAND operation, which is 0 if the bitwise AND of
        the inputs is 1, and 1 otherwise.
    """
    return ~(a & b)


def b_nor(a, b):
    """
    Performs bitwise NOR (NOT OR) operation between two input bytes, 'a' and 'b'.

    This function takes two byte inputs 'a' and 'b' and calculates the result
    of the bitwise NOR operation ~(a | b), where '|' represents the bitwise OR operation
    and '~' represents the bitwise NOT operation.

    Parameters:
    a (int): The first input byte.
    b (int): The second input byte.

    Returns:
    int: The result of ~(a | b), the bitwise NOR operation between 'a' and 'b'.
    """
    return ~(a | b)


def b_nxor(a, b):
    """
    Perform bitwise negated XOR (b_nxor) operation between two bytes, 'a' and 'b'.

    The function calculates the bitwise negated XOR of 'a' and 'b', which is equivalent
    to applying the XOR operation between 'a' and 'b' and then performing a bitwise
    NOT operation on the result.

    Args:
        a (int): An byte operand for the bitwise operation.
        b (int): Another byte operand for the bitwise operation.

    Returns:
        int: The result of the bitwise negated XOR operation between 'a' and 'b'.
    """
    return ~(a ^ b)


def b_three_nand(a, b, c):
    """
    Compute the 3-input NAND gate result.

    This function calculates the logical NOT-AND (NAND) operation for three input values: a, b, and c.
    
    Args:
    a (int): The first input binary value (0 or 1).
    b (int): The second input binary value (0 or 1).
    c (int): The third input binary value (0 or 1).
    
    Returns:
    int: The result of the 3-input NAND operation, which is 1 if the logical NOT-AND of all inputs is 0, otherwise 0.
    """
    return ~(a & b & c) & 1


def b_three_nor(a, b, c):
    """
    Performs a three-input NOR operation on the given inputs.

    This function calculates the result of a three-input NOR (NOT-OR) gate operation,
    which involves taking the logical NOR of three input values (a, b, and c), and then
    applying a bitwise NOT operation to the result. The final output is obtained by
    performing a bitwise AND operation with 1 to ensure a single bit output.

    Args:
    a (int): The first input value (0 or 1).
    b (int): The second input value (0 or 1).
    c (int): The third input value (0 or 1).

    Returns:
    int: The result of the three-input NOR operation, a single bit either 0 or 1.
    """
    return ~(a | b | c) & 1


def b_three_nxor(a, b, c):
    """
    Calculate the three-input negated exclusive OR (NXOR) operation.

    This function takes three input values (a, b, c) and performs a bitwise
    exclusive OR (XOR) operation on them. The result of the XOR operation is
    then inverted (bitwise NOT), and the least significant bit is extracted
    using a bitwise AND operation with 1.

    Parameters:
    a (int): The first input bit (0 or 1).
    b (int): The second input bit (0 or 1).
    c (int): The third input bit (0 or 1).

    Returns:
    int: The result of the three-input NXOR operation, which is either 0 or 1.
    """
    return ~(a ^ b ^ c) & 1


def b_three_xor(a, b, c):
    """
    Calculate the bitwise three-way XOR operation with negation.

    This function takes three input bytes, 'a', 'b', and 'c', and performs a bitwise
    three-way XOR (^) operation between them. The result of this XOR operation is then
    bitwise negated using the '~' operator. The final negated XOR result is returned.

    Args:
        a (int): The first input byte.
        b (int): The second input byte.
        c (int): The third input byte.

    Returns:
        int: The result of ~(a ^ b ^ c), i.e., the bitwise negated three-way XOR result.
    """
    return ~(a ^ b ^ c)

