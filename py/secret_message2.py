import string

nmbr = int(input('Enter your encode number: '))

alpha = string.ascii_lowercase
ch_alpha = list(alpha)

for i in range(0, 26):
    ch_alpha[(i - nmbr) % 26] = alpha[i]
    
d = {}

for i in range(0, 26):
    d[alpha[i]] = ch_alpha[i]


msg = input('Enter your messege: ')
l = []

for ch in msg:
    change = d.get(ch)
    if change: l.append(change)
    else: l.append(ch)

encrypted_msg = ''.join(l)


print('Encrypted messege:', encrypted_msg)