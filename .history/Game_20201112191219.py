


def fight():
    m_hp = 1000
    m_power = 100
    d_hp = 1200
    d_power = 200

    while True:
        m_hp = m_hp - d_power
        d_hp = d_hp - m_power
        print(m_hp)
        if m_hp <= 0:
            print("我输了")
            break
        elif d_hp <=0:
            print("我赢了")
            break
        elif:
            print("平局")
            break

fight()
# print("我赢了") if m_hp > d_hp else print("我输了")



