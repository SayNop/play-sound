import os
import time
import pygame
import keyboard


key_audio_config = []


def load_config():
    with open('./config.ini') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('#'):
                continue
            options = line.split(' ')
            if len(options) != 3:
                print(f'该行格式出现问题，无法加载此音乐 {line}')
                continue
            if not os.path.exists('./' + options[1]):
                print(f'该音乐不存在，无法加载此音乐 {line}')
                continue
            key_audio_config.append({
                'key': 'ctrl+' + options[0],
                'file': './' + options[1],
                'desc': options[2]
            })
            print(f'已加载音乐: {options[2]}')


def play_audio(file_path, desc):
    print(f'正在播放： {desc}')
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()


def stop_audio():
    print('停止')
    pygame.mixer.music.stop()


def main():
    pygame.mixer.init()
    print('Developed by Leopold Yang')
    load_config()
    print('加载配置信息完成')

    for item in key_audio_config:
        keyboard.add_hotkey(item['key'], lambda config=item: play_audio(config['file'], config['desc']))

    keyboard.add_hotkey('ctrl+`', stop_audio)

    while True:
        time.sleep(0.2)


main()
