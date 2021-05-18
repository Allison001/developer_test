
m_hp = 1000
m_power = 500
d_hp = 1200
d_power = 300


while True:

    m_hp = m_hp - d_power
    d_hp = d_hp= m_power

    if m_hp > d_hp:
        print("我赢了")
        br
    elif d_hp > m_hp:
        print("我输了")
    else:
        print("平局")

# print("我赢了") if m_hp > d_hp else print("我输了")



