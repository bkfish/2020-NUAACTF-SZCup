## medium
首先用ida打开，可能有些人会无从下手。分析一个程序首先要从`main`函数开始，但是可能有些ida会看不到main函数的位置:
![](./img/rev01.png)
main函数的原型为:
```C
int main(int argc, char* argv[], char* env[]){

}
```
这个`argc`和`argv`以及`env`编译器生成的，所以会有一份类似符号的东西存在文件中，可以用这些变量寻找main函数的入口。一般来说，在进行这个变量赋值的位置前后的函数，就是main函数，在这个题目中就是在:
![](./img/rev02.png)
或者，可以用另一个方法来定位`main`函数，也就是使用字符串:
![](./img/rev03.png)
题目点开的时候会出现这几个字符串，可以在ida中找到这几个字符串:
![](./img/rev04.png)
然后就能用交叉引用 （按下x）跳转到main函数中去。

（不过这个题目的主要逻辑其实不在这边，所以找到main函数之后可能还会一头雾水（笑））

在打开ida的时候，应该会注意到这个地方:
![](./img/rev05.png)
如果之前分析过exe的同学会主要，这个地方不只是识别成了一个普通的exe，而是**一个带有.net环境的exe，也就是运行在CLR环境下的代码**，其实也就是用`C#`这类程序写的代码编译出来的二进制文件。
如果这个能够理清逻辑的话，应该会注意到这个函数比较可疑：
![](./img/rev06.png)
然后跟进去，会找到其好像调用了一个函数指针：
```
.data:0040D1BC ; int (__cdecl *dword_40D1BC)(_DWORD)
.data:0040D1BC dword_40D1BC    dd 6000008h             ; DATA XREF: sub_40123B↑r
```
这个`6000008h`其实并不是一个真正的地址，而是C#中的函数metatoken，是C#用于定位函数集中每个函数的一个独一无二的标识符。

然后这个时候我们使用一些可以逆向C#的工具（推荐ilspy），然后找到token为6000008的函数：
```C
// <Module>
internal unsafe static void EncryptStr(char* input)
{
	$ArrayType$$$BY0EF@H $ArrayType$$$BY0EF@H = 45;
	*(ref $ArrayType$$$BY0EF@H + 4) = 15;
	*(ref $ArrayType$$$BY0EF@H + 8) = 67;
	*(ref $ArrayType$$$BY0EF@H + 12) = 61;
	*(ref $ArrayType$$$BY0EF@H + 16) = 8;
	*(ref $ArrayType$$$BY0EF@H + 20) = 68;
	*(ref $ArrayType$$$BY0EF@H + 24) = 9;
	*(ref $ArrayType$$$BY0EF@H + 28) = 39;
	*(ref $ArrayType$$$BY0EF@H + 32) = 60;
	*(ref $ArrayType$$$BY0EF@H + 36) = 2;
	*(ref $ArrayType$$$BY0EF@H + 40) = 56;
	*(ref $ArrayType$$$BY0EF@H + 44) = 63;
	*(ref $ArrayType$$$BY0EF@H + 48) = 36;
	*(ref $ArrayType$$$BY0EF@H + 52) = 38;
	*(ref $ArrayType$$$BY0EF@H + 56) = 28;
	*(ref $ArrayType$$$BY0EF@H + 60) = 29;
	*(ref $ArrayType$$$BY0EF@H + 64) = 57;
	*(ref $ArrayType$$$BY0EF@H + 68) = 50;
	*(ref $ArrayType$$$BY0EF@H + 72) = 1;
	*(ref $ArrayType$$$BY0EF@H + 76) = 0;
	*(ref $ArrayType$$$BY0EF@H + 80) = 51;
	*(ref $ArrayType$$$BY0EF@H + 84) = 52;
	*(ref $ArrayType$$$BY0EF@H + 88) = 17;
	*(ref $ArrayType$$$BY0EF@H + 92) = 3;
	*(ref $ArrayType$$$BY0EF@H + 96) = 26;
	*(ref $ArrayType$$$BY0EF@H + 100) = 21;
	*(ref $ArrayType$$$BY0EF@H + 104) = 40;
	*(ref $ArrayType$$$BY0EF@H + 108) = 11;
	*(ref $ArrayType$$$BY0EF@H + 112) = 37;
	*(ref $ArrayType$$$BY0EF@H + 116) = 16;
	*(ref $ArrayType$$$BY0EF@H + 120) = 31;
	*(ref $ArrayType$$$BY0EF@H + 124) = 22;
	*(ref $ArrayType$$$BY0EF@H + 128) = 32;
	*(ref $ArrayType$$$BY0EF@H + 132) = 19;
	*(ref $ArrayType$$$BY0EF@H + 136) = 33;
	*(ref $ArrayType$$$BY0EF@H + 140) = 4;
	*(ref $ArrayType$$$BY0EF@H + 144) = 66;
	*(ref $ArrayType$$$BY0EF@H + 148) = 53;
	*(ref $ArrayType$$$BY0EF@H + 152) = 65;
	*(ref $ArrayType$$$BY0EF@H + 156) = 25;
	*(ref $ArrayType$$$BY0EF@H + 160) = 41;
	*(ref $ArrayType$$$BY0EF@H + 164) = 44;
	*(ref $ArrayType$$$BY0EF@H + 168) = 20;
	*(ref $ArrayType$$$BY0EF@H + 172) = 7;
	*(ref $ArrayType$$$BY0EF@H + 176) = 12;
	*(ref $ArrayType$$$BY0EF@H + 180) = 18;
	*(ref $ArrayType$$$BY0EF@H + 184) = 64;
	*(ref $ArrayType$$$BY0EF@H + 188) = 30;
	*(ref $ArrayType$$$BY0EF@H + 192) = 49;
	*(ref $ArrayType$$$BY0EF@H + 196) = 58;
	*(ref $ArrayType$$$BY0EF@H + 200) = 10;
	*(ref $ArrayType$$$BY0EF@H + 204) = 62;
	*(ref $ArrayType$$$BY0EF@H + 208) = 24;
	*(ref $ArrayType$$$BY0EF@H + 212) = 43;
	*(ref $ArrayType$$$BY0EF@H + 216) = 48;
	*(ref $ArrayType$$$BY0EF@H + 220) = 46;
	*(ref $ArrayType$$$BY0EF@H + 224) = 6;
	*(ref $ArrayType$$$BY0EF@H + 228) = 47;
	*(ref $ArrayType$$$BY0EF@H + 232) = 13;
	*(ref $ArrayType$$$BY0EF@H + 236) = 35;
	*(ref $ArrayType$$$BY0EF@H + 240) = 42;
	*(ref $ArrayType$$$BY0EF@H + 244) = 14;
	*(ref $ArrayType$$$BY0EF@H + 248) = 59;
	*(ref $ArrayType$$$BY0EF@H + 252) = 23;
	*(ref $ArrayType$$$BY0EF@H + 256) = 27;
	*(ref $ArrayType$$$BY0EF@H + 260) = 34;
	*(ref $ArrayType$$$BY0EF@H + 264) = 54;
	*(ref $ArrayType$$$BY0EF@H + 268) = 55;
	*(ref $ArrayType$$$BY0EF@H + 272) = 5;
	$ArrayType$$$BY0EF@_W $ArrayType$$$BY0EF@_W = 65;
	*(ref $ArrayType$$$BY0EF@_W + 2) = 66;
	*(ref $ArrayType$$$BY0EF@_W + 4) = 67;
	*(ref $ArrayType$$$BY0EF@_W + 6) = 68;
	*(ref $ArrayType$$$BY0EF@_W + 8) = 69;
	*(ref $ArrayType$$$BY0EF@_W + 10) = 70;
	*(ref $ArrayType$$$BY0EF@_W + 12) = 71;
	*(ref $ArrayType$$$BY0EF@_W + 14) = 72;
	*(ref $ArrayType$$$BY0EF@_W + 16) = 73;
	*(ref $ArrayType$$$BY0EF@_W + 18) = 74;
	*(ref $ArrayType$$$BY0EF@_W + 20) = 75;
	*(ref $ArrayType$$$BY0EF@_W + 22) = 76;
	*(ref $ArrayType$$$BY0EF@_W + 24) = 77;
	*(ref $ArrayType$$$BY0EF@_W + 26) = 78;
	*(ref $ArrayType$$$BY0EF@_W + 28) = 79;
	*(ref $ArrayType$$$BY0EF@_W + 30) = 80;
	*(ref $ArrayType$$$BY0EF@_W + 32) = 81;
	*(ref $ArrayType$$$BY0EF@_W + 34) = 82;
	*(ref $ArrayType$$$BY0EF@_W + 36) = 83;
	*(ref $ArrayType$$$BY0EF@_W + 38) = 84;
	*(ref $ArrayType$$$BY0EF@_W + 40) = 85;
	*(ref $ArrayType$$$BY0EF@_W + 42) = 86;
	*(ref $ArrayType$$$BY0EF@_W + 44) = 87;
	*(ref $ArrayType$$$BY0EF@_W + 46) = 88;
	*(ref $ArrayType$$$BY0EF@_W + 48) = 89;
	*(ref $ArrayType$$$BY0EF@_W + 50) = 90;
	*(ref $ArrayType$$$BY0EF@_W + 52) = 97;
	*(ref $ArrayType$$$BY0EF@_W + 54) = 98;
	*(ref $ArrayType$$$BY0EF@_W + 56) = 99;
	*(ref $ArrayType$$$BY0EF@_W + 58) = 100;
	*(ref $ArrayType$$$BY0EF@_W + 60) = 101;
	*(ref $ArrayType$$$BY0EF@_W + 62) = 102;
	*(ref $ArrayType$$$BY0EF@_W + 64) = 103;
	*(ref $ArrayType$$$BY0EF@_W + 66) = 104;
	*(ref $ArrayType$$$BY0EF@_W + 68) = 105;
	*(ref $ArrayType$$$BY0EF@_W + 70) = 106;
	*(ref $ArrayType$$$BY0EF@_W + 72) = 107;
	*(ref $ArrayType$$$BY0EF@_W + 74) = 108;
	*(ref $ArrayType$$$BY0EF@_W + 76) = 109;
	*(ref $ArrayType$$$BY0EF@_W + 78) = 110;
	*(ref $ArrayType$$$BY0EF@_W + 80) = 111;
	*(ref $ArrayType$$$BY0EF@_W + 82) = 112;
	*(ref $ArrayType$$$BY0EF@_W + 84) = 113;
	*(ref $ArrayType$$$BY0EF@_W + 86) = 114;
	*(ref $ArrayType$$$BY0EF@_W + 88) = 115;
	*(ref $ArrayType$$$BY0EF@_W + 90) = 116;
	*(ref $ArrayType$$$BY0EF@_W + 92) = 117;
	*(ref $ArrayType$$$BY0EF@_W + 94) = 118;
	*(ref $ArrayType$$$BY0EF@_W + 96) = 119;
	*(ref $ArrayType$$$BY0EF@_W + 98) = 120;
	*(ref $ArrayType$$$BY0EF@_W + 100) = 121;
	*(ref $ArrayType$$$BY0EF@_W + 102) = 122;
	*(ref $ArrayType$$$BY0EF@_W + 104) = 48;
	*(ref $ArrayType$$$BY0EF@_W + 106) = 49;
	*(ref $ArrayType$$$BY0EF@_W + 108) = 50;
	*(ref $ArrayType$$$BY0EF@_W + 110) = 51;
	*(ref $ArrayType$$$BY0EF@_W + 112) = 52;
	*(ref $ArrayType$$$BY0EF@_W + 114) = 53;
	*(ref $ArrayType$$$BY0EF@_W + 116) = 54;
	*(ref $ArrayType$$$BY0EF@_W + 118) = 55;
	*(ref $ArrayType$$$BY0EF@_W + 120) = 56;
	*(ref $ArrayType$$$BY0EF@_W + 122) = 57;
	*(ref $ArrayType$$$BY0EF@_W + 124) = 92;
	*(ref $ArrayType$$$BY0EF@_W + 126) = 47;
	*(ref $ArrayType$$$BY0EF@_W + 128) = 43;
	*(ref $ArrayType$$$BY0EF@_W + 130) = 45;
	*(ref $ArrayType$$$BY0EF@_W + 132) = 95;
	*(ref $ArrayType$$$BY0EF@_W + 134) = 123;
	*(ref $ArrayType$$$BY0EF@_W + 136) = 125;
	char* ptr = input;
	if (*input != 0)
	{
		do
		{
			ptr++;
		}
		while (*(short*)ptr != 0);
	}
	int num = ptr - input / 2 >> 1;
	string text = null;
	int num2 = 0;
	if (0 < num)
	{
		while (true)
		{
			int num3 = 0;
			while (true)
			{
				$ArrayType$$$BY0EF@_W* ptr2 = &$ArrayType$$$BY0EF@_W;
				do
				{
					ptr2 += 2 / sizeof($ArrayType$$$BY0EF@_W);
				}
				while (*(short*)ptr2 != 0);
				if (num3 >= ptr2 - ref $ArrayType$$$BY0EF@_W / sizeof($ArrayType$$$BY0EF@_W) >> 1)
				{
					goto IL_52F;
				}
				if (*(num2 * 2 + input) == *(num3 * 2 + ref $ArrayType$$$BY0EF@_W))
				{
					goto IL_510;
				}
				num3++;
			}
			IL_53B:
			num2++;
			if (num2 >= num)
			{
				break;
			}
			continue;
			IL_510:
			if (num3 != -1)
			{
				text += (char)(*(*(num3 * 4 + ref $ArrayType$$$BY0EF@H) * 2 + ref $ArrayType$$$BY0EF@_W));
				goto IL_53B;
			}
			IL_52F:
			text += "=";
			goto IL_53B;
		}
	}
	Console.WriteLine(text);
}

```
看起来好长，不过我们可以整理一下，然后观察这个` $ArrayType$$$BY0EF@_W`的赋值规律，大概能猜到是一个**WCHAR**。整理出来如下:
```C
table = [ 45, 15, 67, 61, 8, 68, 9, 39, 60, 2, 56, 63, 36, 38, 28, 29, 57, 50, 1, 0, 51, 52, 17, 3, 26, 21, 40, 11, 37, 16, 31, 22, 32, 19, 33, 4, 66, 53, 65, 25, 41, 44, 20, 7, 12, 18, 64, 30, 49, 58, 10, 62, 24, 43, 48, 46, 6, 47, 13, 35, 42, 14, 59, 23, 27, 34, 54, 55, 5 ]
chars = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,48,49,50,51,52,53,54,55,56,57,92,47,43,45,95,123,125]
```
观察逻辑，发现程序做了一下几个事情：
1. 计算输入的长度
```
char* ptr = input;
	if (*input != 0)
	{
		do
		{
			ptr++;
		}
		while (*(short*)ptr != 0);
	}
```
(之后有多次出现类似的逻辑)
2. 检查input[i] 和 chars[j]是否相等
```
int num3 = 0;
while (true)
{
	$ArrayType$$$BY0EF@_W* ptr2 = &$ArrayType$$$BY0EF@_W;
	do
	{
		ptr2 += 2 / sizeof($ArrayType$$$BY0EF@_W);
	}
	while (*(short*)ptr2 != 0);
	if (num3 >= ptr2 - ref $ArrayType$$$BY0EF@_W / sizeof($ArrayType$$$BY0EF@_W) >> 1)
	{
		goto IL_52F;
	}
	if (*(num2 * 2 + input) == *(num3 * 2 + ref $ArrayType$$$BY0EF@_W))
	{
		goto IL_510;
	}
	num3++;
}
```
3. 如果相等，则此时将table[j]对应的数字index，将字符串char[index]拼接到text上:
```
IL_510:
if (num3 != -1)
{
	text += (char)(*(*(num3 * 4 + ref $ArrayType$$$BY0EF@H) * 2 + ref $ArrayType$$$BY0EF@_W));
	goto IL_53B;
}
```
否则在字符串末尾加上=
```
IL_52F:
			text += "=";
			goto IL_53B;
```

于是可以知道，这就是一个【置换加密】，我们根据上述逻辑，可以写出解密逻辑:
```python
test = "W1og39p2Kp+2_Zpx2{/yF"
tmp = [45, 15, 67, 61, 8, 68, 9, 39, 60, 2, 56, 63, 36, 38, 28, 29, 57, 50, 1, 0, 51, 52, 17, 3, 26, 21, 40, 11, 37, 16, 31, 22, 32, 19, 33, 4, 66, 53, 65, 25, 41, 44, 20, 7, 12, 18, 64, 30, 49, 58, 10, 62, 24, 43, 48, 46, 6, 47, 13, 35, 42, 14, 59, 23, 27, 34, 54, 55, 5]
chars = [65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,97,98,99,100,101,102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,48,49,50,51,52,53,54,55,56,57,92,47,43,45,95,123,125]
for each in test:
    print(chars[tmp.index(chars.find(each))],end='')
```

### 另一条路
其实这个题目是可以直接猜出答案的。因为是【置换加密】，那么每个字符对应的密文就是一定的，所以。。。只需要把所有的密文明文对应关系找出来就好了。。。

### flag
`flag{Do_you_know_CLR}`