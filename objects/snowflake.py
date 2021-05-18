_DISCORD_EPOCH = 1420070400000  # first second of 2015


def snowflake_to_timestamp(snowflake: str) -> int:
    return (int(snowflake) >> 22) + _DISCORD_EPOCH


def timestamp_to_snowflake(timestamp: int) -> str:
    return str((timestamp - _DISCORD_EPOCH) << 22)
