import streamlit as st
import time
import random

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="Magic Lab - Disney Edition",
    page_icon="🔮",
    layout="wide"
)

# ==============================================================================
# PHẦN CSS TRANG TRÍ (ĐÃ NÂNG CẤP ĐỘ SÁNG)
# ==============================================================================
st.markdown("""
<style>
    /* 1. Nhúng Font chữ */
    @import url('https://fonts.googleapis.com/css2?family=Jolly+Lodger&family=Creepster&family=Roboto:wght@400;700&display=swap');

    /* 2. Hình nền & Màu chữ toàn trang */
    .stApp {
        background: radial-gradient(circle at center, #2b1055 0%, #000000 100%);
        background-size: cover;
        background-attachment: fixed;
        color: #ffffff !important; /* Buộc chữ màu trắng */
    }
    
    /* Chỉnh màu cho tất cả văn bản thường */
    p, span, div, label {
        color: #e0e0e0;
        font-family: 'Roboto', sans-serif;
        font-size: 1.1rem;
    }

    /* 3. Tiêu đề lớn */
    h1 {
        font-family: 'Creepster', cursive;
        color: #00ff9d; 
        text-shadow: 4px 4px 0px #4b0082;
        text-align: center;
        font-size: 5rem !important;
        margin-bottom: 10px;
    }

    h2 {
        font-family: 'Jolly Lodger', cursive;
        color: #ffcc00;
        text-shadow: 3px 3px 0px #000;
        font-size: 3.5rem !important;
        text-align: center;
    }

    /* 4. Thẻ chứa (Card) - Tăng độ sáng nền để chữ dễ đọc hơn */
    .team-card {
        background: rgba(0, 0, 0, 0.6); /* Nền đen mờ đậm hơn để nổi chữ trắng */
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 25px;
        margin-top: 10px;
        border: 2px solid rgba(255, 255, 255, 0.2);
        box-shadow: 0 0 20px rgba(0, 0, 0, 0.8);
    }
    
    .glow-ice { box-shadow: 0 0 30px #00ffff; border: 2px solid #00ffff; }
    .glow-fire { box-shadow: 0 0 30px #ff4500; border: 2px solid #ff4500; }

    /* 5. Nút bấm */
    .stButton > button {
        font-family: 'Jolly Lodger', cursive;
        font-size: 1.8rem;
        background: linear-gradient(180deg, #6a11cb 0%, #2575fc 100%);
        color: white !important;
        border: 2px solid #fff;
        border-radius: 15px;
        height: 60px;
        transition: transform 0.2s;
    }
    .stButton > button:hover {
        transform: scale(1.05);
        color: #ffcc00 !important;
        border-color: #ffcc00;
    }

    /* 6. Ô nhập liệu - Làm sáng lên */
    .stNumberInput input {
        background-color: rgba(255, 255, 255, 0.9) !important; /* Nền trắng sáng */
        color: #2b1055 !important; /* Chữ đậm màu tím */
        font-weight: 900;
        font-size: 1.5rem;
        border: 2px solid #00ff9d;
        border-radius: 10px;
        text-align: center;
    }
    
    /* 7. Thông báo lỗi/thành công to rõ */
    .stAlert {
        font-weight: bold;
        font-size: 1.2rem;
    }

</style>
""", unsafe_allow_html=True)

# ==============================================================================
# HÀM HỖ TRỢ: TẠO GỢI Ý THÔNG MINH (SMART HINTS)
# ==============================================================================
def get_hint(level, inputs):
    """
    Hàm này kiểm tra hệ số nhập vào và trả về gợi ý cụ thể xem nguyên tố nào đang sai.
    inputs: Danh sách hệ số [a, b, c...]
    """
    try:
        msg = ""
        # Level 0: Na + O2 -> Na2O (a, b, c)
        if level == 0:
            a, b, c = inputs
            if a != 2*c: msg += f"⚠️ Natri: Trái có {a}, Phải có {2*c}. Chưa bằng! "
            if 2*b != c: msg += f"⚠️ Oxi: Trái có {2*b}, Phải có {c}. Oxi đi đâu rồi? "
        
        # Level 1: Fe + HCl -> FeCl2 + H2 (a, b, c, d)
        elif level == 1:
            a, b, c, d = inputs
            if a != c: msg += f"⚠️ Sắt (Fe) chưa cân bằng. "
            if b != 2*c: msg += f"⚠️ Clo (Cl): Trái {b}, Phải {2*c}. "
            if b != 2*d: msg += f"⚠️ Hiđro (H) đang lệch. "

        # Level 2: Al + O2 -> Al2O3 (a, b, c)
        elif level == 2:
            a, b, c = inputs
            if a != 2*c: msg += f"⚠️ Nhôm (Al) lệch rồi. "
            if 2*b != 3*c: msg += f"⚠️ Oxi: Trái {2*b}, Phải {3*c}. Tìm Bội chung nhỏ nhất xem? "

        # Level 3: Mg + HCl -> MgCl2 + H2 (a, b, c, d)
        elif level == 3:
            a, b, c, d = inputs
            if a != c: msg += "⚠️ Magie (Mg) chưa bằng. "
            if b != 2*c: msg += "⚠️ Clo (Cl) đang lệch cán cân. "
            
        # Level 4: P + O2 -> P2O5 (a, b, c)
        elif level == 4:
            a, b, c = inputs
            if a != 2*c: msg += "⚠️ Phốt pho (P) chưa ổn. "
            if 2*b != 5*c: msg += "⚠️ Oxi: Bên chẵn bên lẻ sao bằng được? "

        if msg == "": 
            return "⚖️ Cán cân vẫn đang lệch! Hãy kiểm tra lại tỷ lệ."
        return msg
    except:
        return "❌ Công thức sai cấu trúc!"

# Danh sách ảnh GIF "thất bại" vui nhộn
FAIL_GIFS = [
    "https://media.giphy.com/media/oe33xf3B50fsc/giphy.gif", # Nổ hoạt hình
    "https://media.giphy.com/media/26n6WywJyh39n1pW8/giphy.gif", # Minion nổ
    "https://media.giphy.com/media/3oKIPwoeGErMmaI43S/giphy.gif", # Phù thủy thất bại
    "https://media.giphy.com/media/l2JHVUriDGEtWOx0c/giphy.gif"  # Cân lệch (tượng trưng)
]

# ==============================================================================
# LOGIC GAME CHÍNH
# ==============================================================================
def che_do_doi_khang():
    st.markdown("<h1>⚡ MAGIC LAB DUEL ⚡</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color: #ccc;'>Đại Chiến Phòng Thí Nghiệm Ma Thuật</h3>", unsafe_allow_html=True)
    
    # Nút Reset
    col_r1, col_r2, col_r3 = st.columns([1, 2, 1])
    with col_r2:
        if st.button("🔄 CHẾ TẠO LẠI TỪ ĐẦU", use_container_width=True):
            st.session_state.p1_index = 0
            st.session_state.p2_index = 0
            st.rerun()

    st.write("") 

    # KHỞI TẠO STATE
    if 'p1_index' not in st.session_state: st.session_state.p1_index = 0
    if 'p2_index' not in st.session_state: st.session_state.p2_index = 0

    # DỮ LIỆU
    equations = [
        ("CẤP 1: THUỐC NỔ NHẸ", "Na + O_2 \longrightarrow Na_2O", [4, 1, 2]),
        ("CẤP 2: AXIT RỒNG", "Fe + HCl \longrightarrow FeCl_2 + H_2", [1, 2, 1, 1]),
        ("CẤP 3: GIÁP KIM LOẠI", "Al + O_2 \longrightarrow Al_2O_3", [4, 3, 2]),
        ("CẤP 4: THUỐC TĂNG LỰC", "Mg + HCl \longrightarrow MgCl_2 + H_2", [1, 2, 1, 1]),
        ("CẤP 5: BOM KHÓI", "P + O_2 \longrightarrow P_2O_5", [4, 5, 2])
    ]

    col1, col_mid, col2 = st.columns([1, 0.1, 1])

    # --- ĐỘI 1 (BĂNG) ---
    with col1:
        st.markdown("""
        <div class='team-card glow-ice'>
            <h2 style='color: #00ffff;'>❄️ TEAM ICE</h2>
        </div>
        """, unsafe_allow_html=True)
        st.write("")

        if st.session_state.p1_index < len(equations):
            idx = st.session_state.p1_index
            q = equations[idx]
            
            st.progress(idx / len(equations), text=f"Mana: {idx}/5")
            
            with st.container(border=True):
                st.markdown(f"**🔮 {q[0]}**")
                st.latex(q[1])
            
            with st.form(key=f"f1_{idx}"):
                cols = st.columns(len(q[2]))
                inputs = [c.number_input("HS", 1, 99, 1, key=f"i1_{idx}_{i}") for i, c in enumerate(cols)]
                submit = st.form_submit_button("🧪 PHA CHẾ")
            
            if submit:
                if inputs == q[2]:
                    st.success("✨ CHÍNH XÁC! PHA CHẾ THÀNH CÔNG!")
                    time.sleep(0.8)
                    st.session_state.p1_index += 1
                    st.rerun()
                else:
                    # HIỆU ỨNG TRẢ LỜI SAI
                    hint_msg = get_hint(idx, inputs) # Lấy gợi ý thông minh
                    st.error(f"💥 BÙM! {hint_msg}")
                    st.image(random.choice(FAIL_GIFS), caption="Thí nghiệm thất bại rồi!", use_container_width=True)
        else:
            st.balloons()
            st.markdown("<div class='team-card glow-ice'><h2 style='color:#00ffff'>WINNER!</h2></div>", unsafe_allow_html=True)
            st.image("https://media.giphy.com/media/TdfyKrN7HGTIY/giphy.gif")

    # --- CỘT GIỮA ---
    with col_mid:
        st.markdown("<br><br><br><h1 style='color:white'>VS</h1>", unsafe_allow_html=True)

    # --- ĐỘI 2 (LỬA) ---
    with col2:
        st.markdown("""
        <div class='team-card glow-fire'>
            <h2 style='color: #ff4500;'>🔥 TEAM FIRE</h2>
        </div>
        """, unsafe_allow_html=True)
        st.write("")

        if st.session_state.p2_index < len(equations):
            idx = st.session_state.p2_index
            q = equations[idx]
            
            st.progress(idx / len(equations), text=f"Mana: {idx}/5")
            
            with st.container(border=True):
                st.markdown(f"**🔮 {q[0]}**")
                st.latex(q[1])
            
            with st.form(key=f"f2_{idx}"):
                cols = st.columns(len(q[2]))
                inputs = [c.number_input("HS", 1, 99, 1, key=f"i2_{idx}_{i}") for i, c in enumerate(cols)]
                submit = st.form_submit_button("🧪 PHA CHẾ")
            
            if submit:
                if inputs == q[2]:
                    st.success("✨ CHÍNH XÁC! TUYỆT VỜI!")
                    time.sleep(0.8)
                    st.session_state.p2_index += 1
                    st.rerun()
                else:
                    # HIỆU ỨNG TRẢ LỜI SAI
                    hint_msg = get_hint(idx, inputs)
                    st.error(f"💥 NỔ TUNG! {hint_msg}")
                    st.image(random.choice(FAIL_GIFS), caption="Cẩn thận củi lửa!", use_container_width=True)
        else:
            st.snow()
            st.markdown("<div class='team-card glow-fire'><h2 style='color:#ff4500'>WINNER!</h2></div>", unsafe_allow_html=True)
            st.image("https://media.giphy.com/media/Lopx9eUi34rbq/giphy.gif")

if __name__ == "__main__":
    che_do_doi_khang()
