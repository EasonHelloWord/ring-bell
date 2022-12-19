import sounddevice
import soundfile
import time
import threading
import os,json,sys
def play(files,de):
    print(time.strftime("[%Y-%m-%d %H:%M:%S]",time.localtime(time.time())),end="")
    if files == "data/start.wav":
        print(f'{de}:播放上课铃')
    if files == "data/end.wav":
        print(f'{de}:播放下课铃')
    if files == "data/eye.wav":
        print(f'{de}:播放眼保健操铃声')
    array, smp_rt = soundfile.read(files, dtype = 'float32') 
    sounddevice.play(array,smp_rt,device=de)
    sounddevice.wait()

def seeforclass(start,end,eye,de):
    while True:
        if time.strftime('%H:%M:%S',time.localtime(time.time())) in start:
            play('data/start.wav',de)
        if time.strftime('%H:%M:%S',time.localtime(time.time())) in end:
            play('data/end.wav',de)
        if time.strftime('%H:%M:%S',time.localtime(time.time())) in eye:
            play('data/eye.wav',de)
        time.sleep(0.1)

def seeforme(start,end,eye,de):
    while True:
        if time.strftime('%H:%M:%S',time.localtime(time.time())) in start:
            play('data/start.wav',de)
        if time.strftime('%H:%M:%S',time.localtime(time.time())) in end:
            play('data/end.wav',de)
        if time.strftime('%H:%M:%S',time.localtime(time.time())) in eye:
            play('data/eye.wav',de)
        time.sleep(0.1)


if __name__ =='__main__':
    if not os.path.exists('config.json'):#生成
        basic = {'start':['07:59:03','08:59:03','10:19:03',"12:59:03","13:59:03","14:59:03","15:59:03"],
            'end':['08:45:00',"11:05:00","13:45:00","15:45:00","16:45:00"],
            'eye':["09:45:00",'14:45:00'],
            'de_class':'CABLE Input (VB-Audio Virtual C, MME',
            'de_me':'LG IPS FULLHD (NVIDIA High Defi, MME'}
        json.dump(basic,open('config.json','w'),indent=4)
        time.sleep(0.3)
        print("配置文件生成完毕，请前往'config.json'完成设置~")
        os.system('pause')
    data = json.load(open('config.json','r'))
    start = data['start']
    end = data['end']
    eye = data['eye']
    de_class = data["de_class"]
    de_me=data['de_me']
    t1 = threading.Thread(name='t1',target=seeforclass,args=[start,end,eye,de_class],daemon=True)
    t2 = threading.Thread(name='t2',target=seeforme,args=[start,end,eye,de_me],daemon=True)
    t1.start()
    t2.start()
    while True:
        a = input("1:关闭铃声，2:播放上课铃，3：播放下课铃，4：播放眼保健操铃声\n")
        if a == "1":
            python = sys.executable
            os.execl(python, python, *sys.argv)
        if a == "2":
            t3=threading.Thread(name='t3',target=play,args=['data/start.wav',de_class],daemon=True)
            t4=threading.Thread(name='t4',target=play,args=['data/start.wav',de_me],daemon=True)
            t3.start()
            t4.start()
        if a == "3":
            t5=threading.Thread(name='t5',target=play,args=['data/end.wav',de_class],daemon=True)
            t6=threading.Thread(name='t6',target=play,args=['data/end.wav',de_me],daemon=True)
            t5.start()
            t6.start()
        if a == "4":
            t7=threading.Thread(name='t7',target=play,args=['data/eye.wav',de_class],daemon=True)
            t8=threading.Thread(name='t8',target=play,args=['data/eye.wav',de_me],daemon=True)
            t7.start()
            t8.start()