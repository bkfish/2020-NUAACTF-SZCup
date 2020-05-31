这个题目的加密算法其实是老算法`Menezes-Vanstone cryptosystem`

### 解析椭圆曲线
首先，要能够成功用openssl解析证书，才能够知道这个椭圆曲线的参数。解析的指令为:
```
openssl ec -in p384-key.pem -text
```
输出的内容为:
```
Private-Key: (384 bit)
priv:
    e0:5b:05:a4:d6:c3:36:fb:a9:34:6a:64:93:2f:14:
    5a:4c:89:d6:41:a0:7a:4c:dd:a1:85:da:ed:a7:94:
    3f:a0:dc:c2:42:88:20:cc:7f:f7:64:4d:81:79:17:
    eb:ca:ce
pub:
    04:86:25:db:50:57:80:51:60:3a:33:67:9d:dc:3a:
    47:25:8f:38:55:3f:22:84:0d:70:76:a2:f8:e2:02:
    96:da:56:88:6a:7e:2e:24:0f:cf:0b:57:75:f4:74:
    ca:0b:06:90:b0:41:c4:46:ff:ef:03:ae:4b:3e:62:
    2f:5b:99:64:9a:26:41:72:e7:df:a8:5b:5c:e8:74:
    68:ac:43:6e:67:9f:31:a7:92:ae:88:30:41:4e:81:
    51:5d:dc:61:db:c7:08
Field Type: prime-field
Prime:
    00:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:
    ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:
    ff:ff:fe:ff:ff:ff:ff:00:00:00:00:00:00:00:00:
    ff:ff:ff:ff
A:
    00:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:
    ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:
    ff:ff:fe:ff:ff:ff:ff:00:00:00:00:00:00:00:00:
    ff:ff:ff:fc
B:
    00:b3:31:2f:a7:e2:3e:e7:e4:98:8e:05:6b:e3:f8:
    2d:19:18:1d:9c:6e:fe:81:41:12:03:14:08:8f:50:
    13:87:5a:c6:56:39:8d:8a:2e:d1:9d:2a:85:c8:ed:
    d3:ec:2a:ef
Generator (uncompressed):
    04:aa:87:ca:22:be:8b:05:37:8e:b1:c7:1e:f3:20:
    ad:74:6e:1d:3b:62:8b:a7:9b:98:59:f7:41:e0:82:
    54:2a:38:55:02:f2:5d:bf:55:29:6c:3a:54:5e:38:
    72:76:0a:b7:36:17:de:4a:96:26:2c:6f:5d:9e:98:
    bf:92:92:dc:29:f8:f4:1d:bd:28:9a:14:7c:e9:da:
    31:13:b5:f0:b8:c0:0a:60:b1:ce:1d:7e:81:9d:7a:
    43:1d:7c:90:ea:0e:5f
Order:
    00:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:
    ff:ff:ff:ff:ff:ff:ff:ff:ff:ff:c7:63:4d:81:f4:
    37:2d:df:58:1a:0d:b2:48:b0:a7:7a:ec:ec:19:6a:
    cc:c5:29:73
Cofactor:  1 (0x1)
Seed:
    a3:35:92:6a:a3:19:a2:7a:1d:00:89:6a:67:73:a4:
    82:7a:cd:ac:73
```
这里可以知道，priv的值为`0xe05b05a4d6c336fba9346a64932f145a4c89d641a07a4cdda185daeda7943fa0dcc2428820cc7ff7644d817917ebcace`，pubkey的开头值为`04`，表示之后的84个数字从中间分成两份，分别表示公钥中的两个点。这里我们能够知道生成元为
```
G(0xAA87CA22BE8B05378EB1C71EF320AD746E1D3B628BA79B9859F741E082542A385502F25DBF55296C3A545E3872760AB7,0x3617DE4A96262C6F5D9E98BF9292DC29F8F41DBD289A147CE9DA3113B5F0B8C00A60B1CE1D7E819D7A431D7C90EA0E5F)
```
然后可以直接用椭圆曲线的公式:
```
Pubkey=G*PrivKey
```
算出来。

### Menezes-Vanstone 加密
其实这里使用的就是`Menezes-Vanstone`加密算法。如果能够在网上搜到的话应该可以找到更加相信的数学说明。（PS：密码学的课本上也有这个算法）

看到给出的加密公式
```
x1 = int(codecs.encode(flag[:12],'hex'),16)
x2 = int(codecs.encode(flag[12:],'hex'),16)
X = (x1,x2)
k = randrange(1, n-1)
y0 = k*generator_384
KPoint = k*PubKey
Y = (X[0] * KPoint.x() % _p, X[1]*KPoint.y() % _p)
```
这里的`y0`和`Y`都是已知的。X是明文，用公式写起来就是
```
y0=(k*Genrator.x, k*Genrator.y)
(Kpoint.x, Kpoint.y)=(Pubkey.x*k, Pubkey.y*k)
Y[0] = X[0]*Kpoint.x mod _p
Y[1] = X[1]*Kpoint.x mod _p
```
这里可以看到公钥参与到了明文的加密中，所以解密肯定时要用到密钥的。但是这里的k是一个随机数，这个随机数并没有公开，要怎么办呢？注意到之前加密中没有参与的y0，可以想到解密的关键就是**利用y0**
```
首先我们知道:
(Kpoint.x, Kpoint.y)=(Pubkey.x*k, Pubkey.y*k)
而
y0 = (k*Genrator.x, k*Genrator.y)
由于此时我们知道密钥PrivKey，则此时有
(Pubkey.x, Pubkey.y) = (Generator.x*Privkey, Generator.y*Privkey)
所以可以得到
(Kpoint.x, Kpoint.y)=(Pubkey.x*k, Pubkey.y*k)    
					=(Generator.x*Privkey*k, Generator.y*Privkey*k)
					=(Generator.x*k, Generator.y*k)*PrivKey
					=y0*PrivKey
```
由上述式子可以得到关键点`Kpoint`，于是就可以避免知道k。那么最后明文的求法就是:
```
X[0] = Y[0]*Kpoint.x^(-1) mod _p
X[1] = Y[1]*Kpoint.y^(-1) mod _p
```
这里`Kpoint.x^(-1)|Kpoint.y^(-1)`表示对应的数值在mod_p下的逆元。

flag：
```
flag{3CC_I3_Use7f1_HaHA}
```