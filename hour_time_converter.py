# minute_data、単位は分
minute_data = [30, 155, 180, 74, 11, 60, 82]


# 分を[時, 分]に換算する関数を作成して下さい
def convert_hour_minute(minute):
    hour = int(minute / 60)
    remain = minute % 60
    # within the one line,
    # h_m_data = [h_m_split(x) for x in minute_data]

    # print("hour" + str(int(hour)))
    # print("min" + str(remain))
    return [hour, remain]


# リスト内包表記を用いて所定の配列を作成して下さい
list = [convert_hour_minute(minute) for minute in minute_data]

# 出力して下さい
print(list)

