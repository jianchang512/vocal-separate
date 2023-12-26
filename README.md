[English README](./README_EN.md)  / [Discord](https://discord.gg/TMCM2PfHzQ) / QQ群 902124277

# 音乐人声分离工具

这是一个极简的人声和背景音乐分离工具，本地化网页操作，无需连接外网，使用 2stems/4stems/5stems 模型。

> 
> 将一首歌曲或者含有背景音乐的音视频文件，拖拽到本地网页中，即可将其中的人声和音乐声分离为单独的音频wav文件，可选单独分离“钢琴声”、“贝斯声”、“鼓声”等
> 
> 自动调用本地浏览器打开本地网页，模型已内置，无需连接外网下载。
> 
> 支持视频(mp4/mov/mkv/avi/mpeg)和音频(mp3/wav)格式
> 
> 只需点两下鼠标，一选择音视频文件，二启动处理。
> 


# 视频演示

https://github.com/jianchang512/vocal-separate/assets/3378335/8e6b1b20-70d4-45e3-b106-268888fc0240



![image](./images/1.png)



# 预编译Win版使用方法/Linux和Mac源码部署

1. 右侧[Releases](https://github.com/jianchang512/vocal-separate/releases)中下载预编译文件

2. 下载后解压到某处，比如 E:/vocal-separate

3. 双击 start.exe ，等待自动打开浏览器窗口即可

4. 点击页面中的上传区域，在弹窗中找到想分离的音视频文件，或直接拖拽音频文件到上传区域，然后点击“立即分离”，稍等片刻，底部会显示每个分离文件以及播放控件，点击播放。

5. 如果机器拥有英伟达GPU，并正确配置了CUDA环境，将自动使用CUDA加速


# 源码部署(Linux/Mac/Window)

0. 要求 python 3.9->3.11

1. 创建空目录，比如 E:/vocal-separate, 在这个目录下打开 cmd 窗口，方法是地址栏中输入 `cmd`, 然后回车。

	使用git拉取源码到当前目录 ` git clone git@github.com:jianchang512/vocal-separate.git . `

2. 创建虚拟环境 `python -m venv venv`

3. 激活环境，win下命令 `%cd%/venv/scripts/activate`，linux和Mac下命令 `source ./venv/bin/activate`

4. 安装依赖: `pip install -r requirements.txt`

5. win下解压 ffmpeg.7z，将其中的`ffmpeg.exe`和`ffprobe.exe`放在项目目录下, linux和mac 到 [ffmpeg官网](https://ffmpeg.org/download.html)下载对应版本ffmpeg，解压其中的`ffmpeg`和`ffprobe`二进制程序放到项目根目录下

6. [下载模型压缩包](https://github.com/jianchang512/vocal-separate/releases/download/0.0/models-all.7z)，在项目根目录下的 `pretrained_models` 文件夹中解压，解压后，`pretrained_models`中将有3个文件夹，分别是`2stems`/`3stems`/`5stems`

7. 执行  `python  start.py `，等待自动打开本地浏览器窗口。



# CUDA 加速支持

**安装CUDA工具**

如果你的电脑拥有 Nvidia 显卡，先升级显卡驱动到最新，然后去安装对应的 
   [CUDA Toolkit 11.8](https://developer.nvidia.com/cuda-downloads)  和  [cudnn for CUDA11.X](https://developer.nvidia.com/rdp/cudnn-archive)。
   
   安装完成成，按`Win + R`,输入 `cmd`然后回车，在弹出的窗口中输入`nvcc --version`,确认有版本信息显示，类似该图
   ![image](https://github.com/jianchang512/pyvideotrans/assets/3378335/e68de07f-4bb1-4fc9-bccd-8f841825915a)

   然后继续输入`nvidia-smi`,确认有输出信息，并且能看到cuda版本号，类似该图
   ![image](https://github.com/jianchang512/pyvideotrans/assets/3378335/71f1d7d3-07f9-4579-b310-39284734006b)



# 注意事项

0. 中文音乐或中式乐器，建议选择使用`2stems`模型，其他模型对“钢琴、贝斯、鼓”可单独分离出文件
1. 如果电脑没有NVIDIA显卡或未配置cuda环境，不要选择 4stems和5stems模型，尤其是处理较长时长的音频时, 否则很可能耗尽内存



# 致谢

本项目主要依赖的其他项目

1. https://github.com/deezer/spleeter
2. https://github.com/pallets/flask
3. https://ffmpeg.org/
4. https://layui.dev

