from py_rete.common import V
from py_rete.conditions import Cond
from py_rete.conditions import Filter
from py_rete.fact import Fact
from py_rete.network import ReteNetwork
from py_rete.production import Production


def reteChucVu(soBuoiDay=15, chucVu="Giảng viên", buoiThem=0):
    net = ReteNetwork()
    c_soBuoiDay = Cond('f-0', 'soBuoiDay', V('x'))
    c_hang11 = Cond('f-2', 'hang', 'hang1')
    c_hang12 = Cond('f-2', 'hang', 'hang2')
    c_loaiBangCap = Cond('f-1', 'chucVu', V('y'))

    f0 = Filter(lambda x: x >= 15)
    f1 = Filter(lambda x: x < 20)
    f2 = Filter(lambda x: x >= 20)

    f3 = Filter(lambda y: y == "Giảng viên")
    f4 = Filter(lambda y: y == "Phó khoa")
    f5 = Filter(lambda y: y == "Trưởng khoa")

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
            f['buoiThem'] += 5
        else:
            f['buoiThem'] += 2
        net.update_fact(f)
        print(f['chucVu'])
        print(1)

    @Production(c_loaiBangCap & f4)
    def p3(net):
        if f['hang'] == 'hang1':
            f['buoiThem'] += 8
        else:
            f['buoiThem'] += 3
        net.update_fact(f)
        print(f['chucVu'])
        print(2)

    @Production(c_loaiBangCap & f5)
    def p4(net):
        if f['hang'] == 'hang1':
            f['buoiThem'] += 10
        else:
            f['buoiThem'] += 5
        net.update_fact(f)
        print(f['chucVu'])
        print(3)

    net.add_production(p0)
    net.add_production(p1)
    net.add_production(p2)
    net.add_production(p3)
    net.add_production(p4)

    f = Fact(soBuoiDay=soBuoiDay, chucVu=chucVu, buoiThem=buoiThem)
    net.add_fact(f)
    am0 = net.build_or_share_alpha_memory(c_soBuoiDay)
    net.run(2)
    return f
