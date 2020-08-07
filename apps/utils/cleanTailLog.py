import re
from apps.utils.redis_zset import RedisZset


def regexLogLine(lineStr: str) -> tuple:
    zset = RedisZset('adcodeRank')
    pattern = re.compile('adcode=(\d+)')
    search = pattern.findall(lineStr)
    if search:
        zset.zincrby(str(search[0]), 1)

    rank = zset.zrevrange(last=10)

    rankPage = [int(value) for key, value in rank]
    nameRanl = [key.decode('utf-8') for key, value in rank]
    return rankPage, nameRanl
