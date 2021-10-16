########################### RSA Dengan Prime nya banyak #############################################

c = 6488293261606014277091392128869233168531548849050248399359686121417746626783526637347685122158877385411976583903280710790714922412127596041361750573

n = 314023974770865158461482639051188010602202272692554382231234062425892672456098976348343947571949650134800387751275012586806886360188626923542802460259

e = 65537

#dicari dulu primesnya bisa pakai script python (primefac.factorint(N)) atau pakai factordb
primes = [1042919235925477, 577192626661733, 954969218713903, 1071402216629609, 1056588654801203, 928709697809027, 925078120771379, 631399780140607, 1089461387596753, 816523781051353]

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m


# From https://crypto.stackexchange.com/questions/31109/rsa-enc-decryption-with-multiple-prime-modulus-using-crt
ts = []
xs = []
ds = []

for i in range(len(primes)):
    ds.append(modinv(e, primes[i]-1))

m = primes[0]

for i in range(1, len(primes)):
    ts.append(modinv(m, primes[i]))
    m = m * primes[i]

for i in range(len(primes)):
    xs.append(pow((c%primes[i]), ds[i], primes[i]))

x = xs[0]
m = primes[0]

for i in range(1, len(primes)):
    x = x + m * ((xs[i] - x % primes[i]) * (ts[i-1] % primes[i]))
    m = m * primes[i]


print hex(x%n)[2:-1].decode("hex")
