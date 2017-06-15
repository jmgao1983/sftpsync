以ubuntu 16.04 为例  
#0.安装paramiko模块
  *pip install --upgrade pip*  
  *pip install paramiko*  
  如果安装失败，可能需要  
  *apt-get install gcc*  
  *apt-get install python-dev*  
  *apt-get install libssl-dev*  
#1.安装openvpn
  *apt-get install openvpn*  
  配置非root用户使用openvpn  
  *chmod u+s /usr/sbin/openvpn*  
  *ln -s /usr/sbin/openvpn /usr/bin/openvpn*  
  准备vpn配置文件 clients.ovpn 放到conf目录  
#2.修改配置文件
  conf目录下修改example_my_env.py文件中各项参数  
  然后重命名  
  *mv example_my_env.py my_env.py*  
#3.运行
  进入程序目录  
  *python start.py*  
#4.定时任务
  修改conf目录下cron_sftpsync文件  
  _30 6 2,17 * * user python /path/start.py > /dev/null 2>&1_  
  修改user为你的系统普通用户  
  修改/path为程序的工作目录  
  *sudo cp cron_sftpsync /etc/cron.d/sftpsync*  
