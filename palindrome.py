def palindrome(str):
    if str == str[::-1]:
        return true
    else:
        return false
string = input("madam")
result = palindrome(string)
if result:
    print("str is palindrome")
else:
    print(str is not palindrome)