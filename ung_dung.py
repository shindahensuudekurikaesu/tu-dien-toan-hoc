import math
import random

def du_bao_thoi_tiet_luong_giac(t):
    """
    Ứng dụng: Hàm số lượng giác (Chương 1).
    Mô phỏng nhiệt độ trong ngày theo hàm sin: T(t) = A*sin(B(t-C)) + D
    """
    nhiet_do = 5 * math.sin((math.pi / 12) * (t - 6)) + 27
    return round(nhiet_do, 1)

def ke_hoach_tiet_kiem_csc(u1, d, n):
    """
    Ứng dụng: Cấp số cộng (Chương 2).
    Tính tổng số tiền sau n tháng và số tiền tháng cuối.
    """
    tong_tien = (n / 2) * (2 * u1 + (n - 1) * d)
    un = u1 + (n - 1) * d 
    return {"tong": tong_tien, "thang_cuoi": un}

def mo_phong_xac_suat_lo_to(so_chon, so_luong_ve=1000):
    """
    Ứng dụng: Xác suất (Chương 5).
    Mô phỏng thực nghiệm rút thăm ngẫu nhiên.
    """
    thang_loi = 0
    for _ in range(so_luong_ve):
        ket_qua = random.randint(1, 100) 
        if ket_qua == so_chon:
            thang_loi += 1
    
    xac_suat_thuc_nghiem = (thang_loi / so_luong_ve) * 100
    return f"{xac_suat_thuc_nghiem}%"
