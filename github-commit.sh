#!/bin/bash
# Author: menah3m
# Date: 2020-08-20 
# Description:往github推送代码

echo "初始化中~"
git pull origin master;
git add -A;
read -p "请输入commit信息，按Enter跳过" commit_info
if [ ! -n "$commit_info" ] ; then
    git commit -m `date +"%F %T"`;
else git commit -m "${commit_info}";
fi;
git push origin master;
echo "推送完成~"