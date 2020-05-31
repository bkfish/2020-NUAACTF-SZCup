# wp

进去之后发现先 decode 了一层之后再运行，发现是 base 64 decode。然后将 decode 的东西导出来发现是个 elf 文件，再次逆向发现有一层异或，解开异或就可以了。

``` code
flag{C4n_y0u_f1nd_1t_0n_r4md1sk}
```
