import streamlit as st
import time

# --- CẤU HÌNH TRANG (Phải đặt dòng này đầu tiên) ---
st.set_page_config(
    page_title="Magic Lab - Phòng Thí Nghiệm Ảo",
    page_icon="🧪",
    layout="wide" # Dùng 'wide' để chế độ 2 người chơi hiển thị đẹp hơn
)

# --- CSS TÙY CHỈNH ---
st.markdown("""
<style>
    .big-font { font-size:20px !important; font-weight: bold; }
    .success-text { color: green; font-weight: bold; font-size: 24px; text-align: center; }
    .error-text { color: red; font-weight: bold; }
    /* Tô màu nền cho 2 phe */
    [data-testid="stVerticalBlock"] > [style*="flex-direction: column;"] > [data-testid="stVerticalBlock"] {
        border: 1px solid #f0f2f6;
        border-radius: 10px;
        padding: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# CHỨC NĂNG 1: CHẾ ĐỘ LUYỆN TẬP CÁ NHÂN (SINGLE PLAYER)
# ==============================================================================
def che_do_luyen_tap():
    st.header("⚗️ CHẾ ĐỘ LUYỆN TẬP: CÂN BẰNG PHƯƠNG TRÌNH")
    st.info("Hướng dẫn: Nhập hệ số cân bằng vào các ô bên dưới để kích hoạt phản ứng.")

    # Chọn bài tập (Để mở rộng sau này)
    bai_tap = st.selectbox("Chọn phản ứng muốn thực hiện:", 
                           ["Sắt cháy trong Oxi (Fe + O2)", "Phốt pho cháy (P + O2)"])

    st.divider()

    if bai_tap == "Sắt cháy trong Oxi (Fe + O2)":
        st.subheader("Phương trình:  $Fe + O_2 \longrightarrow Fe_3O_4$")
        
        # Giao diện nhập liệu
        c1, c2, c3, c4, c5 = st.columns([1, 0.2, 1, 0.2, 1])
        with c1:
            h1 = st.number_input("Hệ số Fe", 1, 10, 1, key="s_fe")
        with c2: st.markdown("## +")
        with c3:
            h2 = st.number_input("Hệ số O2", 1, 10, 1, key="s_o2")
        with c4: st.markdown("## ➝")
        with c5:
            h3 = st.number_input("Hệ số Fe3O4", 1, 10, 1, key="s_fe3o4")

        # Nút kiểm tra
        if st.button("🔥 KÍCH HOẠT PHẢN ỨNG 🔥", use_container_width=True):
            # Logic kiểm tra
            fe_trai, fe_phai = h1 * 1, h3 * 3
            o_trai, o_phai = h2 * 2, h3 * 4
            
            if fe_trai == fe_phai and o_trai == o_phai:
                st.balloons()
                st.markdown('<p class="success-text">✨ CHÍNH XÁC! PHẢN ỨNG XẢY RA MÃNH LIỆT! ✨</p>', unsafe_allow_html=True)
                st.video("https://www.youtube.com/watch?v=5MDH92VxPEQ") # Video Fe cháy
            else:
                st.error(f"Chưa cân bằng! Fe: {fe_trai} vs {fe_phai} | Oxi: {o_trai} vs {o_phai}")

    elif bai_tap == "Phốt pho cháy (P + O2)":
        st.subheader("Phương trình:  $P + O_2 \longrightarrow P_2O_5$")
        # Copy giao diện tương tự và sửa logic kiểm tra...
        # (Bạn có thể thêm code tương tự như trên vào đây)
        st.warning("Tính năng đang cập nhật thêm bài tập...")

# ==============================================================================
# CHỨC NĂNG 2: CHẾ ĐỘ ĐỐI KHÁNG (WIZARD DUEL)
# ==============================================================================
def che_do_doi_khang():
    st.header("⚔️ ĐẠI CHIẾN PHÙ THỦY (2 NGƯỜI CHƠI)")
    st.markdown("Luật chơi: Hai bên cùng giải 5 phương trình. Bên nào xong trước và đúng hết sẽ thắng!")
    st.divider()

    # Dữ liệu 5 phương trình
    equations = [
        ("Na + O2", "Na2O", [4, 1, 2]),
        ("Fe + HCl", "FeCl2 + H2", [1, 2, 1, 1]),
        ("Al + O2", "Al2O3", [4, 3, 2]),
        ("Mg + HCl", "MgCl2 + H2", [1, 2, 1, 1]),
        ("P + O2", "P2O5", [4, 5, 2])
    ]

    col1, col_mid, col2 = st.columns([1, 0.05, 1])

    # --- NGƯỜI CHƠI 1 ---
    with col1:
        st.subheader("❄️ ĐỘI BĂNG (Player 1)")
        p1_inputs = []
        for i, eq in enumerate(equations):
            st.write(f"**Câu {i+1}:** {eq[0]} ➝ {eq[1]}")
            cols = st.columns(len(eq[2]))
            row = [c.number_input(f"p1_c{i}_{j}", 1, 10, 1, key=f"p1_{i}_{j}", label_visibility="collapsed") for j, c in enumerate(cols)]
            p1_inputs.append(row)
            st.write("---")
        
        if st.button("❄️ ĐỘI BĂNG NỘP BÀI", type="primary", use_container_width=True):
            score = sum([1 for i, ans in enumerate(p1_inputs) if ans == equations[i][2]])
            if score == 5:
                st.balloons()
                st.success("🏆 ĐỘI BĂNG CHIẾN THẮNG TUYỆT ĐỐI!")
            else:
                st.error(f"Sai rồi! Bạn mới đúng {score}/5 câu.")

    # --- ĐƯỜNG KẺ GIỮA ---
    with col_mid:
        st.markdown("<div style='height: 100%; border-left: 2px solid grey;'></div>", unsafe_allow_html=True)

    # --- NGƯỜI CHƠI 2 ---
    with col2:
        st.subheader("🔥 ĐỘI LỬA (Player 2)")
        p2_inputs = []
        for i, eq in enumerate(equations):
            st.write(f"**Câu {i+1}:** {eq[0]} ➝ {eq[1]}")
            cols = st.columns(len(eq[2]))
            row = [c.number_input(f"p2_c{i}_{j}", 1, 10, 1, key=f"p2_{i}_{j}", label_visibility="collapsed") for j, c in enumerate(cols)]
            p2_inputs.append(row)
            st.write("---")

        if st.button("🔥 ĐỘI LỬA NỘP BÀI", type="primary", use_container_width=True):
            score = sum([1 for i, ans in enumerate(p2_inputs) if ans == equations[i][2]])
            if score == 5:
                st.snow()
                st.success("🏆 ĐỘI LỬA CHIẾN THẮNG TUYỆT ĐỐI!")
            else:
                st.error(f"Sai rồi! Bạn mới đúng {score}/5 câu.")

# ==============================================================================
# MENU ĐIỀU HƯỚNG CHÍNH (SIDEBAR)
# ==============================================================================

# Tạo thanh bên (Sidebar) để chọn chế độ
st.sidebar.title("MENU ĐIỀU KHIỂN")
chon_che_do = st.sidebar.radio(
    "Chọn chế độ chơi:",
    ["Luyện Tập (1 Người)", "Đại Chiến (2 Người)"]
)

st.sidebar.markdown("---")
st.sidebar.info("Ứng dụng hỗ trợ môn KHTN 8\n© Giáo viên thiết kế.")

# Điều hướng logic
if chon_che_do == "Luyện Tập (1 Người)":
    che_do_luyen_tap()
else:
    che_do_doi_khang()
