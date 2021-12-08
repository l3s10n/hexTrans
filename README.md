# hexTrans

实现为hex编码的内容添加任意前缀：

```
"0a0b0c" --> "\x0a\x0b\x0c"
"0a0b0c" --> "%0a%0b%0c"
"0a0b0c" --> "\0a\0b\0c"
"0a0b0c" --> "whatever0awhatever0bwhatever0c"
```

你或许可以在使用gopher协议或者将hex编码转化为某个编程语言能识别的hex编码时用到它。

# install

```shell
$ chmod +x install.sh
$ sudo ./install.sh
```

# Usage

```
Usage: hexTrans <hexString> <Separator>

Example: 
        input: hexTrans 'aabbcc' '%'
        output: %aa%bb%cc
```

