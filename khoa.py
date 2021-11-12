from py_rete.common import V
from py_rete.conditions import Cond
from py_rete.conditions import Filter
from py_rete.fact import Fact
from py_rete.network import ReteNetwork
from py_rete.production import Production


def reteKhoa(soBuoiDay=15, khoa="Công nghệ thông tin", buoiThem=0):
    net = ReteNetwork()
    c_soBuoiDay = Cond('f-0', 'soBuoiDay', V('x'))
    c_hang1 = Cond('f-2', 'hang', 'hang1')
    c_hang2 = Cond('f-2', 'hang', 'hang2')
    c_loaiBangCap = Cond('f-1', 'khoa', V('y'))

    f0 = Filter(lambda x: x >= 15)
    f1 = Filter(lambda x: x < 20)
    f2 = Filter(lambda x: x >= 20)

    f3 = Filter(lambda y: y == "Công nghệ thông tin")
    f4 = Filter(lambda y: y == "Điện tử viễn thông")

    @Production(c_soBuoiDay & f0 & f1)
    def p0(net):
        f['hang'] = 'hang2'
        net.update_fact(f)
        print(str(f['soBuoiDay']) + " Thuộc hạng 2")

    @Production(c_soBuoiDay & f2)
    def p1(net):
        f['hang'] = 'hang1'
        net.update_fact(f)
        print(str(f['soBuoiDay']) + "Thuộc hạng 1")

    @Production(c_loaiBangCap & f3)
    def p2(net):
        if f['hang'] == 'hang1':
            f['buoiThem'] += 3
        else:
            f['buoiThem'] += 2
        net.update_fact(f)
        print(f['khoa'])
        print(1)

    @Production(c_loaiBangCap & f4)
    def p3(net):
        if f['hang'] == 'hang1':
            f['buoiThem'] += 2
        else:
            f['buoiThem'] += 1
        net.update_fact(f)
        print(f['khoa'])
        print(2)

    net.add_production(p0)
    net.add_production(p1)
    net.add_production(p2)
    net.add_production(p3)

    f = Fact(soBuoiDay=soBuoiDay, khoa=khoa, buoiThem=buoiThem)
    net.add_fact(f)
    am0 = net.build_or_share_alpha_memory(c_soBuoiDay)
    net.run(2)
    return f
