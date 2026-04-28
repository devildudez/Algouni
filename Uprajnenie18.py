S = ["Amazon", "Yahoo", "eBay", "Yahoo", "Yahoo", "Oracle"]
S_prime = ["Yahoo", "eBay", "Yahoo", "Oracle"]
s = 0
s_p = 0
while s_p < len(S_prime) and s < len(S):
    if S[s] == S_prime[s_p]:
        s_p += 1
    else:
        s += 1

if s_p == len(S_prime):
    print(True)
else:
    print(False)

print(s_p == len(S_prime))