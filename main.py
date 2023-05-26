import time
import pyperclip
import pyautogui


def copy():
    with open('settings.txt', 'r', encoding='utf-8') as f:
        f_read = f.readlines()
        for line in f_read:
            ls = line.split(':')
            try:
                _time = eval(ls[1])
            except:
                _time = 0
    for i in range(5):
        print(f'还有{5 - i}秒进行模拟，请将光标移至要复制处')
        time.sleep(1)
    paste = pyperclip.paste()
    pyautogui.typewrite(f'{paste}', interval=_time)


if __name__ == '__main__':
    print(
        '此程序开源，开源地址：https://github.com/21201205xY/205xY-small-procedures/tree/main\n'
        '此程序会自动读取你电脑剪切板的内容并模拟键盘输出\n'
        '(可在setting中更改单个字符输出间隔，暂不支持中文模拟输入)\n'
        '将要复制内容复制后，输入\'1\'以开始粘贴:'
        , end='')
    flag = eval(input())
    while flag == 1:
        copy()
        flag = 0
