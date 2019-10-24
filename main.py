from os import system
from random import uniform, randint
from time import sleep

from tqdm import tqdm


def touch_back():
    """
    模拟点击安卓的返回键
    :return:
    """
    system('adb shell input keyevent KEYCODE_BACK')


def swipe():
    """
    模拟滑动
    :return:
    """
    system('adb shell input swipe {} 1600 {} 1200'.format(randint(800, 1000), randint(800, 1000)))


def shop_around():
    """
    逛店铺
    :return:
    """
    for i in range(20):
        system('adb shell input tap 900 1200')
        bar = tqdm(range(100))

        for item in bar:
            bar.set_description('开始逛第 {} 间店铺'.format(i + 1))
            sleep(0.25)

        touch_back()
        sleep(uniform(2, 4))


def main_conference_hall():
    """
    浏览双十一主会场
    :return:
    """
    system('adb shell input tap 900 1350')

    bar = tqdm(range(100))
    for item in bar:
        bar.set_description('开始浏览双十一主会场')
        sleep(0.25)

    touch_back()
    sleep(uniform(2, 4))


def conference_hall():
    """
    浏览其他分会场
    :return:
    """
    for i in range(4):
        system('adb shell input tap 900 1500')

        bar = tqdm(range(100))
        for item in bar:
            bar.set_description('开始浏览第 {} 个分会场'.format(i + 1))
            sleep(0.25)

        touch_back()
        sleep(uniform(2, 4))


def other():
    """
    其他猫币任务
    :return:
    """
    for i in range(2):
        system('adb shell input tap 900 1500')

        bar = tqdm(range(100))
        for item in bar:
            bar.set_description('开始其他猫币任务 {} '.format(i + 1))
            sleep(0.25)

        touch_back()
        sleep(uniform(2, 4))


def farm():
    """
    天猫农场
    :return:
    """
    system('adb shell input tap 900 1650')
    sleep(uniform(2, 4))

    system('adb shell input tap 150 1550')

    bar = tqdm(range(100))
    for item in bar:
        bar.set_description('开始浏览天猫农场')
        sleep(0.40)

    touch_back()
    touch_back()


if __name__ == '__main__':
    shop_around()
    main_conference_hall()
    conference_hall()
    swipe()
    other()
    farm()
