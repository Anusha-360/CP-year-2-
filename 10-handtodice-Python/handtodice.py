# Write the (very short) function handtodice(hand) that takes a hand, which is a 3-digit
# integer, and returns 3 values, each of the 3 dice in the hand. For example:
# assert(handToDice(123) == (1,2,3))
# assert(handToDice(214) == (2,1,4))
# assert(handToDice(422) == (4,2,2))
# Hint: You might find // and % useful here, and also getKthDigit().

def handtodice(hand):
    first = hand // 100
    second = (hand % 100) // 10
    third = (hand % 100) % 10
    return first, second, third

#reference: https://github.com/Chiver/15-112-Fundamentals-of-Programming/blob/master/hw1_Version2.py