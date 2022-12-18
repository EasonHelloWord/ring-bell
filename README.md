# 本程序为网课打铃所编写
本程序基于[vb-audiop](https://vb-audio.com/)运行，并仅适用于windows与mac系统
## 程序原理
vb-audiop扬声器广播至麦克风
## 使用方式
### 初始化
前往[vb-audiop](https://vb-audio.com/)下载vb-audiop并安装  
把本程序放入一个文件夹中并在此文件夹下生成data文件夹  
在data中放入上课铃下课铃以及眼保健操铃声（文件格式为wav）  
命名为start.wav end.wav eye.wav  
类似于：  
main
>data  
>>end.wav  
>>start.wav  
>>eye.wav 
> 
>ring-bell.exe  

检查音频设备：您可以在cmd或PowerShell窗口下依次输入
```
pip3 install sounddevice==0.4.5
python
import sounddevice
print(sounddevice.query_devices())
```
随后启动本程序生成config.json文件  
自行更改打铃时间及根据自身需要填写两个扬声器设备  
回到程序按任意键继续即可完成安装  

## 客户端配置
打开腾讯会议，麦克风选择VB-Audio Virtual并保持开启  
打开音频选项，关闭自动降噪（很重要）  
此时自身麦克风讲无法使用（因为腾讯只能同时使用一个麦克风）  
可以通过obs的麦克风侦听进行解决（正好解决了网课录屏录不进自己声音的问题）（方式自行百度）  
到此所有配置都已经结束了  
可以开始美好网课啦