math_db = {

    "Euclid": {
        "achievement": "Cha đẻ của hình học, viết cuốn Elements.",
        "fun_fact": "Sách Elements được dùng hơn 2000 năm."
    },

    "Pythagoras": {
        "achievement": "Định lý Pythagoras trong tam giác vuông.",
        "fun_fact": "Ông tin rằng mọi thứ đều liên quan đến số."
    },

    "Archimedes": {
        "achievement": "Phát hiện nguyên lý Archimedes về lực đẩy.",
        "fun_fact": "Ông hét 'Eureka!' khi phát hiện ra nguyên lý."
    },

    "Isaac Newton": {
        "achievement": "Phát minh giải tích và định luật chuyển động.",
        "fun_fact": "Ông làm nhiều khám phá trong thời gian cách ly dịch bệnh."
    },

    "Gottfried Wilhelm Leibniz": {
        "achievement": "Đồng phát minh giải tích.",
        "fun_fact": "Ông tạo ra ký hiệu tích phân ∫."
    },

    "Leonhard Euler": {
        "achievement": "Giới thiệu ký hiệu e, f(x), π.",
        "fun_fact": "Ông viết hơn 800 cuốn sách và bài báo."
    },

    "Carl Friedrich Gauss": {
        "achievement": "Được gọi là Hoàng tử Toán học.",
        "fun_fact": "Ông giải bài toán tổng từ 1 đến 100 khi mới 7 tuổi."
    },

    "Bernhard Riemann": {
        "achievement": "Đặt nền móng cho hình học hiện đại.",
        "fun_fact": "Giả thuyết Riemann vẫn chưa được chứng minh."
    },

    "Joseph Fourier": {
        "achievement": "Phát triển chuỗi Fourier.",
        "fun_fact": "Công trình của ông dùng trong xử lý tín hiệu."
    },

    "Pierre-Simon Laplace": {
        "achievement": "Đóng góp lớn cho xác suất và thiên văn học.",
        "fun_fact": "Ông được gọi là Newton của Pháp."
    },

    "Blaise Pascal": {
        "achievement": "Đóng góp cho xác suất và tam giác Pascal.",
        "fun_fact": "Ông cũng phát minh máy tính cơ học."
    },

    "Alan Turing": {
        "achievement": "Cha đẻ của khoa học máy tính.",
        "fun_fact": "Ông giúp giải mã Enigma trong Thế chiến II."
    },

    "John von Neumann": {
        "achievement": "Đóng góp cho máy tính và lý thuyết trò chơi.",
        "fun_fact": "Ông có trí nhớ gần như hoàn hảo."
    },

    "Andrew Wiles": {
        "achievement": "Chứng minh định lý Fermat cuối cùng.",
        "fun_fact": "Ông làm việc bí mật trong 7 năm."
    },

    "Terence Tao": {
        "achievement": "Một trong những nhà toán học vĩ đại hiện nay.",
        "fun_fact": "Ông là giáo sư khi mới 24 tuổi."
    },

    "Emmy Noether": {
        "achievement": "Đóng góp quan trọng cho đại số trừu tượng.",
        "fun_fact": "Einstein gọi bà là thiên tài toán học."
    }

}

# Hàm tìm kiếm
def search_mathematician(name):
    if name in math_db:
        print("\nTên:", name)
        print("Thành tựu:", math_db[name]["achievement"])
        print("Fun fact:", math_db[name]["fun_fact"])
    else:
        print("Không tìm thấy.")

# Menu
def nthnt():
  while True:
      print("\n===== DATABASE NHÀ TOÁN HỌC =====")
      print("1. Tìm nhà toán học")
      print("2. Xem danh sách")
      print("3. Thoát")

      choice = input("Chọn: ")

      if choice == "1":
          name = input("Nhập tên: ")
          search_mathematician(name)

      elif choice == "2":
          print("\nDanh sách:")
          for name in math_db:
              print("-", name)

      elif choice == "3":
          break