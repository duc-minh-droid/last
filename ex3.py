def palindrome(str):
    str = str.lower()
    if len(str) == 0 or len(str) == 1:
        return True
    else:   
        if str[0] == str[-1]:
            new_str = str[1:-1]
            return palindrome(new_str)
    return False

def palindrome_check(str = 'anna'):
    if palindrome(str):
        print("This is a palindrome")
    else:
        print("This is not a palindrome")

palindrome_check()