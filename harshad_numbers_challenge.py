"""In mathematics, a harshad number (or Niven number) in a given number base is an integer
that is divisible by the sum of its digits when written in that base. Harshad numbers in base n
 are also known as n-harshad (or n-Niven) numbers. Harshad numbers were defined by D. R. Kaprekar,
  a mathematician from India. The word "harshad" comes from the Sanskrit harṣa (joy) + da (give),
   meaning joy-giver. The term "Niven number" arose from a paper delivered by Ivan M. Niven
   at a conference on number theory in 1977. All integers between zero and n are n-harshad numbers.
   This program checks if the entered number is Harshad number."""

def isHarshad(n):
    div = 0
    l=len(n)
    for i in range(l):
        div+=int(n[i])
    if int(n)%div ==0:
        return True
    return False

inp = input("Enter an integer:\n")
if(isHarshad(inp)):
    print("Yes, it's Harshad number.")
else:
    print("No, not a Harshad.")
