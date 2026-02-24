tu_dien_chu_de_2 = {   'Dãy số': {   'Cách cho dãy số': {   'công thức': 'u_{n+1} = f(u_n)',
                                         'kí hiệu': 'u_n, u_{n+1}',
                                         'ví dụ': 'u_1 = 1, u_{n+1} = u_n + 2',
                                         'định nghĩa': 'Dãy số có thể cho bằng công thức tổng '
                                                       'quát, truy hồi hoặc liệt kê.'},
                  'Cấp số cộng': {   'công thức': 'u_n = u_1 + (n-1)d',
                                     'kí hiệu': '(u_n), d',
                                     'ví dụ': '1, 3, 5, 7, ... (d = 2)',
                                     'định nghĩa': 'Là dãy số mà hiệu của hai số hạng liên tiếp '
                                                   'không đổi.'},
                  'Cấp số nhân': {   'công thức': 'u_n = u_1 q^{n-1}',
                                     'kí hiệu': '(u_n), q',
                                     'ví dụ': '2, 4, 8, 16, ... (q = 2)',
                                     'định nghĩa': 'Là dãy số mà tỉ số của hai số hạng liên tiếp '
                                                   'không đổi.'},
                  'Dãy số': {   'công thức': 'u: \mathbb{N} \to \mathbb{R}',
                                'kí hiệu': '(u_n)',
                                'ví dụ': 'u_n = 2n + 1',
                                'định nghĩa': 'Là một hàm số xác định trên tập các số tự nhiên.'},
                  'Số hạng tổng quát của cấp số cộng': {   'công thức': 'u_n = u_1 + (n-1)d',
                                                           'kí hiệu': 'u_n',
                                                           'ví dụ': 'u_5 = u_1 + 4d',
                                                           'định nghĩa': 'Số hạng thứ n được xác '
                                                                         'định theo công thức tổng '
                                                                         'quát.'},
                  'Số hạng tổng quát của cấp số nhân': {   'công thức': 'u_n = u_1 q^{n-1}',
                                                           'kí hiệu': 'u_n',
                                                           'ví dụ': 'u_4 = u_1 q^3',
                                                           'định nghĩa': 'Số hạng thứ n được xác '
                                                                         'định theo công thức tổng '
                                                                         'quát.'},
                  'Tổng n số hạng đầu của cấp số cộng': {   'công thức': 'S_n = \dfrac{n(u_1 + '
                                                                         'u_n)}{2}',
                                                            'kí hiệu': 'S_n',
                                                            'ví dụ': 'S_5 = \dfrac{5(u_1 + '
                                                                     'u_5)}{2}',
                                                            'định nghĩa': 'Tổng của n số hạng đầu '
                                                                          'tiên của cấp số cộng.'},
                  'Tổng n số hạng đầu của cấp số nhân (q ≠ 1)': {   'công thức': 'S_n = u_1 '
                                                                                 '\dfrac{q^n - '
                                                                                 '1}{q - 1}',
                                                                    'kí hiệu': 'S_n',
                                                                    'ví dụ': 'S_3 = u_1 '
                                                                             '\dfrac{q^3 - 1}{q - '
                                                                             '1}',
                                                                    'định nghĩa': 'Tổng của n số '
                                                                                  'hạng đầu tiên '
                                                                                  'của cấp số nhân '
                                                                                  'khi q khác 1.'}},
    'Giải tích': {   'Giới hạn của dãy số': {   'công thức': '\lim \frac{1}{n^k} = 0; \lim q^n '
                                                             '= 0 \text{ (|q| < 1)}',
                                                'hình_ve': 'limit((2*n+1)/n, n, oo)',
                                                'kí hiệu': '\lim_{n \to +\infty} u_n = L '
                                                           '\text{ hoặc } u_n \to L',
                                                'ví dụ': '\lim \frac{2n+1}{n} = 2',
                                                'định nghĩa': 'Dãy số (u_n) có giới hạn L khi n '
                                                              'tiến ra vô cùng nếu khoảng cách '
                                                              '|u_n - L| nhỏ tùy ý khi n đủ lớn.'},
                     'Giới hạn hữu hạn của hàm số': {   'công thức': '\text{Các quy tắc cộng, '
                                                                     'trừ, nhân, chia giới hạn '
                                                                     'tương tự số thực.}',
                                                        'hình_ve': 'plot(x**2 + 1, (x, -2, 2)) # '
                                                                   'Vẽ đồ thị để thấy sự hội tụ '
                                                                   'tại x=1',
                                                        'kí hiệu': '\lim_{x \to x_0} f(x) = L',
                                                        'ví dụ': '\lim_{x \to 1} (x^2 + 1) = 2',
                                                        'định nghĩa': 'Hàm số f(x) có giới hạn L '
                                                                      'khi x tiến dần đến x_0 nếu '
                                                                      'giá trị f(x) gần L tùy ý '
                                                                      'khi x đủ gần x_0.'},
                     'Giới hạn một bên': {   'công thức': '\lim_{x \to a} f(x) tồn tại ⇔ '
                                                          '\lim_{x \to a^-} f(x) = \lim_{x \to '
                                                          'a^+} f(x)',
                                             'kí hiệu': '\lim_{x \to a^-}, \lim_{x \to a^+}',
                                             'ví dụ': '\lim_{x \to 0^+} \dfrac{1}{x} = +\infty',
                                             'định nghĩa': 'Giới hạn khi x tiến đến a từ bên trái '
                                                           'hoặc bên phải.'},
                     'Giới hạn vô cực': {   'công thức': '\frac{L}{0} \to \infty; '
                                                         '\frac{L}{\infty} \to 0',
                                            'hình_ve': "plot(1/x, (x, 0.1, 5), title='Tiệm cận "
                                                       "đứng tại x=0')",
                                            'kí hiệu': '\lim_{x \to x_0} f(x) = +\infty; '
                                                       '\lim_{x \to x_0} f(x) = -\infty',
                                            'ví dụ': '\lim_{x \to 0^+} \frac{1}{x} = +\infty',
                                            'định nghĩa': 'Khi x tiến tới x_0 hoặc vô cực, giá trị '
                                                          'f(x) tăng hoặc giảm không giới hạn.'},
                     'Hàm số liên tục trên một khoảng': {   'công thức': '\text{Hàm số sơ cấp '
                                                                         'liên tục trên các khoảng '
                                                                         'xác định của chúng.}',
                                                            'hình_ve': 'plot(sqrt(x), (x, 0, 10))',
                                                            'kí hiệu': 'f \in C(a; b)',
                                                            'ví dụ': 'y = \sqrt{x} \text{ liên '
                                                                     'tục trên } [0; +\infty).',
                                                            'định nghĩa': 'Hàm số liên tục tại mọi '
                                                                          'điểm thuộc khoảng đó.'},
                     'Hàm số liên tục tại một điểm': {   'công thức': '\lim_{x \to x_0} f(x) = '
                                                                      'f(x_0)',
                                                         'hình_ve': 'plot(Piecewise((x**2, x < 1), '
                                                                    '(2-x, x >= 1)), (x, 0, 2)) # '
                                                                    'Vẽ hàm ghép để kiểm tra tính '
                                                                    'liên tục',
                                                         'kí hiệu': '\text{Liên tục tại } x_0',
                                                         'ví dụ': '\text{Hàm đa thức luôn liên '
                                                                  'tục trên } \mathbb{R}.',
                                                         'định nghĩa': 'Hàm số f(x) liên tục tại '
                                                                       'x_0 nếu giới hạn của hàm '
                                                                       'số tại đó bằng đúng giá '
                                                                       'trị của hàm số.'},
                     'Quy tắc tính đạo hàm cơ bản': {   'công thức': [   "(u \pm v)' = u' \pm v'",
                                                                         "(uv)' = u'v + uv'",
                                                                         "(\frac{u}{v})' = "
                                                                         "\frac{u'v - uv'}{v^2}"],
                                                        'hình_ve': 'plot(sp.diff(x**3 - 2*x, x), '
                                                                   "(x, -2, 2), title='Do thi ham "
                                                                   "dao ham f prime(x)')",
                                                        'kí hiệu': "(u+v)', (uv)', (\frac{u}{v})'",
                                                        'ví dụ': "(x \cdot \sin x)' = \sin x + "
                                                                 'x \cdot \cos x.',
                                                        'định nghĩa': 'Các quy tắc để tính đạo hàm '
                                                                      'của tổng, hiệu, tích, '
                                                                      'thương các hàm số.'},
                     'Ý nghĩa hình học của đạo hàm': {   'công thức': "y - y_0 = f'(x_0)(x - x_0) "
                                                                      '\text{ (Phương trình tiếp '
                                                                      'tuyến)}',
                                                         'hình_ve': 'plot(x**2, 2*x - 1, (x, -1, '
                                                                    "3), title='Do thi va Tiep "
                                                                    "tuyen')",
                                                         'kí hiệu': "k = f'(x_0)",
                                                         'ví dụ': '\text{Tiếp tuyến của } y=x^2 '
                                                                  '\text{ tại } (1,1) \text{ là '
                                                                  '} y = 2(x-1) + 1 = 2x - 1.',
                                                         'định nghĩa': "Đạo hàm f'(x_0) là hệ số "
                                                                       'góc của tiếp tuyến của đồ '
                                                                       'thị hàm số y = f(x) tại '
                                                                       'điểm M(x_0; f(x_0)).'},
                     'Đạo hàm cấp hai': {   'công thức': "f''(x) = (f'(x))'",
                                            'hình_ve': 'plot(x**3, 3*x**2, 6*x, (x, -2, 2), '
                                                       "title='Dao ham cap 1 va cap 2')",
                                            'kí hiệu': "f''(x) \text{ hoặc } y''",
                                            'ví dụ': "y = x^3 \Rightarrow y' = 3x^2 \Rightarrow "
                                                     "y'' = 6x.",
                                            'định nghĩa': 'Đạo hàm của đạo hàm cấp một. Có ý nghĩa '
                                                          'vật lý là gia tốc của chuyển động.'},
                     'Đạo hàm của các hàm lượng giác': {   'công thức': [   "(\sin x)' = \cos x",
                                                                            "(\cos x)' = -\sin x",
                                                                            "(\tan x)' = "
                                                                            '\frac{1}{\cos^2 x}',
                                                                            "(\cot x)' = "
                                                                            '-\frac{1}{\sin^2 '
                                                                            'x}'],
                                                           'hình_ve': 'plot(sp.sin(x), sp.cos(x), '
                                                                      '(x, -sp.pi, sp.pi), '
                                                                      "title='Ham so va Dao ham "
                                                                      "luong giac')",
                                                           'kí hiệu': "(\sin x)', (\cos x)', "
                                                                      "(\tan x)', (\cot x)'",
                                                           'ví dụ': "(\sin 2x)' = 2\cos 2x.",
                                                           'định nghĩa': 'Bảng đạo hàm của 4 hàm '
                                                                         'số lượng giác cơ bản.'},
                     'Đạo hàm của hàm hợp': {   'công thức': "(u^n)' = n \cdot u^{n-1} \cdot u'",
                                                'hình_ve': 'plot(sp.diff((x**2+1)**3, x), (x, -1, '
                                                           '1))',
                                                'kí hiệu': "y'_x = y'_u \cdot u'_x",
                                                'ví dụ': "((x^2+1)^3)' = 3(x^2+1)^2 \cdot 2x = "
                                                         '6x(x^2+1)^2.',
                                                'định nghĩa': 'Nếu y = f(u) và u = u(x) thì đạo '
                                                              'hàm của y theo x được tính qua '
                                                              'trung gian u.'},
                     'Đạo hàm tại một điểm': {   'công thức': "f'(x_0) = \lim_{x \to x_0} "
                                                              '\frac{f(x) - f(x_0)}{x - x_0}',
                                                 'hình_ve': "plot(x**2, (x, -2, 2), title='Minh "
                                                            "hoa dao ham tai mot diem')",
                                                 'kí hiệu': "f'(x_0) = \lim_{\Delta x \to 0} "
                                                            '\frac{f(x_0 + \Delta x) - '
                                                            'f(x_0)}{\Delta x}',
                                                 'ví dụ': '\text{Tính đạo hàm của } f(x) = x^2 '
                                                          "\text{ tại } x=1 \Rightarrow f'(1) = "
                                                          '2.',
                                                 'định nghĩa': 'Đạo hàm của hàm số y = f(x) tại '
                                                               'điểm x_0 là giới hạn của tỉ số '
                                                               'giữa số gia của hàm số và số gia '
                                                               'của đối số khi số gia đối số tiến '
                                                               'dần về 0.'},
                     'Định lí giá trị trung gian': {   'công thức': '\text{Dùng để chứng minh '
                                                                    'phương trình có nghiệm.}',
                                                       'hình_ve': 'plot(x**3 + x - 1, (x, 0, 1)) # '
                                                                  'Đường cong cắt trục hoành',
                                                       'kí hiệu': 'f(a) \cdot f(b) < 0 '
                                                                  '\Rightarrow \exists c \in '
                                                                  '(a, b): f(c) = 0',
                                                       'ví dụ': '\text{Chứng minh } x^3 + x - 1 = '
                                                                '0 \text{ có nghiệm trong } (0, '
                                                                '1).',
                                                       'định nghĩa': 'Nếu f(x) liên tục trên [a; '
                                                                     'b] và f(a).f(b) < 0 thì tồn '
                                                                     'tại ít nhất một điểm c thuộc '
                                                                     '(a; b) sao cho f(c) = 0.'}},
    'Hàm số và Biểu thức Đại số': {   'Bất phương trình bậc hai': {   'công thức': '\text{Nghiệm '
                                                                                   'dựa trên bảng '
                                                                                   'xét dấu của '
                                                                                   'tam thức bậc '
                                                                                   'hai.}',
                                                                      'hình_ve': 'sp.plot_implicit(x**2 '
                                                                                 '- 3*x + 2 < 0, '
                                                                                 '(x, -1, 4), (y, '
                                                                                 '-1, 1), '
                                                                                 "title='Mien "
                                                                                 'nghiem x^2 - 3x '
                                                                                 "+ 2 < 0')",
                                                                      'kí hiệu': 'ax^2 + bx + c '
                                                                                 '\ge 0',
                                                                      'ví dụ': 'x^2 - 3x + 2 < 0 '
                                                                               '\Leftrightarrow x '
                                                                               '\in (1; 2).',
                                                                      'định nghĩa': 'Là bất phương '
                                                                                    'trình dạng '
                                                                                    'ax^2 + bx + c '
                                                                                    '> 0 (hoặc <, '
                                                                                    '\le, \ge).'},
                                      'Dấu của tam thức bậc hai': {   'công thức': '\Delta < 0 '
                                                                                   '\Rightarrow a '
                                                                                   '\cdot f(x) > '
                                                                                   '0, \forall x '
                                                                                   '\in '
                                                                                   '\mathbb{R}.',
                                                                      'hình_ve': 'plot(x**2 - 4*x '
                                                                                 '+ 5, (x, -1, 5), '
                                                                                 "title='f(x) luon "
                                                                                 'cung dau voi a '
                                                                                 "khi Delta < 0')",
                                                                      'kí hiệu': 'f(x) \text{ '
                                                                                 'cùng dấu với } a '
                                                                                 '\text{ khi } '
                                                                                 '\Delta < 0.',
                                                                      'ví dụ': 'x^2 - 4x + 5 > 0 '
                                                                               '\text{ với mọi } '
                                                                               'x \in \mathbb{R} '
                                                                               '\text{ vì } '
                                                                               '\Delta = -4 < 0 '
                                                                               '\text{ và } a = 1 '
                                                                               '> 0.',
                                                                      'định nghĩa': 'Xét dấu của '
                                                                                    'biểu thức '
                                                                                    'f(x) = ax^2 + '
                                                                                    'bx + c dựa '
                                                                                    'vào dấu của a '
                                                                                    'và biệt thức '
                                                                                    '\Delta.'},
                                      'Hàm số': {   'công thức': 'D \text{ là tập xác định, } x '
                                                                 '\text{ là biến số, } y \text{ '
                                                                 'là hàm số.}',
                                                    'hình_ve': 'plot(sp.sqrt(x-1), (x, 1, 10), '
                                                               "title='Do thi ham so y = "
                                                               "sqrt(x-1)')",
                                                    'kí hiệu': 'y = f(x), x \in D',
                                                    'ví dụ': 'y = \sqrt{x-1} \text{ có TXĐ } D = '
                                                             '[1; +\infty).',
                                                    'định nghĩa': 'Cho tập hợp khác rỗng D '
                                                                  '\subset \mathbb{R}. Hàm số f '
                                                                  'xác định trên D là một quy tắc '
                                                                  'cho tương ứng mỗi số x \in D '
                                                                  'với duy nhất một số y \in '
                                                                  '\mathbb{R}.'},
                                      'Hàm số bậc hai': {   'công thức': '\text{Đỉnh } '
                                                                         'I\left(-\frac{b}{2a}; '
                                                                         '-\frac{\Delta}{4a}\right), '
                                                                         '\text{ trục đối xứng } '
                                                                         'x = -\frac{b}{2a}.',
                                                            'hình_ve': 'plot(x**2 - 2*x + 3, (x, '
                                                                       "-2, 4), title='Parabol y = "
                                                                       "x^2 - 2x + 3')",
                                                            'kí hiệu': 'P: y = ax^2 + bx + c',
                                                            'ví dụ': 'y = x^2 - 2x + 3 \text{ có '
                                                                     'đỉnh } I(1; 2).',
                                                            'định nghĩa': 'Hàm số cho bởi công '
                                                                          'thức y = ax^2 + bx + c '
                                                                          '(a \neq 0). Đồ thị là '
                                                                          'một đường Parabol.'},
                                      'Hàm số lôgarit': {   'hình_ve': 'plot(sp.log(x, sp.E), (x, '
                                                                       "0.1, 5), title='Ham so "
                                                                       "Logarit tu nhien ln(x)')",
                                                            'kí hiệu': 'y = \log_a x',
                                                            'tính_chất': '\text{Tập xác định } D '
                                                                         '= (0; +\infty). \text{ '
                                                                         'Đồ thị đối xứng với hàm '
                                                                         'số mũ qua đường thẳng y '
                                                                         '= x.}',
                                                            'ví dụ': 'y = \ln x \text{ (lôgarit '
                                                                     'tự nhiên cơ số e).}',
                                                            'định nghĩa': 'Hàm số có dạng y = '
                                                                          'log_a(x) với cơ số a '
                                                                          'dương và khác 1.'},
                                      'Hàm số mũ': {   'hình_ve': 'plot(2**x, (0.5)**x, (x, -2, '
                                                                  "2), title='Ham so mu a>1 va "
                                                                  "0<a<1')",
                                                       'kí hiệu': 'y = a^x',
                                                       'tính_chất': '\text{Nếu } a > 1 \text{ '
                                                                    'hàm đồng biến; nếu } 0 < a < '
                                                                    '1 \text{ hàm nghịch biến. '
                                                                    'Luôn đi qua (0;1).}',
                                                       'ví dụ': 'y = 2^x \text{ tăng trưởng rất '
                                                                'nhanh khi x tăng.}',
                                                       'định nghĩa': 'Hàm số có dạng y = a^x với '
                                                                     'cơ số a dương và khác 1.'},
                                      'Lôgarit': {   'công thức': [   '\log_a (MN) = \log_a M + '
                                                                      '\log_a N',
                                                                      '\log_a (\frac{M}{N}) = '
                                                                      '\log_a M - \log_a N',
                                                                      '\log_a M^\alpha = \alpha '
                                                                      '\log_a M',
                                                                      '\log_a b = \frac{\log_c '
                                                                      'b}{\log_c a} \text{ (Đổi '
                                                                      'cơ số)}'],
                                                     'hình_ve': 'plot(sp.log(x, 2), (x, 0.1, 5), '
                                                                "title='Do thi ham so Logarit')",
                                                     'kí hiệu': '\log_a b = \alpha '
                                                                '\Leftrightarrow a^\alpha = b '
                                                                '\text{ (với } 0 < a \neq 1, b > '
                                                                '0 \text{)}',
                                                     'ví dụ': '\log_2 8 = 3 \text{ vì } 2^3 = 8.',
                                                     'định nghĩa': 'Lôgarit cơ số a của b là số mũ '
                                                                   'alpha sao cho a mũ alpha bằng '
                                                                   'b.'},
                                      'Phép tính lũy thừa': {   'công thức': [   'a^m \cdot a^n = '
                                                                                 'a^{m+n}',
                                                                                 '\frac{a^m}{a^n} '
                                                                                 '= a^{m-n}',
                                                                                 '(a^m)^n = a^{m '
                                                                                 '\cdot n}',
                                                                                 '\sqrt[n]{a^m} = '
                                                                                 'a^{\frac{m}{n}}'],
                                                                'hình_ve': 'plot(x**2, x**3, (x, '
                                                                           "0, 2), title='Cac ham "
                                                                           "luy thua co ban')",
                                                                'kí hiệu': 'a^\alpha \text{ (a '
                                                                           'là cơ số, } \alpha '
                                                                           '\text{ là số mũ)}',
                                                                'ví dụ': '8^{\frac{2}{3}} = '
                                                                         '\sqrt[3]{8^2} = '
                                                                         '\sqrt[3]{64} = 4.',
                                                                'định nghĩa': 'Mở rộng khái niệm '
                                                                              'lũy thừa từ số mũ '
                                                                              'nguyên sang số mũ '
                                                                              'hữu tỉ và số thực.'},
                                      'Phương trình mũ và lôgarit cơ bản': {   'công thức': [   'a^x '
                                                                                                '= '
                                                                                                'b '
                                                                                                '\Leftrightarrow '
                                                                                                'x '
                                                                                                '= '
                                                                                                '\log_a '
                                                                                                'b '
                                                                                                '\text{ '
                                                                                                '(với '
                                                                                                'b '
                                                                                                '> '
                                                                                                '0)}',
                                                                                                '\log_a '
                                                                                                'x '
                                                                                                '= '
                                                                                                'b '
                                                                                                '\Leftrightarrow '
                                                                                                'x '
                                                                                                '= '
                                                                                                'a^b'],
                                                                               'hình_ve': 'plot(2**x, '
                                                                                          '5, (x, '
                                                                                          '0, 3), '
                                                                                          "title='Giao "
                                                                                          'diem la '
                                                                                          'nghiem '
                                                                                          'cua '
                                                                                          'phuong '
                                                                                          "trinh')",
                                                                               'kí hiệu': 'a^x = '
                                                                                          'b; '
                                                                                          '\log_a '
                                                                                          'x = b',
                                                                               'ví dụ': '2^x = 5 '
                                                                                        '\Leftrightarrow '
                                                                                        'x = '
                                                                                        '\log_2 '
                                                                                        '5.',
                                                                               'định nghĩa': 'Giải '
                                                                                             'phương '
                                                                                             'trình '
                                                                                             'tìm '
                                                                                             'x '
                                                                                             'nằm '
                                                                                             'ở vị '
                                                                                             'trí '
                                                                                             'số '
                                                                                             'mũ '
                                                                                             'hoặc '
                                                                                             'trong '
                                                                                             'biểu '
                                                                                             'thức '
                                                                                             'lôgarit.'},
                                      'Sự biến thiên của hàm số': {   'công thức': '\frac{f(x_2) '
                                                                                   '- f(x_1)}{x_2 '
                                                                                   '- x_1} > 0 '
                                                                                   '\Rightarrow '
                                                                                   '\text{Hàm số '
                                                                                   'đồng biến.}',
                                                                      'hình_ve': 'plot(2*x + 1, '
                                                                                 '(x, -5, 5), '
                                                                                 "title='Ham so "
                                                                                 'dong bien y = 2x '
                                                                                 "+ 1')",
                                                                      'kí hiệu': 'x_1 < x_2 '
                                                                                 '\Rightarrow '
                                                                                 'f(x_1) < f(x_2) '
                                                                                 '\text{ (đồng '
                                                                                 'biến)}',
                                                                      'ví dụ': 'y = 2x + 1 \text{ '
                                                                               'đồng biến trên } '
                                                                               '\mathbb{R} '
                                                                               '\text{ vì } a = 2 '
                                                                               '> 0.',
                                                                      'định nghĩa': 'Hàm số đồng '
                                                                                    'biến (tăng) '
                                                                                    'nếu x tăng '
                                                                                    'thì y tăng. '
                                                                                    'Hàm số nghịch '
                                                                                    'biến (giảm) '
                                                                                    'nếu x tăng '
                                                                                    'thì y giảm.'},
                                      'Đồ thị hàm số bậc hai': {   'công thức': '\Delta = b^2 - '
                                                                                '4ac',
                                                                   'hình_ve': 'plot(x**2, -x**2, '
                                                                              '(x, -3, 3), '
                                                                              "title='Be lom cua "
                                                                              'Parabol (a>0 va '
                                                                              "a<0)')",
                                                                   'kí hiệu': 'a > 0 \cup, a < 0 '
                                                                              '\cap',
                                                                   'ví dụ': 'y = -x^2 \text{ có '
                                                                            'bề lõm quay xuống '
                                                                            'dưới và đỉnh là gốc '
                                                                            'tọa độ } O(0;0).',
                                                                   'định nghĩa': 'Bề lõm hướng lên '
                                                                                 'trên nếu a > 0, '
                                                                                 'hướng xuống dưới '
                                                                                 'nếu a < 0.'}},
    'Hình học Không gian': {   'Giao tuyến của hai mặt phẳng': {   'công thức': '\begin{cases} A '
                                                                                '\in (P) \cap '
                                                                                '(Q) \\ B \in '
                                                                                '(P) \cap (Q) '
                                                                                '\end{cases} '
                                                                                '\Rightarrow AB = '
                                                                                '(P) \cap (Q)',
                                                                   'hình_ve': 'sp.plotting.plot3d(x '
                                                                              '+ y, (x, -1, 1), '
                                                                              '(y, -1, 1), '
                                                                              'show=False)',
                                                                   'kí hiệu': 'd = (P) \cap (Q)',
                                                                   'ví dụ': '\text{Giao tuyến của '
                                                                            '(SAB) và (SAD) trong '
                                                                            'hình chóp là SA.}',
                                                                   'định nghĩa': 'Đường thẳng '
                                                                                 'chung của hai '
                                                                                 'mặt phẳng phân '
                                                                                 'biệt. Để tìm '
                                                                                 'giao tuyến, ta '
                                                                                 'tìm hai điểm '
                                                                                 'chung phân '
                                                                                 'biệt.'},
                               'Góc trong không gian': {   'công thức': '0^\circ \le \varphi '
                                                                        '\le 90^\circ; \cos '
                                                                        '\varphi \text{ tính qua '
                                                                        'tích vô hướng vectơ.}',
                                                           'hình_ve': 'sp.plotting.plot3d_parametric_line(t, '
                                                                      't, 0, (t, 0, 1))',
                                                           'kí hiệu': '\varphi = (d, (P)) = (d, '
                                                                      "d')",
                                                           'ví dụ': '\text{Góc giữa cạnh bên và '
                                                                    'mặt đáy trong hình chóp đều.}',
                                                           'định nghĩa': 'Góc giữa đường thẳng và '
                                                                         'mặt phẳng là góc giữa '
                                                                         'đường thẳng đó và hình '
                                                                         'chiếu của nó trên mặt '
                                                                         'phẳng.'},
                               'Hai mặt phẳng song song': {   'công thức': '\begin{cases} a, b '
                                                                           '\subset (P), a \cap '
                                                                           'b = \{I\} \\ a '
                                                                           '\parallel (Q), b '
                                                                           '\parallel (Q) '
                                                                           '\end{cases} '
                                                                           '\Rightarrow (P) '
                                                                           '\parallel (Q)',
                                                              'hình_ve': 'sp.plotting.plot3d((1, '
                                                                         '(x, -1, 1), (y, -1, 1)), '
                                                                         '(2, (x, -1, 1), (y, -1, '
                                                                         '1)), show=False)',
                                                              'kí hiệu': '(P) \parallel (Q)',
                                                              'ví dụ': '\text{Hai mặt đáy của '
                                                                       'hình lăng trụ song song '
                                                                       'với nhau.}',
                                                              'định nghĩa': 'Hai mặt phẳng không '
                                                                            'có điểm chung.'},
                               'Hai mặt phẳng vuông góc': {   'công thức': '\begin{cases} d '
                                                                           '\perp (Q) \\ d '
                                                                           '\subset (P) '
                                                                           '\end{cases} '
                                                                           '\Rightarrow (P) '
                                                                           '\perp (Q)',
                                                              'hình_ve': 'sp.plotting.plot3d(0, '
                                                                         '(x, -1, 1), (y, -1, 1), '
                                                                         'show=False)',
                                                              'kí hiệu': '(P) \perp (Q)',
                                                              'ví dụ': '\text{Mặt bên (SAB) vuông '
                                                                       'góc với mặt đáy (ABC) nếu '
                                                                       'đường cao SH vuông góc với '
                                                                       'đáy.}',
                                                              'định nghĩa': 'Hai mặt phẳng gọi là '
                                                                            'vuông góc với nhau '
                                                                            'nếu mặt phẳng này '
                                                                            'chứa một đường thẳng '
                                                                            'vuông góc với mặt '
                                                                            'phẳng kia.'},
                               'Hình lăng trụ và Hình chóp cụt': {   'công thức': '\text{Các mặt '
                                                                                  'bên của hình '
                                                                                  'lăng trụ là các '
                                                                                  'hình bình '
                                                                                  'hành.}',
                                                                     'hình_ve': 'sp.plotting.plot3d_parametric_line((0, '
                                                                                '0, t), (1, 0, t), '
                                                                                '(0, 1, t), (t, 0, '
                                                                                '1))',
                                                                     'kí hiệu': "ABC.A'B'C' "
                                                                                '\text{ (Lăng trụ '
                                                                                'tam giác)}',
                                                                     'ví dụ': '\text{Hình hộp là '
                                                                              'một trường hợp đặc '
                                                                              'biệt của hình lăng '
                                                                              'trụ có đáy là hình '
                                                                              'bình hành.}',
                                                                     'định nghĩa': 'Hình lăng trụ '
                                                                                   'có hai đáy là '
                                                                                   'hai đa giác '
                                                                                   'bằng nhau và '
                                                                                   'nằm trên hai '
                                                                                   'mặt phẳng song '
                                                                                   'song, các cạnh '
                                                                                   'bên song song '
                                                                                   'và bằng nhau.'},
                               'Khoảng cách trong không gian': {   'công thức': '\text{Khoảng '
                                                                                'cách giữa hai '
                                                                                'đường thẳng chéo '
                                                                                'nhau là độ dài '
                                                                                'đoạn vuông góc '
                                                                                'chung.}',
                                                                   'hình_ve': 'sp.plotting.plot3d_parametric_line(0, '
                                                                              '0, t, (t, 0, 1))',
                                                                   'kí hiệu': 'd(M, (P)) = MH '
                                                                              '\text{ (với } H '
                                                                              '\text{ là hình '
                                                                              'chiếu của } M '
                                                                              '\text{ trên } '
                                                                              '(P)\text{)}',
                                                                   'ví dụ': '\text{Tính chiều cao '
                                                                            'hình chóp chính là '
                                                                            'tính } d(S, (ABC)).',
                                                                   'định nghĩa': 'Khoảng cách từ '
                                                                                 'điểm M đến mặt '
                                                                                 'phẳng (P) là độ '
                                                                                 'dài đoạn vuông '
                                                                                 'góc kẻ từ M đến '
                                                                                 '(P).'},
                               'Phép chiếu song song': {   'công thức': '\text{Bảo toàn tính '
                                                                        'thẳng hàng, thứ tự điểm '
                                                                        'và tỉ số độ dài đoạn '
                                                                        'thẳng song song.}',
                                                           'hình_ve': 'sp.plotting.plot3d(x, (x, '
                                                                      '-1, 1), (y, -1, 1), '
                                                                      'show=False)',
                                                           'kí hiệu': "pr_{(P), l} (M) = M'",
                                                           'ví dụ': '\text{Hình biểu diễn của '
                                                                    'hình vuông qua phép chiếu '
                                                                    'song song là hình bình hành.}',
                                                           'định nghĩa': 'Phép đặt tương ứng mỗi '
                                                                         'điểm M trong không gian '
                                                                         "với điểm M' trên mặt "
                                                                         'phẳng (P) theo phương l '
                                                                         'của đường thẳng cắt '
                                                                         '(P).'},
                               'Thiết diện': {   'công thức': '\text{Tìm các đoạn giao tuyến của '
                                                              'mặt phẳng (P) với từng mặt của hình '
                                                              'khối cho đến khi khép kín.}',
                                                 'hình_ve': 'sp.plotting.plot3d(x + y, (x, -1, 1), '
                                                            '(y, -1, 1), show=False)',
                                                 'kí hiệu': 'H = (P) \cap \text{Hình khối}',
                                                 'ví dụ': '\text{Thiết diện của hình chóp tứ giác '
                                                          'cắt bởi mặt phẳng song song với đáy là '
                                                          'một tứ giác.}',
                                                 'định nghĩa': 'Giao của một mặt phẳng với các mặt '
                                                               'của một hình khối (hình chóp, hình '
                                                               'lăng trụ). Thiết diện là một đa '
                                                               'giác.'},
                               'Điểm, đường thẳng và mặt phẳng': {   'công thức': '\text{Ba cách '
                                                                                  'xác định mặt '
                                                                                  'phẳng: (3 '
                                                                                  'điểm), (đường + '
                                                                                  'điểm), (2 đường '
                                                                                  'cắt nhau).}',
                                                                     'hình_ve': 'sp.plotting.plot3d_parametric_line(t, '
                                                                                't, t, (t, 0, 1))',
                                                                     'kí hiệu': 'A, B \in '
                                                                                '\Delta; \Delta '
                                                                                '\subset (P); (P) '
                                                                                '\equiv (ABC)',
                                                                     'ví dụ': '\text{Hình chóp '
                                                                              'S.ABCD có các mặt '
                                                                              'bên là (SAB), '
                                                                              '(SBC),...}',
                                                                     'định nghĩa': 'Các đối tượng '
                                                                                   'cơ bản của '
                                                                                   'hình học không '
                                                                                   'gian. Một mặt '
                                                                                   'phẳng được xác '
                                                                                   'định bởi 3 '
                                                                                   'điểm không '
                                                                                   'thẳng hàng, '
                                                                                   'hoặc 1 đường '
                                                                                   'thẳng và 1 '
                                                                                   'điểm ngoài '
                                                                                   'nó.'},
                               'Đường thẳng song song với mặt phẳng': {   'công thức': '\begin{cases} '
                                                                                       'd '
                                                                                       '\not\subset '
                                                                                       '(P) \\ d '
                                                                                       '\parallel '
                                                                                       "d' \\ d' "
                                                                                       '\subset '
                                                                                       '(P) '
                                                                                       '\end{cases} '
                                                                                       '\Rightarrow '
                                                                                       'd '
                                                                                       '\parallel '
                                                                                       '(P)',
                                                                          'hình_ve': 'sp.plotting.plot3d(0, '
                                                                                     '(x, -1, 1), '
                                                                                     '(y, -1, 1), '
                                                                                     'show=False)',
                                                                          'kí hiệu': 'd \parallel '
                                                                                     '(P)',
                                                                          'ví dụ': '\text{Trong '
                                                                                   'hình hộp, cạnh '
                                                                                   'trên song song '
                                                                                   'với mặt đáy.}',
                                                                          'định nghĩa': 'Đường '
                                                                                        'thẳng và '
                                                                                        'mặt phẳng '
                                                                                        'không có '
                                                                                        'điểm '
                                                                                        'chung.'},
                               'Đường thẳng song song với đường thẳng': {   'công thức': '\text{Định '
                                                                                         'lý 3 '
                                                                                         'đường '
                                                                                         'giao '
                                                                                         'tuyến: } '
                                                                                         '\begin{cases} '
                                                                                         '(P) '
                                                                                         '\cap '
                                                                                         '(Q) = a '
                                                                                         '\\ (Q) '
                                                                                         '\cap '
                                                                                         '(R) = b '
                                                                                         '\\ (R) '
                                                                                         '\cap '
                                                                                         '(P) = c '
                                                                                         '\end{cases} '
                                                                                         '\Rightarrow '
                                                                                         'a, b, c '
                                                                                         '\parallel '
                                                                                         '\text{ '
                                                                                         'hoặc '
                                                                                         'đồng '
                                                                                         'quy.}',
                                                                            'hình_ve': 'sp.plotting.plot3d_parametric_line((t, '
                                                                                       '0, 0), (t, '
                                                                                       '1, 0), (t, '
                                                                                       '0, 1))',
                                                                            'kí hiệu': 'a '
                                                                                       '\parallel '
                                                                                       'b, a '
                                                                                       '\text{ '
                                                                                       'chéo } b',
                                                                            'ví dụ': '\text{Trong '
                                                                                     'hình chóp có '
                                                                                     'đáy là hình '
                                                                                     'bình hành, '
                                                                                     'các cặp cạnh '
                                                                                     'đối diện của '
                                                                                     'đáy song '
                                                                                     'song với '
                                                                                     'nhau.}',
                                                                            'định nghĩa': 'Hai '
                                                                                          'đường '
                                                                                          'thẳng '
                                                                                          'cùng '
                                                                                          'nằm '
                                                                                          'trong '
                                                                                          'một mặt '
                                                                                          'phẳng '
                                                                                          'và '
                                                                                          'không '
                                                                                          'có điểm '
                                                                                          'chung. '
                                                                                          'Trong '
                                                                                          'không '
                                                                                          'gian, '
                                                                                          'hai '
                                                                                          'đường '
                                                                                          'thẳng '
                                                                                          'không '
                                                                                          'cùng '
                                                                                          'nằm '
                                                                                          'trong '
                                                                                          'một mặt '
                                                                                          'phẳng '
                                                                                          'gọi là '
                                                                                          'chéo '
                                                                                          'nhau.'},
                               'Đường thẳng vuông góc với mặt phẳng': {   'công thức': '\begin{cases} '
                                                                                       'd \perp '
                                                                                       'a, d '
                                                                                       '\perp b '
                                                                                       '\\ a, b '
                                                                                       '\subset '
                                                                                       '(P), a '
                                                                                       '\cap b = '
                                                                                       '\{I\} '
                                                                                       '\end{cases} '
                                                                                       '\Rightarrow '
                                                                                       'd \perp '
                                                                                       '(P)',
                                                                          'hình_ve': 'sp.plotting.plot3d_parametric_line(0, '
                                                                                     '0, t, (t, 0, '
                                                                                     '2))',
                                                                          'kí hiệu': 'd \perp (P)',
                                                                          'ví dụ': '\text{Trong '
                                                                                   'hình chóp '
                                                                                   'S.ABC, nếu } '
                                                                                   'SA \perp '
                                                                                   '(ABC) \text{ '
                                                                                   'thì SA vuông '
                                                                                   'góc với AB, BC '
                                                                                   'và AC.}',
                                                                          'định nghĩa': 'Một đường '
                                                                                        'thẳng '
                                                                                        'được gọi '
                                                                                        'là vuông '
                                                                                        'góc với '
                                                                                        'mặt phẳng '
                                                                                        'nếu nó '
                                                                                        'vuông góc '
                                                                                        'với mọi '
                                                                                        'đường '
                                                                                        'thẳng nằm '
                                                                                        'trong mặt '
                                                                                        'phẳng '
                                                                                        'đó.'},
                               'Định lý Thales trong không gian': {   'công thức': '\text{Nếu } '
                                                                                   '(P) \parallel '
                                                                                   '(Q) \parallel '
                                                                                   '(R) \text{ '
                                                                                   'cắt hai đường '
                                                                                   "thẳng d, d' "
                                                                                   'lần lượt tại '
                                                                                   "A, B, C và A', "
                                                                                   "B', C'.}",
                                                                      'hình_ve': 'sp.plotting.plot3d((1, '
                                                                                 '(x, -1, 1), (y, '
                                                                                 '-1, 1)), (2, (x, '
                                                                                 '-1, 1), (y, -1, '
                                                                                 '1)), (3, (x, -1, '
                                                                                 '1), (y, -1, 1)), '
                                                                                 'show=False)',
                                                                      'kí hiệu': "\frac{AB}{A'B'} "
                                                                                 '= '
                                                                                 "\frac{BC}{B'C'} "
                                                                                 '= '
                                                                                 "\frac{AC}{A'C'}",
                                                                      'ví dụ': '\text{Ứng dụng để '
                                                                               'tính độ dài đoạn '
                                                                               'thẳng trong các '
                                                                               'bài toán lăng trụ '
                                                                               'cắt bởi mặt '
                                                                               'phẳng.}',
                                                                      'định nghĩa': 'Ba mặt phẳng '
                                                                                    'đôi một song '
                                                                                    'song chắn '
                                                                                    'trên hai cát '
                                                                                    'tuyến bất kỳ '
                                                                                    'những đoạn '
                                                                                    'thẳng tương '
                                                                                    'ứng tỉ lệ.'},
                               'Định lý ba đường vuông góc': {   'công thức': '\text{Giúp xác '
                                                                              'định góc giữa đường '
                                                                              'thẳng và mặt '
                                                                              'phẳng.}',
                                                                 'hình_ve': 'sp.plotting.plot3d_parametric_line(t, '
                                                                            '0, t, (t, 0, 1))',
                                                                 'kí hiệu': 'b \perp a '
                                                                            '\Leftrightarrow b '
                                                                            "\perp a'",
                                                                 'ví dụ': '\text{Dùng để chứng '
                                                                          'minh các cạnh bên vuông '
                                                                          'góc với các đường chéo '
                                                                          'của đáy.}',
                                                                 'định nghĩa': 'Cho đường thẳng a '
                                                                               'không vuông góc '
                                                                               'với (P) và đường '
                                                                               'thẳng b nằm trong '
                                                                               '(P). b vuông góc '
                                                                               'với a khi và chỉ '
                                                                               'khi b vuông góc '
                                                                               "với hình chiếu a' "
                                                                               'của a trên (P).'}},
    'Hình học Phẳng và Hệ thức lượng': {   '5 Công thức tính diện tích tam giác': {   'công thức': '1. '
                                                                                                   'S '
                                                                                                   '= '
                                                                                                   '\frac{1}{2}ah_a; '
                                                                                                   '2. '
                                                                                                   'S '
                                                                                                   '= '
                                                                                                   '\frac{1}{2}bc\sin '
                                                                                                   'A; '
                                                                                                   '3. '
                                                                                                   'S '
                                                                                                   '= '
                                                                                                   '\frac{abc}{4R}; '
                                                                                                   '4. '
                                                                                                   'S '
                                                                                                   '= '
                                                                                                   'pr; '
                                                                                                   '5. '
                                                                                                   'S '
                                                                                                   '= '
                                                                                                   '\sqrt{p(p-a)(p-b)(p-c)}',
                                                                                      'hình_ve': 'sp.plot_implicit(sp.And(y '
                                                                                                 '> '
                                                                                                 '0, '
                                                                                                 'y '
                                                                                                 '< '
                                                                                                 '1 '
                                                                                                 '- '
                                                                                                 'sp.abs(x)), '
                                                                                                 '(x, '
                                                                                                 '-1, '
                                                                                                 '1), '
                                                                                                 '(y, '
                                                                                                 '-0.1, '
                                                                                                 '1.2), '
                                                                                                 "title='Mien "
                                                                                                 'dien '
                                                                                                 'tich '
                                                                                                 'tam '
                                                                                                 "giac')",
                                                                                      'kí hiệu': 'S, '
                                                                                                 'p, '
                                                                                                 'R, '
                                                                                                 'r, '
                                                                                                 'h_a',
                                                                                      'ví dụ': '\text{Tam '
                                                                                               'giác '
                                                                                               'có '
                                                                                               '} '
                                                                                               'a=13, '
                                                                                               'b=14, '
                                                                                               'c=15 '
                                                                                               '\Rightarrow '
                                                                                               'p=21, '
                                                                                               'S=84.',
                                                                                      'định nghĩa': 'Các '
                                                                                                    'biến '
                                                                                                    'thể '
                                                                                                    'tính '
                                                                                                    'diện '
                                                                                                    'tích '
                                                                                                    '(S) '
                                                                                                    'tùy '
                                                                                                    'theo '
                                                                                                    'dữ '
                                                                                                    'kiện '
                                                                                                    'đầu '
                                                                                                    'bài.'},
                                           'Bảng dấu và Tính chất đặc biệt': {   'công thức': '\sin(180^\circ '
                                                                                              '- '
                                                                                              '\alpha) '
                                                                                              '= '
                                                                                              '\sin '
                                                                                              '\alpha, '
                                                                                              '\cos(180^\circ '
                                                                                              '- '
                                                                                              '\alpha) '
                                                                                              '= '
                                                                                              '-\cos '
                                                                                              '\alpha, '
                                                                                              '\tan(180^\circ '
                                                                                              '- '
                                                                                              '\alpha) '
                                                                                              '= '
                                                                                              '-\tan '
                                                                                              '\alpha',
                                                                                 'hình_ve': 'plot(sp.sin(x*sp.pi/180), '
                                                                                            '(x, '
                                                                                            '0, '
                                                                                            '180), '
                                                                                            "title='Do "
                                                                                            'thi '
                                                                                            'ham '
                                                                                            'Sin '
                                                                                            'tu 0 '
                                                                                            'den '
                                                                                            '180 '
                                                                                            "do')",
                                                                                 'kí hiệu': '\text{Góc '
                                                                                            'nhọn '
                                                                                            '(0, '
                                                                                            '90): '
                                                                                            'All '
                                                                                            '(+); '
                                                                                            'Góc '
                                                                                            'tù '
                                                                                            '(90, '
                                                                                            '180): '
                                                                                            'Sin '
                                                                                            '(+), '
                                                                                            'còn '
                                                                                            'lại '
                                                                                            '(-).}',
                                                                                 'ví dụ': '\cos '
                                                                                          '120^\circ '
                                                                                          '= '
                                                                                          '-\cos(180^\circ '
                                                                                          '- '
                                                                                          '120^\circ) '
                                                                                          '= '
                                                                                          '-\cos '
                                                                                          '60^\circ '
                                                                                          '= -0.5',
                                                                                 'định nghĩa': 'Dấu '
                                                                                               'của '
                                                                                               'các '
                                                                                               'giá '
                                                                                               'trị '
                                                                                               'lượng '
                                                                                               'giác '
                                                                                               'phụ '
                                                                                               'thuộc '
                                                                                               'vào '
                                                                                               'góc '
                                                                                               'alpha '
                                                                                               'là '
                                                                                               'nhọn '
                                                                                               'hay '
                                                                                               'tù.'},
                                           'Các hệ thức lượng giác cơ bản': {   'công thức': '1 + '
                                                                                             '\tan^2 '
                                                                                             '\alpha '
                                                                                             '= '
                                                                                             '\frac{1}{\cos^2 '
                                                                                             '\alpha}; '
                                                                                             '1 + '
                                                                                             '\cot^2 '
                                                                                             '\alpha '
                                                                                             '= '
                                                                                             '\frac{1}{\sin^2 '
                                                                                             '\alpha}; '
                                                                                             '\tan '
                                                                                             '\alpha '
                                                                                             '\cdot '
                                                                                             '\cot '
                                                                                             '\alpha '
                                                                                             '= 1',
                                                                                'hình_ve': 'plot(sp.sin(x)**2 '
                                                                                           '+ '
                                                                                           'sp.cos(x)**2, '
                                                                                           '(x, '
                                                                                           '-5, '
                                                                                           '5), '
                                                                                           "title='Tong "
                                                                                           'binh '
                                                                                           'phuong '
                                                                                           'Sin va '
                                                                                           'Cos '
                                                                                           'luon '
                                                                                           'bang '
                                                                                           "1')",
                                                                                'kí hiệu': '\sin^2 '
                                                                                           '\alpha '
                                                                                           '+ '
                                                                                           '\cos^2 '
                                                                                           '\alpha '
                                                                                           '= 1',
                                                                                'ví dụ': '\text{Biết '
                                                                                         '} \sin '
                                                                                         '\alpha '
                                                                                         '= 0.6, 0 '
                                                                                         '< '
                                                                                         '\alpha '
                                                                                         '< '
                                                                                         '90^\circ '
                                                                                         '\Rightarrow '
                                                                                         '\cos '
                                                                                         '\alpha '
                                                                                         '= '
                                                                                         '\sqrt{1 '
                                                                                         '- 0.6^2} '
                                                                                         '= 0.8',
                                                                                'định nghĩa': 'Các '
                                                                                              'đẳng '
                                                                                              'thức '
                                                                                              'liên '
                                                                                              'hệ '
                                                                                              'giữa '
                                                                                              'sin, '
                                                                                              'cos, '
                                                                                              'tan, '
                                                                                              'cot '
                                                                                              'của '
                                                                                              'cùng '
                                                                                              'một '
                                                                                              'góc '
                                                                                              'alpha.'},
                                           'Giá trị lượng giác của một góc': {   'công thức': '\tan '
                                                                                              '\alpha '
                                                                                              '= '
                                                                                              '\frac{\sin '
                                                                                              '\alpha}{\cos '
                                                                                              '\alpha} '
                                                                                              '(\alpha '
                                                                                              '\neq '
                                                                                              '90^\circ), '
                                                                                              '\cot '
                                                                                              '\alpha '
                                                                                              '= '
                                                                                              '\frac{\cos '
                                                                                              '\alpha}{\sin '
                                                                                              '\alpha} '
                                                                                              '(\alpha '
                                                                                              '\neq '
                                                                                              '0^\circ, '
                                                                                              '180^\circ)',
                                                                                 'hình_ve': 'sp.plot_implicit(sp.And(x**2 '
                                                                                            '+ '
                                                                                            'y**2 '
                                                                                            '<= 1, '
                                                                                            'y >= '
                                                                                            '0), '
                                                                                            '(x, '
                                                                                            '-1.5, '
                                                                                            '1.5), '
                                                                                            '(y, '
                                                                                            '-0.5, '
                                                                                            '1.5), '
                                                                                            "title='Nua "
                                                                                            'duong '
                                                                                            'tron '
                                                                                            'don '
                                                                                            "vi')",
                                                                                 'kí hiệu': '\sin '
                                                                                            '\alpha '
                                                                                            '= '
                                                                                            'y_M, '
                                                                                            '\cos '
                                                                                            '\alpha '
                                                                                            '= '
                                                                                            'x_M, '
                                                                                            '\tan '
                                                                                            '\alpha '
                                                                                            '= '
                                                                                            '\frac{y_M}{x_M}, '
                                                                                            '\cot '
                                                                                            '\alpha '
                                                                                            '= '
                                                                                            '\frac{x_M}{y_M}',
                                                                                 'ví dụ': '\text{Với '
                                                                                          '} '
                                                                                          '\alpha '
                                                                                          '= '
                                                                                          '90^\circ '
                                                                                          '\Rightarrow '
                                                                                          'M(0, 1) '
                                                                                          '\Rightarrow '
                                                                                          '\sin '
                                                                                          '90^\circ '
                                                                                          '= 1, '
                                                                                          '\cos '
                                                                                          '90^\circ '
                                                                                          '= 0.',
                                                                                 'định nghĩa': 'Tọa '
                                                                                               'độ '
                                                                                               'của '
                                                                                               'điểm '
                                                                                               'M(x, '
                                                                                               'y) '
                                                                                               'trên '
                                                                                               'nửa '
                                                                                               'đường '
                                                                                               'tròn '
                                                                                               'đơn '
                                                                                               'vị '
                                                                                               'ứng '
                                                                                               'với '
                                                                                               'góc '
                                                                                               'alpha.'},
                                           'Định lí Côsin và Hệ quả': {   'công thức': '\cos A = '
                                                                                       '\frac{b^2 '
                                                                                       '+ c^2 - '
                                                                                       'a^2}{2bc}; '
                                                                                       'm_a^2 = '
                                                                                       '\frac{2(b^2 '
                                                                                       '+ c^2) - '
                                                                                       'a^2}{4} '
                                                                                       '\text{ '
                                                                                       '(Đường '
                                                                                       'trung '
                                                                                       'tuyến)}',
                                                                          'hình_ve': 'plot(sp.Piecewise((x*sp.sqrt(3), '
                                                                                     'sp.And(x>=0, '
                                                                                     'x<=0.5)), '
                                                                                     '(sp.sqrt(3)*(1-x), '
                                                                                     'sp.And(x>0.5, '
                                                                                     'x<=1))), (x, '
                                                                                     '-0.5, 1.5), '
                                                                                     "title='Minh "
                                                                                     'hoa tam giac '
                                                                                     "deu')",
                                                                          'kí hiệu': 'a^2 = b^2 + '
                                                                                     'c^2 - 2bc '
                                                                                     '\cos A',
                                                                          'ví dụ': '\text{Tam '
                                                                                   'giác đều cạnh '
                                                                                   'a } '
                                                                                   '\Rightarrow '
                                                                                   'm_a = '
                                                                                   '\sqrt{\frac{2(a^2 '
                                                                                   '+ a^2) - '
                                                                                   'a^2}{4}} = '
                                                                                   '\frac{a\sqrt{3}}{2}',
                                                                          'định nghĩa': 'Tính cạnh '
                                                                                        'khi biết '
                                                                                        '2 cạnh và '
                                                                                        'góc xen '
                                                                                        'giữa, '
                                                                                        'hoặc tính '
                                                                                        'góc khi '
                                                                                        'biết 3 '
                                                                                        'cạnh.'},
                                           'Định lí Sin': {   'công thức': 'R = \frac{a}{2 \sin '
                                                                           'A}; a = 2R \sin A',
                                                              'hình_ve': 'sp.plot_implicit(x**2 + '
                                                                         'y**2 - 1, (x, -1.2, '
                                                                         '1.2), (y, -1.2, 1.2), '
                                                                         "title='Duong tron ngoai "
                                                                         "tiep ban kinh R=1')",
                                                              'kí hiệu': '\frac{a}{\sin A} = '
                                                                         '\frac{b}{\sin B} = '
                                                                         '\frac{c}{\sin C} = 2R',
                                                              'ví dụ': '\text{Trong tam giác '
                                                                       'vuông tại A, } '
                                                                       '\frac{a}{\sin 90^\circ} '
                                                                       '= 2R \Rightarrow a = 2R '
                                                                       '\text{ (Cạnh huyền là '
                                                                       'đường kính).}',
                                                              'định nghĩa': 'Mối quan hệ giữa '
                                                                            'cạnh, góc đối diện và '
                                                                            'bán kính đường tròn '
                                                                            'ngoại tiếp R.'}},
    'Lượng giác': {   'Công thức lượng giác cơ bản': {   'công thức': '1 + \tan^2\alpha = '
                                                                      '\dfrac{1}{\cos^2\alpha}; '
                                                                      '1 + \cot^2\alpha = '
                                                                      '\dfrac{1}{\sin^2\alpha}',
                                                         'hình_ve': 'sp.plotting.plot(sp.sin(x)**2 '
                                                                    '+ sp.cos(x)**2, (x, -sp.pi, '
                                                                    "sp.pi), title='Do thi f(x) = "
                                                                    "sin^2 + cos^2 = 1')",
                                                         'kí hiệu': '\sin^2\alpha + '
                                                                    '\cos^2\alpha = 1',
                                                         'ví dụ': '\tan \alpha \cdot \cot '
                                                                  '\alpha = 1',
                                                         'định nghĩa': 'Các hệ thức liên hệ mật '
                                                                       'thiết giữa các giá trị '
                                                                       'lượng giác của cùng một '
                                                                       'góc.'},
                      'Giá trị lượng giác của một góc': {   'công thức': '\tan\alpha = '
                                                                         '\dfrac{\sin\alpha}{\cos\alpha}; '
                                                                         '\cot\alpha = '
                                                                         '\dfrac{\cos\alpha}{\sin\alpha}',
                                                            'hình_ve': 'sp.plotting.plot_parametric((t, '
                                                                       '0, (t, 0, 1)), (0, t, (t, '
                                                                       "0, 1)), title='Truc Sin "
                                                                       '(dung) va Truc Cos '
                                                                       "(ngang)')",
                                                            'kí hiệu': '\sin\alpha, '
                                                                       '\cos\alpha, '
                                                                       '\tan\alpha, \cot\alpha',
                                                            'ví dụ': '\sin 30^\circ = 0.5; \cos '
                                                                     '30^\circ = \sqrt{3}/2',
                                                            'định nghĩa': 'Cho góc lượng giác '
                                                                          'alpha, gọi M(x; y) là '
                                                                          'điểm biểu diễn của góc '
                                                                          'này trên đường tròn '
                                                                          'lượng giác đơn vị. Khi '
                                                                          'đó: x = cos(alpha), y = '
                                                                          'sin(alpha).'},
                      'Góc lượng giác': {   'công thức': '\alpha = \widehat{(Ox, Oy)} + '
                                                         'k360^\circ \text{ hoặc } \alpha + '
                                                         'k2\pi',
                                            'hình_ve': 'sp.plotting.plot_parametric(sp.cos(t), '
                                                       "sp.sin(t), (t, 0, sp.pi/3), title='Goc "
                                                       "luong giac duong (60 do)')",
                                            'kí hiệu': '(Ox, Oy), \alpha',
                                            'ví dụ': '\alpha = 60^\circ, \alpha = -30^\circ',
                                            'định nghĩa': 'Là góc có xét đến chiều quay. Góc lượng '
                                                          'giác được xác định bởi tia đầu và tia '
                                                          'cuối.'},
                      'Hàm số y = cos x': {   'công thức': 'D = \mathbb{R}, T = 2\pi',
                                              'hình_ve': 'sp.plotting.plot(sp.cos(x), (x, '
                                                         "-2*sp.pi, 2*sp.pi), title='Do thi ham so "
                                                         "y = cos(x)')",
                                              'kí hiệu': 'y = \cos x',
                                              'ví dụ': '\cos(x + 2\pi) = \cos x',
                                              'định nghĩa': 'Hàm số chẵn, tuần hoàn với chu kỳ '
                                                            '2\pi, tập giá trị [-1; 1].'},
                      'Hàm số y = cot x': {   'công thức': 'D = \mathbb{R} \setminus \{k\pi\}',
                                              'hình_ve': 'sp.plotting.plot(1/sp.tan(x), (x, 0.1, '
                                                         "sp.pi - 0.1), title='Do thi ham so y = "
                                                         "cot(x)')",
                                              'kí hiệu': 'y = \cot x',
                                              'ví dụ': '\cot(\pi/4) = 1',
                                              'định nghĩa': 'Hàm số lẻ, tuần hoàn với chu kỳ '
                                                            '\pi.'},
                      'Hàm số y = sin x': {   'công thức': 'D = \mathbb{R}, T = 2\pi',
                                              'hình_ve': 'sp.plotting.plot(sp.sin(x), (x, '
                                                         "-2*sp.pi, 2*sp.pi), title='Do thi ham so "
                                                         "y = sin(x)')",
                                              'kí hiệu': 'y = \sin x',
                                              'ví dụ': '\sin(x + 2\pi) = \sin x',
                                              'định nghĩa': 'Hàm số lẻ, tuần hoàn với chu kỳ '
                                                            '2\pi, tập giá trị [-1; 1].'},
                      'Hàm số y = tan x': {   'công thức': 'D = \mathbb{R} \setminus '
                                                           '\{\dfrac{\pi}{2} + k\pi\}',
                                              'hình_ve': 'sp.plotting.plot(sp.tan(x), (x, -sp.pi/2 '
                                                         "+ 0.1, sp.pi/2 - 0.1), title='Do thi ham "
                                                         "so y = tan(x)')",
                                              'kí hiệu': 'y = \tan x',
                                              'ví dụ': '\tan(x + \pi) = \tan x',
                                              'định nghĩa': 'Hàm số lẻ, tuần hoàn với chu kỳ '
                                                            '\pi.'},
                      'Phương trình lượng giác cơ bản': {   'công thức': '\sin x = \sin \alpha '
                                                                         '\Leftrightarrow x = '
                                                                         '\alpha + k2\pi \text{ '
                                                                         'hoặc } x = \pi - '
                                                                         '\alpha + k2\pi',
                                                            'hình_ve': 'sp.plotting.plot(sp.sin(x), '
                                                                       '0.5, (x, -2*sp.pi, '
                                                                       "2*sp.pi), title='Giao diem "
                                                                       'sin(x) va duong thang '
                                                                       "y=0.5')",
                                                            'kí hiệu': '\sin x = a, \cos x = a, '
                                                                       '\tan x = a, \cot x = a',
                                                            'ví dụ': '\sin x = 0 \Leftrightarrow '
                                                                     'x = k\pi',
                                                            'định nghĩa': 'Các phương trình có '
                                                                          'dạng f(x) = a với f là '
                                                                          'hàm số lượng giác.'},
                      'Đường tròn lượng giác': {   'công thức': 'x^2 + y^2 = 1',
                                                   'hình_ve': 'sp.plot_implicit(x**2 + y**2 - 1, '
                                                              '(x, -1.5, 1.5), (y, -1.5, 1.5), '
                                                              "title='Duong tron luong giac')",
                                                   'kí hiệu': '(O;1)',
                                                   'ví dụ': 'M(\cos\alpha, \sin\alpha) \text{ '
                                                            'thuộc đường tròn lượng giác.}',
                                                   'định nghĩa': 'Là đường tròn tâm O bán kính 1 '
                                                                 'trong mặt phẳng tọa độ, quy ước '
                                                                 'chiều dương là ngược chiều kim '
                                                                 'đồng hồ.'}},
    'Mệnh đề và Tập hợp': {   'Các tập con của số thực': {   'công thức': '[a; b] = \{x \in '
                                                                          '\mathbb{R} \mid a '
                                                                          '\le x \le b\}',
                                                             'kí hiệu': '(a; b), [a; b], [a; b), '
                                                                        '(a; b]',
                                                             'ví dụ': 'x \in [1; 2] '
                                                                      '\Leftrightarrow 1 \le x '
                                                                      '\le 2',
                                                             'định nghĩa': 'Biểu diễn các khoảng, '
                                                                           'đoạn, nửa khoảng trên '
                                                                           'trục số thực.'},
                              'Lượng từ toán học': {   'công thức': '\overline{\forall x \in X, '
                                                                    'P(x)} \equiv \exists x \in '
                                                                    'X, \overline{P(x)}',
                                                       'kí hiệu': '\forall, \exists',
                                                       'ví dụ': '\forall x \in \mathbb{R}, x^2 '
                                                                '+ 1 > 0.',
                                                       'định nghĩa': 'Sử dụng kí hiệu với mọi và '
                                                                     'tồn tại để biểu thị phạm vi '
                                                                     'của biến.'},
                              'Mệnh đề kéo theo': {   'công thức': 'P \text{ là giả thiết, } Q '
                                                                   '\text{ là kết luận.}',
                                                      'kí hiệu': 'P \Rightarrow Q',
                                                      'ví dụ': '\text{Nếu } a \vdots 6 \text{ '
                                                               'thì } a \vdots 3.',
                                                      'định nghĩa': "Dạng 'Nếu P thì Q'. Chỉ sai "
                                                                    'khi P đúng mà Q sai.'},
                              'Mệnh đề phủ định': {   'công thức': 'P \text{ đúng } '
                                                                   '\Leftrightarrow \overline{P} '
                                                                   '\text{ sai.}',
                                                      'kí hiệu': '\overline{P}',
                                                      'ví dụ': "\overline{P}: \text{'15 không "
                                                               "phải là số lẻ'}.",
                                                      'định nghĩa': 'Mệnh đề phủ định của P được '
                                                                    'thiết lập bằng cách thêm hoặc '
                                                                    "bớt từ 'không' hoặc 'không "
                                                                    "phải' vào trước vị ngữ của "
                                                                    'P.'},
                              'Mệnh đề toán học': {   'công thức': 'P \in \{\text{Đ}, '
                                                                   '\text{S}\}',
                                                      'kí hiệu': 'P, Q, R',
                                                      'ví dụ': "P: \text{'15 là số lẻ' là mệnh đề "
                                                               'đúng.}',
                                                      'định nghĩa': 'Là một câu khẳng định có tính '
                                                                    'đúng hoặc sai rõ ràng. Một '
                                                                    'mệnh đề không thể vừa đúng '
                                                                    'vừa sai.'},
                              'Mệnh đề tương đương': {   'công thức': 'P \Leftrightarrow Q '
                                                                      '\equiv (P \Rightarrow Q) '
                                                                      '\land (Q \Rightarrow P)',
                                                         'kí hiệu': 'P \Leftrightarrow Q',
                                                         'ví dụ': '\text{Tam giác đều } '
                                                                  '\Leftrightarrow \text{ Tam '
                                                                  'giác có 3 cạnh bằng nhau.}',
                                                         'định nghĩa': 'Khi cả hai mệnh đề kéo '
                                                                       'theo thuận và đảo đều '
                                                                       'đúng.'},
                              'Mệnh đề đảo': {   'công thức': '\text{Mệnh đề đảo không nhất thiết '
                                                              'đúng khi mệnh đề thuận đúng.}',
                                                 'kí hiệu': 'Q \Rightarrow P',
                                                 'ví dụ': '\text{Nếu } a \vdots 3 \text{ thì } '
                                                          'a \vdots 6 \text{ (Mệnh đề đảo này '
                                                          'sai)}.',
                                                 'định nghĩa': 'Đảo vị trí của P và Q trong mệnh '
                                                               'đề kéo theo.'},
                              'Phép giao': {   'công thức': 'A \cap B = \{x \mid x \in A '
                                                            '\land x \in B\}',
                                               'kí hiệu': 'A \cap B',
                                               'ví dụ': '[1; 4] \cap [3; 5] = [3; 4]',
                                               'định nghĩa': 'Gồm các phần tử chung của cả hai tập '
                                                             'hợp.'},
                              'Phép hiệu và Phần bù': {   'công thức': 'C_A B = \{x \in A \mid '
                                                                       'x \notin B\} \text{ '
                                                                       '(với } B \subset A '
                                                                       '\text{)}',
                                                          'kí hiệu': 'A \setminus B, C_A B',
                                                          'ví dụ': '\mathbb{R} \setminus '
                                                                   '(-\infty; 0] = (0; +\infty)',
                                                          'định nghĩa': 'Hiệu A \ B là các phần '
                                                                        'tử thuộc A nhưng không '
                                                                        'thuộc B. Phần bù dùng khi '
                                                                        'B là tập con của A.'},
                              'Phép hợp': {   'công thức': 'A \cup B = \{x \mid x \in A \lor '
                                                           'x \in B\}',
                                              'kí hiệu': 'A \cup B',
                                              'ví dụ': '\{1, 2\} \cup \{3, 4\} = \{1, 2, 3, '
                                                       '4\}',
                                              'định nghĩa': 'Gồm các phần tử thuộc ít nhất một '
                                                            'trong hai tập hợp.'},
                              'Quan hệ tập hợp': {   'công thức': 'A = B \Leftrightarrow (A '
                                                                  '\subset B) \land (B \subset '
                                                                  'A)',
                                                     'kí hiệu': 'A \subset B, A = B',
                                                     'ví dụ': '\{1, 2\} \subset \{1, 2, 3\}',
                                                     'định nghĩa': 'A là con B nếu mọi phần tử của '
                                                                   'A đều thuộc B. A bằng B nếu '
                                                                   'chúng có cùng phần tử.'},
                              'Tập hợp': {   'công thức': 'A = \{x \in X \mid P(x)\}',
                                             'kí hiệu': 'a \in A, b \notin A',
                                             'ví dụ': '\mathbb{N} = \{0, 1, 2, 3, \dots\}',
                                             'định nghĩa': 'Một tập hợp bao gồm các đối tượng được '
                                                           'gọi là phần tử.'}},
    'Phương trình và Bất phương trình': {   'Bài toán tối ưu (Quy hoạch tuyến tính)': {   'công thức': '\text{Giá '
                                                                                                       'trị '
                                                                                                       'tối '
                                                                                                       'ưu '
                                                                                                       'luôn '
                                                                                                       'đạt '
                                                                                                       'được '
                                                                                                       'tại '
                                                                                                       'một '
                                                                                                       'trong '
                                                                                                       'các '
                                                                                                       'đỉnh '
                                                                                                       'của '
                                                                                                       'đa '
                                                                                                       'giác '
                                                                                                       'miền '
                                                                                                       'nghiệm.}',
                                                                                          'hình_ve': 'sp.plot_implicit(sp.And(x '
                                                                                                     '>= '
                                                                                                     '0, '
                                                                                                     'y '
                                                                                                     '>= '
                                                                                                     '0, '
                                                                                                     'x '
                                                                                                     '+ '
                                                                                                     'y '
                                                                                                     '<= '
                                                                                                     '1), '
                                                                                                     '(x, '
                                                                                                     '-0.5, '
                                                                                                     '1.5), '
                                                                                                     '(y, '
                                                                                                     '-0.5, '
                                                                                                     '1.5), '
                                                                                                     "title='Da "
                                                                                                     'giac '
                                                                                                     'nghiem '
                                                                                                     '(Tam '
                                                                                                     'giac '
                                                                                                     "OAB)')",
                                                                                          'kí hiệu': 'F(x; '
                                                                                                     'y) '
                                                                                                     '= '
                                                                                                     'ax '
                                                                                                     '+ '
                                                                                                     'by',
                                                                                          'ví dụ': '\text{Tìm '
                                                                                                   'max '
                                                                                                   '} '
                                                                                                   'F '
                                                                                                   '= '
                                                                                                   '2x '
                                                                                                   '+ '
                                                                                                   '3y '
                                                                                                   '\text{ '
                                                                                                   'với '
                                                                                                   '} '
                                                                                                   '(x; '
                                                                                                   'y) '
                                                                                                   '\in '
                                                                                                   '\text{ '
                                                                                                   'miền '
                                                                                                   'tam '
                                                                                                   'giác '
                                                                                                   '} '
                                                                                                   'O(0;0), '
                                                                                                   'A(1;0), '
                                                                                                   'B(0;1).',
                                                                                          'định nghĩa': 'Tìm '
                                                                                                        'giá '
                                                                                                        'trị '
                                                                                                        'lớn '
                                                                                                        'nhất '
                                                                                                        'hoặc '
                                                                                                        'nhỏ '
                                                                                                        'nhất '
                                                                                                        'của '
                                                                                                        'biểu '
                                                                                                        'thức '
                                                                                                        'F '
                                                                                                        '= '
                                                                                                        'ax '
                                                                                                        '+ '
                                                                                                        'by '
                                                                                                        'trên '
                                                                                                        'một '
                                                                                                        'miền '
                                                                                                        'nghiệm '
                                                                                                        'cho '
                                                                                                        'trước.'},
                                            'Bất phương trình bậc nhất hai ẩn': {   'công thức': 'a, '
                                                                                                 'b, '
                                                                                                 'c '
                                                                                                 '\in '
                                                                                                 '\mathbb{R}, '
                                                                                                 'a^2 '
                                                                                                 '+ '
                                                                                                 'b^2 '
                                                                                                 '\neq '
                                                                                                 '0',
                                                                                    'kí hiệu': 'ax '
                                                                                               '+ '
                                                                                               'by '
                                                                                               '\le '
                                                                                               'c',
                                                                                    'ví dụ': '2x + '
                                                                                             '3y > '
                                                                                             '6 '
                                                                                             '\text{ '
                                                                                             'là '
                                                                                             'một '
                                                                                             'bất '
                                                                                             'phương '
                                                                                             'trình '
                                                                                             'bậc '
                                                                                             'nhất '
                                                                                             'hai '
                                                                                             'ẩn.}',
                                                                                    'định nghĩa': 'Là '
                                                                                                  'bất '
                                                                                                  'phương '
                                                                                                  'trình '
                                                                                                  'có '
                                                                                                  'dạng '
                                                                                                  'ax '
                                                                                                  '+ '
                                                                                                  'by '
                                                                                                  '< '
                                                                                                  'c '
                                                                                                  '(hoặc '
                                                                                                  '>, '
                                                                                                  '<=, '
                                                                                                  '>=), '
                                                                                                  'trong '
                                                                                                  'đó '
                                                                                                  'a, '
                                                                                                  'b '
                                                                                                  'không '
                                                                                                  'đồng '
                                                                                                  'thời '
                                                                                                  'bằng '
                                                                                                  '0.'},
                                            'Hệ bất phương trình bậc nhất hai ẩn': {   'công thức': '\text{Miền '
                                                                                                    'nghiệm '
                                                                                                    'là '
                                                                                                    'giao '
                                                                                                    'của '
                                                                                                    'các '
                                                                                                    'miền '
                                                                                                    'nghiệm '
                                                                                                    'của '
                                                                                                    'từng '
                                                                                                    'bất '
                                                                                                    'phương '
                                                                                                    'trình '
                                                                                                    'trong '
                                                                                                    'hệ.}',
                                                                                       'kí hiệu': '\begin{cases} '
                                                                                                  'a_1x '
                                                                                                  '+ '
                                                                                                  'b_1y '
                                                                                                  '\le '
                                                                                                  'c_1 '
                                                                                                  '\\ '
                                                                                                  'a_2x '
                                                                                                  '+ '
                                                                                                  'b_2y '
                                                                                                  '\le '
                                                                                                  'c_2 '
                                                                                                  '\end{cases}',
                                                                                       'ví dụ': '\text{Hệ: '
                                                                                                '} '
                                                                                                '\{x '
                                                                                                '\ge '
                                                                                                '0, '
                                                                                                'y '
                                                                                                '\ge '
                                                                                                '0, '
                                                                                                'x '
                                                                                                '+ '
                                                                                                'y '
                                                                                                '\le '
                                                                                                '2\}',
                                                                                       'định nghĩa': 'Gồm '
                                                                                                     'hai '
                                                                                                     'hay '
                                                                                                     'nhiều '
                                                                                                     'bất '
                                                                                                     'phương '
                                                                                                     'trình '
                                                                                                     'bậc '
                                                                                                     'nhất '
                                                                                                     'hai '
                                                                                                     'ẩn '
                                                                                                     'được '
                                                                                                     'xét '
                                                                                                     'đồng '
                                                                                                     'thời.'},
                                            'Miền nghiệm của bất phương trình': {   'công thức': '\text{Cách '
                                                                                                 'xác '
                                                                                                 'định: '
                                                                                                 'Vẽ '
                                                                                                 'đường '
                                                                                                 'thẳng '
                                                                                                 '} '
                                                                                                 'd: '
                                                                                                 'ax '
                                                                                                 '+ '
                                                                                                 'by '
                                                                                                 '= '
                                                                                                 'c, '
                                                                                                 '\text{ '
                                                                                                 'thử '
                                                                                                 'một '
                                                                                                 'điểm '
                                                                                                 '} '
                                                                                                 'M '
                                                                                                 '\notin '
                                                                                                 'd.',
                                                                                    'hình_ve': 'sp.plot_implicit(x '
                                                                                               '+ '
                                                                                               'y '
                                                                                               '< '
                                                                                               '1, '
                                                                                               '(x, '
                                                                                               '-2, '
                                                                                               '2), '
                                                                                               '(y, '
                                                                                               '-2, '
                                                                                               '2), '
                                                                                               "title='Mien "
                                                                                               'nghiem: '
                                                                                               'x '
                                                                                               '+ '
                                                                                               'y '
                                                                                               '< '
                                                                                               "1')",
                                                                                    'kí hiệu': 'S '
                                                                                               '= '
                                                                                               '\{(x, '
                                                                                               'y) '
                                                                                               '\in '
                                                                                               '\mathbb{R}^2 '
                                                                                               '\mid '
                                                                                               'ax '
                                                                                               '+ '
                                                                                               'by '
                                                                                               '< '
                                                                                               'c\}',
                                                                                    'ví dụ': '\text{Miền '
                                                                                             'nghiệm '
                                                                                             'của '
                                                                                             '} x '
                                                                                             '+ y '
                                                                                             '< 1 '
                                                                                             '\text{ '
                                                                                             'là '
                                                                                             'nửa '
                                                                                             'mặt '
                                                                                             'phẳng '
                                                                                             'chứa '
                                                                                             'gốc '
                                                                                             'tọa '
                                                                                             'độ } '
                                                                                             'O(0;0) '
                                                                                             '\text{ '
                                                                                             'bỏ '
                                                                                             'biên.}',
                                                                                    'định nghĩa': 'Tập '
                                                                                                  'hợp '
                                                                                                  'các '
                                                                                                  'cặp '
                                                                                                  'số '
                                                                                                  '(x; '
                                                                                                  'y) '
                                                                                                  'làm '
                                                                                                  'cho '
                                                                                                  'bất '
                                                                                                  'phương '
                                                                                                  'trình '
                                                                                                  'đúng. '
                                                                                                  'Trên '
                                                                                                  'mặt '
                                                                                                  'phẳng '
                                                                                                  'tọa '
                                                                                                  'độ, '
                                                                                                  'miền '
                                                                                                  'nghiệm '
                                                                                                  'thường '
                                                                                                  'là '
                                                                                                  'một '
                                                                                                  'nửa '
                                                                                                  'mặt '
                                                                                                  'phẳng.'},
                                            'Miền nghiệm của hệ (Đa giác nghiệm)': {   'công thức': '\text{Các '
                                                                                                    'đỉnh '
                                                                                                    'của '
                                                                                                    'đa '
                                                                                                    'giác '
                                                                                                    'là '
                                                                                                    'giao '
                                                                                                    'điểm '
                                                                                                    'của '
                                                                                                    'các '
                                                                                                    'đường '
                                                                                                    'thẳng '
                                                                                                    'biên.}',
                                                                                       'kí hiệu': '\text{Miền '
                                                                                                  'đa '
                                                                                                  'giác '
                                                                                                  '} '
                                                                                                  'ABCD',
                                                                                       'ví dụ': '\text{Hệ '
                                                                                                '} '
                                                                                                '\{x '
                                                                                                '\ge '
                                                                                                '0, '
                                                                                                'y '
                                                                                                '\ge '
                                                                                                '0, '
                                                                                                'x+y '
                                                                                                '\le '
                                                                                                '1\} '
                                                                                                '\text{ '
                                                                                                'có '
                                                                                                'miền '
                                                                                                'nghiệm '
                                                                                                'là '
                                                                                                'tam '
                                                                                                'giác '
                                                                                                'vuông '
                                                                                                'OAB.}',
                                                                                       'định nghĩa': 'Miền '
                                                                                                     'nghiệm '
                                                                                                     'của '
                                                                                                     'hệ '
                                                                                                     'thường '
                                                                                                     'là '
                                                                                                     'một '
                                                                                                     'miền '
                                                                                                     'đa '
                                                                                                     'giác '
                                                                                                     '(có '
                                                                                                     'thể '
                                                                                                     'không '
                                                                                                     'giới '
                                                                                                     'hạn) '
                                                                                                     'trên '
                                                                                                     'mặt '
                                                                                                     'phẳng '
                                                                                                     'tọa '
                                                                                                     'độ.'}},
    'Thống kê': {   'Các định lí về giới hạn': {   'công thức': '\lim (f(x) + g(x)) = \lim f(x) '
                                                                '+ \lim g(x)',
                                                   'kí hiệu': '\lim (f(x) + g(x))',
                                                   'ví dụ': '\lim_{x \to 1} (x^2 + 3x) = 1 + 3 = '
                                                            '4',
                                                   'định nghĩa': 'Các quy tắc tính giới hạn của '
                                                                 'tổng, hiệu, tích, thương.'},
                    'Giới hạn của dãy số': {   'công thức': '\lim_{n \to \infty} u_n = L',
                                               'kí hiệu': '\lim u_n = L',
                                               'ví dụ': '\lim_{n \to \infty} \dfrac{1}{n} = 0',
                                               'định nghĩa': 'Dãy số (u_n) có giới hạn L khi n '
                                                             'tiến tới vô cực nếu u_n tiến gần đến '
                                                             'L.'},
                    'Giới hạn của hàm số tại một điểm': {   'công thức': '\lim_{x \to a} f(x) = '
                                                                         'L',
                                                            'kí hiệu': '\lim_{x \to a} f(x)',
                                                            'ví dụ': '\lim_{x \to 2} (x^2) = 4',
                                                            'định nghĩa': 'Hàm số f(x) có giới hạn '
                                                                          'L khi x tiến tới a nếu '
                                                                          'f(x) tiến gần đến L.'},
                    'Giới hạn hữu hạn của dãy số': {   'công thức': '\lim_{n \to \infty} c = c '
                                                                    '(c là hằng số)',
                                                       'kí hiệu': '\lim_{n \to \infty} u_n = L',
                                                       'ví dụ': '\lim_{n \to \infty} 5 = 5',
                                                       'định nghĩa': 'Dãy số có giới hạn bằng một '
                                                                     'số thực xác định.'},
                    'Giới hạn một bên': {   'công thức': '\lim_{x \to a} f(x) tồn tại ⇔ \lim_{x '
                                                         '\to a^-} f(x) = \lim_{x \to a^+} f(x)',
                                            'kí hiệu': '\lim_{x \to a^-}, \lim_{x \to a^+}',
                                            'ví dụ': '\lim_{x \to 0^+} \dfrac{1}{x} = +\infty',
                                            'định nghĩa': 'Giới hạn khi x tiến đến a từ bên trái '
                                                          'hoặc bên phải.'},
                    'Giới hạn vô cực của dãy số': {   'công thức': '\lim_{n \to \infty} n = '
                                                                   '+\infty',
                                                      'kí hiệu': '\lim u_n = \pm\infty',
                                                      'ví dụ': '\lim_{n \to \infty} (-n) = '
                                                               '-\infty',
                                                      'định nghĩa': 'Dãy số có giá trị tăng hoặc '
                                                                    'giảm không bị chặn.'},
                    'Giới hạn vô cực của hàm số': {   'công thức': '\lim_{x \to +\infty} '
                                                                   '\dfrac{1}{x} = 0',
                                                      'kí hiệu': '\lim_{x \to a} f(x) = '
                                                                 '\pm\infty',
                                                      'ví dụ': '\lim_{x \to 0} \dfrac{1}{x^2} = '
                                                               '+\infty',
                                                      'định nghĩa': 'Hàm số có giá trị tăng hoặc '
                                                                    'giảm không bị chặn khi x tiến '
                                                                    'tới a hoặc vô cực.'},
                    'Mốt': {   'công thức': '\text{Giá trị } x_i \text{ ứng với } n_i = \max '
                                            '\{n_i\}',
                               'hình_ve': 'sp.plotting.plot(sp.Piecewise((1, sp.And(x>0.9, '
                                          'x<1.1)), (2, sp.And(x>1.9, x<2.1)), (3, sp.And(x>2.9, '
                                          "x<3.1)), (0, True)), (x, 0, 4), title='Mo phong bieu do "
                                          "cot (Mode=3)')",
                               'kí hiệu': 'M_o',
                               'ví dụ': '\text{Mẫu: } \{1, 2, 2, 3, 3, 3\} \Rightarrow M_o = 3',
                               'định nghĩa': 'Giá trị xuất hiện với tần số lớn nhất trong mẫu số '
                                             'liệu.'},
                    'Phương sai & Độ lệch chuẩn': {   'công thức': 's = \sqrt{\frac{1}{n} \sum '
                                                                   '(x_i - \bar{x})^2}',
                                                      'hình_ve': 'sp.plotting.plot(sp.exp(-(x-10)**2/2), '
                                                                 'sp.exp(-(x-10)**2/10), (x, 0, '
                                                                 "20), title='Do lech chuan nho "
                                                                 "(cao) va lon (thap)')",
                                                      'kí hiệu': 's^2, s',
                                                      'ví dụ': '\text{Độ lệch chuẩn càng lớn, dữ '
                                                               'liệu càng rời xa số trung bình.}',
                                                      'định nghĩa': 'Số đặc trưng đo mức độ phân '
                                                                    'tán của các số liệu quanh số '
                                                                    'trung bình.'},
                    'Số trung bình': {   'công thức': '\bar{x} = \frac{x_1 + x_2 + ... + x_n}{n} '
                                                      '= \frac{\sum_{i=1}^{k} n_i x_i}{N}',
                                         'hình_ve': 'sp.plotting.plot(sp.Piecewise((0, x < 7), (1, '
                                                    "x == 7), (0, x > 7)), (x, 4, 10), title='Diem "
                                                    "trung binh tai x=7')",
                                         'kí hiệu': '\bar{x}',
                                         'ví dụ': '\text{Mẫu: } \{5, 7, 9\} \Rightarrow '
                                                  '\bar{x} = 7',
                                         'định nghĩa': 'Giá trị trung bình cộng của các số liệu, '
                                                       'dùng để đại diện cho xu thế trung tâm của '
                                                       'mẫu số liệu.'},
                    'Trung vị': {   'công thức': '\text{Nếu n lẻ: } M_e = x_{\frac{n+1}{2}}. '
                                                 '\text{ Nếu n chẵn: } M_e = '
                                                 '\frac{1}{2}(x_{\frac{n}{2}} + '
                                                 'x_{\frac{n}{2}+1})',
                                    'hình_ve': 'sp.plotting.plot(sp.Piecewise((0, x < 3.5), (2, x '
                                               "== 3.5), (0, x > 3.5)), (x, 0, 10), title='Trung "
                                               "vi tai x=3.5')",
                                    'kí hiệu': 'M_e',
                                    'ví dụ': '\text{Mẫu: } \{2, 3, 4, 100\} \Rightarrow M_e = '
                                             '3.5',
                                    'định nghĩa': 'Số đứng ở vị trí giữa của mẫu số liệu sau khi '
                                                  'đã sắp xếp theo thứ tự không giảm.'},
                    'Tứ phân vị': {   'công thức': 'Q_2 = M_e; Q_1 = \text{Trung vị nửa dưới}; '
                                                   'Q_3 = \text{Trung vị nửa trên}',
                                      'hình_ve': "sp.plotting.plot(2, 4, 6, (x, 0, 8), title='Cac "
                                                 "gia tri Q1, Q2, Q3')",
                                      'kí hiệu': 'Q_1, Q_2, Q_3',
                                      'ví dụ': '\text{Mẫu: } \{1, 2, 3, 4, 5, 6, 7\} '
                                               '\Rightarrow Q_1=2, Q_2=4, Q_3=6',
                                      'định nghĩa': 'Ba giá trị chia mẫu số liệu đã sắp xếp thành '
                                                    '4 phần bằng nhau.'},
                    'Xác suất của biến cố': {   'công thức': '0 \le P(A) \le 1',
                                                'hình_ve': 'sp.plot_implicit(sp.Or(x**2 + y**2 < '
                                                           '1, (x-1)**2 + y**2 < 1), (x, -2, 3), '
                                                           "(y, -2, 2), title='Bieu do Venn minh "
                                                           "hoa xac suat')",
                                                'kí hiệu': 'P(A) = n(A)/n(\Omega)',
                                                'ví dụ': 'P(A) = 0.5 \text{ nghĩa là khả năng xảy '
                                                         'ra là 50%.}',
                                                'định nghĩa': 'Tỉ số giữa số kết quả thuận lợi và '
                                                              'tổng số kết quả có thể xảy ra.'}},
    'Tổ hợp, Xác suất': {   'Biến cố': {   'công thức': 'n(A) \text{ là số kết quả thuận lợi cho '
                                                        'biến cố A.}',
                                           'kí hiệu': 'A, B, C \subset \Omega',
                                           'ví dụ': "\text{Gieo con xúc xắc, biến cố A 'số chấm "
                                                    "lẻ': } A = \{1, 3, 5\} \Rightarrow n(A) = "
                                                    '3.',
                                           'định nghĩa': 'Là một tập con của không gian mẫu. Mỗi '
                                                         'phần tử của biến cố được gọi là một kết '
                                                         'quả thuận lợi.'},
                            'Biến cố giao và Biến cố độc lập': {   'công thức': '\text{Nếu A, B '
                                                                                'độc lập: } P(A '
                                                                                '\cap B) = P(A) '
                                                                                '\cdot P(B)',
                                                                   'hình_ve': 'plot(Piecewise((0.2, '
                                                                              'sp.And(x > 0.4, x < '
                                                                              '0.6)), (0, True)), '
                                                                              '(x, 0, 1), '
                                                                              "title='Phan giao "
                                                                              'nhau giua hai bien '
                                                                              "co')",
                                                                   'kí hiệu': 'A \cap B \text{ '
                                                                              'hoặc } A.B',
                                                                   'ví dụ': '\text{Hai người cùng '
                                                                            'bắn vào bia một cách '
                                                                            'độc lập. Xác suất cả '
                                                                            'hai cùng trúng là '
                                                                            'tích xác suất của '
                                                                            'từng người.}',
                                                                   'định nghĩa': 'Hai biến cố độc '
                                                                                 'lập nếu việc xảy '
                                                                                 'ra hay không xảy '
                                                                                 'ra của biến cố '
                                                                                 'này không làm '
                                                                                 'thay đổi xác '
                                                                                 'suất xảy ra của '
                                                                                 'biến cố kia.'},
                            'Biến cố hợp và Quy tắc cộng': {   'công thức': 'P(A \cup B) = P(A) + '
                                                                            'P(B) - P(A \cap B). '
                                                                            '\text{ Nếu A, B xung '
                                                                            'khắc: } P(A \cup B) '
                                                                            '= P(A) + P(B)',
                                                               'hình_ve': 'plot(Piecewise((1, x < '
                                                                          '0.3), (0.5, x < 0.7), '
                                                                          '(0, True)), (x, 0, 1), '
                                                                          "title='Bieu do Venn cho "
                                                                          "Bien co Hop')",
                                                               'kí hiệu': 'A \cup B',
                                                               'ví dụ': '\text{Chọn 1 thẻ từ 10 '
                                                                        "thẻ. A: 'số chẵn', B: 'số "
                                                                        "chia hết cho 5' } "
                                                                        '\Rightarrow A \cup B: '
                                                                        "\text{'số chẵn hoặc chia "
                                                                        "hết cho 5'}.",
                                                               'định nghĩa': 'Biến cố hợp của A và '
                                                                             'B là biến cố xảy ra '
                                                                             'khi có ít nhất một '
                                                                             'trong hai biến cố A '
                                                                             'hoặc B xảy ra.'},
                            'Biến cố không thể và Biến cố chắc chắn': {   'công thức': 'P(\varnothing) '
                                                                                       '= 0; '
                                                                                       'P(\Omega) '
                                                                                       '= 1',
                                                                          'kí hiệu': '\varnothing '
                                                                                     '\text{ '
                                                                                     '(không thể), '
                                                                                     '} \Omega '
                                                                                     '\text{ '
                                                                                     '(chắc chắn)}',
                                                                          'ví dụ': '\text{Gieo '
                                                                                   'xúc xắc mặt 7 '
                                                                                   'chấm là biến '
                                                                                   'cố không thể.}',
                                                                          'định nghĩa': 'Biến cố '
                                                                                        'không bao '
                                                                                        'giờ xảy '
                                                                                        'ra gọi là '
                                                                                        'biến cố '
                                                                                        'không '
                                                                                        'thể. Biến '
                                                                                        'cố luôn '
                                                                                        'luôn xảy '
                                                                                        'ra gọi là '
                                                                                        'biến cố '
                                                                                        'chắc '
                                                                                        'chắn.'},
                            'Biến cố đối': {   'công thức': 'P(\overline{A}) = 1 - P(A)',
                                               'kí hiệu': '\overline{A}',
                                               'ví dụ': '\text{Xác suất bắn trượt = 1 - Xác suất '
                                                        'bắn trúng.}',
                                               'định nghĩa': "Là biến cố 'A không xảy ra'. Nếu A "
                                                             'là một tập con của \Omega thì biến '
                                                             'cố đối là phần bù của A trong '
                                                             '\Omega.'},
                            'Biến cố đối (Nhắc lại và nâng cao)': {   'công thức': 'P(\overline{A}) '
                                                                                   '= 1 - P(A)',
                                                                      'hình_ve': 'plot(1, (x, 0, '
                                                                                 "1), fill={ 'y1': "
                                                                                 '0.3 }, '
                                                                                 "title='Bien co "
                                                                                 'doi la phan bu '
                                                                                 'trong Khong gian '
                                                                                 "mau')",
                                                                      'kí hiệu': '\overline{A}',
                                                                      'ví dụ': '\text{Tính xác '
                                                                               "suất 'có ít nhất "
                                                                               "một lần' thường "
                                                                               'thông qua biến cố '
                                                                               "đối 'không có lần "
                                                                               "nào'.}",
                                                                      'định nghĩa': 'Biến cố đối '
                                                                                    'của A là biến '
                                                                                    "cố 'A không "
                                                                                    "xảy ra'."},
                            'Chỉnh hợp': {   'công thức': 'A_n^k = \frac{n!}{(n-k)!} \text{ (với '
                                                          '} 1 \le k \le n \text{)}',
                                             'hình_ve': 'sp.plotting.plot(sp.ff(x, 3), (x, 3, 10), '
                                                        "title='Chinh hop chap 3 cua n (A_n^3)')",
                                             'kí hiệu': 'A_n^k',
                                             'ví dụ': '\text{Chọn 3 người làm lớp trưởng, lớp '
                                                      'phó, thư ký từ 10 người: } A_{10}^3 = 720.',
                                             'định nghĩa': 'Chọn k phần tử từ n phần tử khác nhau '
                                                           'và sắp xếp chúng theo một thứ tự nhất '
                                                           'định.'},
                            'Các quy tắc tính xác suất cơ bản': {   'công thức': '\text{Thường '
                                                                                 'dùng Hoán vị, '
                                                                                 'Chỉnh hợp, Tổ '
                                                                                 'hợp để đếm phần '
                                                                                 'tử.}',
                                                                    'kí hiệu': '\text{Quy tắc '
                                                                               'cộng, Quy tắc '
                                                                               'nhân}',
                                                                    'ví dụ': '\text{Lấy ngẫu '
                                                                             'nhiên 3 viên bi từ '
                                                                             'túi. Cần tính } '
                                                                             'C_n^k \text{ cho cả '
                                                                             'tử và mẫu.}',
                                                                    'định nghĩa': 'Sử dụng quy tắc '
                                                                                  'cộng và quy tắc '
                                                                                  'nhân từ chương '
                                                                                  'tổ hợp để tìm '
                                                                                  'n(A) và '
                                                                                  'n(\Omega).'},
                            'Giai thừa': {   'công thức': 'n! = n \cdot (n-1) \cdot \dots '
                                                          '\cdot 1; \text{ Quy ước: } 0! = 1',
                                             'hình_ve': "plot(sp.gamma(x+1), (x, 0, 5), title='Ham "
                                                        "Gamma (Giai thua mo rong)')",
                                             'kí hiệu': 'n!',
                                             'ví dụ': '5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 '
                                                      '= 120',
                                             'định nghĩa': 'Tích của n số nguyên dương đầu tiên.'},
                            'Hoán vị': {   'công thức': 'P_n = n!',
                                           'hình_ve': 'sp.plotting.plot(sp.factorial(x), (x, 0, '
                                                      "6), title='Su tang truong cua hoan vi P_n')",
                                           'kí hiệu': 'P_n',
                                           'ví dụ': '\text{Xếp 5 học sinh vào một hàng ngang có } '
                                                    '5! = 120 \text{ cách.}',
                                           'định nghĩa': 'Sắp xếp n phần tử khác nhau vào n vị trí '
                                                         '(có thứ tự).'},
                            'Không gian mẫu': {   'công thức': 'n(\Omega) \text{ là số phần tử '
                                                               'của không gian mẫu.}',
                                                  'kí hiệu': '\Omega',
                                                  'ví dụ': '\text{Gieo 2 đồng xu: } \Omega = '
                                                           '\{SS, SN, NS, NN\} \Rightarrow '
                                                           'n(\Omega) = 4.',
                                                  'định nghĩa': 'Tập hợp tất cả các kết quả có thể '
                                                                'xảy ra của phép thử ngẫu nhiên.'},
                            'Nhị thức Newton': {   'công thức': '(a + b)^n = \sum_{k=0}^{n} C_n^k '
                                                                'a^{n-k} b^k',
                                                   'hình_ve': "print('Tam giac Pascal minh hoa he "
                                                              "so:'); [print([sp.binomial(n, k) "
                                                              'for k in range(n+1)]) for n in '
                                                              'range(6)]',
                                                   'kí hiệu': '(a + b)^n',
                                                   'ví dụ': '(a + b)^n = C_n^0 a^n + C_n^1 '
                                                            'a^{n-1}b + \dots + C_n^n b^n',
                                                   'định nghĩa': 'Công thức khai triển biểu thức '
                                                                 'lũy thừa của một tổng hai số '
                                                                 'hạng.'},
                            'Phép thử ngẫu nhiên': {   'kí hiệu': 'T',
                                                       'ví dụ': '\text{Gieo một đồng xu 2 lần; '
                                                                'Rút một quân bài từ bộ bài 52 '
                                                                'lá.}',
                                                       'định nghĩa': 'Là một hành động hay thực '
                                                                     'nghiệm mà kết quả không thể '
                                                                     'biết trước, nhưng ta biết '
                                                                     'được tập hợp tất cả các kết '
                                                                     'quả có thể xảy ra.'},
                            'Quy tắc cộng': {   'công thức': '\text{Tổng số cách hoàn thành công '
                                                             'việc là: } N = m + n',
                                                'hình_ve': 'sp.plot_implicit(sp.Or(sp.And(x>0, '
                                                           'x<5, y>0, y<1), sp.And(x>6, x<10, y>0, '
                                                           'y<1)), (x, 0, 11), (y, -1, 2), '
                                                           "title='Quy tac cong: Hop cua hai tap "
                                                           "hop roi rac')",
                                                'kí hiệu': 'm + n',
                                                'ví dụ': '\text{Chọn 1 quyển sách từ 5 sách Toán '
                                                         'hoặc 4 sách Lí } \Rightarrow 5 + 4 = 9 '
                                                         '\text{ cách.}',
                                                'định nghĩa': 'Một công việc được hoàn thành bởi '
                                                              'một trong hai phương án độc lập. '
                                                              'Phương án A có m cách, phương án B '
                                                              'có n cách.'},
                            'Quy tắc nhân': {   'công thức': '\text{Tổng số cách hoàn thành công '
                                                             'việc là: } N = m \cdot n',
                                                'hình_ve': 'sp.plot_implicit(sp.And(x >= 1, x <= '
                                                           '3, y >= 1, y <= 2), (x, 0, 4), (y, 0, '
                                                           "3), title='Quy tac nhan: To hop m x "
                                                           "n')",
                                                'kí hiệu': 'm \times n',
                                                'ví dụ': '\text{Chọn một bộ quần áo gồm 3 áo và 2 '
                                                         'quần } \Rightarrow 3 \cdot 2 = 6 '
                                                         '\text{ cách.}',
                                                'định nghĩa': 'Một công việc bao gồm nhiều công '
                                                              'đoạn liên tiếp nhau. Công đoạn 1 có '
                                                              'm cách, công đoạn 2 có n cách.'},
                            'Sơ đồ cây': {   'công thức': '\text{Mỗi nhánh đại diện cho một lựa '
                                                          'chọn tại một công đoạn.}',
                                             'hình_ve': 'sp.plotting.plot_parametric((t, t, (t, 0, '
                                                        "1)), (t, -t, (t, 0, 1)), title='Mo phong "
                                                        "nhanh so do cay')",
                                             'kí hiệu': '\text{Tree}',
                                             'ví dụ': '\text{Liệt kê các kết quả khi tung đồng xu '
                                                      '2 lần liên tiếp.}',
                                             'định nghĩa': 'Công cụ trực quan để liệt kê tất cả '
                                                           'các khả năng của một bài toán đếm.'},
                            'Sơ đồ hình cây trong xác suất': {   'công thức': '\text{Xác suất của '
                                                                              'một nhánh bằng tích '
                                                                              'các xác suất trên '
                                                                              'các đoạn của nhánh '
                                                                              'đó.}',
                                                                 'hình_ve': 'plot(sp.Heaviside(x-0.5), '
                                                                            "(x, 0, 1), title='Mo "
                                                                            'phong phan nhanh xac '
                                                                            "suat')",
                                                                 'kí hiệu': '\text{Tree Diagram}',
                                                                 'ví dụ': '\text{Sử dụng để giải '
                                                                          'các bài toán chẩn đoán '
                                                                          'y khoa hoặc sản xuất '
                                                                          'sản phẩm lỗi.}',
                                                                 'định nghĩa': 'Công cụ trực quan '
                                                                               'để tính xác suất '
                                                                               'của các phép thử '
                                                                               'nhiều giai đoạn.'},
                            'Tam giác Pascal': {   'công thức': 'C_n^k = C_{n-1}^{k-1} + C_{n-1}^k',
                                                   'hình_ve': 'sp.plotting.plot(sp.Piecewise((1, '
                                                              'sp.And(x>0.9, x<1.1)), (4, '
                                                              'sp.And(x>1.9, x<2.1)), (6, '
                                                              'sp.And(x>2.9, x<3.1)), (4, '
                                                              'sp.And(x>3.9, x<4.1)), (1, '
                                                              'sp.And(x>4.9, x<5.1)), (0, True)), '
                                                              "(x, 0, 6), title='He so dong 4 tam "
                                                              "giac Pascal')",
                                                   'kí hiệu': '\text{Pascal Triangle}',
                                                   'ví dụ': '\text{Dòng 4: 1, 4, 6, 4, 1}',
                                                   'định nghĩa': 'Bảng tam giác các hệ số của nhị '
                                                                 'thức Newton.'},
                            'Tổ hợp': {   'công thức': 'C_n^k = \frac{n!}{k!(n-k)!}',
                                          'hình_ve': 'sp.plotting.plot(sp.binomial(x, 3), (x, 3, '
                                                     "10), title='To hop chap 3 cua n (C_n^3)')",
                                          'kí hiệu': 'C_n^k \text{ hoặc } \binom{n}{k}',
                                          'ví dụ': '\text{Chọn 3 người đi trực nhật từ 10 người: '
                                                   '} C_{10}^3 = 120.',
                                          'định nghĩa': 'Chọn k phần tử từ n phần tử khác nhau '
                                                        '(không quan tâm thứ tự).'},
                            'Xác suất có điều kiện': {   'công thức': 'P(A|B) = \frac{P(A \cap '
                                                                      'B)}{P(B)} \text{ (với } '
                                                                      'P(B) > 0\text{)}',
                                                         'hình_ve': "plot(x, (x, 0, 1), title='Xac "
                                                                    'suat co dieu kien phu thuoc '
                                                                    "vao tap con B')",
                                                         'kí hiệu': 'P(A|B)',
                                                         'ví dụ': '\text{Xác suất lấy được bi đỏ '
                                                                  'ở lần 2 khi biết lần 1 đã lấy '
                                                                  'được bi xanh (không hoàn lại).}',
                                                         'định nghĩa': 'Xác suất của biến cố A với '
                                                                       'điều kiện biến cố B đã xảy '
                                                                       'ra.'},
                            'Định nghĩa cổ điển của xác suất': {   'công thức': 'P(A) = '
                                                                                '\frac{n(A)}{n(\Omega)} '
                                                                                '\text{ (với } 0 '
                                                                                '\le P(A) \le 1 '
                                                                                '\text{)}',
                                                                   'kí hiệu': 'P(A)',
                                                                   'ví dụ': '\text{Chọn 2 học '
                                                                            'sinh từ nhóm 10 học '
                                                                            'sinh (6 nam, 4 nữ). '
                                                                            'Xác suất 2 nữ: } P = '
                                                                            '\frac{C_4^2}{C_{10}^2}.',
                                                                   'định nghĩa': 'Tỉ số giữa số '
                                                                                 'kết quả thuận '
                                                                                 'lợi cho biến cố '
                                                                                 'và tổng số kết '
                                                                                 'quả có thể xảy '
                                                                                 'ra (trong điều '
                                                                                 'kiện các kết quả '
                                                                                 'đồng khả '
                                                                                 'năng).'}},
    'Vectơ và Phương pháp Tọa độ Oxy': {   'Các dạng phương trình đặc biệt': {   'công thức': '\text{Đoạn '
                                                                                              'chắn: '
                                                                                              '} '
                                                                                              '\frac{x}{a} '
                                                                                              '+ '
                                                                                              '\frac{y}{b} '
                                                                                              '= '
                                                                                              '1; '
                                                                                              '\text{ '
                                                                                              'Hệ '
                                                                                              'số '
                                                                                              'góc: '
                                                                                              '} y '
                                                                                              '= '
                                                                                              'k(x '
                                                                                              '- '
                                                                                              'x_0) '
                                                                                              '+ '
                                                                                              'y_0',
                                                                                 'hình_ve': 'sp.plotting.plot(3*(1 '
                                                                                            '- '
                                                                                            'x/2), '
                                                                                            '(x, '
                                                                                            '-1, '
                                                                                            '3), '
                                                                                            "title='Phuong "
                                                                                            'trinh '
                                                                                            'doan '
                                                                                            "chan')",
                                                                                 'kí hiệu': '\text{Đoạn '
                                                                                            'chắn, '
                                                                                            'Hệ số '
                                                                                            'góc}',
                                                                                 'ví dụ': '\text{Đường '
                                                                                          'thẳng '
                                                                                          'cắt Ox '
                                                                                          'tại '
                                                                                          '(2;0), '
                                                                                          'Oy tại '
                                                                                          '(0;3) '
                                                                                          'là: } '
                                                                                          '\frac{x}{2} '
                                                                                          '+ '
                                                                                          '\frac{y}{3} '
                                                                                          '= 1.',
                                                                                 'định nghĩa': 'Phương '
                                                                                               'trình '
                                                                                               'theo '
                                                                                               'đoạn '
                                                                                               'chắn '
                                                                                               'và '
                                                                                               'phương '
                                                                                               'trình '
                                                                                               'có '
                                                                                               'hệ '
                                                                                               'số '
                                                                                               'góc '
                                                                                               'k.'},
                                           'Góc và Khoảng cách': {   'công thức': '\cos\alpha = '
                                                                                  '\frac{|a_1a_2 '
                                                                                  '+ '
                                                                                  'b_1b_2|}{\sqrt{a_1^2+b_1^2}\sqrt{a_2^2+b_2^2}}; '
                                                                                  'd(M, \Delta) = '
                                                                                  '\frac{|ax_0 + '
                                                                                  'by_0 + '
                                                                                  'c|}{\sqrt{a^2 '
                                                                                  '+ b^2}}',
                                                                     'hình_ve': 'sp.plotting.plot((3*x '
                                                                                '+ 5)/4, (x, -2, '
                                                                                "2), title='Khoang "
                                                                                'cach tu O den 3x '
                                                                                "- 4y + 5 = 0')",
                                                                     'kí hiệu': '\cos(d_1, d_2), '
                                                                                'd(M, \Delta)',
                                                                     'ví dụ': 'd(O, \Delta: 3x - '
                                                                              '4y + 5 = 0) = 1.',
                                                                     'định nghĩa': 'Góc giữa hai '
                                                                                   'đường thẳng (0 '
                                                                                   '\le \alpha '
                                                                                   '\le 90) và '
                                                                                   'khoảng cách từ '
                                                                                   'điểm đến đường '
                                                                                   'thẳng.'},
                                           'Hệ trục tọa độ Oxy': {   'công thức': 'A(x_A; y_A), '
                                                                                  'B(x_B; y_B) '
                                                                                  '\Rightarrow '
                                                                                  '\vec{AB} = '
                                                                                  '(x_B - x_A; y_B '
                                                                                  '- y_A)',
                                                                     'hình_ve': 'sp.plotting.plot_parametric((t, '
                                                                                '2*t, (t, 0, 1)), '
                                                                                "title='Vecto co "
                                                                                "toa do (1, 2)')",
                                                                     'kí hiệu': '\vec{u} = (x; y) '
                                                                                '\Leftrightarrow '
                                                                                '\vec{u} = '
                                                                                'x\vec{i} + '
                                                                                'y\vec{j}',
                                                                     'ví dụ': 'A(1; 2), B(3; 5) '
                                                                              '\Rightarrow '
                                                                              '\vec{AB} = (2; 3)',
                                                                     'định nghĩa': 'Biểu diễn '
                                                                                   'vectơ thông '
                                                                                   'qua tọa độ '
                                                                                   'trên mặt '
                                                                                   'phẳng.'},
                                           'Phương trình tham số của đường thẳng': {   'công thức': '\begin{cases} '
                                                                                                    'x '
                                                                                                    '= '
                                                                                                    'x_0 '
                                                                                                    '+ '
                                                                                                    'u_1t '
                                                                                                    '\\ '
                                                                                                    'y '
                                                                                                    '= '
                                                                                                    'y_0 '
                                                                                                    '+ '
                                                                                                    'u_2t '
                                                                                                    '\end{cases} '
                                                                                                    '(t '
                                                                                                    '\in '
                                                                                                    '\mathbb{R})',
                                                                                       'hình_ve': 'sp.plotting.plot_parametric(1 '
                                                                                                  '+ '
                                                                                                  '2*t, '
                                                                                                  '-1 '
                                                                                                  '+ '
                                                                                                  '3*t, '
                                                                                                  '(t, '
                                                                                                  '-2, '
                                                                                                  '2), '
                                                                                                  "title='Phuong "
                                                                                                  'trinh '
                                                                                                  'tham '
                                                                                                  'so '
                                                                                                  "d')",
                                                                                       'kí hiệu': 'd: '
                                                                                                  '\text{ '
                                                                                                  'tham '
                                                                                                  'số '
                                                                                                  '} '
                                                                                                  't',
                                                                                       'ví dụ': '\text{Đường '
                                                                                                'thẳng '
                                                                                                'qua '
                                                                                                '} '
                                                                                                'M(1; '
                                                                                                '-1) '
                                                                                                '\text{ '
                                                                                                'có '
                                                                                                'VTCP '
                                                                                                '} '
                                                                                                '\vec{u}(2; '
                                                                                                '3): '
                                                                                                '\begin{cases} '
                                                                                                'x '
                                                                                                '= '
                                                                                                '1 '
                                                                                                '+ '
                                                                                                '2t '
                                                                                                '\\ '
                                                                                                'y '
                                                                                                '= '
                                                                                                '-1 '
                                                                                                '+ '
                                                                                                '3t '
                                                                                                '\end{cases}',
                                                                                       'định nghĩa': 'Lập '
                                                                                                     'được '
                                                                                                     'khi '
                                                                                                     'biết '
                                                                                                     'một '
                                                                                                     'điểm '
                                                                                                     'M_0(x_0; '
                                                                                                     'y_0) '
                                                                                                     'và '
                                                                                                     'một '
                                                                                                     'VTCP '
                                                                                                     '\vec{u}(u_1; '
                                                                                                     'u_2).'},
                                           'Phương trình tiếp tuyến của đường tròn': {   'công thức': '(x_0 '
                                                                                                      '- '
                                                                                                      'a)(x '
                                                                                                      '- '
                                                                                                      'x_0) '
                                                                                                      '+ '
                                                                                                      '(y_0 '
                                                                                                      '- '
                                                                                                      'b)(y '
                                                                                                      '- '
                                                                                                      'y_0) '
                                                                                                      '= '
                                                                                                      '0 '
                                                                                                      '\text{ '
                                                                                                      'hoặc '
                                                                                                      '} '
                                                                                                      'd(I, '
                                                                                                      'd) '
                                                                                                      '= '
                                                                                                      'R',
                                                                                         'hình_ve': 'sp.plot_implicit(sp.Or(x**2 '
                                                                                                    '+ '
                                                                                                    'y**2 '
                                                                                                    '- '
                                                                                                    '5, '
                                                                                                    'x '
                                                                                                    '+ '
                                                                                                    '2*y '
                                                                                                    '- '
                                                                                                    '5), '
                                                                                                    '(x, '
                                                                                                    '-4, '
                                                                                                    '4), '
                                                                                                    '(y, '
                                                                                                    '-4, '
                                                                                                    '4), '
                                                                                                    "title='Duong "
                                                                                                    'tron '
                                                                                                    'va '
                                                                                                    'tiep '
                                                                                                    'tuyen '
                                                                                                    'tai '
                                                                                                    '(1, '
                                                                                                    "2)')",
                                                                                         'kí hiệu': 'd '
                                                                                                    '\text{ '
                                                                                                    'tiếp '
                                                                                                    'xúc '
                                                                                                    '} '
                                                                                                    '(C)',
                                                                                         'ví dụ': '\text{Tiếp '
                                                                                                  'tuyến '
                                                                                                  'của '
                                                                                                  '} '
                                                                                                  'x^2+y^2=5 '
                                                                                                  '\text{ '
                                                                                                  'tại '
                                                                                                  '} '
                                                                                                  '(1; '
                                                                                                  '2) '
                                                                                                  '\text{ '
                                                                                                  'là: '
                                                                                                  '} '
                                                                                                  'x '
                                                                                                  '+ '
                                                                                                  '2y '
                                                                                                  '- '
                                                                                                  '5 '
                                                                                                  '= '
                                                                                                  '0.',
                                                                                         'định nghĩa': 'Tiếp '
                                                                                                       'tuyến '
                                                                                                       'd '
                                                                                                       'tại '
                                                                                                       'điểm '
                                                                                                       'M_0(x_0; '
                                                                                                       'y_0) '
                                                                                                       'thuộc '
                                                                                                       'đường '
                                                                                                       'tròn.'},
                                           'Phương trình tổng quát của đường thẳng': {   'công thức': 'a(x '
                                                                                                      '- '
                                                                                                      'x_0) '
                                                                                                      '+ '
                                                                                                      'b(y '
                                                                                                      '- '
                                                                                                      'y_0) '
                                                                                                      '= '
                                                                                                      '0 '
                                                                                                      '\Leftrightarrow '
                                                                                                      'ax '
                                                                                                      '+ '
                                                                                                      'by '
                                                                                                      '+ '
                                                                                                      '(-(ax_0 '
                                                                                                      '+ '
                                                                                                      'by_0)) '
                                                                                                      '= '
                                                                                                      '0',
                                                                                         'hình_ve': 'sp.plotting.plot((11 '
                                                                                                    '- '
                                                                                                    '3*x)/4, '
                                                                                                    '(x, '
                                                                                                    '-5, '
                                                                                                    '5), '
                                                                                                    "title='Phuong "
                                                                                                    'trinh '
                                                                                                    'tong '
                                                                                                    'quat '
                                                                                                    '3x '
                                                                                                    '+ '
                                                                                                    '4y '
                                                                                                    '- '
                                                                                                    '11 '
                                                                                                    '= '
                                                                                                    "0')",
                                                                                         'kí hiệu': 'ax '
                                                                                                    '+ '
                                                                                                    'by '
                                                                                                    '+ '
                                                                                                    'c '
                                                                                                    '= '
                                                                                                    '0',
                                                                                         'ví dụ': '\text{Đường '
                                                                                                  'thẳng '
                                                                                                  'qua '
                                                                                                  '} '
                                                                                                  'M(1; '
                                                                                                  '2), '
                                                                                                  'VTPT '
                                                                                                  '\vec{n}(3; '
                                                                                                  '4) '
                                                                                                  '\Rightarrow '
                                                                                                  '3x '
                                                                                                  '+ '
                                                                                                  '4y '
                                                                                                  '- '
                                                                                                  '11 '
                                                                                                  '= '
                                                                                                  '0.',
                                                                                         'định nghĩa': 'Lập '
                                                                                                       'được '
                                                                                                       'khi '
                                                                                                       'biết '
                                                                                                       'một '
                                                                                                       'điểm '
                                                                                                       'M_0(x_0; '
                                                                                                       'y_0) '
                                                                                                       'và '
                                                                                                       'một '
                                                                                                       'VTPT '
                                                                                                       '\vec{n}(a; '
                                                                                                       'b).'},
                                           'Phương trình đường tròn': {   'công thức': 'x^2 + y^2 '
                                                                                       '- 2ax - '
                                                                                       '2by + c = '
                                                                                       '0 \text{ '
                                                                                       'với } c = '
                                                                                       'a^2 + b^2 '
                                                                                       '- R^2 '
                                                                                       '\text{ '
                                                                                       '(ĐK: } a^2 '
                                                                                       '+ b^2 - c '
                                                                                       '> 0)',
                                                                          'hình_ve': 'sp.plot_implicit((x-2)**2 '
                                                                                     '+ (y+3)**2 - '
                                                                                     '16, (x, -3, '
                                                                                     '7), (y, -8, '
                                                                                     '2), '
                                                                                     "title='Duong "
                                                                                     'tron tam '
                                                                                     'I(2, -3) ban '
                                                                                     "kinh R=4')",
                                                                          'kí hiệu': '(x-a)^2 + '
                                                                                     '(y-b)^2 = '
                                                                                     'R^2',
                                                                          'ví dụ': 'x^2 + y^2 - 4x '
                                                                                   '+ 6y - 3 = 0 '
                                                                                   '\Rightarrow '
                                                                                   'I(2; -3), R = '
                                                                                   '4.',
                                                                          'định nghĩa': 'Đường '
                                                                                        'tròn (C) '
                                                                                        'tâm I(a; '
                                                                                        'b), bán '
                                                                                        'kính R.'},
                                           'Tích của vectơ với một số': {   'công thức': '|k\vec{a}| '
                                                                                         '= |k| '
                                                                                         '\cdot '
                                                                                         '|\vec{a}|; '
                                                                                         '\text{ '
                                                                                         'G là '
                                                                                         'trọng '
                                                                                         'tâm } '
                                                                                         '\triangle '
                                                                                         'ABC '
                                                                                         '\Leftrightarrow '
                                                                                         '\vec{GA} '
                                                                                         '+ '
                                                                                         '\vec{GB} '
                                                                                         '+ '
                                                                                         '\vec{GC} '
                                                                                         '= '
                                                                                         '\vec{0}',
                                                                            'hình_ve': 'sp.plotting.plot_parametric((t, '
                                                                                       '0, (t, 0, '
                                                                                       '1)), (t, '
                                                                                       '0, (t, 0, '
                                                                                       '2)), '
                                                                                       "title='Vecto "
                                                                                       'a va vecto '
                                                                                       "2a')",
                                                                            'kí hiệu': 'k\vec{a}',
                                                                            'ví dụ': '\text{I là '
                                                                                     'trung điểm '
                                                                                     'AB } '
                                                                                     '\Leftrightarrow '
                                                                                     '\vec{MA} + '
                                                                                     '\vec{MB} = '
                                                                                     '2\vec{MI} '
                                                                                     '\text{ (với '
                                                                                     'M bất kỳ).}',
                                                                            'định nghĩa': 'Là một '
                                                                                          'vectơ '
                                                                                          'cùng '
                                                                                          'phương '
                                                                                          'với '
                                                                                          'vectơ '
                                                                                          'ban '
                                                                                          'đầu, độ '
                                                                                          'dài gấp '
                                                                                          '|k| '
                                                                                          'lần.'},
                                           'Tích vô hướng của hai vectơ': {   'công thức': '\vec{a} '
                                                                                           '\cdot '
                                                                                           '\vec{b} '
                                                                                           '= '
                                                                                           '|\vec{a}| '
                                                                                           '\cdot '
                                                                                           '|\vec{b}| '
                                                                                           '\cdot '
                                                                                           '\cos(\vec{a}, '
                                                                                           '\vec{b}) '
                                                                                           '= '
                                                                                           'x_1x_2 '
                                                                                           '+ '
                                                                                           'y_1y_2',
                                                                              'hình_ve': 'sp.plotting.plot_parametric((t, '
                                                                                         '0, (t, '
                                                                                         '0, 1)), '
                                                                                         '(0, t, '
                                                                                         '(t, 0, '
                                                                                         '1)), '
                                                                                         "title='Hai "
                                                                                         'vecto '
                                                                                         'vuong '
                                                                                         'goc co '
                                                                                         'tich vo '
                                                                                         'huong '
                                                                                         "bang 0')",
                                                                              'kí hiệu': '\vec{a} '
                                                                                         '\cdot '
                                                                                         '\vec{b}',
                                                                              'ví dụ': '\vec{a} '
                                                                                       '\perp '
                                                                                       '\vec{b} '
                                                                                       '\Leftrightarrow '
                                                                                       '\vec{a} '
                                                                                       '\cdot '
                                                                                       '\vec{b} = '
                                                                                       '0 '
                                                                                       '\Leftrightarrow '
                                                                                       'x_1x_2 + '
                                                                                       'y_1y_2 = 0',
                                                                              'định nghĩa': 'Là '
                                                                                            'một '
                                                                                            'con '
                                                                                            'số '
                                                                                            '(không '
                                                                                            'phải '
                                                                                            'vectơ), '
                                                                                            'bằng '
                                                                                            'tích '
                                                                                            'độ '
                                                                                            'dài '
                                                                                            'nhân '
                                                                                            'với '
                                                                                            'cosin '
                                                                                            'góc '
                                                                                            'xen '
                                                                                            'giữa.'},
                                           'Tổng và Hiệu của hai vectơ': {   'công thức': '\vec{AB} '
                                                                                          '+ '
                                                                                          '\vec{BC} '
                                                                                          '= '
                                                                                          '\vec{AC} '
                                                                                          '\text{ '
                                                                                          '(Quy '
                                                                                          'tắc 3 '
                                                                                          'điểm)}; '
                                                                                          '\vec{AB} '
                                                                                          '- '
                                                                                          '\vec{AC} '
                                                                                          '= '
                                                                                          '\vec{CB}',
                                                                             'hình_ve': 'sp.plot_implicit(sp.Or(sp.And(y==0, '
                                                                                        'x>=0, '
                                                                                        'x<=2), '
                                                                                        'sp.And(x==0, '
                                                                                        'y>=0, '
                                                                                        'y<=1), '
                                                                                        'sp.And(y==1, '
                                                                                        'x>=0, '
                                                                                        'x<=2), '
                                                                                        'sp.And(x==2, '
                                                                                        'y>=0, '
                                                                                        'y<=1)), '
                                                                                        '(x, -0.5, '
                                                                                        '2.5), (y, '
                                                                                        '-0.5, '
                                                                                        '1.5), '
                                                                                        "title='Quy "
                                                                                        'tac hinh '
                                                                                        'binh '
                                                                                        "hanh')",
                                                                             'kí hiệu': '\vec{a} '
                                                                                        '+ '
                                                                                        '\vec{b}, '
                                                                                        '\vec{a} '
                                                                                        '- '
                                                                                        '\vec{b}',
                                                                             'ví dụ': '\text{Quy '
                                                                                      'tắc hình '
                                                                                      'bình hành: '
                                                                                      '} \vec{AB} '
                                                                                      '+ \vec{AD} '
                                                                                      '= \vec{AC}',
                                                                             'định nghĩa': 'Quy '
                                                                                           'tắc '
                                                                                           'cộng '
                                                                                           '(nối '
                                                                                           'đuôi) '
                                                                                           'và quy '
                                                                                           'tắc '
                                                                                           'trừ '
                                                                                           '(chung '
                                                                                           'gốc).'},
                                           'Vectơ': {   'công thức': '|\vec{AB}| = AB \text{ (độ '
                                                                     'dài vectơ là khoảng cách '
                                                                     'giữa hai điểm)}',
                                                        'hình_ve': 'sp.plotting.plot_parametric(t, '
                                                                   "t, (t, 0, 1), title='Minh hoa "
                                                                   "vecto tu (0,0) den (1,1)')",
                                                        'kí hiệu': '\vec{a}, \vec{AB}, \vec{0} '
                                                                   '\text{ (vectơ không)}',
                                                        'ví dụ': '\vec{0} \text{ có độ dài bằng '
                                                                 '0, hướng tùy ý.}',
                                                        'định nghĩa': 'Vectơ là một đoạn thẳng có '
                                                                      'hướng. Điểm bắt đầu gọi là '
                                                                      'điểm đầu, điểm kết thúc gọi '
                                                                      'là điểm cuối.'},
                                           'Vectơ chỉ phương': {   'công thức': '\text{Nếu } '
                                                                                '\vec{u} \text{ '
                                                                                'là VTCP thì } '
                                                                                'k\vec{u} (k '
                                                                                '\neq 0) \text{ '
                                                                                'cũng là VTCP.}',
                                                                   'hình_ve': 'sp.plotting.plot_parametric((t, '
                                                                              '1.5*t, (t, 0, 1)), '
                                                                              "title='Minh hoa "
                                                                              "VTCP (u1, u2)')",
                                                                   'kí hiệu': '\vec{u} = (u_1; '
                                                                              'u_2)',
                                                                   'ví dụ': '\text{Đường thẳng đi '
                                                                            'qua } A(1; 2), B(3; '
                                                                            '5) \text{ có VTCP } '
                                                                            '\vec{u} = \vec{AB} '
                                                                            '= (2; 3).',
                                                                   'định nghĩa': 'Vectơ \vec{u} '
                                                                                 '\neq \vec{0} '
                                                                                 'được gọi là VTCP '
                                                                                 'của đường thẳng '
                                                                                 'd nếu giá của nó '
                                                                                 'song song hoặc '
                                                                                 'trùng với d.'},
                                           'Vectơ cùng phương, cùng hướng': {   'công thức': '\vec{a} '
                                                                                             '= '
                                                                                             'k\vec{b} '
                                                                                             '\text{ '
                                                                                             '(điều '
                                                                                             'kiện '
                                                                                             'để '
                                                                                             'hai '
                                                                                             'vectơ '
                                                                                             'cùng '
                                                                                             'phương)}',
                                                                                'hình_ve': 'sp.plotting.plot_parametric((t, '
                                                                                           '1, (t, '
                                                                                           '0, '
                                                                                           '1)), '
                                                                                           '(t, 2, '
                                                                                           '(t, 0, '
                                                                                           '1)), '
                                                                                           "title='Hai "
                                                                                           'vecto '
                                                                                           'cung '
                                                                                           "phuong')",
                                                                                'kí hiệu': '\vec{a} '
                                                                                           '\parallel '
                                                                                           '\vec{b}',
                                                                                'ví dụ': '\text{Trong '
                                                                                         'hình '
                                                                                         'bình '
                                                                                         'hành '
                                                                                         'ABCD, } '
                                                                                         '\vec{AB} '
                                                                                         '\text{ '
                                                                                         'và } '
                                                                                         '\vec{DC} '
                                                                                         '\text{ '
                                                                                         'cùng '
                                                                                         'hướng.}',
                                                                                'định nghĩa': 'Hai '
                                                                                              'vectơ '
                                                                                              'cùng '
                                                                                              'nằm '
                                                                                              'trên '
                                                                                              'một '
                                                                                              'đường '
                                                                                              'thẳng '
                                                                                              'hoặc '
                                                                                              'hai '
                                                                                              'đường '
                                                                                              'thẳng '
                                                                                              'song '
                                                                                              'song '
                                                                                              'thì '
                                                                                              'cùng '
                                                                                              'phương. '
                                                                                              'Nếu '
                                                                                              'cùng '
                                                                                              'phương, '
                                                                                              'chúng '
                                                                                              'có '
                                                                                              'thể '
                                                                                              'cùng '
                                                                                              'hướng '
                                                                                              'hoặc '
                                                                                              'ngược '
                                                                                              'hướng.'},
                                           'Vectơ pháp tuyến': {   'công thức': '\vec{u} \perp '
                                                                                '\vec{n} '
                                                                                '\Leftrightarrow '
                                                                                'a \cdot u_1 + b '
                                                                                '\cdot u_2 = 0. '
                                                                                '\text{ Chuyển '
                                                                                'đổi: } '
                                                                                '\vec{u}(u_1; '
                                                                                'u_2) \rightarrow '
                                                                                '\vec{n}(-u_2; '
                                                                                'u_1).',
                                                                   'hình_ve': 'sp.plotting.plot_parametric((t, '
                                                                              '0.5*t, (t, 0, 1)), '
                                                                              '(-0.5*t, t, (t, 0, '
                                                                              "1)), title='VTCP "
                                                                              '(xanh) vuong goc '
                                                                              "VTPT (do)')",
                                                                   'kí hiệu': '\vec{n} = (a; b)',
                                                                   'ví dụ': '\text{Đường thẳng có '
                                                                            'VTCP } \vec{u}(1; '
                                                                            '-2) \text{ thì có '
                                                                            'VTPT } \vec{n}(2; '
                                                                            '1).',
                                                                   'định nghĩa': 'Vectơ \vec{n} '
                                                                                 '\neq \vec{0} '
                                                                                 'được gọi là VTPT '
                                                                                 'của đường thẳng '
                                                                                 'd nếu giá của nó '
                                                                                 'vuông góc với '
                                                                                 'd.'},
                                           'Vị trí tương đối giữa hai đường thẳng': {   'công thức': '\text{Cắt '
                                                                                                     'nhau: '
                                                                                                     '} '
                                                                                                     'a_1b_2 '
                                                                                                     '- '
                                                                                                     'a_2b_1 '
                                                                                                     '\neq '
                                                                                                     '0; '
                                                                                                     '\text{ '
                                                                                                     'Vuông '
                                                                                                     'góc: '
                                                                                                     '} '
                                                                                                     'a_1a_2 '
                                                                                                     '+ '
                                                                                                     'b_1b_2 '
                                                                                                     '= '
                                                                                                     '0',
                                                                                        'hình_ve': 'sp.plotting.plot(2-x, '
                                                                                                   'x, '
                                                                                                   '(x, '
                                                                                                   '-1, '
                                                                                                   '3), '
                                                                                                   "title='Vị "
                                                                                                   'tri '
                                                                                                   'tuong '
                                                                                                   'doi: '
                                                                                                   'Cat '
                                                                                                   "nhau')",
                                                                                        'kí hiệu': 'd_1 '
                                                                                                   '\cap '
                                                                                                   'd_2, '
                                                                                                   'd_1 '
                                                                                                   '\parallel '
                                                                                                   'd_2, '
                                                                                                   'd_1 '
                                                                                                   '\equiv '
                                                                                                   'd_2, '
                                                                                                   'd_1 '
                                                                                                   '\perp '
                                                                                                   'd_2',
                                                                                        'ví dụ': 'x '
                                                                                                 '+ '
                                                                                                 'y '
                                                                                                 '- '
                                                                                                 '2 '
                                                                                                 '= '
                                                                                                 '0 '
                                                                                                 '\text{ '
                                                                                                 'và '
                                                                                                 '} '
                                                                                                 'x '
                                                                                                 '- '
                                                                                                 'y '
                                                                                                 '= '
                                                                                                 '0 '
                                                                                                 '\text{ '
                                                                                                 'cắt '
                                                                                                 'nhau '
                                                                                                 'tại '
                                                                                                 '} '
                                                                                                 '(1; '
                                                                                                 '1).',
                                                                                        'định nghĩa': 'Dựa '
                                                                                                      'trên '
                                                                                                      'số '
                                                                                                      'nghiệm '
                                                                                                      'của '
                                                                                                      'hệ '
                                                                                                      'phương '
                                                                                                      'trình '
                                                                                                      'hoặc '
                                                                                                      'tỉ '
                                                                                                      'số '
                                                                                                      'các '
                                                                                                      'hệ '
                                                                                                      'số.'},
                                           'Đường Elip': {   'công thức': 'c^2 = a^2 - b^2; '
                                                                          'F_1(-c; 0), F_2(c; 0); '
                                                                          '\text{ Độ dài trục '
                                                                          'lớn: } 2a, \text{ trục '
                                                                          'bé: } 2b',
                                                             'hình_ve': 'sp.plot_implicit(x**2/16 '
                                                                        '+ y**2/9 - 1, (x, -5, 5), '
                                                                        "(y, -4, 4), title='Duong "
                                                                        'Elip (E): x^2/16 + y^2/9 '
                                                                        "= 1')",
                                                             'kí hiệu': '(E): \frac{x^2}{a^2} + '
                                                                        '\frac{y^2}{b^2} = 1 (a > '
                                                                        'b > 0)',
                                                             'ví dụ': '\frac{x^2}{16} + '
                                                                      '\frac{y^2}{9} = 1 '
                                                                      '\Rightarrow a=4, b=3, '
                                                                      'c=\sqrt{7}.',
                                                             'định nghĩa': 'Tập hợp các điểm M sao '
                                                                           'cho MF_1 + MF_2 = 2a.'},
                                           'Đường Hypebol': {   'công thức': 'c^2 = a^2 + b^2; '
                                                                             'F_1(-c; 0), F_2(c; '
                                                                             '0); \text{ Trục '
                                                                             'thực: } 2a, \text{ '
                                                                             'trục ảo: } 2b',
                                                                'hình_ve': 'sp.plot_implicit(x**2/9 '
                                                                           '- y**2/16 - 1, (x, '
                                                                           '-10, 10), (y, -10, '
                                                                           "10), title='Duong "
                                                                           'Hypebol (H): x^2/9 - '
                                                                           "y^2/16 = 1')",
                                                                'kí hiệu': '(H): \frac{x^2}{a^2} '
                                                                           '- \frac{y^2}{b^2} = 1 '
                                                                           '(a, b > 0)',
                                                                'ví dụ': '\frac{x^2}{9} - '
                                                                         '\frac{y^2}{16} = 1 '
                                                                         '\Rightarrow a=3, b=4, '
                                                                         'c=5.',
                                                                'định nghĩa': 'Tập hợp các điểm M '
                                                                              'sao cho |MF_1 - '
                                                                              'MF_2| = 2a.'},
                                           'Đường Parabol': {   'công thức': 'F(p/2; 0); \text{ '
                                                                             'Đường chuẩn: } x = '
                                                                             '-p/2',
                                                                'hình_ve': 'sp.plot_implicit(y**2 '
                                                                           '- 4*x, (x, -2, 6), (y, '
                                                                           "-5, 5), title='Duong "
                                                                           "Parabol y^2 = 4x')",
                                                                'kí hiệu': '(P): y^2 = 2px (p > 0)',
                                                                'ví dụ': 'y^2 = 4x \Rightarrow '
                                                                         'p=2, F(1; 0), \text{ '
                                                                         'chuẩn } x = -1.',
                                                                'định nghĩa': 'Tập hợp các điểm M '
                                                                              'cách đều tiêu điểm '
                                                                              'F và đường chuẩn '
                                                                              'delta.'}}}
