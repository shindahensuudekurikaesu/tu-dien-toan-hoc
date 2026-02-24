import math
import random

class Toan11ThucTien:
    """
    Module ứng dụng các thuật toán trọng tâm của chương trình Toán 11.
    """
    @staticmethod
    def du_bao_thoi_tiet_luong_giac(t):
        """
        Ứng dụng: Hàm số lượng giác (Chương 1).
        Mô phỏng nhiệt độ trong ngày theo hàm sin: T(t) = A*sin(B(t-C)) + D
        """
        nhiet_do = 5 * math.sin((math.pi / 12) * (t - 6)) + 27
        return round(nhiet_do, 1)

    @staticmethod
    def ke_hoach_tiet_kiem_csc(u1, d, n):
        """
        Ứng dụng: Cấp số cộng (Chương 2).
        Bài toán: Mỗi tháng tiết kiệm thêm một khoản cố định d.
        Tính tổng số tiền sau n tháng.
        """
        tong_tien = (n / 2) * (2 * u1 + (n - 1) * d)
        un = u1 + (n - 1) * d 
        return {"tong": tong_tien, "thang_cuoi": un}

    @staticmethod
    def mo_phong_xac_suat_lo_to(so_chon, so_luong_ve=1000):
        """
        Ứng dụng: Xác suất (Chương 5).
        Mô phỏng thực tế việc rút thăm ngẫu nhiên để tính xác suất thực nghiệm.
        """
        thang_loi = 0
        for _ in range(so_luong_ve):
            ket_qua = random.randint(1, 100) 
            if ket_qua == so_chon:
                thang_loi += 1
        
        xac_suat_thuc_nghiem = (thang_loi / so_luong_ve) * 100
        return f"{xac_suat_thuc_nghiem}%"

if __name__ == "__main__":
    toan = Toan11ThucTien()

    print("--- 1. ỨNG DỤNG LƯỢNG GIÁC ---")
    gio = 14
    print(f"Nhiệt độ dự báo lúc {gio}h chiều: {toan.du_bao_thoi_tiet_luong_giac(gio)}°C")

    print("\n--- 2. ỨNG DỤNG CẤP SỐ CỘNG ---")
  
    kq_tk = toan.ke_hoach_tiet_kiem_csc(1000000, 200000, 12)
    print(f"Tổng tiền tiết kiệm sau 1 năm: {kq_tk['tong']:,} VNĐ")
    print(f"Tháng cuối cùng bạn phải gửi vào: {kq_tk['thang_cuoi']:,} VNĐ")

    print("\n--- 3. ỨNG DỤNG XÁC SUẤT ---")
    so_may_man = 68
    print(f"Xác suất trúng giải khi thử 1000 lần với số {so_may_man}: {toan.mo_phong_xac_suat_lo_to(so_may_man)}")
