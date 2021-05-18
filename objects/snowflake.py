_DISCORD_EPOCH = 1420070400000  # first second of 2015


Snowflake = str


def snowflake_to_timestamp(snowflake: Snowflake) -> int:
    return (int(snowflake) >> 22) + _DISCORD_EPOCH


def timestamp_to_snowflake(timestamp: int) -> Snowflake:
    return Snowflake((timestamp - _DISCORD_EPOCH) << 22)
