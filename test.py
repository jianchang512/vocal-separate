from spleeter.separator import Separator
import os
separator = Separator('spleeter:2stems', multiprocess=False)
noextname="1"
dirname=os.path.join("./static/files",noextname)

separator.separate_to_file("./lao59.mp3", destination=dirname, filename_format="{instrument}.{codec}")
a_name = f"{dirname}/{noextname}vocals.wav"