from nonebot.adapters.onebot.v11 import Bot
from utils.image_utils import BuildImage
from services.log import logger
from typing import Optional
from datetime import datetime
from .model import BlackWord


async def show_black_text_list(
    bot: Bot,
    user: Optional[int],
    group_id: Optional[int],
    date: Optional[datetime],
    data_type: str = "=",
) -> BuildImage:
    data = await BlackWord.get_black_data(user, group_id, date, data_type)
    font_w, font_h = BuildImage(0, 0, font_size=20).getsize("正")
    A = BuildImage(1600, len(data) * (font_h + 3), color="#f9f6f2", font_size=20)
    # await A.apaste(BuildImage(0, 0, plain_text="昵称\tUSER_ID\t群号\t文本\t检测\t等级\t日期", font_size=30), (50, 10), True)
    friend_list = await bot.get_friend_list()
    user_name_list = []
    user_id_list = []
    group_id_list = []
    plant_text_list = []
    black_word_list = []
    punish_list = []
    punish_level_list = []
    create_time_list = []
    for x in data:
        try:
            if x.group_id:
                user_name = (
                    await bot.get_group_member_info(
                        group_id=x.group_id, user_id=x.user_qq
                    )
                )["card"]
            else:
                user_name = [
                    u["nickname"] for u in friend_list if u["user_id"] == x.user_qq
                ][0]
        except Exception as e:
            logger.warning(
                f"show_black_text_list 获取 USER {x.user_qq} user_name 失败 {type(e)}：{e}"
            )
            user_name = x.user_qq
        user_name_list.append(user_name)
        user_id_list.append(x.user_qq)
        group_id_list.append(x.group_id)
        plant_text_list.append(" ".join(x.plant_text.split("\n")))
        black_word_list.append(x.black_word)
        punish_list.append(x.punish)
        punish_level_list.append(x.punish_level)
        create_time_list.append(x.create_time.replace(microsecond=0))
    a_cur_w = 10
    max_h = 0
    line_list = []
    for l in [
        user_name_list,
        user_id_list,
        group_id_list,
        plant_text_list,
        black_word_list,
        punish_list,
        punish_level_list,
        create_time_list,
    ]:
        cur_h = 0
        if l == plant_text_list:
            tw = 220
        elif l == create_time_list:
            tw = 290
        else:
            tw = 160
        tmp = BuildImage(tw, len(data) * (font_h + 2), color="#f9f6f2", font_size=20)
        for x in l:
            await tmp.atext((0, cur_h), str(x))
            cur_h += font_h + 2
            if cur_h > max_h:
                max_h = cur_h
        await A.apaste(tmp, (a_cur_w, 10))
        if l == punish_level_list:
            a_cur_w += 90
        elif l == plant_text_list:
            a_cur_w += 250
        else:
            a_cur_w += 175
        if l != create_time_list:
            line_list.append(a_cur_w)
            # await A.aline((a_cur_w-10, 0, a_cur_w-10, A.h), fill=(202, 105, 137), width=3)
    # A.show()
    # return A
    bk = BuildImage(A.w, A.h + 200, color="#f9f6f2", font_size=35)
    cur_h = font_h + 1 + 10
    for _ in range(len(data)):
        await A.aline((0, cur_h, A.w, cur_h), fill=(202, 105, 137), width=1)
        cur_h += font_h + 2
    await bk.apaste(A, (0, 200))
    for lw in line_list[:-1]:
        await bk.aline((lw - 10, 0, lw - 10, A.h + 200), fill=(202, 105, 137), width=3)
    await bk.aline((1200, 0, 1200, A.h + 200), fill=(202, 105, 137), width=3)
    await bk.aline((0, 190, bk.w, 190), fill=(202, 105, 137), width=3)
    await bk.atext((40, 80), "昵称")
    await bk.atext((220, 80), "UID")
    await bk.atext((400, 80), "GID")
    await bk.atext((600, 80), "文本")
    await bk.atext((800, 80), "检测")
    await bk.atext((1000, 80), "惩罚")
    await bk.atext((1128, 80), "等级")
    await bk.atext((1300, 80), "记录日期")
    if bk.w * bk.h > 5000000:
        await bk.aresize(0.7)
    return bk
