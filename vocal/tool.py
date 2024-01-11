import subprocess
import sys
import webbrowser
import requests
import tensorflow
import vocal
from vocal import cfg

def runffmpeg(arg):
    cmd = ["ffmpeg","-hide_banner","-vsync","0","-y"]
    if cfg.cuda>0:
        cmd.extend(["-hwaccel", "cuda","-hwaccel_output_format","cuda"])
    cmd = cmd + arg
    p = subprocess.Popen(cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            creationflags=0 if sys.platform != 'win32' else subprocess.CREATE_NO_WINDOW)
    while True:
        try:
            #等待0.1未结束则异常
            outs, errs = p.communicate(timeout=0.5)
            errs=str(errs)
            if errs:
                errs = errs.replace('\\\\','\\').replace('\r',' ').replace('\n',' ')
                errs=errs[errs.find("Error"):]
            # 成功
            if p.returncode==0:
                return "ok"
            # 失败
            if cfg.cuda:
                errs+="[error] Please try upgrading the graphics card driver and reconfigure CUDA"
            return errs
        except subprocess.TimeoutExpired as e:
            # 如果前台要求停止
            pass
        except Exception as e:
            #出错异常
            errs=f"[error]ffmpeg:error {cmd=},\n{str(e)}"
            return errs
def checkupdate():
    try:
        res=requests.get("https://raw.githubusercontent.com/jianchang512/vocal-separate/main/version.json")
        print(f"{res.status_code=}")
        if res.status_code==200:
            d=res.json()
            print(f"{d=}")
            if d['version_num']>vocal.VERSION:
                cfg.updatetips=f'New version {d["version"]}'
    except Exception as e:
        print(e)


def openweb(web_address):
    webbrowser.open("http://"+web_address)
    print(f"\n{cfg.transobj['lang8']} http://{web_address}")