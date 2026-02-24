from IPython.display import display, Math

chuong_1_toan_10 = {
    "Mệnh đề toán học": {
        "định nghĩa": r"Là một câu khẳng định có tính đúng hoặc sai rõ ràng. Một mệnh đề không thể vừa đúng vừa sai.",
        "kí hiệu": r"P, Q, R",
        "công thức": r"P \in \{\text{Đ}, \text{S}\}",
        "ví dụ": r"P: \text{'15 là số lẻ' là mệnh đề đúng.}"
    },
    "Mệnh đề phủ định": {
        "định nghĩa": r"Mệnh đề phủ định của P được thiết lập bằng cách thêm hoặc bớt từ 'không' hoặc 'không phải' vào trước vị ngữ của P.",
        "kí hiệu": r"\overline{P}",
        "công thức": r"P \text{ đúng } \Leftrightarrow \overline{P} \text{ sai.}",
        "ví dụ": r"\overline{P}: \text{'15 không phải là số lẻ'}."
    },
    "Mệnh đề kéo theo": {
        "định nghĩa": r"Dạng 'Nếu P thì Q'. Chỉ sai khi P đúng mà Q sai.",
        "kí hiệu": r"P \Rightarrow Q",
        "công thức": r"P \text{ là giả thiết, } Q \text{ là kết luận.}",
        "ví dụ": r"\text{Nếu } a \vdots 6 \text{ thì } a \vdots 3."
    },
    "Mệnh đề đảo": {
        "định nghĩa": r"Đảo vị trí của P và Q trong mệnh đề kéo theo.",
        "kí hiệu": r"Q \Rightarrow P",
        "công thức": r"\text{Mệnh đề đảo không nhất thiết đúng khi mệnh đề thuận đúng.}",
        "ví dụ": r"\text{Nếu } a \vdots 3 \text{ thì } a \vdots 6 \text{ (Mệnh đề đảo này sai)}."
    },
    "Mệnh đề tương đương": {
        "định nghĩa": r"Khi cả hai mệnh đề kéo theo thuận và đảo đều đúng.",
        "kí hiệu": r"P \Leftrightarrow Q",
        "công thức": r"P \Leftrightarrow Q \equiv (P \Rightarrow Q) \land (Q \Rightarrow P)",
        "ví dụ": r"\text{Tam giác đều } \Leftrightarrow \text{ Tam giác có 3 cạnh bằng nhau.}"
    },
    "Lượng từ toán học": {
        "định nghĩa": r"Sử dụng kí hiệu với mọi và tồn tại để biểu thị phạm vi của biến.",
        "kí hiệu": r"\forall, \exists",
        "công thức": r"\overline{\forall x \in X, P(x)} \equiv \exists x \in X, \overline{P(x)}",
        "ví dụ": r"\forall x \in \mathbb{R}, x^2 + 1 > 0."
    },
    "Tập hợp": {
        "định nghĩa": r"Một tập hợp bao gồm các đối tượng được gọi là phần tử.",
        "kí hiệu": r"a \in A, b \notin A",
        "công thức": r"A = \{x \in X \mid P(x)\}",
        "ví dụ": r"\mathbb{N} = \{0, 1, 2, 3, \dots\}"
    },
    "Quan hệ tập hợp": {
        "định nghĩa": r"A là con B nếu mọi phần tử của A đều thuộc B. A bằng B nếu chúng có cùng phần tử.",
        "kí hiệu": r"A \subset B, A = B",
        "công thức": r"A = B \Leftrightarrow (A \subset B) \land (B \subset A)",
        "ví dụ": r"\{1, 2\} \subset \{1, 2, 3\}"
    },
    "Phép giao": {
        "định nghĩa": r"Gồm các phần tử chung của cả hai tập hợp.",
        "kí hiệu": r"A \cap B",
        "công thức": r"A \cap B = \{x \mid x \in A \land x \in B\}",
        "ví dụ": r"[1; 4] \cap [3; 5] = [3; 4]"
    },
    "Phép hợp": {
        "định nghĩa": r"Gồm các phần tử thuộc ít nhất một trong hai tập hợp.",
        "kí hiệu": r"A \cup B",
        "công thức": r"A \cup B = \{x \mid x \in A \lor x \in B\}",
        "ví dụ": r"\{1, 2\} \cup \{3, 4\} = \{1, 2, 3, 4\}"
    },
    "Phép hiệu và Phần bù": {
        "định nghĩa": r"Hiệu A \ B là các phần tử thuộc A nhưng không thuộc B. Phần bù dùng khi B là tập con của A.",
        "kí hiệu": r"A \setminus B, C_A B",
        "công thức": r"C_A B = \{x \in A \mid x \notin B\} \text{ (với } B \subset A \text{)}",
        "ví dụ": r"\mathbb{R} \setminus (-\infty; 0] = (0; +\infty)"
    },
    "Các tập con của số thực": {
        "định nghĩa": r"Biểu diễn các khoảng, đoạn, nửa khoảng trên trục số thực.",
        "kí hiệu": r"(a; b), [a; b], [a; b), (a; b]",
        "công thức": r"[a; b] = \{x \in \mathbb{R} \mid a \le x \le b\}",
        "ví dụ": r"x \in [1; 2] \Leftrightarrow 1 \le x \le 2"
    }
}

chuong_2_toan_10 = {
    "Bất phương trình bậc nhất hai ẩn": {
        "định nghĩa": "Là bất phương trình có dạng tổng quát với hai biến x, y.",
        "kí hiệu": "f(x, y) < 0",
        "công thức": r"ax + by + c < 0 \quad (a^2 + b^2 \neq 0)",
        "ví dụ": r"2x - y + 3 \ge 0"
    },
    "Miền nghiệm của BPT": {
        "định nghĩa": "Tập hợp các cặp số (x; y) thỏa mãn bất phương trình. Hình học là một nửa mặt phẳng được chia bởi đường thẳng d.",
        "kí hiệu": r"\mathcal{D}",
        "công thức": r"d: ax + by + c = 0",
        "ví dụ": r"\text{Xét } O(0;0) \text{ để xác định miền nghiệm của } x + y - 2 < 0."
    },
    "Hệ bất phương trình bậc nhất hai ẩn": {
        "định nghĩa": "Tập hợp gồm từ hai bất phương trình bậc nhất hai ẩn trở lên.",
        "kí hiệu": r"\begin{cases} f_i(x,y) \ge 0 \end{cases}",
        "công thức": r"\begin{cases} a_1x + b_1y \le c_1 \\ a_2x + b_2y \le c_2 \end{cases}",
        "ví dụ": r"\begin{cases} x \ge 0 \\ y \ge 0 \\ x + y \le 1 \end{cases}"
    },
    "Miền nghiệm của hệ BPT": {
        "định nghĩa": "Giao của các miền nghiệm của các bất phương trình trong hệ. Thường là miền đa giác (lồi).",
        "kí hiệu": r"\mathcal{S} = \bigcap \mathcal{D}_i",
        "công thức": r"\text{Đa giác bao gồm cả biên hoặc không biên.}",
        "ví dụ": r"\text{Miền nghiệm hệ } \{x \ge 0, y \ge 0, x+y \le 1\} \text{ là tam giác } OAB."
    },
    "Bài toán tối ưu hóa (Quy hoạch tuyến tính)": {
        "định nghĩa": "Tìm giá trị lớn nhất hoặc nhỏ nhất của biểu thức bậc nhất trên một miền nghiệm cho trước.",
        "kí hiệu": r"F(x, y) = ax + by",
        "công thức": r"\min/\max F(x, y) \text{ thường đạt được tại các đỉnh của đa giác miền nghiệm.}",
        "ví dụ": r"\text{Tìm max } F(x, y) = x + 2y \text{ với } (x, y) \in \text{ miền đa giác.}"
    }
}

chuong_3_toan_10 = {
    "Hàm số bậc hai": {
        "định nghĩa": r"Hàm số cho bởi công thức bậc hai của biến số x.",
        "kí hiệu": r"y = f(x)",
        "công thức": r"y = ax^2 + bx + c \quad (a \neq 0)",
        "ví dụ": r"y = x^2 - 4x + 3"
    },
    "Đồ thị hàm số bậc hai (Parabol)": {
        "định nghĩa": r"Đường cong Parabol có đỉnh I, đối xứng qua đường thẳng x.",
        "kí hiệu": r"P",
        "công thức": r"\text{Đỉnh } I\left(-\frac{b}{2a}; -\frac{\Delta}{4a}\right), \text{ Trục đối xứng } x = -\frac{b}{2a}",
        "ví dụ": r"\text{Với } y = x^2 - 2x, \text{ đỉnh là } I(1; -1)."
    },
    "Sự biến thiên": {
        "định nghĩa": r"Sự tăng giảm của hàm số trên các khoảng dựa vào dấu của hệ số a.",
        "kí hiệu": r"a > 0 \text{ hoặc } a < 0",
        "công thức": r"a > 0: \text{ NB trên } (-\infty; -\frac{b}{2a}), \text{ ĐB trên } (-\frac{b}{2a}; +\infty)",
        "ví dụ": r"a = 1 > 0: \text{ Hàm số đạt cực tiểu tại đỉnh.}"
    },
    "Tam thức bậc hai": {
        "định nghĩa": r"Biểu thức đại số bậc hai theo biến x.",
        "kí hiệu": r"f(x) = ax^2 + bx + c",
        "công thức": r"\Delta = b^2 - 4ac",
        "ví dụ": r"f(x) = x^2 - 3x + 2 \text{ có } \Delta = (-3)^2 - 4(1)(2) = 1"
    },
    "Định lý về dấu của tam thức bậc hai": {
        "định nghĩa": r"Quy tắc xác định giá trị âm, dương của tam thức dựa vào biệt thức và hệ số a.",
        "kí hiệu": r"f(x) \gtrless 0",
        "công thức": r"\Delta < 0 \Rightarrow f(x) \text{ cùng dấu với } a, \forall x \in \mathbb{R}",
        "ví dụ": r"x^2 + x + 1 > 0, \forall x \in \mathbb{R} \text{ vì } \Delta = -3 < 0, a = 1 > 0."
    }
}

chuong_4_toan_10 = {
    "Giá trị lượng giác của một góc từ 0 đến 180 độ": {
        "định nghĩa": r"Mở rộng khái niệm lượng giác cho góc tù bằng nửa đường tròn đơn vị.",
        "kí hiệu": r"\sin \alpha, \cos \alpha, \tan \alpha, \cot \alpha",
        "công thức": r"\sin(180^\circ - \alpha) = \sin \alpha, \cos(180^\circ - \alpha) = -\cos \alpha",
        "ví dụ": r"\sin 150^\circ = \sin 30^\circ = \frac{1}{2}"
    },
    "Định lý Cosin": {
        "định nghĩa": r"Mối liên hệ giữa ba cạnh và cosin của một góc trong tam giác bất kỳ.",
        "kí hiệu": r"a, b, c, \cos A",
        "công thức": r"a^2 = b^2 + c^2 - 2bc \cdot \cos A",
        "ví dụ": r"\text{Tam giác có } b=3, c=4, \hat{A}=60^\circ \Rightarrow a^2 = 3^2+4^2-2 \cdot 3 \cdot 4 \cdot \frac{1}{2} = 13"
    },
    "Định lý Sin": {
        "định nghĩa": r"Tỉ số giữa mỗi cạnh và sin của góc đối diện bằng đường kính đường tròn ngoại tiếp.",
        "kí hiệu": r"R \text{ (bán kính đường tròn ngoại tiếp)}",
        "công thức": r"\frac{a}{\sin A} = \frac{b}{\sin B} = \frac{c}{\sin C} = 2R",
        "ví dụ": r"\text{Tam giác có } a=10, \hat{A}=30^\circ \Rightarrow R = \frac{10}{2 \cdot \sin 30^\circ} = 10"
    },
    "Các công thức tính diện tích tam giác": {
        "định nghĩa": r"Các cách tính diện tích dựa trên cạnh, góc và bán kính đường tròn nội/ngoại tiếp.",
        "kí hiệu": r"S, p \text{ (nửa chu vi)}, r \text{ (bán kính nội tiếp)}",
        "công thức": r"S = \frac{1}{2}bc\sin A = \frac{abc}{4R} = pr = \sqrt{p(p-a)(p-b)(p-c)}",
        "ví dụ": r"\text{Tam giác } 3, 4, 5 \text{ có } p=6 \Rightarrow S = \sqrt{6(6-3)(6-4)(6-5)} = 6"
    },
    "Giải tam giác và ứng dụng thực tế": {
        "định nghĩa": r"Tìm các yếu tố chưa biết của tam giác khi đã biết một số yếu tố cho trước.",
        "kí hiệu": r"\text{Giải tam giác}",
        "công thức": r"\text{Sử dụng linh hoạt định lý Sin, Cos và tổng 3 góc } = 180^\circ",
        "ví dụ": r"\text{Biết 3 cạnh, dùng định lý Cosin để tìm các góc.}"
    }
}

chuong_5_toan_10 = {
    "Khái niệm Vectơ": {
        "định nghĩa": r"Đoạn thẳng có hướng, nghĩa là đã chỉ rõ điểm đầu và điểm cuối.",
        "kí hiệu": r"\vec{a}, \vec{AB}, \vec{0}",
        "công thức": r"|\vec{AB}| = \text{độ dài đoạn thẳng AB}",
        "ví dụ": r"\vec{AB} \text{ có điểm đầu A, điểm cuối B.}",
        "hình": "plt.quiver(0, 0, 3, 2, angles='xy', scale_units='xy', scale=1, color='r'); plt.text(1.5, 1.2, r'\\vec{a}'); plt.xlim(-1, 4); plt.ylim(-1, 3); plt.grid(); plt.show()"
    },
    "Tổng và hiệu của hai vectơ": {
        "định nghĩa": r"Phép toán cộng hai vectơ theo quy tắc ba điểm hoặc quy tắc hình bình hành.",
        "kí hiệu": r"\vec{a} + \vec{b}, \vec{a} - \vec{b}",
        "công thức": r"\vec{AB} + \vec{BC} = \vec{AC}; \quad \vec{OA} + \vec{OB} = \vec{OC} \text{ (C là đỉnh HBH)}",
        "ví dụ": r"\vec{u} = (1; 2), \vec{v} = (2; 1) \Rightarrow \vec{u} + \vec{v} = (3; 3)",
        "hình": "plt.quiver([0, 3, 0], [0, 2, 0], [3, 1, 4], [2, 1, 3], angles='xy', scale_units='xy', scale=1, color=['r','b','g']); plt.text(1.5, 1, r'\\vec{a}'); plt.text(3.5, 2.5, r'\\vec{b}'); plt.text(2, 2.5, r'\\vec{a}+\\vec{b}'); plt.xlim(-1, 5); plt.ylim(-1, 4); plt.grid(); plt.show()"
    },
    "Tích của một số với một vectơ": {
        "định nghĩa": r"Kết quả là một vectơ cùng phương với vectơ ban đầu, độ dài gấp |k| lần.",
        "kí hiệu": r"k\vec{a}",
        "công thức": r"|k\vec{a}| = |k| \cdot |\vec{a}|",
        "ví dụ": r"k=2 \Rightarrow 2\vec{a} \text{ cùng hướng và dài gấp đôi } \vec{a}.",
        "hình": "plt.quiver([0, 0], [1, 0], [1, 2], [0, 0], angles='xy', scale_units='xy', scale=1, color=['r','b']); plt.xlim(-1, 3); plt.ylim(-1, 2); plt.grid(); plt.show()"
    },
    "Tọa độ của vectơ": {
        "định nghĩa": r"Biểu diễn vectơ thông qua các vectơ đơn vị trên hệ trục tọa độ Oxy.",
        "kí hiệu": r"\vec{u} = (x; y)",
        "công thức": r"\vec{u} = x\vec{i} + y\vec{j}; \quad |\vec{u}| = \sqrt{x^2 + y^2}",
        "ví dụ": r"A(1; 2), B(4; 6) \Rightarrow \vec{AB} = (3; 4), |\vec{AB}| = 5",
        "hình": "plt.axhline(0, color='black', lw=1); plt.axvline(0, color='black', lw=1); plt.quiver(0, 0, 3, 4, angles='xy', scale_units='xy', scale=1); plt.xlim(-1, 5); plt.ylim(-1, 5); plt.grid(); plt.show()"
    },
    "Tích vô hướng của hai vectơ": {
        "định nghĩa": r"Một số thực bằng tích độ dài hai vectơ và cosin góc xen giữa.",
        "kí hiệu": r"\vec{a} \cdot \vec{b}",
        "công thức": r"\vec{a} \cdot \vec{b} = |\vec{a}| \cdot |\vec{b}| \cdot \cos(\vec{a}, \vec{b}) = x_1x_2 + y_1y_2",
        "ví dụ": r"\vec{a} \perp \vec{b} \Leftrightarrow \vec{a} \cdot \vec{b} = 0",
        "hình": "plt.quiver([0, 0], [0, 0], [3, 0], [0, 3], angles='xy', scale_units='xy', scale=1); plt.text(1, 0.2, r'\\vec{a}'); plt.text(0.2, 1, r'\\vec{b}'); plt.xlim(-1, 4); plt.ylim(-1, 4); plt.grid(); plt.show()"
    }
}

chuong_6_toan_10 = {
    "Số trung bình (Mean)": {
        "định nghĩa": r"Giá trị trung bình cộng của các số liệu, dùng để đại diện cho xu thế trung tâm của mẫu số liệu.",
        "kí hiệu": r"\bar{x}",
        "công thức": r"\bar{x} = \frac{x_1 + x_2 + ... + x_n}{n} = \frac{\sum_{i=1}^{k} n_i x_i}{N}",
        "ví dụ": r"\text{Mẫu: } \{5, 7, 9\} \Rightarrow \bar{x} = \frac{5+7+9}{3} = 7",
        "hình": "plt.figure(figsize=(6,2)); plt.stem([5, 7, 9], [1, 1, 1]); plt.axvline(7, color='r', label='Mean=7'); plt.legend(); plt.title('Vị trí số trung bình'); plt.show()"
    },
    "Trung vị (Median)": {
        "định nghĩa": r"Số đứng ở vị trí giữa của mẫu số liệu sau khi đã sắp xếp theo thứ tự không giảm.",
        "kí hiệu": r"M_e",
        "công thức": r"\text{Nếu n lẻ: } M_e = x_{\frac{n+1}{2}}. \text{ Nếu n chẵn: } M_e = \frac{1}{2}(x_{\frac{n}{2}} + x_{\frac{n}{2}+1})",
        "ví dụ": r"\text{Mẫu: } \{2, 3, 4, 100\} \Rightarrow M_e = \frac{3+4}{2} = 3.5",
        "hình": "data=[2, 3, 4, 100]; plt.figure(figsize=(6,1)); plt.scatter(data, [0]*4); plt.axvline(3.5, color='g', label='Median'); plt.legend(); plt.show()"
    },
    "Tứ phân vị (Quartiles)": {
        "định nghĩa": r"Ba giá trị chia mẫu số liệu đã sắp xếp thành 4 phần có số lượng phần tử bằng nhau.",
        "kí hiệu": r"Q_1, Q_2, Q_3",
        "công thức": r"Q_2 = M_e; Q_1 = \text{Trung vị nửa dưới}; Q_3 = \text{Trung vị nửa trên}",
        "ví dụ": r"\text{Mẫu: } \{1, 2, 3, 4, 5, 6, 7\} \Rightarrow Q_1=2, Q_2=4, Q_3=6",
        "hình": "data=[1, 2, 3, 4, 5, 6, 7]; plt.boxplot(data, vert=False, patch_artist=True); plt.title('Biểu đồ hộp (Box plot)'); plt.show()"
    },
    "Mốt (Mode)": {
        "định nghĩa": r"Giá trị xuất hiện với tần số lớn nhất trong mẫu số liệu.",
        "kí hiệu": r"M_o",
        "công thức": r"\text{Giá trị } x_i \text{ ứng với } n_i = \max \{n_1, n_2, ..., n_k\}",
        "ví dụ": r"\text{Mẫu: } \{1, 2, 2, 3, 3, 3\} \Rightarrow M_o = 3",
        "hình": "plt.bar(['1', '2', '3'], [1, 2, 3], color='orange'); plt.ylabel('Tần số'); plt.show()"
    },
    "Khoảng biến thiên & Khoảng tứ phân vị": {
        "định nghĩa": r"Đo độ phân tán của mẫu số liệu. Khoảng tứ phân vị giúp loại bỏ các giá trị ngoại lệ.",
        "kí hiệu": r"R, \Delta_Q",
        "công thức": r"R = x_{max} - x_{min}; \quad \Delta_Q = Q_3 - Q_1",
        "ví dụ": r"\text{Mẫu: } \{1, 5, 10\} \Rightarrow R = 10-1 = 9, \Delta_Q = 7.5 - 2.5 = 5",
        "hình": "data=[1, 2, 5, 8, 10]; plt.hlines(1, 1, 10, colors='r', label='Range'); plt.boxplot(data, vert=False); plt.legend(); plt.show()"
    },
    "Phương sai & Độ lệch chuẩn": {
        "định nghĩa": r"Số đặc trưng đo mức độ phân tán của các số liệu quanh số trung bình.",
        "kí hiệu": r"s^2, s",
        "công thức": r"s^2 = \frac{1}{n} \sum (x_i - \bar{x})^2; \quad s = \sqrt{s^2}",
        "ví dụ": r"\text{Số liệu càng tập trung quanh } \bar{x} \text{ thì } s \text{ càng nhỏ.}",
        "hình": "x=np.linspace(0,20,100); plt.plot(x, 1/2*np.exp(-(x-10)**2/8), label='s nhỏ'); plt.plot(x, 1/5*np.exp(-(x-10)**2/50), label='s lớn'); plt.legend(); plt.title('Phân phối và Độ lệch chuẩn'); plt.show()"
    },
    "Giá trị ngoại lệ (Outliers)": {
        "định nghĩa": r"Giá trị nằm quá xa so với phần lớn các giá trị trong mẫu.",
        "kí hiệu": r"x < Q_1 - 1.5\Delta_Q \text{ hoặc } x > Q_3 + 1.5\Delta_Q",
        "công thức": r"[Q_1 - 1.5\Delta_Q, Q_3 + 1.5\Delta_Q] \text{ là rào cản chuẩn.}",
        "ví dụ": r"\text{Mẫu: } \{1, 2, 3, 100\} \Rightarrow 100 \text{ là giá trị ngoại lệ.}",
        "hình": "data=[1, 2, 3, 4, 25]; plt.boxplot(data, vert=False); plt.text(25, 1.1, 'Outlier'); plt.show()"
    },
    "Biểu đồ tần số hình cột & đoạn thẳng": {
        "định nghĩa": r"Trực quan hóa sự phân bố tần số của các giá trị.",
        "kí hiệu": r"Histogram, Line Graph",
        "công thức": r"\text{Trục hoành: Giá trị; Trục tung: Tần số/Tần suất}",
        "ví dụ": r"\text{Dùng để so sánh số lượng giữa các nhóm dữ liệu.}",
        "hình": "plt.plot([1, 2, 3, 4], [10, 25, 15, 30], marker='o'); plt.title('Biểu đồ đoạn thẳng'); plt.show()"
    }
}

chuong_1_toan_11 = {
    "Góc lượng giác": {"định nghĩa": r"Là góc có xét đến chiều quay. Góc lượng giác được xác định bởi tia đầu và tia cuối.",
                       "kí hiệu": r"(Ox, Oy), \alpha",
                       "công thức": r"\alpha = \widehat{(Ox, Oy)}",
                       "ví dụ": r"\alpha = 60^\circ, \alpha = -30^\circ"},

    "Đường tròn lượng giác": {"định nghĩa": r"Là đường tròn tâm O bán kính 1 trong mặt phẳng tọa độ.",
                              "kí hiệu": r"(O;1)",
                              "công thức": r"x^2 + y^2 = 1",
                              "ví dụ": r"M(\cos\alpha, \sin\alpha) thuộc (O;1)"},

    "Giá trị lượng giác của một góc": {"định nghĩa": r"Với mỗi góc lượng giác xác định các giá trị sin, cos, tan, cot.",
                                       "kí hiệu": r"\sin\alpha, \cos\alpha, \tan\alpha, \cot\alpha",
                                       "công thức": r"\tan\alpha = \dfrac{\sin\alpha}{\cos\alpha}",
                                       "ví dụ": r"\sin 30^\circ = \dfrac{1}{2}"},

    "Công thức lượng giác cơ bản": {"định nghĩa": r"Các hệ thức liên hệ giữa sin và cos.",
                                    "kí hiệu": r"\sin^2\alpha + \cos^2\alpha = 1",
                                    "công thức": r"1 + \tan^2\alpha = \dfrac{1}{\cos^2\alpha}",
                                    "ví dụ": r"\sin^2 45^\circ + \cos^2 45^\circ = 1"},

    "Hàm số y = sin x": {"định nghĩa": r"Hàm số xác định với mọi x thuộc R.",
                         "kí hiệu": r"y = \sin x",
                         "công thức": r"Tập xác định: \mathbb{R}, Chu kỳ: 2\pi",
                         "ví dụ": r"\sin(x + 2\pi) = \sin x"},

    "Hàm số y = cos x": {"định nghĩa": r"Hàm số xác định với mọi x thuộc R.",
                         "kí hiệu": r"y = \cos x",
                         "công thức": r"Tập xác định: \mathbb{R}, Chu kỳ: 2\pi",
                         "ví dụ": r"\cos(x + 2\pi) = \cos x"},

    "Hàm số y = tan x": {"định nghĩa": r"Hàm số xác định khi cos x ≠ 0.",
                         "kí hiệu": r"y = \tan x",
                         "công thức": r"Tập xác định: \mathbb{R} \setminus \{\dfrac{\pi}{2} + k\pi\}",
                         "ví dụ": r"\tan(x + \pi) = \tan x"},

    "Phương trình lượng giác cơ bản": {"định nghĩa": r"Các phương trình dạng sin x = a, cos x = a, tan x = a.",
                                       "kí hiệu": r"\sin x = a",
                                       "công thức": r"\sin x = a \Leftrightarrow x = \arcsin a + k2\pi",
                                       "ví dụ": r"\sin x = 0 \Leftrightarrow x = k\pi"}
}
chuong_2_toan_11 = {
    "Dãy số": {"định nghĩa": r"Là một hàm số xác định trên tập các số tự nhiên.",
               "kí hiệu": r"(u_n)",
               "công thức": r"u: \mathbb{N} \to \mathbb{R}",
               "ví dụ": r"u_n = 2n + 1"},

    "Cách cho dãy số": {"định nghĩa": r"Dãy số có thể cho bằng công thức tổng quát, truy hồi hoặc liệt kê.",
                        "kí hiệu": r"u_n, u_{n+1}",
                        "công thức": r"u_{n+1} = f(u_n)",
                        "ví dụ": r"u_1 = 1, u_{n+1} = u_n + 2"},

    "Cấp số cộng": {"định nghĩa": r"Là dãy số mà hiệu của hai số hạng liên tiếp không đổi.",
                    "kí hiệu": r"(u_n), d",
                    "công thức": r"u_n = u_1 + (n-1)d",
                    "ví dụ": r"1, 3, 5, 7, ... (d = 2)"},

    "Số hạng tổng quát của cấp số cộng": {"định nghĩa": r"Số hạng thứ n được xác định theo công thức tổng quát.",
                                           "kí hiệu": r"u_n",
                                           "công thức": r"u_n = u_1 + (n-1)d",
                                           "ví dụ": r"u_5 = u_1 + 4d"},

    "Tổng n số hạng đầu của cấp số cộng": {"định nghĩa": r"Tổng của n số hạng đầu tiên của cấp số cộng.",
                                            "kí hiệu": r"S_n",
                                            "công thức": r"S_n = \dfrac{n(u_1 + u_n)}{2}",
                                            "ví dụ": r"S_5 = \dfrac{5(u_1 + u_5)}{2}"},

    "Cấp số nhân": {"định nghĩa": r"Là dãy số mà tỉ số của hai số hạng liên tiếp không đổi.",
                    "kí hiệu": r"(u_n), q",
                    "công thức": r"u_n = u_1 q^{n-1}",
                    "ví dụ": r"2, 4, 8, 16, ... (q = 2)"},

    "Số hạng tổng quát của cấp số nhân": {"định nghĩa": r"Số hạng thứ n được xác định theo công thức tổng quát.",
                                          "kí hiệu": r"u_n",
                                          "công thức": r"u_n = u_1 q^{n-1}",
                                          "ví dụ": r"u_4 = u_1 q^3"},

    "Tổng n số hạng đầu của cấp số nhân (q ≠ 1)": {"định nghĩa": r"Tổng của n số hạng đầu tiên của cấp số nhân khi q khác 1.",
                                                    "kí hiệu": r"S_n",
                                                    "công thức": r"S_n = u_1 \dfrac{q^n - 1}{q - 1}",
                                                    "ví dụ": r"S_3 = u_1 \dfrac{q^3 - 1}{q - 1}"}
}
chuong_3_toan_11 = {
    "Mẫu số liệu ghép nhóm": {"định nghĩa": r"Là mẫu số liệu được phân chia thành các lớp (nhóm) với tần số tương ứng.",
                               "kí hiệu": r"[a_i; b_i), n_i",
                               "công thức": r"N = \sum n_i",
                               "ví dụ": r"Chia điểm kiểm tra thành các lớp: [0;2), [2;4), [4;6), ..."},

    "Bảng phân bố tần số ghép nhóm": {"định nghĩa": r"Bảng thể hiện các lớp giá trị và tần số tương ứng.",
                                       "kí hiệu": r"n_i, f_i",
                                       "công thức": r"f_i = \dfrac{n_i}{N}",
                                       "ví dụ": r"Lớp [4;6) có n_i = 10"},

    "Số trung bình cộng của mẫu ghép nhóm": {"định nghĩa": r"Được tính bằng trung bình cộng có trọng số của các giá trị đại diện lớp.",
                                              "kí hiệu": r"\overline{x}",
                                              "công thức": r"\overline{x} = \dfrac{\sum n_i x_i}{N}",
                                              "ví dụ": r"Nếu x_i là trung điểm lớp thì \overline{x} = \dfrac{\sum n_i x_i}{N}"},

    "Trung vị của mẫu ghép nhóm": {"định nghĩa": r"Là giá trị chia mẫu thành hai phần có tần số bằng nhau (xấp xỉ theo lớp chứa trung vị).",
                                    "kí hiệu": r"Me",
                                    "công thức": r"Me = L + \dfrac{\dfrac{N}{2} - F}{n_m}h",
                                    "ví dụ": r"L là cận dưới lớp trung vị, h là độ rộng lớp"},

    "Mốt của mẫu ghép nhóm": {"định nghĩa": r"Là giá trị đại diện của lớp có tần số lớn nhất (lớp mốt).",
                               "kí hiệu": r"Mo",
                               "công thức": r"Mo = L + \dfrac{n_m - n_{m-1}}{(n_m - n_{m-1}) + (n_m - n_{m+1})}h",
                               "ví dụ": r"L là cận dưới lớp có tần số lớn nhất"},

    "Ý nghĩa của các số đặc trưng": {"định nghĩa": r"Các số trung bình, trung vị, mốt phản ánh giá trị trung tâm của mẫu số liệu.",
                                      "kí hiệu": r"\overline{x}, Me, Mo",
                                      "công thức": r"\overline{x} \approx Me \approx Mo \text{ (khi phân bố đối xứng)}",
                                      "ví dụ": r"Dùng để đánh giá mức độ điển hình của dữ liệu"}
}
chuong_4_toan_11 = {
    "Hai đường thẳng song song": {"định nghĩa": r"Hai đường thẳng trong không gian được gọi là song song nếu chúng cùng nằm trong một mặt phẳng và không có điểm chung.",
                                   "kí hiệu": r"a \parallel b",
                                   "công thức": r"a \parallel b \Leftrightarrow a, b \subset (P) \text{ và } a \cap b = \varnothing",
                                   "ví dụ": r"Trong hình hộp ABCD.A'B'C'D', ta có AB \parallel CD"},

    "Đường thẳng song song với mặt phẳng": {"định nghĩa": r"Đường thẳng d được gọi là song song với mặt phẳng (P) nếu d không nằm trong (P) và không có điểm chung với (P).",
                                             "kí hiệu": r"d \parallel (P)",
                                             "công thức": r"d \parallel (P) \Leftrightarrow d \cap (P) = \varnothing",
                                             "ví dụ": r"Trong hình chóp S.ABCD, nếu AB \parallel CD thì AB \parallel (SCD)"},

    "Hai mặt phẳng song song": {"định nghĩa": r"Hai mặt phẳng được gọi là song song nếu chúng không có điểm chung.",
                                 "kí hiệu": r"(P) \parallel (Q)",
                                 "công thức": r"(P) \parallel (Q) \Rightarrow (P) \cap (Q) = \varnothing",
                                 "ví dụ": r"Trong hình hộp, (ABCD) \parallel (A'B'C'D')"},

    "Tính chất đường thẳng song song": {"định nghĩa": r"Qua một điểm nằm ngoài một đường thẳng cho trước, có duy nhất một đường thẳng song song với đường thẳng đó.",
                                         "kí hiệu": r"\exists ! d' \parallel d",
                                         "công thức": r"M \notin d \Rightarrow \exists ! d' \text{ qua } M \text{ và } d' \parallel d",
                                         "ví dụ": r"Qua điểm A ngoài d, chỉ có một đường thẳng song song với d"},

    "Định lí về giao tuyến song song": {"định nghĩa": r"Nếu hai mặt phẳng song song bị cắt bởi mặt phẳng thứ ba thì các giao tuyến song song với nhau.",
                                         "kí hiệu": r"d_1 \parallel d_2",
                                         "công thức": r"(P) \parallel (Q), (R) \cap (P) = d_1, (R) \cap (Q) = d_2 \Rightarrow d_1 \parallel d_2",
                                         "ví dụ": r"Cắt hai mặt phẳng song song bởi mặt phẳng thứ ba được hai đường thẳng song song"}
}
chuong_5_toan_11 = {
    "Giới hạn của dãy số": {"định nghĩa": r"Dãy số (u_n) có giới hạn L khi n tiến tới vô cực nếu u_n tiến gần đến L.",
                             "kí hiệu": r"\lim u_n = L",
                             "công thức": r"\lim_{n \to \infty} u_n = L",
                             "ví dụ": r"\lim_{n \to \infty} \dfrac{1}{n} = 0"},

    "Giới hạn hữu hạn của dãy số": {"định nghĩa": r"Dãy số có giới hạn bằng một số thực xác định.",
                                     "kí hiệu": r"\lim_{n \to \infty} u_n = L",
                                     "công thức": r"\lim_{n \to \infty} c = c (c là hằng số)",
                                     "ví dụ": r"\lim_{n \to \infty} 5 = 5"},

    "Giới hạn vô cực của dãy số": {"định nghĩa": r"Dãy số có giá trị tăng hoặc giảm không bị chặn.",
                                    "kí hiệu": r"\lim u_n = \pm\infty",
                                    "công thức": r"\lim_{n \to \infty} n = +\infty",
                                    "ví dụ": r"\lim_{n \to \infty} (-n) = -\infty"},

    "Giới hạn của hàm số tại một điểm": {"định nghĩa": r"Hàm số f(x) có giới hạn L khi x tiến tới a nếu f(x) tiến gần đến L.",
                                          "kí hiệu": r"\lim_{x \to a} f(x)",
                                          "công thức": r"\lim_{x \to a} f(x) = L",
                                          "ví dụ": r"\lim_{x \to 2} (x^2) = 4"},

    "Giới hạn một bên": {"định nghĩa": r"Giới hạn khi x tiến đến a từ bên trái hoặc bên phải.",
                         "kí hiệu": r"\lim_{x \to a^-}, \lim_{x \to a^+}",
                         "công thức": r"\lim_{x \to a} f(x) tồn tại ⇔ \lim_{x \to a^-} f(x) = \lim_{x \to a^+} f(x)",
                         "ví dụ": r"\lim_{x \to 0^+} \dfrac{1}{x} = +\infty"},

    "Giới hạn vô cực của hàm số": {"định nghĩa": r"Hàm số có giá trị tăng hoặc giảm không bị chặn khi x tiến tới a hoặc vô cực.",
                                    "kí hiệu": r"\lim_{x \to a} f(x) = \pm\infty",
                                    "công thức": r"\lim_{x \to +\infty} \dfrac{1}{x} = 0",
                                    "ví dụ": r"\lim_{x \to 0} \dfrac{1}{x^2} = +\infty"},

    "Các định lí về giới hạn": {"định nghĩa": r"Các quy tắc tính giới hạn của tổng, hiệu, tích, thương.",
                                 "kí hiệu": r"\lim (f(x) + g(x))",
                                 "công thức": r"\lim (f(x) + g(x)) = \lim f(x) + \lim g(x)",
                                 "ví dụ": r"\lim_{x \to 1} (x^2 + 3x) = 1 + 3 = 4"}
}