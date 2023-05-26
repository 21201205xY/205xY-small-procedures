import time
import pyperclip
import pyautogui


def copy():
    print('此程序会自动读取你电脑剪切板的内容并模拟键盘输出\n(暂不支持中文模拟输入)')
    with open('settings.txt', 'r', encoding='utf-8') as f:
        f_read = f.readlines()
        for line in f_read:
            ls = line.split(':')
            try:
                _time = eval(ls[1])
            except SyntaxError:
                _time = 0
    for i in range(5):
        print(f'还有{5 - i}秒进行模拟，请将光标移至要复制处')
        time.sleep(0.1)
    paste = pyperclip.paste()
    pyautogui.typewrite(f'{paste}', interval=_time)


if __name__ == '__main__':
    copy()
