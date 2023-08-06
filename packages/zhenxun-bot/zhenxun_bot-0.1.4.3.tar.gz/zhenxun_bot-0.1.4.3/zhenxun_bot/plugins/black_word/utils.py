from utils.utils import cn2py, get_bot
from configs.path_config import DATA_PATH
from typing import Optional, Union
from .model import BlackWord
from configs.config import Config
from pathlib import Path
from services.log import logger
from models.ban_user import BanUser
from nonebot.adapters.onebot.v11.exception import ActionFailed
from models.group_member_info import GroupInfoUser
from utils.http_utils import AsyncHttpx
import random

try:
    import ujson as json
except ModuleNotFoundError:
    import json


class BlackWordManager:

    """
    敏感词管理
    """

    def __init__(self, file: Optional[Path]):
        self._word_list = {
            "1": [],
            "2": [],
            "3": [],
            "4": ["sb", "nmsl", "mdzz", "2b", "jb", "操", "废物", "憨憨", "cnm", "rnm"],
            "5": [],
        }
        self._py_list = {
            "1": [],
            "2": [],
            "3": [],
            "4": [
                "shabi",
                "wocaonima",
                "sima",
                "sabi",
                "zhizhang",
                "naocan",
                "caonima",
                "simadongxi",
                "simawanyi",
                "hanbi",
                "hanpi",
                "laji",
            ],
            "5": [],
        }
        file.parent.mkdir(parents=True, exist_ok=True)
        # if file.exists():
        #     # 清空默认配置
        #     with open(file, "r", encoding="utf8") as f:
        #         self._word_list = json.load(f)
        #     for i in self._word_list:
        #         for word in self._word_list[i]:
        #             if word.startswith("*py*"):
        #                 self._word_list[i].remove(word)
        #                 if word[4:].strip():
        #                     self._py_list[i].append(word[4:])
        # else:
        #     with open(file, "w", encoding="utf8") as f:
        #         json.dump(
        #             self._word_list,
        #             f,
        #             ensure_ascii=False,
        #             indent=4,
        #         )

    async def check(
        self, user_id: int, group_id: Optional[int], message: str
    ) -> Optional[Union[str, bool]]:
        """
        检查是否包含黑名单词汇
        :param user_id: 用户id
        :param group_id: 群号
        :param message: 消息
        """
        if self._word_list or self._py_list:
            if data := self._check(message):
                if data[0]:
                    await _add_user_black_word(
                        user_id, group_id, data[0], message, int(data[1])
                    )
                    return True
            if Config.get_config(
                "black_word", "ALAPI_CHECK_FLAG"
            ) and not await check_text(message):
                await send_msg(
                    0, None, f"USER {user_id} GROUP {group_id} ALAPI 疑似检测：{message}"
                )
        return False

    def _check(self, message: str) -> "Optional[str], int":
        """
        检测文本是否违规
        :param message: 检测消息
        """
        # 移除空格
        message = message.replace(" ", "").strip()
        py_msg = cn2py(message).lower()
        for x in [self._word_list, self._py_list]:
            for level in x:
                if message in x[level] or py_msg in x[level]:
                    return message if message in x[level] else py_msg, level
        for x in [self._word_list, self._py_list]:
            for level in x:
                for m in x[level]:
                    if m in message or m in py_msg:
                        return m, -1
        return None, 0


async def _add_user_black_word(
    user_id: int,
    group_id: Optional[int],
    black_word: str,
    message: str,
    punish_level: int,
):
    """

    :param user_id: 用户id
    :param group_id: 群号
    :param black_word: 触发的黑名单词汇
    :param message: 原始文本
    :param punish_level: 惩罚等级
    """
    cycle_days = Config.get_config("black_word", "CYCLE_DAYS")
    cycle_days = cycle_days if cycle_days else 7
    user_count = await BlackWord.get_user_count(user_id, cycle_days, punish_level)
    # 周期内超过次数直接提升惩罚
    if Config.get_config(
        "black_word", "AUTO_ADD_PUNISH_LEVEL"
    ) and user_count > Config.get_config("black_word", "ADD_PUNISH_LEVEL_TO_COUNT"):
        punish_level -= 1
    await BlackWord.add_user_black_word(
        user_id, group_id, black_word, message, punish_level
    )
    logger.info(
        f"已将 USER {user_id} GROUP {group_id} 添加至黑名单词汇记录 Black_word：{black_word} Plant_text：{message}"
    )
    # 自动惩罚
    if Config.get_config("black_word", "AUTO_PUNISH") and punish_level != -1:
        await _punish_handle(user_id, group_id, punish_level, black_word)


async def _punish_handle(
    user_id: int, group_id: Optional[int], punish_level: int, black_word: str
):
    """
    惩罚措施，级别越低惩罚越严
    :param user_id: 用户id
    :param group_id: 群号
    :param black_word: 触发的黑名单词汇
    """
    logger.info(f"BlackWord USER {user_id} 触发 {punish_level} 级惩罚...")
    # 周期天数
    cycle_days = Config.get_config("black_word", "CYCLE_DAYS")
    cycle_days = cycle_days if cycle_days else 7
    # 用户周期内触发punish_level级惩罚的次数
    user_count = await BlackWord.get_user_count(user_id, cycle_days, punish_level)
    # 容忍次数：List[int]
    tolerate_count = Config.get_config("black_word", "TOLERATE_COUNT")
    if not tolerate_count or len(tolerate_count) < 5:
        tolerate_count = [5, 2, 2, 2, 2]
    if punish_level == 1 and user_count > tolerate_count[punish_level - 1]:
        # 永久ban
        await _get_punish(1, user_id, group_id)
        # 删除好友
        await _get_punish(2, user_id, group_id)
        # 退出所在所有群聊
        await _get_punish(3, user_id, group_id)
        await BlackWord.set_user_punish(user_id, "永久ban 删除好友 退出所在所有群聊", black_word)
    elif punish_level == 2 and user_count > tolerate_count[punish_level - 1]:
        # 永久ban
        await _get_punish(1, user_id, group_id)
        # 删除好友
        await _get_punish(2, user_id, group_id)
        await BlackWord.set_user_punish(user_id, "永久ban 删除好友", black_word)
    elif punish_level == 3 and user_count > tolerate_count[punish_level - 1]:
        # 永久ban
        await _get_punish(1, user_id, group_id)
        await BlackWord.set_user_punish(user_id, "永久ban", black_word)
    elif punish_level == 4 and user_count > tolerate_count[punish_level - 1]:
        # ban指定时长
        ban_time = await _get_punish(4, user_id, group_id)
        await BlackWord.set_user_punish(user_id, f"ban {ban_time}分钟", black_word)
    elif punish_level == 5 and user_count > tolerate_count[punish_level - 1]:
        # 口头警告
        warning_result = await _get_punish(5, user_id, group_id)
        await BlackWord.set_user_punish(user_id, f"口头警告：{warning_result}", black_word)
    await send_msg(
        user_id,
        group_id,
        f"BlackWordChecker：该条发言已被记录，目前你在{cycle_days}天内的发表{punish_level}"
        f"言论记录次数为：{user_count}次，请注意你的发言\n"
        f"* 如果你不清楚惩罚机制，请发送“惩罚机制” *",
    )


async def _get_punish(
    id_: int, user_id: int, group_id: Optional[int] = None
) -> Optional[Union[int, str]]:
    """
    通过id_获取惩罚
    :param id_: id
    :param user_id: 用户id
    :param group_id: 群号
    """
    bot = get_bot()
    # 忽略的群聊
    _ignore_group = Config.get_config("black_word", "IGNORE_GROUP")
    # 处罚 id 4 ban 时间：int，List[int]
    ban_duration = Config.get_config("black_word", "BAN_DURATION")
    # 口头警告内容
    warning_result = Config.get_config("black_word", "WARNING_RESULT")
    # 永久ban
    if id_ == 1:
        if str(user_id) not in bot.config.superusers:
            await BanUser.ban(user_id, 10, 99999999)
            await send_msg(user_id, group_id, f"BlackWordChecker 永久ban USER {user_id}")
            logger.info(f"BlackWord 永久封禁 USER {user_id}...")
    # 删除好友
    elif id_ == 2:
        if str(user_id) not in bot.config.superusers:
            try:
                await bot.delete_friend(user_id=user_id)
                await send_msg(
                    user_id, group_id, f"BlackWordChecker 删除好友 USER {user_id}"
                )
                logger.info(f"BlackWord 删除好友 {user_id}...")
            except ActionFailed:
                pass
    # 退出所有所在群聊
    elif id_ == 3:
        for g in await GroupInfoUser.get_user_all_group(user_id):
            if g not in _ignore_group:
                try:
                    await send_msg(
                        user_id, g, f"BlackWordChecker 因用户 USER {user_id} 触发惩罚退出该群"
                    )
                    await bot.set_group_leave(group_id=g)
                    logger.info(f"BlackWord 退出 USER {user_id} 所在群聊：{g}...")
                except ActionFailed:
                    pass
    # 封禁用户指定时间
    elif id_ == 4:
        # if str(user_id) not in bot.config.superusers:
        if isinstance(ban_duration, list):
            ban_duration = random.randint(ban_duration[0], ban_duration[1])
        await BanUser.ban(user_id, 9, ban_duration * 60)
        await send_msg(
            user_id,
            group_id,
            f"BlackWordChecker 对用户 USER {user_id} 进行封禁 {ban_duration} 分钟处罚。",
        )
        logger.info(f"BlackWord 封禁 USER {user_id} {ban_duration}分钟...")
        return ban_duration
    # 口头警告
    elif id_ == 5:
        if group_id:
            await bot.send_group_msg(group_id=group_id, message=warning_result)
        else:
            await bot.send_private_msg(user_id=user_id, message=warning_result)
        logger.info(f"BlackWord 口头警告 USER {user_id}")
        return warning_result
    return None


async def send_msg(user_id: int, group_id: Optional[int], message: str):
    """
    发送消息
    :param user_id: user_id
    :param group_id: group_id
    :param message: message
    """
    bot = get_bot()
    if not user_id:
        user_id = int(list(bot.config.superusers)[0])
    if group_id:
        await bot.send_group_msg(group_id=group_id, message=message)
    else:
        await bot.send_private_msg(user_id=user_id, message=message)


async def check_text(text: str) -> bool:
    """
    ALAPI文本检测，检测输入违规
    :param text: 回复
    """
    if not Config.get_config("alapi", "ALAPI_TOKEN"):
        return True
    params = {"token": Config.get_config("alapi", "ALAPI_TOKEN"), "text": text}
    try:
        data = (
            await AsyncHttpx.get(
                "https://v2.alapi.cn/api/censor/text", timeout=4, params=params
            )
        ).json()
        if data["code"] == 200:
            return data["data"]["conclusion_type"] == 2
    except Exception as e:
        logger.error(f"检测违规文本错误...{type(e)}：{e}")
    return True


black_word_manager = BlackWordManager(DATA_PATH / "black_word" / "black_word.json")
