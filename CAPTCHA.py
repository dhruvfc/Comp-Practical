import random as r
def generate_captcha(length=6):
    captcha = ""
    for ch in range(length):
        pick=r.randint(0,3)
        if pick == 0:
            captcha += chr(r.randint(65,90))
        elif pick == 1:
            captcha += chr(r.randint(97,122))
        else:
            captcha += chr(r.randint(48,57))
    return captcha
l = int(input("Enter the length of CAPTCHA: "))
print(f'Your CAPTCHA code: {generate_captcha(l)}')
