from nonebot import on_notice, NoticeSession, CommandSession
import os
import random
import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from .valid_code import do
import time
import signal
from nonebot import on_command
import os.path

# 处理成员增加
msg=None
code=None
from_id=None
flag=False
@on_notice('group_increase')
async def _(session: NoticeSession):
    global code
    # 欢迎入群
    await session.send('[CQ:at,qq='+str(session.event.user_id)+'] Welcome！')
    code=do(str(session.event.user_id))
    await session.send('[CQ:image,file=file:///C:\\code\\'+str(session.event.user_id)+'.png]')
    await session.send('请输入图中验证码证明你不是机器人\r\n请注意 请按照\"Code\"+图上内容 进行回答（例如 Code 12345）')
    global from_id,flag
    from_id=str(session.event.user_id)
    flag=False

@on_command('验证码', aliases=("Code"),only_to_me=False)
async def _(session: CommandSession):
    global msg,code,flag
    if str(session.event.user_id)==str(from_id):
        if flag==False:
            msg = session.current_arg_text.strip()
            msg=str(msg).lower()
            code=str(code).lower()
            if msg==code:
                await session.send('恭喜你逃过一劫，欢迎来到本群！')
                flag=True
                code=None
            else :
                await session.bot.set_group_kick(user_id=session.event.user_id,group_id=session.event.group_id)
                await session.send("很遗憾，这位朋友被移出了群聊")
                flag=True
                code=None


