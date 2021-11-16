s = 'abcdefghijklmnopqrstuvwxyz'
    
msg = input('Enter your message: ').lower()
n = int(input('Enter your number: '))

len_alpha = len(s)
ascii_a = ord('a')

l = []

for ch in msg:

    if ch in s: # 'ch' is a valid alphabhet
        ch_num = ord(ch) - ascii_a
        modulus = (ch_num + n) % len_alpha
        ch_change = s[modulus]

    else: # 'ch' is not a valid alphabhet
        ch_change = ch
    
    l.append(ch_change)

encrypted_msg = ''.join(l)

print('Current messege:', msg)
print('Encrypted messege:', encrypted_msg)
