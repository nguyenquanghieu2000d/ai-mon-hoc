from bangCap import reteBangCap
from chucVu import reteChucVu
from khoa import reteKhoa

HE_SO_LUONG = 300000


def tinhNamKinhNghiem(namKinhNghiem, luong): 
    if namKinhNghiem >= 3:
        luong += (10 * HE_SO_LUONG)
    luong += (namKinhNghiem * 3 * HE_SO_LUONG)
    return luong

def tinhluong(phiGuiXe, thuongThem, chucVu, khoa, namKinhNghiem, thoiGianLamViec, bangCap, soBuoiDay):
    f = dict()
    f['buoiThem'] = 0
    if(bangCap != "0"): 
        print("Có bằng cấp")
        f = reteBangCap(soBuoiDay, bangCap)
        print(f)
    if(chucVu != "0"): 
        print("Có chức vụ")
        f = reteChucVu(soBuoiDay, chucVu, f['buoiThem'])
        print("chucVu" + str(f))

    if(khoa != "0"): 
        f = reteKhoa(soBuoiDay, khoa, f['buoiThem'])
        print(f)
    luong = HE_SO_LUONG * soBuoiDay + HE_SO_LUONG * f['buoiThem']
    
    # Thưởng năm kinh nghiệm
    if(namKinhNghiem != "0"): luong = tinhNamKinhNghiem(namKinhNghiem, luong)

    
    # Thưởng năm cống hiến
    luong += 0.05 * soBuoiDay * HE_SO_LUONG

    # Thưởng phí gửi xe
    luong += phiGuiXe

    # Thưởng thêm
    luong += thuongThem

    return luong
