tu_dien_chu_de = {
  'Mệnh đề và Tập hợp': {
        'Mệnh đề toán học': {
            'định nghĩa': 'Là một câu khẳng định có tính đúng hoặc sai rõ ràng. Một mệnh đề không thể vừa đúng vừa sai.',
            'kí hiệu': 'P, Q, R',
            'công thức': 'P thuộc {Đúng, Sai}',
            'ví dụ': "P: '15 là số lẻ' là mệnh đề đúng.",
        },
        'Mệnh đề phủ định': {
            'định nghĩa': "Mệnh đề phủ định của P được thiết lập bằng cách thêm hoặc bớt từ 'không' hoặc 'không phải' vào trước vị ngữ của P.",
            'kí hiệu': 'P gạch đầu',
            'công thức': 'P đúng tương đương P gạch đầu sai.',
            'ví dụ': "P gạch đầu: '15 không phải là số lẻ'.",
        },
        'Mệnh đề kéo theo': {
            'định nghĩa': "Dạng 'Nếu P thì Q'. Chỉ sai khi P đúng mà Q sai.",
            'kí hiệu': 'P => Q',
            'công thức': 'P là giả thiết, Q là kết luận.',
            'ví dụ': 'Nếu a chia hết cho 6 thì a chia hết cho 3.',
        },
        'Mệnh đề đảo': {
            'định nghĩa': 'Đảo vị trí của P và Q trong mệnh đề kéo theo.',
            'kí hiệu': 'Q => P',
            'công thức': 'Mệnh đề đảo không nhất thiết đúng khi mệnh đề thuận đúng.',
            'ví dụ': 'Nếu a chia hết cho 3 thì a chia hết cho 6 (Mệnh đề đảo này sai).',
        },
        'Mệnh đề tương đương': {
            'định nghĩa': 'Khi cả hai mệnh đề kéo theo thuận và đảo đều đúng.',
            'kí hiệu': 'P <=> Q',
            'công thức': 'P <=> Q tương đương (P => Q) và (Q => P)',
            'ví dụ': 'Tam giác đều <=> Tam giác có 3 cạnh bằng nhau.',
        },
        'Lượng từ toán học': {
            'định nghĩa': 'Sử dụng kí hiệu với mọi và tồn tại để biểu thị phạm vi của biến.',
            'kí hiệu': 'V (với mọi), E (tồn tại)',
            'công thức': 'Phủ định của (với mọi x thuộc X, P(x)) là (tồn tại x thuộc X, P(x) sai)',
            'ví dụ': 'Với mọi x thuộc R, x^2 + 1 > 0.',
        },
        'Tập hợp': {
            'định nghĩa': 'Một tập hợp bao gồm các đối tượng được gọi là phần tử.',
            'kí hiệu': 'a thuộc A, b không thuộc A',
            'công thức': 'A = {x thuộc X | P(x)}',
            'ví dụ': 'N = {0, 1, 2, 3, ...}',
        },
        'Quan hệ tập hợp': {
            'định nghĩa': 'A là con B nếu mọi phần tử của A đều thuộc B. A bằng B nếu chúng có cùng phần tử.',
            'kí hiệu': 'A con B, A = B',
            'công thức': 'A = B <=> (A con B) và (B con A)',
            'ví dụ': '{1, 2} con {1, 2, 3}',
        },
        'Phép giao': {
            'định nghĩa': 'Gồm các phần tử chung của cả hai tập hợp.',
            'kí hiệu': 'A giao B',
            'công thức': 'A giao B = {x | x thuộc A và x thuộc B}',
            'ví dụ': '[1; 4] giao [3; 5] = [3; 4]',
        },
        'Phép hợp': {
            'định nghĩa': 'Gồm các phần tử thuộc ít nhất một trong hai tập hợp.',
            'kí hiệu': 'A hợp B',
            'công thức': 'A hợp B = {x | x thuộc A hoặc x thuộc B}',
            'ví dụ': '{1, 2} hợp {3, 4} = {1, 2, 3, 4}',
        },
        'Phép hiệu và Phần bù': {
            'định nghĩa': 'Hiệu A \ B là các phần tử thuộc A nhưng không thuộc B. Phần bù dùng khi B là tập con của A.',
            'kí hiệu': 'A \ B, C_A(B)',
            'công thức': 'C_A(B) = {x thuộc A | x không thuộc B} (với B con A)',
            'ví dụ': 'R \ (-vô cùng; 0] = (0; +vô cùng)',
        },
        'Các tập con của số thực': {
            'định nghĩa': 'Biểu diễn các khoảng, đoạn, nửa khoảng trên trục số thực.',
            'kí hiệu': '(a; b), [a; b], [a; b), (a; b]',
            'công thức': '[a; b] = {x thuộc R | a <= x <= b}',
            'ví dụ': 'x thuộc [1; 2] <=> 1 <= x <= 2',
        }
  },
    'Hàm số và Biểu thức Đại số': {
        'Hàm số': {
            'định nghĩa': 'Cho tập hợp khác rỗng D thuộc R. Hàm số f xác định trên D là một quy tắc cho tương ứng mỗi số x thuộc D với duy nhất một số y thuộc R.',
            'kí hiệu': 'y = f(x), x thuộc D',
            'công thức': 'D là tập xác định, x là biến số, y là hàm số.',
            'ví dụ': 'y = căn(x-1) có tập xác định D = [1; +vô cùng).',
        },
        'Sự biến thiên của hàm số': {
            'định nghĩa': 'Hàm số đồng biến (tăng) nếu x tăng thì y tăng. Hàm số nghịch biến (giảm) nếu x tăng thì y giảm.',
            'kí hiệu': 'x1 < x2 suy ra f(x1) < f(x2) (đồng biến)',
            'công thức': '(f(x2) - f(x1)) / (x2 - x1) > 0 suy ra Hàm số đồng biến.',
            'ví dụ': 'y = 2x + 1 đồng biến trên R vì hệ số a = 2 > 0.',
        },
        'Hàm số bậc hai': {
            'định nghĩa': 'Hàm số cho bởi công thức y = ax^2 + bx + c (với a khác 0). Đồ thị là một đường Parabol.',
            'kí hiệu': 'P: y = ax^2 + bx + c',
            'công thức': 'Đỉnh I(-b/2a; -Delta/4a), trục đối xứng x = -b/2a.',
            'ví dụ': 'y = x^2 - 2x + 3 có đỉnh I(1; 2).',
        },
        'Đồ thị hàm số bậc hai': {
            'định nghĩa': 'Bề lõm hướng lên trên nếu a > 0, hướng xuống dưới nếu a < 0.',
            'kí hiệu': 'a > 0: bề lõm quay lên, a < 0: bề lõm quay xuống',
            'công thức': 'Delta = b^2 - 4ac',
            'ví dụ': 'y = -x^2 có bề lõm quay xuống dưới và đỉnh là gốc tọa độ O(0;0).',
        },
        'Dấu của tam thức bậc hai': {
            'định nghĩa': 'Xét dấu của biểu thức f(x) = ax^2 + bx + c dựa vào dấu của a và biệt thức Delta.',
            'kí hiệu': 'f(x) cùng dấu với a khi Delta < 0.',
            'công thức': 'Delta < 0 suy ra a * f(x) > 0 với mọi x thuộc R.',
            'ví dụ': 'x^2 - 4x + 5 > 0 với mọi x thuộc R vì Delta = -4 < 0 và a = 1 > 0.',
        },
        'Bất phương trình bậc hai': {
            'định nghĩa': 'Là bất phương trình có dạng ax^2 + bx + c > 0 (hoặc < 0, <= 0, >= 0) với a khác 0.',
            'kí hiệu': 'ax^2 + bx + c >= 0',
            'công thức': 'Nghiệm dựa trên bảng xét dấu của tam thức bậc hai.',
            'ví dụ': 'x^2 - 3x + 2 < 0 tương đương x thuộc khoảng (1; 2).',
        },
        'Phép tính lũy thừa': {
            'định nghĩa': 'Mở rộng khái niệm lũy thừa từ số mũ nguyên sang số mũ hữu tỉ và số thực.',
            'kí hiệu': 'a^alpha (a là cơ số, alpha là số mũ)',
            'công thức': [
                'a^m * a^n = a^(m+n)',
                'a^m / a^n = a^(m-n)',
                '(a^m)^n = a^(m*n)',
                'căn bậc n của a^m = a^(m/n)'
            ],
            'ví dụ': '8^(2/3) = căn bậc 3 của (8^2) = căn bậc 3 của 64 = 4.',
        },
        'Lôgarit': {
            'định nghĩa': 'Hàm số có dạng y = log_a(x) với cơ số a > 0 và a khác 1.',
            'kí hiệu': 'log_a(b) = alpha tương đương a^alpha = b (với 0 < a khác 1, b > 0)',
            'công thức': [
                'log_a(MN) = log_a(M) + log_a(N)',
                'log_a(M/N) = log_a(M) - log_a(N)',
                'log_a(M^alpha) = alpha * log_a(M)',
                'log_a(b) = log_c(b) / log_c(a) (Công thức đổi cơ số)'
            ],
            'ví dụ': 'log_2(8) = 3 vì 2^3 = 8.',
        },
        'Hàm số mũ': {
            'định nghĩa': 'Hàm số có dạng y = a^x với cơ số a > 0 và a khác 1.',
            'kí hiệu': 'y = a^x',
            'tính_chất': 'Nếu a > 1 hàm đồng biến; nếu 0 < a < 1 hàm nghịch biến. Luôn đi qua điểm (0;1).',
            'ví dụ': 'y = 2^x tăng trưởng rất nhanh khi x tăng.',
        },
        'Hàm số lôgarit': {
            'định nghĩa': 'Hàm số có dạng y = log_a(x) với cơ số a dương và khác 1.',
            'kí hiệu': 'y = log_a(x)',
            'tính_chất': 'Tập xác định D = (0; +vô cùng). Đồ thị đối xứng với hàm số mũ qua đường thẳng y = x.',
            'ví dụ': 'y = ln(x) là lôgarit tự nhiên cơ số e xấp xỉ 2.718.',
        },
        'Phương trình mũ và lôgarit cơ bản': {
            'định nghĩa': 'Giải phương trình tìm x nằm ở vị trí số mũ hoặc trong biểu thức lôgarit.',
            'kí hiệu': 'a^x = b; log_a(x) = b',
            'công thức': [
                'a^x = b tương đương x = log_a(b) (với b > 0)',
                'log_a(x) = b tương đương x = a^b'
            ],
            'ví dụ': '2^x = 5 tương đương x = log_2(5).',
        }
  },
    'Dãy số': {
        'Dãy số': {
            'định nghĩa': 'Là một hàm số xác định trên tập các số tự nhiên.',
            'kí hiệu': '(un)',
            'công thức': 'u: N -> R',
            'ví dụ': 'un = 2n + 1',
        },
        'Cách cho dãy số': {
            'định nghĩa': 'Dãy số có thể cho bằng công thức tổng quát, truy hồi hoặc liệt kê.',
            'kí hiệu': 'un, u(n+1)',
            'công thức': 'u(n+1) = f(un)',
            'ví dụ': 'u1 = 1, u(n+1) = un + 2',
        },
        'Cấp số cộng': {
            'định nghĩa': 'Là dãy số mà hiệu của hai số hạng liên tiếp không đổi.',
            'kí hiệu': '(un), công sai d',
            'công thức': 'un = u1 + (n-1)d',
            'ví dụ': '1, 3, 5, 7, ... (d = 2)',
        },
        'Số hạng tổng quát của cấp số cộng': {
            'định nghĩa': 'Số hạng thứ n được xác định theo công thức tổng quát.',
            'kí hiệu': 'un',
            'công thức': 'un = u1 + (n-1)d',
            'ví dụ': 'u5 = u1 + 4d',
        },
        'Tổng n số hạng đầu của cấp số cộng': {
            'định nghĩa': 'Tổng của n số hạng đầu tiên của cấp số cộng.',
            'kí hiệu': 'Sn',
            'công thức': 'Sn = n * (u1 + un) / 2',
            'ví dụ': 'S5 = 5 * (u1 + u5) / 2',
        },
        'Cấp số nhân': {
            'định nghĩa': 'Là dãy số mà tỉ số của hai số hạng liên tiếp không đổi.',
            'kí hiệu': '(un), công bội q',
            'công thức': 'un = u1 * q^(n-1)',
            'ví dụ': '2, 4, 8, 16, ... (q = 2)',
        },
        'Số hạng tổng quát của cấp số nhân': {
            'định nghĩa': 'Số hạng thứ n được xác định theo công thức tổng quát.',
            'kí hiệu': 'un',
            'công thức': 'un = u1 * q^(n-1)',
            'ví dụ': 'u4 = u1 * q^3',
        },
        'Tổng n số hạng đầu của cấp số nhân (q khác 1)': {
            'định nghĩa': 'Tổng của n số hạng đầu tiên của cấp số nhân khi q khác 1.',
            'kí hiệu': 'Sn',
            'công thức': 'Sn = u1 * (q^n - 1) / (q - 1)',
            'ví dụ': 'S3 = u1 * (q^3 - 1) / (q - 1)',
        }
  },
  'Phương trình và Bất phương trình': {
        'Bất phương trình bậc nhất hai ẩn': {
            'định nghĩa': 'Là bất phương trình có dạng ax + by < c (hoặc >, <=, >=), trong đó a và b không đồng thời bằng 0.',
            'kí hiệu': 'ax + by <= c',
            'công thức': 'a, b, c thuộc R; a^2 + b^2 khác 0',
            'ví dụ': '2x + 3y > 6 là một bất phương trình bậc nhất hai ẩn.',
        },
        'Miền nghiệm của bất phương trình': {
            'định nghĩa': 'Tập hợp các cặp số (x; y) làm cho bất phương trình đúng. Trên mặt phẳng tọa độ, miền nghiệm thường là một nửa mặt phẳng.',
            'kí hiệu': 'S = {(x, y) thuộc R^2 | ax + by < c}',
            'công thức': 'Cách xác định: Vẽ đường thẳng d: ax + by = c, sau đó thử một điểm M không nằm trên d.',
            'ví dụ': 'Miền nghiệm của x + y < 1 là nửa mặt phẳng chứa gốc tọa độ O(0;0) và không bao gồm đường biên.',
        },
        'Hệ bất phương trình bậc nhất hai ẩn': {
            'định nghĩa': 'Gồm hai hay nhiều bất phương trình bậc nhất hai ẩn được xét đồng thời.',
            'kí hiệu': 'Hệ gồm {a1x + b1y <= c1; a2x + b2y <= c2}',
            'công thức': 'Miền nghiệm của hệ là phần giao của các miền nghiệm của từng bất phương trình thành phần.',
            'ví dụ': 'Hệ bất phương trình: {x >= 0, y >= 0, x + y <= 2}',
        },
        'Miền nghiệm của hệ (Đa giác nghiệm)': {
            'định nghĩa': 'Miền nghiệm của hệ thường là một miền đa giác (có thể không giới hạn) trên mặt phẳng tọa độ.',
            'kí hiệu': 'Miền đa giác ABCD',
            'công thức': 'Các đỉnh của đa giác là giao điểm của các đường thẳng biên của hệ.',
            'ví dụ': 'Hệ {x >= 0, y >= 0, x + y <= 1} có miền nghiệm là tam giác vuông OAB.',
        },
        'Bài toán tối ưu (Quy hoạch tuyến tính)': {
            'định nghĩa': 'Tìm giá trị lớn nhất hoặc nhỏ nhất của biểu thức F = ax + by trên một miền nghiệm cho trước.',
            'kí hiệu': 'F(x; y) = ax + by',
            'công thức': 'Giá trị tối ưu (max hoặc min) luôn đạt được tại một trong các đỉnh của đa giác miền nghiệm.',
            'ví dụ': 'Tìm giá trị lớn nhất của F = 2x + 3y với (x; y) thuộc miền tam giác O(0;0), A(1;0), B(0;1).',
        }
  },
  'Hình học Phẳng và Hệ thức lượng': {
        'Giá trị lượng giác của một góc': {
            'định nghĩa': 'Tọa độ của điểm M(x, y) trên nửa đường tròn đơn vị ứng với góc alpha.',
            'kí hiệu': 'sin(alpha) = yM, cos(alpha) = xM, tan(alpha) = yM/xM, cot(alpha) = xM/yM',
            'công thức': 'tan(alpha) = sin(alpha)/cos(alpha) (alpha khác 90 độ), cot(alpha) = cos(alpha)/sin(alpha) (alpha khác 0 và 180 độ)',
            'ví dụ': 'Với alpha = 90 độ suy ra M(0, 1) nên sin(90) = 1, cos(90) = 0.',
        },
        'Bảng dấu và Tính chất đặc biệt': {
            'định nghĩa': 'Dấu của các giá trị lượng giác phụ thuộc vào góc alpha là nhọn hay tù.',
            'kí hiệu': 'Góc nhọn (0, 90): Tất cả (+); Góc tù (90, 180): Sin (+), còn lại (-).',
            'công thức': 'sin(180 - alpha) = sin(alpha), cos(180 - alpha) = -cos(alpha), tan(180 - alpha) = -tan(alpha)',
            'ví dụ': 'cos(120) = -cos(180 - 120) = -cos(60) = -0.5',
        },
        'Các hệ thức lượng giác cơ bản': {
            'định nghĩa': 'Các đẳng thức liên hệ giữa sin, cos, tan, cot của cùng một góc alpha.',
            'kí hiệu': 'sin^2(alpha) + cos^2(alpha) = 1',
            'công thức': '1 + tan^2(alpha) = 1/cos^2(alpha); 1 + cot^2(alpha) = 1/sin^2(alpha); tan(alpha) * cot(alpha) = 1',
            'ví dụ': 'Biết sin(alpha) = 0.6 và alpha nhọn suy ra cos(alpha) = căn(1 - 0.6^2) = 0.8',
        },
        'Định lí Côsin và Hệ quả': {
            'định nghĩa': 'Tính cạnh khi biết 2 cạnh và góc xen giữa, hoặc tính góc khi biết 3 cạnh.',
            'kí hiệu': 'a^2 = b^2 + c^2 - 2bc * cos(A)',
            'công thức': 'cos(A) = (b^2 + c^2 - a^2) / (2bc); ma^2 = [2(b^2 + c^2) - a^2] / 4 (Công thức đường trung tuyến)',
            'ví dụ': 'Tam giác đều cạnh a suy ra ma = căn(3)*a/2',
        },
        'Định lí Sin': {
            'định nghĩa': 'Mối quan hệ giữa cạnh, góc đối diện và bán kính đường tròn ngoại tiếp R.',
            'kí hiệu': 'a/sin(A) = b/sin(B) = c/sin(C) = 2R',
            'công thức': 'R = a / (2 * sin(A)); a = 2R * sin(A)',
            'ví dụ': 'Trong tam giác vuông tại A, a/sin(90) = 2R suy ra a = 2R (Cạnh huyền là đường kính).',
        },
        '5 Công thức tính diện tích tam giác': {
            'định nghĩa': 'Các biến thể tính diện tích (S) tùy theo dữ kiện đầu bài.',
            'kí hiệu': 'S, p (nửa chu vi), R, r, ha (đường cao)',
            'công thức': [
                '1. S = (1/2) * a * ha',
                '2. S = (1/2) * b * c * sin(A)',
                '3. S = (a * b * c) / (4R)',
                '4. S = p * r',
                '5. S = căn[p * (p-a) * (p-b) * (p-c)] (Công thức Heron)'
            ],
            'ví dụ': 'Tam giác có ba cạnh 13, 14, 15 suy ra nửa chu vi p = 21, diện tích S = 84.',
        }
  },
  'Hình học Không gian': {
        'Điểm, đường thẳng và mặt phẳng': {
            'định nghĩa': 'Các đối tượng cơ bản của hình học không gian. Một mặt phẳng được xác định bởi 3 điểm không thẳng hàng, hoặc 1 đường thẳng và 1 điểm ngoài nó.',
            'kí hiệu': 'A, B thuộc Delta; Delta con (P); (P) trung với (ABC)',
            'công thức': 'Ba cách xác định mặt phẳng: (3 điểm), (đường thẳng + điểm), (2 đường thẳng cắt nhau).',
            'ví dụ': 'Hình chóp S.ABCD có các mặt bên là (SAB), (SBC), v.v.',
        },
        'Giao tuyến của hai mặt phẳng': {
            'định nghĩa': 'Đường thẳng chung của hai mặt phẳng phân biệt. Để tìm giao tuyến, ta tìm hai điểm chung phân biệt.',
            'kí hiệu': 'd = (P) giao (Q)',
            'công thức': 'Nếu A và B cùng thuộc giao của (P) và (Q) thì AB là giao tuyến.',
            'ví dụ': 'Giao tuyến của (SAB) và (SAD) trong hình chóp là cạnh chung SA.',
        },
        'Đường thẳng song song với mặt phẳng': {
            'định nghĩa': 'Đường thẳng và mặt phẳng không có điểm chung.',
            'kí hiệu': 'd // (P)',
            'công thức': 'Nếu d không nằm trong (P) và d song song với một đường thẳng d_phay nằm trong (P) thì d // (P).',
            'ví dụ': 'Trong hình hộp, cạnh của mặt trên song song với mặt đáy.',
        },
        'Hai mặt phẳng song song': {
            'định nghĩa': 'Hai mặt phẳng không có bất kỳ điểm chung nào.',
            'kí hiệu': '(P) // (Q)',
            'công thức': 'Nếu mặt phẳng (P) chứa hai đường thẳng cắt nhau a, b và cả a, b đều song song với mặt phẳng (Q) thì (P) // (Q).',
            'ví dụ': 'Hai mặt đáy của hình lăng trụ luôn song song với nhau.',
        },
        'Phép chiếu song song': {
            'định nghĩa': 'Phép đặt tương ứng mỗi điểm M trong không gian với điểm M_phay trên mặt phẳng (P) theo phương chiếu l.',
            'kí hiệu': 'Chieu(P, l) (M) = M_phay',
            'công thức': 'Bảo toàn tính thẳng hàng, thứ tự điểm và tỉ số độ dài các đoạn thẳng song song.',
            'ví dụ': 'Hình biểu diễn của hình vuông qua phép chiếu song song thường là hình bình hành.',
        },
        'Đường thẳng song song với đường thẳng': {
            'định nghĩa': 'Hai đường thẳng cùng nằm trong một mặt phẳng và không có điểm chung. Nếu không cùng nằm trong một mặt phẳng thì gọi là chéo nhau.',
            'kí hiệu': 'a // b, a cheo b',
            'công thức': 'Định lý 3 đường giao tuyến: Nếu 3 mặt phẳng cắt nhau theo 3 giao tuyến phân biệt thì 3 giao tuyến đó hoặc song song hoặc đồng quy.',
            'ví dụ': 'Trong hình chóp có đáy là hình bình hành, các cặp cạnh đối của đáy song song với nhau.',
        },
        'Thiết diện': {
            'định nghĩa': 'Giao của một mặt phẳng với các mặt của một hình khối. Thiết diện luôn là một đa giác.',
            'kí hiệu': 'H = (P) giao Hinh_Khoi',
            'công thức': 'Tìm các đoạn giao tuyến của mặt phẳng (P) với từng mặt của hình khối cho đến khi tạo thành đa giác khép kín.',
            'ví dụ': 'Thiết diện của hình chóp tứ giác cắt bởi mặt phẳng song song với đáy là một tứ giác.',
        },
        'Định lý Thales trong không gian': {
            'định nghĩa': 'Ba mặt phẳng đôi một song song chắn trên hai cát tuyến bất kỳ những đoạn thẳng tương ứng tỉ lệ.',
            'kí hiệu': 'AB / A_phay_B_phay = BC / B_phay_C_phay',
            'công thức': 'Nếu (P) // (Q) // (R) cắt hai đường thẳng d, d_phay lần lượt tại A, B, C và A_phay, B_phay, C_phay.',
            'ví dụ': 'Sử dụng để tính tỉ số độ dài đoạn thẳng trong các bài toán lăng trụ bị cắt.',
        },
        'Hình lăng trụ và Hình chóp cụt': {
            'định nghĩa': 'Hình lăng trụ có hai đáy là hai đa giác bằng nhau nằm trên hai mặt phẳng song song, các cạnh bên song song và bằng nhau.',
            'kí hiệu': 'ABC.A_phay_B_phay_C_phay',
            'công thức': 'Các mặt bên của hình lăng trụ luôn là các hình bình hành.',
            'ví dụ': 'Hình hộp là một trường hợp đặc biệt của hình lăng trụ có đáy là hình bình hành.',
        },
        'Đường thẳng vuông góc với mặt phẳng': {
            'định nghĩa': 'Đường thẳng vuông góc với mặt phẳng nếu nó vuông góc với mọi đường thẳng nằm trong mặt phẳng đó.',
            'kí hiệu': 'd vuong goc (P)',
            'công thức': 'Nếu d vuông góc với hai đường thẳng cắt nhau a và b cùng nằm trong (P) thì d vuông góc với (P).',
            'ví dụ': 'Nếu SA vuông góc với đáy (ABC) thì SA vuông góc với AB, BC và AC.',
        },
        'Định lý ba đường vuông góc': {
            'định nghĩa': 'Cho đường thẳng a không vuông góc (P) và b nằm trong (P). b vuông góc với a khi và chỉ khi b vuông góc với hình chiếu của a trên (P).',
            'kí hiệu': 'b vuong goc a tương đương b vuong goc a_phay',
            'công thức': 'Dùng để xác định góc giữa đường thẳng và mặt phẳng.',
            'ví dụ': 'Chứng minh các cạnh bên vuông góc với các đường chéo của mặt đáy.',
        },
        'Hai mặt phẳng vuông góc': {
            'định nghĩa': 'Hai mặt phẳng vuông góc nếu mặt phẳng này chứa một đường thẳng vuông góc với mặt phẳng kia.',
            'kí hiệu': '(P) vuong goc (Q)',
            'công thức': 'Nếu d vuông góc (Q) và d nằm trong (P) thì (P) vuông góc (Q).',
            'ví dụ': 'Mặt bên (SAB) vuông góc với đáy (ABC) nếu đường cao SH nằm trong (SAB) vuông góc với đáy.',
        },
        'Khoảng cách trong không gian': {
            'định nghĩa': 'Khoảng cách từ điểm M đến mặt phẳng (P) là độ dài đoạn vuông góc từ M đến (P).',
            'kí hiệu': 'd(M, (P)) = MH (với H là hình chiếu của M)',
            'công thức': 'Khoảng cách giữa hai đường thẳng chéo nhau là độ dài đoạn vuông góc chung của chúng.',
            'ví dụ': 'Chiều cao của hình chóp là khoảng cách từ đỉnh S đến mặt đáy.',
        },
        'Góc trong không gian': {
            'định nghĩa': 'Góc giữa đường thẳng và mặt phẳng là góc giữa đường thẳng đó và hình chiếu của nó trên mặt phẳng.',
            'kí hiệu': 'phi = góc(d, (P))',
            'công thức': 'Góc phi nằm trong khoảng từ 0 đến 90 độ.',
            'ví dụ': 'Góc giữa cạnh bên và mặt đáy trong hình chóp đều.',
        }
  },
  'Vectơ và Phương pháp Tọa độ Oxy': {
        'Vectơ': {
            'định nghĩa': 'Vectơ là một đoạn thẳng có hướng. Điểm bắt đầu gọi là điểm đầu, điểm kết thúc gọi là điểm cuối.',
            'kí hiệu': 'vecto a, vecto AB, vecto 0 (vecto không)',
            'công thức': 'Do dai vecto AB = khoang cach giua hai diem A va B.',
            'ví dụ': 'Vecto không có độ dài bằng 0 và hướng tùy ý.',
        },
        'Vectơ cùng phương, cùng hướng': {
            'định nghĩa': 'Hai vecto cùng nằm trên một đường thẳng hoặc hai đường thẳng song song thì cùng phương. Nếu cùng phương, chúng có thể cùng hướng hoặc ngược hướng.',
            'kí hiệu': 'vecto a // vecto b',
            'công thức': 'vecto a = k * vecto b (điều kiện để hai vecto cùng phương)',
            'ví dụ': 'Trong hình bình hành ABCD, vecto AB và vecto DC cùng hướng.',
        },
        'Tổng và Hiệu của hai vectơ': {
            'định nghĩa': 'Quy tắc cộng (nối đuôi) và quy tắc trừ (chung gốc).',
            'kí hiệu': 'vecto a + vecto b, vecto a - vecto b',
            'công thức': 'vecto AB + vecto BC = vecto AC (Quy tắc 3 điểm); vecto AB - vecto AC = vecto CB',
            'ví dụ': 'Quy tắc hình bình hành: vecto AB + vecto AD = vecto AC.',
        },
        'Tích của vectơ với một số': {
            'định nghĩa': 'Là một vecto cùng phương với vecto ban đầu, độ dài gấp |k| lần.',
            'kí hiệu': 'k * vecto a',
            'công thức': 'Do dai (k * vecto a) = |k| * do dai vecto a; G là trọng tâm tam giác ABC <=> vecto GA + vecto GB + vecto GC = vecto 0',
            'ví dụ': 'I là trung điểm AB <=> vecto MA + vecto MB = 2 * vecto MI (với M bất kỳ).',
        },
        'Hệ trục tọa độ Oxy': {
            'định nghĩa': 'Biểu diễn vecto thông qua tọa độ trên mặt phẳng Oxy.',
            'kí hiệu': 'vecto u = (x; y) tương đương vecto u = x*i + y*j',
            'công thức': 'A(xA; yA), B(xB; yB) suy ra vecto AB = (xB - xA; yB - yA)',
            'ví dụ': 'A(1; 2), B(3; 5) suy ra vecto AB = (2; 3).',
        },
        'Tích vô hướng của hai vectơ': {
            'định nghĩa': 'Là một con số, bằng tích độ dài nhân với cosin góc xen giữa.',
            'kí hiệu': 'vecto a . vecto b',
            'công thức': 'vecto a . vecto b = |a| * |b| * cos(a, b) = x1*x2 + y1*y2',
            'ví dụ': 'Hai vecto vuông góc <=> tích vô hướng bằng 0 <=> x1*x2 + y1*y2 = 0.',
        },
        'Vectơ chỉ phương (VTCP)': {
            'định nghĩa': 'Vecto u khác 0 là VTCP của đường thẳng d nếu giá của nó song song hoặc trùng với d.',
            'kí hiệu': 'vecto u = (u1; u2)',
            'công thức': 'Nếu u là VTCP thì k*u (k khác 0) cũng là VTCP.',
            'ví dụ': 'Đường thẳng qua A(1; 2) và B(3; 5) có VTCP là vecto AB = (2; 3).',
        },
        'Vectơ pháp tuyến (VTPT)': {
            'định nghĩa': 'Vecto n khác 0 là VTPT của đường thẳng d nếu giá của nó vuông góc với d.',
            'kí hiệu': 'vecto n = (a; b)',
            'công thức': 'vecto u vuông góc vecto n. Chuyển đổi: u(u1; u2) sang n(-u2; u1).',
            'ví dụ': 'Đường thẳng có VTCP u(1; -2) thì có VTPT n(2; 1).',
        },
        'Phương trình tham số của đường thẳng': {
            'định nghĩa': 'Lập được khi biết một điểm M0(x0; y0) và một VTCP u(u1; u2).',
            'kí hiệu': 'd: sử dụng tham số t',
            'công thức': 'x = x0 + u1*t và y = y0 + u2*t',
            'ví dụ': 'Đường thẳng qua M(1; -1) có VTCP u(2; 3): {x = 1 + 2t; y = -1 + 3t}',
        },
        'Phương trình tổng quát của đường thẳng': {
            'định nghĩa': 'Lập được khi biết một điểm M0(x0; y0) và một VTPT n(a; b).',
            'kí hiệu': 'ax + by + c = 0',
            'công thức': 'a(x - x0) + b(y - y0) = 0',
            'ví dụ': 'Đường thẳng qua M(1; 2), VTPT n(3; 4) suy ra: 3x + 4y - 11 = 0.',
        },
        'Các dạng phương trình đặc biệt': {
            'định nghĩa': 'Phương trình theo đoạn chắn và phương trình có hệ số góc k.',
            'kí hiệu': 'Đoạn chắn, Hệ số góc',
            'công thức': 'Đoạn chắn: x/a + y/b = 1; Hệ số góc: y = k(x - x0) + y0',
            'ví dụ': 'Đường thẳng cắt Ox tại (2;0), Oy tại (0;3) là: x/2 + y/3 = 1.',
        },
        'Vị trí tương đối giữa hai đường thẳng': {
            'định nghĩa': 'Dựa trên số nghiệm của hệ phương trình hoặc tỉ số các hệ số.',
            'kí hiệu': 'd1 cắt d2, d1 // d2, d1 trùng d2, d1 vuông góc d2',
            'công thức': 'Vuông góc: a1*a2 + b1*b2 = 0; Cắt nhau: a1*b2 - a2*b1 khác 0.',
            'ví dụ': 'x + y - 2 = 0 và x - y = 0 cắt nhau tại điểm (1; 1).',
        },
        'Góc và Khoảng cách': {
            'định nghĩa': 'Góc giữa hai đường thẳng (0 đến 90 độ) và khoảng cách từ điểm đến đường thẳng.',
            'kí hiệu': 'cos(d1, d2), d(M, delta)',
            'công thức': 'd(M, delta) = |a*x0 + b*y0 + c| / căn(a^2 + b^2)',
            'ví dụ': 'Khoảng cách từ gốc tọa độ O đến đường thẳng 3x - 4y + 5 = 0 bằng 1.',
        },
        'Phương trình đường tròn': {
            'định nghĩa': 'Đường tròn (C) tâm I(a; b), bán kính R.',
            'kí hiệu': '(x-a)^2 + (y-b)^2 = R^2',
            'công thức': 'x^2 + y^2 - 2ax - 2by + c = 0 (điều kiện: a^2 + b^2 - c > 0)',
            'ví dụ': 'x^2 + y^2 - 4x + 6y - 3 = 0 có tâm I(2; -3), bán kính R = 4.',
        },
        'Phương trình tiếp tuyến của đường tròn': {
            'định nghĩa': 'Tiếp tuyến d tại điểm M0(x0; y0) thuộc đường tròn.',
            'kí hiệu': 'd tiếp xúc (C)',
            'công thức': '(x0 - a)(x - x0) + (y0 - b)(y - y0) = 0 hoặc d(I, d) = R',
            'ví dụ': 'Tiếp tuyến của x^2 + y^2 = 5 tại (1; 2) là: x + 2y - 5 = 0.',
        },
        'Đường Elip': {
            'định nghĩa': 'Tập hợp các điểm M sao cho MF1 + MF2 = 2a.',
            'kí hiệu': '(E): x^2/a^2 + y^2/b^2 = 1 (a > b > 0)',
            'công thức': 'c^2 = a^2 - b^2; F1(-c; 0), F2(c; 0); Trục lớn: 2a, Trục bé: 2b',
            'ví dụ': 'x^2/16 + y^2/9 = 1 suy ra a=4, b=3, c=căn(7).',
        },
        'Đường Hypebol': {
            'định nghĩa': 'Tập hợp các điểm M sao cho |MF1 - MF2| = 2a.',
            'kí hiệu': '(H): x^2/a^2 - y^2/b^2 = 1',
            'công thức': 'c^2 = a^2 + b^2; Trục thực: 2a, Trục ảo: 2b',
            'ví dụ': 'x^2/9 - y^2/16 = 1 suy ra a=3, b=4, c=5.',
        },
        'Đường Parabol': {
            'định nghĩa': 'Tập hợp các điểm M cách đều tiêu điểm F và đường chuẩn delta.',
            'kí hiệu': '(P): y^2 = 2px (p > 0)',
            'công thức': 'Tiêu điểm F(p/2; 0); Đường chuẩn: x = -p/2',
            'ví dụ': 'y^2 = 4x suy ra p=2, F(1; 0), đường chuẩn x = -1.',
        }
  },
  'Lượng giác': {
        'Góc lượng giác': {
            'định nghĩa': 'Là góc có xét đến chiều quay. Góc lượng giác được xác định bởi tia đầu và tia cuối.',
            'kí hiệu': '(Ox, Oy), alpha',
            'công thức': 'alpha = goc(Ox, Oy) + k*360 độ hoặc alpha = goc(Ox, Oy) + k*2*pi',
            'ví dụ': 'alpha = 60 độ, alpha = -30 độ',
        },
        'Đường tròn lượng giác': {
            'định nghĩa': 'Là đường tròn tâm O bán kính bằng 1 trong mặt phẳng tọa độ, quy ước chiều dương là ngược chiều kim đồng hồ.',
            'kí hiệu': '(O; 1)',
            'công thức': 'x^2 + y^2 = 1',
            'ví dụ': 'Điểm M(cos alpha, sin alpha) luôn nằm trên đường tròn lượng giác.',
        },
        'Giá trị lượng giác của một góc': {
            'định nghĩa': 'Cho góc lượng giác alpha, gọi M(x; y) là điểm biểu diễn góc này trên đường tròn lượng giác. Khi đó: x = cos(alpha), y = sin(alpha).',
            'kí hiệu': 'sin(alpha), cos(alpha), tan(alpha), cot(alpha)',
            'công thức': 'tan(alpha) = sin(alpha)/cos(alpha); cot(alpha) = cos(alpha)/sin(alpha)',
            'ví dụ': 'sin(30 độ) = 0.5; cos(30 độ) = căn(3)/2',
        },
        'Công thức lượng giác cơ bản': {
            'định nghĩa': 'Các hệ thức liên hệ mật thiết giữa các giá trị lượng giác của cùng một góc alpha.',
            'kí hiệu': 'sin^2(alpha) + cos^2(alpha) = 1',
            'công thức': '1 + tan^2(alpha) = 1/cos^2(alpha); 1 + cot^2(alpha) = 1/sin^2(alpha)',
            'ví dụ': 'tan(alpha) * cot(alpha) = 1',
        },
        'Hàm số y = sin x': {
            'định nghĩa': 'Là hàm số lẻ, tuần hoàn với chu kỳ 2*pi, tập giá trị nằm trong khoảng từ -1 đến 1.',
            'kí hiệu': 'y = sin(x)',
            'công thức': 'Tập xác định D = R, Chu kỳ T = 2*pi',
            'ví dụ': 'sin(x + 2*pi) = sin(x)',
        },
        'Hàm số y = cos x': {
            'định nghĩa': 'Là hàm số chẵn, tuần hoàn với chu kỳ 2*pi, tập giá trị nằm trong khoảng từ -1 đến 1.',
            'kí hiệu': 'y = cos(x)',
            'công thức': 'Tập xác định D = R, Chu kỳ T = 2*pi',
            'ví dụ': 'cos(x + 2*pi) = cos(x)',
        },
        'Hàm số y = tan x': {
            'định nghĩa': 'Là hàm số lẻ, tuần hoàn với chu kỳ pi.',
            'kí hiệu': 'y = tan(x)',
            'công thức': 'Tập xác định D = R loại bỏ các điểm {pi/2 + k*pi}',
            'ví dụ': 'tan(x + pi) = tan(x)',
        },
        'Hàm số y = cot x': {
            'định nghĩa': 'Là hàm số lẻ, tuần hoàn với chu kỳ pi.',
            'kí hiệu': 'y = cot(x)',
            'công thức': 'Tập xác định D = R loại bỏ các điểm {k*pi}',
            'ví dụ': 'cot(pi/4) = 1',
        },
        'Phương trình lượng giác cơ bản': {
            'định nghĩa': 'Các phương trình có dạng f(x) = a với f là một hàm số lượng giác.',
            'kí hiệu': 'sin(x) = a, cos(x) = a, tan(x) = a, cot(x) = a',
            'công thức': 'sin(x) = sin(alpha) <=> x = alpha + k*2*pi hoặc x = pi - alpha + k*2*pi',
            'ví dụ': 'sin(x) = 0 <=> x = k*pi',
        }
  }
  'Tổ hợp, Xác suất': {
        'Quy tắc cộng': {
            'định nghĩa': 'Một công việc được hoàn thành bởi một trong hai phương án độc lập. Phương án A có m cách, phương án B có n cách.',
            'kí hiệu': 'm + n',
            'công thức': 'Tổng số cách hoàn thành công việc là: N = m + n',
            'ví dụ': 'Chọn 1 quyển sách từ 5 sách Toán hoặc 4 sách Lí suy ra có 5 + 4 = 9 cách.',
        },
        'Quy tắc nhân': {
            'định nghĩa': 'Một công việc bao gồm nhiều công đoạn liên tiếp nhau. Công đoạn 1 có m cách, công đoạn 2 có n cách.',
            'kí hiệu': 'm * n',
            'công thức': 'Tổng số cách hoàn thành công việc là: N = m * n',
            'ví dụ': 'Chọn một bộ quần áo gồm 3 áo và 2 quần suy ra có 3 * 2 = 6 cách.',
        },
        'Sơ đồ cây': {
            'định nghĩa': 'Công cụ trực quan để liệt kê tất cả các khả năng của một bài toán đếm.',
            'kí hiệu': 'Tree Diagram',
            'công thức': 'Mỗi nhánh đại diện cho một lựa chọn tại một công đoạn nhất định.',
            'ví dụ': 'Liệt kê các kết quả khi tung đồng xu 2 lần liên tiếp (Sấp-Sấp, Sấp-Ngửa, v.v.).',
        },
        'Giai thừa': {
            'định nghĩa': 'Tích của n số nguyên dương đầu tiên.',
            'kí hiệu': 'n!',
            'công thức': 'n! = n * (n-1) * ... * 1; Quy ước: 0! = 1',
            'ví dụ': '5! = 5 * 4 * 3 * 2 * 1 = 120',
        },
        'Hoán vị': {
            'định nghĩa': 'Sắp xếp n phần tử khác nhau vào n vị trí (có thứ tự).',
            'kí hiệu': 'Pn',
            'công thức': 'Pn = n!',
            'ví dụ': 'Xếp 5 học sinh vào một hàng ngang có 5! = 120 cách.',
        },
        'Chỉnh hợp': {
            'định nghĩa': 'Chọn k phần tử từ n phần tử khác nhau và sắp xếp chúng theo một thứ tự nhất định.',
            'kí hiệu': 'Ank',
            'công thức': 'Ank = n! / (n-k)! (với 1 <= k <= n)',
            'ví dụ': 'Chọn 3 người làm lớp trưởng, lớp phó, thư ký từ 10 người: A(10,3) = 720.',
        },
        'Tổ hợp': {
            'định nghĩa': 'Chọn k phần tử từ n phần tử khác nhau mà không quan tâm đến thứ tự.',
            'kí hiệu': 'Cnk',
            'công thức': 'Cnk = n! / [k!(n-k)!]',
            'ví dụ': 'Chọn 3 người đi trực nhật từ 10 người: C(10,3) = 120.',
        },
        'Nhị thức Newton': {
            'định nghĩa': 'Công thức khai triển biểu thức lũy thừa của một tổng hai số hạng.',
            'kí hiệu': '(a + b)^n',
            'công thức': '(a + b)^n = Tổng các số hạng Cnk * a^(n-k) * b^k',
            'ví dụ': '(a + b)^2 = C20*a^2 + C21*ab + C22*b^2 = a^2 + 2ab + b^2',
        },
        'Tam giác Pascal': {
            'định nghĩa': 'Bảng tam giác các hệ số của nhị thức Newton.',
            'kí hiệu': 'Pascal Triangle',
            'công thức': 'Cnk = C(n-1, k-1) + C(n-1, k)',
            'ví dụ': 'Dòng 4: 1, 4, 6, 4, 1',
        },
        'Phép thử ngẫu nhiên': {
            'định nghĩa': 'Là hành động mà kết quả không thể biết trước, nhưng ta biết được tập hợp tất cả các kết quả có thể xảy ra.',
            'kí hiệu': 'T',
            'ví dụ': 'Gieo một đồng xu; Rút một quân bài từ bộ bài 52 lá.',
        },
        'Không gian mẫu': {
            'định nghĩa': 'Tập hợp tất cả các kết quả có thể xảy ra của phép thử ngẫu nhiên.',
            'kí hiệu': 'Omega',
            'công thức': 'n(Omega) là số phần tử của không gian mẫu.',
            'ví dụ': 'Gieo 2 đồng xu: Omega = {SS, SN, NS, NN} suy ra n(Omega) = 4.',
        },
        'Biến cố': {
            'định nghĩa': 'Là một tập con của không gian mẫu. Mỗi phần tử của biến cố được gọi là một kết quả thuận lợi.',
            'kí hiệu': 'A, B, C con Omega',
            'công thức': 'n(A) là số kết quả thuận lợi cho biến cố A.',
            'ví dụ': 'Gieo xúc xắc, biến cố A "số chấm lẻ": A = {1, 3, 5} suy ra n(A) = 3.',
        },
        'Biến cố không thể và Biến cố chắc chắn': {
            'định nghĩa': 'Biến cố không bao giờ xảy ra là biến cố không thể. Biến cố luôn luôn xảy ra là biến cố chắc chắn.',
            'kí hiệu': 'Tap_Rong (không thể), Omega (chắc chắn)',
            'công thức': 'P(Rong) = 0; P(Omega) = 1',
            'ví dụ': 'Gieo xúc xắc mặt 7 chấm là biến cố không thể.',
        },
        'Định nghĩa cổ điển của xác suất': {
            'định nghĩa': 'Tỉ số giữa số kết quả thuận lợi và tổng số kết quả có thể xảy ra.',
            'kí hiệu': 'P(A)',
            'công thức': 'P(A) = n(A) / n(Omega)',
            'ví dụ': 'Chọn 2 học sinh từ 10 học sinh (6 nam, 4 nữ). Xác suất 2 nữ là C(4,2) / C(10,2).',
        },
        'Biến cố đối': {
            'định nghĩa': 'Biến cố "A không xảy ra", là phần bù của A trong không gian mẫu Omega.',
            'kí hiệu': 'A_gach_ngang',
            'công thức': 'P(A_gach_ngang) = 1 - P(A)',
            'ví dụ': 'Xác suất bắn trượt = 1 - Xác suất bắn trúng.',
        },
        'Biến cố hợp và Quy tắc cộng': {
            'định nghĩa': 'Biến cố hợp xảy ra khi có ít nhất một trong hai biến cố A hoặc B xảy ra.',
            'kí hiệu': 'A hop B',
            'công thức': 'P(A hop B) = P(A) + P(B) - P(A giao B). Nếu xung khắc: P = P(A) + P(B)',
            'ví dụ': 'Xác suất rút được thẻ số chẵn hoặc số chia hết cho 5.',
        },
        'Biến cố giao và Biến cố độc lập': {
            'định nghĩa': 'Hai biến cố độc lập nếu việc xảy ra của biến cố này không ảnh hưởng đến xác suất của biến cố kia.',
            'kí hiệu': 'A giao B',
            'công thức': 'Nếu A, B độc lập: P(A giao B) = P(A) * P(B)',
            'ví dụ': 'Hai người bắn độc lập vào bia, xác suất cả hai cùng trúng là tích xác suất từng người.',
        },
        'Xác suất có điều kiện': {
            'định nghĩa': 'Xác suất của biến cố A với điều kiện biến cố B đã xảy ra.',
            'kí hiệu': 'P(A|B)',
            'công thức': 'P(A|B) = P(A giao B) / P(B)',
            'ví dụ': 'Xác suất lấy được bi đỏ ở lần 2 khi biết lần 1 đã lấy bi xanh (không hoàn lại).',
        }
  },
  'Thống kê': {
        'Số trung bình': {
            'định nghĩa': 'Giá trị trung bình cộng của các số liệu, dùng để đại diện cho xu thế trung tâm của mẫu số liệu.',
            'kí hiệu': 'x_ngang',
            'công thức': 'x_ngang = (x1 + x2 + ... + xn) / n hoặc Tổng (ni * xi) / N',
            'ví dụ': 'Mẫu số liệu: {5, 7, 9} suy ra x_ngang = 7.',
        },
        'Trung vị': {
            'định nghĩa': 'Số đứng ở vị trí giữa của mẫu số liệu sau khi đã sắp xếp theo thứ tự không giảm.',
            'kí hiệu': 'Me',
            'công thức': 'Nếu n lẻ: Me = số thứ (n+1)/2. Nếu n chẵn: Me = trung bình cộng của hai số giữa.',
            'ví dụ': 'Mẫu số liệu: {2, 3, 4, 100} suy ra Me = (3 + 4) / 2 = 3.5.',
        },
        'Tứ phân vị': {
            'định nghĩa': 'Ba giá trị chia mẫu số liệu đã sắp xếp thành 4 phần có số lượng phần tử bằng nhau.',
            'kí hiệu': 'Q1, Q2, Q3',
            'công thức': 'Q2 bằng trung vị Me; Q1 là trung vị nửa dưới; Q3 là trung vị nửa trên.',
            'ví dụ': 'Mẫu số liệu: {1, 2, 3, 4, 5, 6, 7} suy ra Q1=2, Q2=4, Q3=6.',
        },
        'Mốt': {
            'định nghĩa': 'Giá trị xuất hiện với tần số lớn nhất trong mẫu số liệu.',
            'kí hiệu': 'Mo',
            'công thức': 'Giá trị xi ứng với tần số ni đạt giá trị lớn nhất.',
            'ví dụ': 'Mẫu số liệu: {1, 2, 2, 3, 3, 3} suy ra Mo = 3.',
        },
        'Phương sai và Độ lệch chuẩn': {
            'định nghĩa': 'Số đặc trưng đo mức độ phân tán của các số liệu xung quanh số trung bình.',
            'kí hiệu': 's^2 (phương sai), s (độ lệch chuẩn)',
            'công thức': 's = căn bậc hai của phương sai s^2. s^2 = [Tổng (xi - x_ngang)^2] / n',
            'ví dụ': 'Độ lệch chuẩn càng lớn thì dữ liệu càng phân tán rộng so với số trung bình.',
        },
        'Xác suất của biến cố': {
            'định nghĩa': 'Tỉ số giữa số kết quả thuận lợi và tổng số kết quả có thể xảy ra trong phép thử.',
            'kí hiệu': 'P(A) = n(A) / n(Omega)',
            'công thức': '0 <= P(A) <= 1',
            'ví dụ': 'P(A) = 0.5 nghĩa là khả năng xảy ra biến cố A là 50%.',
        }
  },
  'Giải tích': {
        'Giới hạn của dãy số': {
            'định nghĩa': 'Dãy số (un) có giới hạn L khi n tiến ra vô cùng nếu khoảng cách |un - L| nhỏ tùy ý khi n đủ lớn.',
            'kí hiệu': 'lim un = L khi n -> +vô cùng',
            'công thức': 'lim (1/n^k) = 0; lim (q^n) = 0 nếu |q| < 1',
            'ví dụ': 'lim (2n + 1)/n = 2 khi n tiến ra vô cùng.',
        },
        'Giới hạn hữu hạn của hàm số': {
            'định nghĩa': 'Hàm số f(x) có giới hạn L khi x tiến dần đến x0 nếu giá trị f(x) gần L tùy ý khi x đủ gần x0.',
            'kí hiệu': 'lim f(x) = L khi x -> x0',
            'công thức': 'Các quy tắc cộng, trừ, nhân, chia giới hạn tương tự như với số thực.',
            'ví dụ': 'lim (x^2 + 1) khi x tiến đến 1 bằng 2.',
        },
        'Giới hạn vô cực': {
            'định nghĩa': 'Khi x tiến tới x0 hoặc vô cực, giá trị f(x) tăng hoặc giảm không giới hạn.',
            'kí hiệu': 'lim f(x) = +vô cùng hoặc -vô cùng',
            'công thức': 'Số thực L / 0 -> vô cùng; Số thực L / vô cùng -> 0',
            'ví dụ': 'lim (1/x) khi x tiến đến 0 về phía dương là +vô cùng.',
        },
        'Hàm số liên tục tại một điểm': {
            'định nghĩa': 'Hàm số f(x) liên tục tại x0 nếu giới hạn của hàm số tại đó bằng đúng giá trị của hàm số f(x0).',
            'kí hiệu': 'Liên tục tại x0',
            'công thức': 'lim f(x) khi x -> x0 bằng f(x0)',
            'ví dụ': 'Hàm đa thức luôn liên tục trên tập số thực R.',
        },
        'Hàm số liên tục trên một khoảng': {
            'định nghĩa': 'Hàm số liên tục tại mọi điểm thuộc khoảng đó.',
            'kí hiệu': 'f thuộc C(a; b)',
            'công thức': 'Hàm số sơ cấp liên tục trên các khoảng xác định của chúng.',
            'ví dụ': 'Hàm số y = căn(x) liên tục trên nửa khoảng [0; +vô cùng).',
        },
        'Giới hạn một bên': {
            'định nghĩa': 'Giới hạn khi x tiến đến a từ bên trái (x < a) hoặc bên phải (x > a).',
            'kí hiệu': 'lim f(x) khi x -> a- hoặc x -> a+',
            'công thức': 'Giới hạn tại a tồn tại <=> giới hạn bên trái bằng giới hạn bên phải.',
            'ví dụ': 'lim (1/x) khi x -> 0+ bằng +vô cùng.',
        },
        'Định lí giá trị trung gian': {
            'định nghĩa': 'Nếu f(x) liên tục trên [a; b] và f(a)*f(b) < 0 thì tồn tại ít nhất một điểm c thuộc (a; b) sao cho f(c) = 0.',
            'kí hiệu': 'f(a) * f(b) < 0 => tồn tại nghiệm c',
            'công thức': 'Thường dùng để chứng minh phương trình có nghiệm trên một khoảng.',
            'ví dụ': 'Chứng minh x^3 + x - 1 = 0 có nghiệm trong khoảng (0, 1).',
        },
        'Đạo hàm tại một điểm': {
            'định nghĩa': 'Đạo hàm của y = f(x) tại x0 là giới hạn của tỉ số giữa số gia hàm số và số gia đối số khi số gia đối số tiến về 0.',
            'kí hiệu': "f'(x0)",
            'công thức': "f'(x0) = lim [f(x) - f(x0)] / (x - x0) khi x -> x0",
            'ví dụ': "Đạo hàm của f(x) = x^2 tại x=1 là f'(1) = 2.",
        },
        'Ý nghĩa hình học của đạo hàm': {
            'định nghĩa': "Đạo hàm f'(x0) là hệ số góc của tiếp tuyến của đồ thị hàm số tại điểm M(x0; f(x0)).",
            'kí hiệu': "k = f'(x0)",
            'công thức': "Phương trình tiếp tuyến: y - y0 = f'(x0) * (x - x0)",
            'ví dụ': 'Tiếp tuyến của y = x^2 tại (1, 1) là y = 2x - 1.',
        },
        'Quy tắc tính đạo hàm cơ bản': {
            'định nghĩa': 'Các quy tắc để tính đạo hàm của tổng, hiệu, tích, thương các hàm số.',
            'kí hiệu': "(u+v)', (u-v)', (uv)', (u/v)'",
            'công thức': [
                "(u + v)' = u' + v'",
                "(uv)' = u'v + uv'",
                "(u/v)' = (u'v - uv') / v^2"
            ],
            'ví dụ': 'Đạo hàm của (x * sin x) là sin x + x * cos x.',
        },
        'Đạo hàm của hàm hợp': {
            'định nghĩa': 'Nếu y = f(u) và u = u(x) thì đạo hàm của y theo x được tính qua trung gian u.',
            'kí hiệu': "y'(x) = y'(u) * u'(x)",
            'công thức': "(u^n)' = n * u^(n-1) * u'",
            'ví dụ': "Đạo hàm của (x^2 + 1)^3 là 3*(x^2 + 1)^2 * 2x = 6x*(x^2 + 1)^2.",
        },
        'Đạo hàm của các hàm lượng giác': {
            'định nghĩa': 'Bảng đạo hàm của các hàm số lượng giác cơ bản.',
            'kí hiệu': "(sin x)', (cos x)', (tan x)', (cot x)'",
            'công thức': [
                "(sin x)' = cos x",
                "(cos x)' = -sin x",
                "(tan x)' = 1 / cos^2(x)",
                "(cot x)' = -1 / sin^2(x)"
            ],
            'ví dụ': "Đạo hàm của sin(2x) là 2*cos(2x).",
        },
        'Đạo hàm cấp hai': {
            'định nghĩa': 'Đạo hàm của đạo hàm cấp một. Trong vật lý, nó đại diện cho gia tốc của chuyển động.',
            'kí hiệu': "f''(x) hoặc y''",
            'công thức': "f''(x) = (f'(x))'",
            'ví dụ': "y = x^3 => y' = 3x^2 => y'' = 6x.",
        },
    }
}
