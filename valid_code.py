import os
import random
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

# 生成随机底色 (r,g,b)

def rand_color():
    r=random.randint(0, 255)
    g=random.randint(0, 255)
    b=random.randint(0, 255)
    return r,g,b

# 新建一个120*35的图片，底色随机
def create_picture(width=150,height=35):
    image = Image.new('RGB', (width, height), rand_color())
    return image

def rand_str():
    rand_num=str(random.randint(0,9))# 生成随机数字
    rand_Lower=chr(random.randint(97,122))# 生成随机小写字母
    rand_Upper=chr(random.randint(65,90))#生成随机大写字母
    rand_char=random.choice([rand_num,rand_Lower,rand_Upper])#三者取其一
    return rand_char

def draw_letter(num,image,font_size):
    draw = ImageDraw.Draw(image)
    font_file = os.path.join(os.path.dirname(__file__).replace('\\','/')+"/Courier-New.ttf")
    font = ImageFont.truetype(font_file, size=font_size)
    temp = []
    for i in range(num):
        random_char = rand_str()
        a=random_char
        draw.text((10 + i * 30, -2), a, rand_color(), font=font)
        temp.append(a)

    valid_str= "".join(temp)  # 验证码
    return valid_str,image

def noise(image, width=120, height=35, line_count=3, point_count=20):
    '''

    :param image: 图片对象
    :param width: 图片宽度
    :param height: 图片高度
    :param line_count: 线条数量
    :param point_count: 点的数量
    :return:
    '''
    draw = ImageDraw.Draw(image)
    for i in range(line_count):
        x1 = random.randint(0, width)
        x2 = random.randint(0, width)
        y1 = random.randint(0, height)
        y2 = random.randint(0, height)
        draw.line((x1, y1, x2, y2), fill=rand_color())

        # 画点
        for i in range(point_count):
            draw.point([random.randint(0, width), random.randint(0, height)], fill=rand_color())
            x = random.randint(0, width)
            y = random.randint(0, height)
            draw.arc((x, y, x + 4, y + 4), 0, 90, fill=rand_color())

    return image

def do(name):
    image = create_picture()
    valid_str, image = draw_letter(5, image, 30)
    image = noise(image)
    image.save('C://code/'+str(name)+'.png')
    return valid_str

