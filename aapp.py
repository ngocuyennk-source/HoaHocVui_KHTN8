import streamlit as st
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="Magic Chemical Lab",
    page_icon="🧪",
    layout="centered"
)

# --- CSS TÙY CHỈNH (Để giao diện đẹp hơn) ---
st.markdown("""
<style>
    .big-font { font-size:20px !important; font-weight: bold; }
    .stButton>button { width: 100%; background-color: #ff4b4b; color: white; }
    .success-text { color: green; font-weight: bold; font-size: 24px; }
    .error-text { color: red; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# --- TIÊU ĐỀ VÀ GIỚI THIỆU ---
st.title("🧪 Phòng Thí Nghiệm Ma Thuật")
st.markdown("""
**Nhiệm vụ của Phù thủy tập sự:** Hãy tìm ra **"Thần chú số"** (hệ số cân bằng) để kích hoạt phản ứng giữa **Sắt (Iron** và **Oxygen ($O_2$)**.**Nhiệm vụ của Phù thủy tập sự:** Hãy tìm ra **"Thần chú số"** (hệ số cân bằng) để kích hoạt phản ứng giữa **Sắt (Ironr** và **Oxygen ($O_2$)**.ằng phương trình sau:")

# Chia cột để tạo giao diện ngang giống phương trình hóa học
c1, c2, c3, c4, c5 = st.columns([1, 0.5, 1, 0.5, 1])

with c1:
    st.markdown("### Fe")
    # min_value=1 vì hệ số không thể bằng 0
    he_so_Fe = st.number_input("Hệ số Fe", min_value=1, value=1, label_visibility="collapsed")

with c2:
    st.markdown("## +")

with c3:
    st.markdown("### $O_2$")
    he_so_O2 = st.number_input("Hệ số O2", min_value=1, value=1, label_visibility="collapsed")

with c4:
    st.markdown("## ➝")

with c5:
    st.markdown("### $Fe_3O_4$")
    he_so_Fe3O4 = st.number_input("Hệ số Fe3O4", min_value=1, value=1, label_visibility="collapsed")

st.write("") # Khoảng cách

# --- XỬ LÝ LOGIC (NÚT BẤM) ---
if st.button("🔥 KÍCH HOẠT PHẢN ỨNG 🔥"):
    
    # 1. Tính toán số nguyên tử 2 vế
    # Vế trái (Tham gia)
    Fe_trai = he_so_Fe * 1
    O_trai = he_so_O2 * 2
    
    # Vế phải (Sản phẩm)
    Fe_phai = he_so_Fe3O4 * 3
    O_phai = he_so_Fe3O4 * 4
    
    # Tạo thanh tiến trình (Progress bar) cho hồi hộp
    progress_text = "Đang nạp năng lượng..."
    my_bar = st.progress(0, text=progress_text)
    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(0.5)
    my_bar.empty() # Xóa thanh tiến trình

    # 2. Kiểm tra điều kiện cân bằng
    if (Fe_trai == Fe_phai) and (O_trai == O_phai):
        # --- TRƯỜNG HỢP ĐÚNG (SUCCESS) ---
        st.balloons() # Hiệu ứng bóng bay chúc mừng
        st.markdown('<p class="success-text">✨ CHÍNH XÁC! PHÉP THUẬT ĐÃ ĐƯỢC KÍCH HOẠT! ✨</p>', unsafe_allow_html=True)
        
        # HIỆN PHẦN THƯỞNG: VIDEO PHẢN ỨNG THỰC TẾ
        # Bạn có thể thay link youtube này bằng link khác hoặc video trong máy
        st.video("https://www.youtube.com/watch?v=5MDH92VxPEQ") 
        
        st.info("💡 **Ứng dụng thực tế:** Phản ứng này toả nhiệt rất mạnh, các tia lửa bắn ra chính là các hạt Oxide sắt từ nóng đỏ. Nó là cơ sở để tạo ra pháo hoa đơn giản!")
        
    else:
        # --- TRƯỜNG HỢP SAI (ERROR) ---
        st.error("💥 BÙM! Lò luyện thuốc đã nổ vì sai công thức!")
        
        # Báo lỗi thông minh (Chỉ ra cụ thể sai ở đâu)
        error_msg = ""
        if Fe_trai != Fe_phai:
            error_msg += f"- **Nguyên tố Sắt (Fe):** Bên trái có {Fe_trai}, nhưng bên phải có {Fe_phai}. Vẫn chưa cân bằng!\n"
        if O_trai != O_phai:
            error_msg += f"- **Nguyên tố Oxygen (O):** Bên trái có {O_trai}, nhưng bên phải có {O_phai}. Oxygen đã bay đi đâu rồi?\n"             
        st.warning(error_msg)
        st.write("👉 Hãy thử điều chỉnh lại các con số và kích hoạt lại nhé!")

# --- FOOTER ---
st.markdown("---")
st.caption("Ứng dụng hỗ trợ học tập môn KHTN 8 - Sáng kiến kinh nghiệm của Giáo viên.")
