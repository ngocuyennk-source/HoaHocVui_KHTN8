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
# # ==============================================================================
import streamlit as st
import time

# ==============================================================================
# CHỨC NĂNG 2: CHẾ ĐỘ ĐỐI KHÁNG (CẬP NHẬT: TRẢ LỜI ĐÚNG MỚI QUA CÂU)
# ==============================================================================
def che_do_doi_khang():
    st.header("⚔️ ĐẠI CHIẾN PHÙ THỦY (LUẬT MỚI: TỪNG CÂU)")
    st.markdown("Luật chơi: **Giải quyết xong câu hiện tại mới được mở khóa câu tiếp theo.** Đội nào về đích trước sẽ thắng!")
    
    # Nút Reset game để chơi lại từ đầu
    if st.button("🔄 Bắt đầu trận đấu mới"):
        st.session_state.p1_index = 0
        st.session_state.p2_index = 0
        st.rerun()

    st.divider()

    # 1. KHỞI TẠO TRẠNG THÁI (SESSION STATE) NẾU CHƯA CÓ
    # Biến này giúp nhớ xem mỗi đội đang ở câu số mấy (0, 1, 2...)
    if 'p1_index' not in st.session_state:
        st.session_state.p1_index = 0
    if 'p2_index' not in st.session_state:
        st.session_state.p2_index = 0

    # 2. DỮ LIỆU CÂU HỎI (Câu hỏi, Phương trình hiển thị, Đáp án đúng)
    equations = [
        ("Câu 1: Khởi động", "Na + O_2 \longrightarrow Na_2O", [4, 1, 2]),
        ("Câu 2: Axit cơ bản", "Fe + HCl \longrightarrow FeCl_2 + H_2", [1, 2, 1, 1]),
        ("Câu 3: Kim loại cháy", "Al + O_2 \longrightarrow Al_2O_3", [4, 3, 2]),
        ("Câu 4: Tăng tốc", "Mg + HCl \longrightarrow MgCl_2 + H_2", [1, 2, 1, 1]),
        ("Câu 5: Về đích", "P + O_2 \longrightarrow P_2O_5", [4, 5, 2])
    ]

    col1, col_mid, col2 = st.columns([1, 0.1, 1])

    # --- ĐỘI 1 (PHE BĂNG - TRÁI) ---
    with col1:
        st.subheader("❄️ ĐỘI BĂNG")
        
        # Kiểm tra: Nếu chưa hết câu hỏi thì hiện câu tiếp theo
        if st.session_state.p1_index < len(equations):
            # Lấy dữ liệu câu hỏi hiện tại dựa trên chỉ số index
            current_q_p1 = equations[st.session_state.p1_index]
            
            # Hiển thị thanh tiến trình
            st.progress(st.session_state.p1_index / len(equations), text=f"Tiến độ: {st.session_state.p1_index}/5")
            
            st.info(f"**{current_q_p1[0]}**")
            st.latex(current_q_p1[1]) # Hiển thị phương trình đẹp
            
            # TẠO FORM NHẬP LIỆU (Để không bị tải lại trang khi nhập số)
            # Quan trọng: key của form phải là duy nhất theo từng câu hỏi
            with st.form(key=f"form_p1_{st.session_state.p1_index}"):
                cols = st.columns(len(current_q_p1[2]))
                inputs_p1 = []
                for idx, c in enumerate(cols):
                    # Key của input cũng phải duy nhất
                    val = c.number_input(f"HS", min_value=1, value=1, label_visibility="collapsed", key=f"p1_input_{st.session_state.p1_index}_{idx}")
                    inputs_p1.append(val)
                
                # Nút nộp bài nằm trong form
                submit_p1 = st.form_submit_button("❄️ Nộp bài & Qua câu")
            
            # XỬ LÝ KHI BẤM NÚT NỘP
            if submit_p1:
                if inputs_p1 == current_q_p1[2]:
                    st.success("Chính xác! Đang mở khóa câu tiếp theo...")
                    time.sleep(0.5) # Dừng 1 xíu cho HS nhìn thấy chữ Chính xác
                    st.session_state.p1_index += 1 # Tăng cấp độ lên 1
                    st.rerun() # Tải lại trang để hiện câu mới
                else:
                    st.error("Chưa đúng! Hãy kiểm tra lại hệ số.")
        else:
            # Khi đã xong hết 5 câu (Về đích)
            st.balloons()
            st.success("🏆 ĐỘI BĂNG ĐÃ VỀ ĐÍCH!")
            st.image("https://media.giphy.com/media/26tOZ42Mg6pbTUPHW/giphy.gif") # Ảnh động cúp vàng (ví dụ)

    # --- ĐƯỜNG KẺ GIỮA ---
    with col_mid:
        # Kẻ một đường dọc để phân chia
        st.markdown("<div style='height: 400px; border-left: 2px solid #e6e6e6; margin-left: 50%;'></div>", unsafe_allow_html=True)

    # --- ĐỘI 2 (PHE LỬA - PHẢI) ---
    with col2:
        st.subheader("🔥 ĐỘI LỬA")
        
        # Logic tương tự Đội 1 nhưng dùng biến p2_index
        if st.session_state.p2_index < len(equations):
            current_q_p2 = equations[st.session_state.p2_index]
            
            st.progress(st.session_state.p2_index / len(equations), text=f"Tiến độ: {st.session_state.p2_index}/5")
            
            st.warning(f"**{current_q_p2[0]}**")
            st.latex(current_q_p2[1])
            
            with st.form(key=f"form_p2_{st.session_state.p2_index}"):
                cols = st.columns(len(current_q_p2[2]))
                inputs_p2 = []
                for idx, c in enumerate(cols):
                    val = c.number_input(f"HS", min_value=1, value=1, label_visibility="collapsed", key=f"p2_input_{st.session_state.p2_index}_{idx}")
                    inputs_p2.append(val)
                
                submit_p2 = st.form_submit_button("🔥 Nộp bài & Qua câu")
            
            if submit_p2:
                if inputs_p2 == current_q_p2[2]:
                    st.success("Chính xác! Đang mở khóa câu tiếp theo...")
                    time.sleep(0.5)
                    st.session_state.p2_index += 1
                    st.rerun()
                else:
                    st.error("Chưa đúng! Hãy kiểm tra lại hệ số.")
        else:
            st.snow()
            st.success("🏆 ĐỘI LỬA ĐÃ VỀ ĐÍCH!")
            st.image("https://media.giphy.com/media/l0HlHJGHe3yAMhdQY/giphy.gif")
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
