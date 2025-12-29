import streamlit as st

st.set_page_config(layout="wide", page_title="Đại Chiến Phù Thủy") # Chỉnh layout rộng để chia đôi đẹp hơn

st.title("⚔️ PHÙ THỦY TRANH TÀI (WIZARD DUEL) ⚔️")
st.markdown("---")

# Dữ liệu 5 phương trình mẫu (Giáo viên có thể thay đổi)
# Cấu trúc: (Chất tham gia, Chất sản phẩm, Đáp án đúng [hệ số])
equations = [
    ("Na + O2", "Na2O", [4, 1, 2]),
    ("Fe + HCl", "FeCl2 + H2", [1, 2, 1, 1]),
    ("Al + O2", "Al2O3", [4, 3, 2]),
    ("P + O2", "P2O5", [4, 5, 2]),
    ("KClO3", "KCl + O2", [2, 2, 3])
]

# Chia 2 cột lớn cho 2 người chơi
col1, col_mid, col2 = st.columns([1, 0.1, 1]) # col_mid để tạo khoảng cách ở giữa

# --- NGƯỜI CHƠI 1 (PHE BĂNG - TRÁI) ---
with col1:
    st.header("❄️ PHE BĂNG (Player 1)")
    st.info("Nhiệm vụ: Cân bằng 5 phương trình bên dưới!")
    
    p1_inputs = [] # Chứa các giá trị nhập của P1
    
    for i, eq in enumerate(equations):
        st.markdown(f"**Câu {i+1}:** {eq[0]} ➝ {eq[1]}")
        # Tạo các ô nhập liệu nhỏ ngang hàng
        cols_input = st.columns(len(eq[2]))
        row_inputs = []
        for j, c in enumerate(cols_input):
            val = c.number_input(f"HS_{i}_{j}_P1", min_value=1, value=1, label_visibility="collapsed", key=f"p1_{i}_{j}")
            row_inputs.append(val)
        p1_inputs.append(row_inputs)
        st.write("---")

    if st.button("❄️ PHE BĂNG HOÀN THÀNH", type="primary"):
        # Kiểm tra đáp án P1
        score_p1 = 0
        for i, ans in enumerate(p1_inputs):
            if ans == equations[i][2]:
                score_p1 += 1
        
        if score_p1 == 5:
            st.balloons()
            st.success("🏆 TUYỆT VỜI! PHE BĂNG ĐÃ CHIẾN THẮNG!")
            st.video("https://www.youtube.com/watch?v=video_bang_tuyet_dep") # Link video phần thưởng
        else:
            st.error(f"Chưa chính xác! Bạn mới đúng {score_p1}/5 câu. Cố lên!")

# --- VẠCH NGĂN CÁCH ---
with col_mid:
    st.markdown("<h1 style='text-align: center; color: grey;'>VS</h1>", unsafe_allow_html=True)

# --- NGƯỜI CHƠI 2 (PHE LỬA - PHẢI) ---
with col2:
    st.header("🔥 PHE LỬA (Player 2)")
    st.warning("Nhiệm vụ: Cân bằng 5 phương trình bên dưới!")
    
    p2_inputs = [] # Chứa các giá trị nhập của P2
    
    for i, eq in enumerate(equations):
        st.markdown(f"**Câu {i+1}:** {eq[0]} ➝ {eq[1]}")
        cols_input = st.columns(len(eq[2]))
        row_inputs = []
        for j, c in enumerate(cols_input):
            val = c.number_input(f"HS_{i}_{j}_P2", min_value=1, value=1, label_visibility="collapsed", key=f"p2_{i}_{j}")
            row_inputs.append(val)
        p2_inputs.append(row_inputs)
        st.write("---")

    if st.button("🔥 PHE LỬA HOÀN THÀNH", type="secondary"):
        # Kiểm tra đáp án P2
        score_p2 = 0
        for i, ans in enumerate(p2_inputs):
            if ans == equations[i][2]:
                score_p2 += 1
        
        if score_p2 == 5:
            st.snow() # Hiệu ứng khác cho đội đỏ (hoặc đổi thành pháo hoa nếu muốn)
            st.success("🏆 XUẤT SẮC! PHE LỬA ĐÃ CHIẾN THẮNG!")
            st.video("https://www.youtube.com/watch?v=video_lua_dep") # Link video phần thưởng
        else:
            st.error(f"Chưa chính xác! Bạn mới đúng {score_p2}/5 câu. Kiểm tra lại nhé!")
