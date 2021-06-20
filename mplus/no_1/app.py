
#metode palindrome
def isPalindrome(str):
    for i in range(0, int(len(str)/2)):
        if str[i] != str[len(str)-i-1]:
            return False

        return True

s = input(str("tuliskan kata : "))

# menambahkan ke list kosong
temp = []
for karakter in s:
    if karakter in ['{','[','(',')',']','}'] :
        temp.append(karakter)

# conver list to str
str1 = ''.join(temp)
unique_str = isPalindrome(str1)

if (unique_str):
    print("True")
else:
    print("False")