import ecdsa
from ecdsa import ellipticcurve
from ecdsa import numbertheory
from random import SystemRandom
import codecs
# NIST Curve P-384:
_p = 39402006196394479212279040100143613805079739270465446667948293404245721771496870329047266088258938001861606973112319
_r = 39402006196394479212279040100143613805079739270465446667946905279627659399113263569398956308152294913554433653942643
# s = 0xa335926aa319a27a1d00896a6773a4827acdac73L
# c = 0x79d1e655f868f02fff48dcdee14151ddb80643c1406d0ca10dfe6fc52009540a495e8042ea5f744f6e184667cc722483L
_b = 0xB3312FA7E23EE7E4988E056BE3F82D19181D9C6EFE8141120314088F5013875AC656398D8A2ED19D2A85C8EDD3EC2AEF
_Gx = 0xAA87CA22BE8B05378EB1C71EF320AD746E1D3B628BA79B9859F741E082542A385502F25DBF55296C3A545E3872760AB7
_Gy = 0x3617DE4A96262C6F5D9E98BF9292DC29F8F41DBD289A147CE9DA3113B5F0B8C00A60B1CE1D7E819D7A431D7C90EA0E5F

# y^2 = x^3+ax+b mod p
# ellipticcurve.CurveFp(p, a, _b, h(flag, not join the encrypt))
# a = -3 mod p = p - 3, so a = -3
curve_384 = ellipticcurve.CurveFp(_p, -3, _b, 1)

# __init__(self, curve, x, y, z, order=None, generator=False)
# 
# Initialise a point that uses Jacobi representation internally.
generator_384 = ellipticcurve.PointJacobi(
    curve_384, _Gx, _Gy, 1, _r, generator=True
)

g = generator_384
n = g.order()
print(hex(n))
# print(hex(n))
randrange = SystemRandom().randrange
# d = randrange(1, n)
d = 0xe05b05a4d6c336fba9346a64932f145a4c89d641a07a4cdda185daeda7943fa0dcc2428820cc7ff7644d817917ebcace

# now PubKey is publickey, d is private key
# notice: here the mul is for curve_mul.
PubKey = d * generator_384

flag = b"flag{3CC_I3_Use7f1_HaHA}"
x1 = int(codecs.encode(flag[:12],'hex'),16)
x2 = int(codecs.encode(flag[12:],'hex'),16)
X = (x1,x2)

k = randrange(1, n-1)
y0 = k*generator_384
KPoint = k*PubKey
Y = (X[0] * KPoint.x() % _p, X[1]*KPoint.y() % _p)

# Y is the encrypty message
print("Encrypt Message:")
print("(C1,C2)=(({},{}),({},{})".format(Y[0],Y[1],y0.x()%_p,y0.y()%_p))

# hint:Menezes-Vanstone cryptosystem
text = """
如果RSA已经难不倒你了，不如试一下椭圆曲线加密吧~
椭圆曲线E(a,b,p): y^2 = x^3+ax+b mod p
密码学中描述一条有限域上的椭圆曲线常用到六个参量：
T=(p,a,b,G,n,h)以及公钥和私钥
都放在p384-key.pem文件里面了（对，私钥也在）
PubKey = PrivKey*generator_384(G)
不过这个算法并不是【正规的椭圆曲线】，所以不要直接上网找脚本哦。这边给出这个椭圆曲线的加密方式:
x1 = int(codecs.encode(flag[:12],'hex'),16)
x2 = int(codecs.encode(flag[12:],'hex'),16)
X = (x1,x2)
k = randrange(1, n-1)
y0 = k*generator_384
KPoint = k*PubKey
Y = (X[0] * KPoint.x() % _p, X[1]*KPoint.y() % _p)

密文就是
Y=({},{})
y0=({},{})


""".format(Y[0],Y[1],y0.x()%_p,y0.y()%_p)

fd = open("ECC.enc",'wt',encoding='utf-8')
fd.write(text)
fd.close()


C = d*y0
x0 = (Y[0]*numbertheory.inverse_mod(C.x(), _p))%_p
x1 = Y[1]*numbertheory.inverse_mod(C.y(), _p)%_p
print(codecs.decode(hex(x0)[2:], 'hex')+codecs.decode(hex(x1)[2:], 'hex'))
# print(hex(x0)[:2], hex(x1))