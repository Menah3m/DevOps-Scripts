#!/bin/bash
# 给定一个包含电话号码列表（一行一个电话号码）的文本文件 file.txt，写一个 bash 脚本输出所有有效的电话号码。

# 你可以假设一个有效的电话号码必须满足以下两种格式： (xxx) xxx-xxxx 或 xxx-xxx-xxxx。（x 表示一个数字）

# 你也可以假设每行前后没有多余的空格字符。

# 示例:

# 假设 file.txt 内容如下：

# 987-123-4567
# 123 456 7890
# (123) 456-7890
# 你的脚本应当输出下列有效的电话号码：

# 987-123-4567
# (123) 456-7890

# 来源：LeetCode
# 链接：https://leetcode-cn.com/problems/valid-phone-numbers



# Read from the file file.txt and output all valid phone numbers to stdout.
#方式1
cat file.txt | gawk --re-interval '/(^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$|^[0-9]{3}-[0-9]{3}-[0-9]{4}$)/{print $0}'

#方式2
gawk --re-interval '/(^\([0-9]{3}\) [0-9]{3}-[0-9]{4}$|^[0-9]{3}-[0-9]{3}-[0-9]{4}$)/{print $0}' file.txt