# UnicodeTransformationIssuesPayload

Unicode Transformation Issues测试的paylaod生成器

# 解决的问题

用于生成AWVS扫描器扫描出来的Unicode Transformation Issues导致xss问题的payload，成功利用可执行javascript和可能可绕过检测

AWVS扫描的情况
![image](https://github.com/c0d1007/UnicodeTransformationIssuesPayload/blob/master/images/3.png)

# 运行情况

直接运行程序，然后输入想要转化的字符串就可生成相应的测试payload。

![image](https://github.com/c0d1007/UnicodeTransformationIssuesPayload/blob/master/images/4.png)

# 测试情况

![image](https://github.com/c0d1007/UnicodeTransformationIssuesPayload/blob/master/images/1.png)

![image](https://github.com/c0d1007/UnicodeTransformationIssuesPayload/blob/master/images/2.jpg)

# 其他

该程序在我看来只是将AWVS扫描出来第一种情况实现了，该类应用可遇不可求呀，其他后续的情况未能再次找到测试的目标，AWVS其他的payload情况未能去测试出来，
有其他方式的生成方式，望告知。
