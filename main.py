from os import system
from random import uniform, random
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
    为模拟人类行为，进去网页前，随机休眠一段时间。
    :return:
    """
    sleep(uniform(2, 4))
    system('adb shell input swipe {} {} {} {}'.format(random.randint(800, 1000), random.randint(1550, 1650),
                                                      random.randint(800, 1000), random.randint(1150, 1250)))


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


def conference_hall():
    """
    浏览其他分会场
    :return:
    """
    for i in range(4):
        system('adb shell input tap 900 1500')

        bar = tqdm(range(100))
        for item in bar:
            bar.set_description('开始浏览第 {} 个分会场'.format(i))
            sleep(0.25)
        touch_back()
        sleep(uniform(2, 4))


if __name__ == '__main__':
    shop_around()
    main_conference_hall()
    conference_hall()
