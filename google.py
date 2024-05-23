#谷歌小姐練習
import subprocess
from urllib.parse import quote
import os, time

#設定文字
words = '你給我翻譯翻譯，甚麼叫做他媽的驚喜'
#轉成符合URL格式的文字
encode_url = quote(words)
#定義指令

#正常速度
# cmd = [
#     'curl',
#     '-X',
#     'GET',
#     f'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q={encode_url}',
#     '-o',
#     f"./{words}.mp3",
# ]

#加速谷歌小姐
# cmd = [
#      "./ffmpeg/bin/ffmpeg.exe",
#      "-i",
#      f"{words}.mp3",
#      "-filter:a",
#      "atempo=2",
#      "-y",
#      f"./{words}_atempo.mp3",
#  ]

#執行程式
# std_output = subprocess.run(cmd)
# if std_output.returncode == 0:
#     print(f'[{words}]下載成功')
# else:
#     print(f'[{words}]下載失敗')

#多句下載
#自動新增資料夾
if not os.path.exists('mp3'):
    os.makedirs('mp3')
#設定多句
list_words = [
    '你給他翻譯翻譯',
    '甚麼叫做',
    '甚麼他媽的叫做',
    '甚麼他媽的叫做他媽的',
    '驚喜',
]
#把每句都下載成mp3
for index, words in enumerate(list_words):
    encode_url = quote(words)

    cmd = [
    'curl',
    '-X',
    'GET',
    f'https://translate.google.com/translate_tts?ie=UTF-8&client=tw-ob&tl=zh-TW&q={encode_url}',
    '-o',
    f"./mp3/{index}.mp3",
    ]

    std_output = subprocess.run(cmd)
    if std_output.returncode == 0:
        print(f'[{index}]下載成功')
    else:
        print(f'[{index}]下載失敗')

    cmd = [
     "./ffmpeg/bin/ffmpeg.exe",
     "-i",
     f"./mp3/{index}.mp3",
     "-filter:a",
     "atempo=2",
     "-y",
     f"./mp3/{index}_atempo.mp3",
    ]
    std_output = subprocess.run(cmd)
    if std_output.returncode == 0:
        print(f'[{index}]轉換成功')
    else:
        print(f'[{index}]轉換失敗')
