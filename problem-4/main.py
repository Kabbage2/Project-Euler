""" 
write function that checks if palindrome that returns True or False
nested for loop that that starts 999 * 999 then 998...100, then 998*998 997 996...100 then 997*997 996 and so on
each product checks for palindrome if true break and print number

for the palindrome convert number into string, then reverse string and compare just using ==

"""

def is_palindrome(s):
    original_string = str(s)
    reversed_string = original_string[::-1]
    if original_string == reversed_string:
        return True
    else:
        return False

    
