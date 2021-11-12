from py_rete.common import V
from py_rete.conditions import Cond
from py_rete.conditions import Filter
from py_rete.fact import Fact
from py_rete.network import ReteNetwork
from py_rete.production import Production


def reteBangCap(soBuoiDay=15, bangCap="Thạc sĩ", chucVu="Giảng viên", buoiThem=0):
    net = ReteNetwork()
    c_soBuoiDay = Cond('f-0', 'soBuoiDay', V('x'))
    c_bangCap = Cond('f-1', 'bangCap', V('e'))


    c_hang1 = Cond('f-3', 'hang', 'hang1')
    c_hang2 = Cond('f-3', 'hang', 'hang2')
    c_hang3 = Cond('f-2', 'hang', 'hang1')
    c_hang4 = Cond('f-2', 'hang', 'hang2')

    c_giangVien = Cond('f-2', 'chucVu', 'Giảng viên')
    c_tienSi = Cond('f-2', 'chucVu', 'Giáo sư')

    f0 = Filter(lambda x: x >= 15)
    f1 = Filter(lambda x: x < 20)
    f2 = Filter(lambda x: x >= 20)

    f3 = Filter(lambda e: e == "Cử nhân")
    f4 = Filter(lambda e: e == "Thạc sĩ")

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

    @Production(c_bangCap & f3)
    def p2(net):
        # f['hang'] = 'hang1'
        # f['buoiThem'] += 10
        net.update_fact(f)
        print("Cử nhân")

    @Production(c_bangCap & f4)
    def p32(net):
        f['buoiThem'] += 10
        net.update_fact(f)
        print("Thạc sĩ")




    @Production(c_hang3 & c_giangVien)
    def p4(net):
        f['buoiThem'] += 10
        net.update_fact(f)
        print("Giảng viên Thuộc hạng 1")

    @Production(c_hang4 & c_giangVien)
    def p5(net):
        f['buoiThem'] += 10
        net.update_fact(f)
        print("Giảng viên Thuộc hạng 2")

    net.add_production(p0)
    net.add_production(p1)
    net.add_production(p2)
    net.add_production(p32)
    # net.add_production(p4)
    # net.add_production(p5)

    f = Fact(soBuoiDay=soBuoiDay, bangCap=bangCap, chucVu=chucVu, buoiThem=buoiThem)
    net.add_fact(f)
    am0 = net.build_or_share_alpha_memory(c_soBuoiDay)
    net.run(3)
    return f


reteBangCap()
