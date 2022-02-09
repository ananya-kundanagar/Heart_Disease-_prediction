from collections import defaultdict
from json.tool import main


def possibility(m,length,s):
    countodd = 0
    for i in range(0,length):
        if m[int(s[i])] & 1:
            countodd +=1
        if countodd >1 :
            return False
    return True


def largestPalindrome(s):
    l = len(s)
    m = defaultdict(lambda:0)
    for i in range(0,l):
        m[int(s[i])] +=1
    if possibility(m,l,s) == False:
        print("-1")
        return
    largest = [None]*l
    front = 0
    for i in range(9,-1,-1):
        if m[i] & 1:
            largest[l//2] = chr(i + 48)
            m[i] -= 1
            while m[i]>0:
                largest[front] = chr(i + 48)
                largest[l- front - 1] = chr(i+48)
                m[i] = m[i] -2
                front = front +2
        else:
            while m[i]>0:
                largest[front] = chr(i + 48)
                largest[l- front - 1] = chr(i+48)
                m[i] = m[i] -2
                front = front +1

    for i in range(0,l):
        print(largest[i],end="")

if __name__ == "__main__":
    s = "388003"
    largestPalindrome(s)
