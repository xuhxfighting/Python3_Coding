#!/usr/bin/python3
#coding=utf-8
'''
时间限制：1秒

空间限制：32768K
给定一个字符串，请你将字符串重新编码，将连续的字符替换成“连续出现的个数+字符”。比如字符串AAAABCCDAA会被编码成4A1B2C1D2A。

输入描述:

每个测试输入包含1个测试用例
每个测试用例输入只有一行字符串，字符串只包括大写英文字母，长度不超过10000。


输出描述:

输出编码后的字符串


输入例子1:

AAAABCCDAA


输出例子1:

4A1B2C1D2A
'''
var1 = input()
n = len(var1)
num = 1
var2 = ''
if n == 1:
    var2 = str(n) + var1
else:
    for i in range(n-1):
        if var1[i] == var1[i+1]:
            num += 1
            if i == n-2:
                var2 = var2 + str(num) + var1[i]
                #print("%d%s" % (num, var1[i]), end='')
        else:
            var2 = var2 + str(num) + var1[i]
            #print("%d%s" %(num,var1[i]),end='')
            num= 1
            if i == n - 2:
                var2 = var2 + str(num) + var1[i+1]
print(var2)
