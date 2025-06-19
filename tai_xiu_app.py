
import streamlit as st

st.set_page_config(page_title="App Tài/Xỉu", layout="centered")
st.title("🎲 App Theo Dõi Cầu Tài/Xỉu")

# Khởi tạo session state
if "history" not in st.session_state:
    st.session_state.history = []
if "suggestion" not in st.session_state:
    st.session_state.suggestion = ""

# Hàm xác định Tài/Xỉu từ điểm
def get_result(point):
    try:
        point = int(point)
        if point >= 11:
            return "Tài"
        elif point <= 10:
            return "Xỉu"
        else:
            return "-"
    except:
        return "-"

# Hàm gợi ý tay tiếp theo
def suggest_next(history):
    if len(history) < 2:
        return "Chưa đủ dữ liệu"
    last = history[-1]
    second_last = history[-2]
    if last == second_last:
        return f"Có thể tiếp tục đánh {last}"
    else:
        return "Cầu gãy - Quan sát thêm"

# Giao diện nhập điểm
with st.form("nhap_diem"):
    col1, col2 = st.columns([2,1])
    with col1:
        point = st.text_input("Nhập điểm số", "")
    with col2:
        submit = st.form_submit_button("Thêm")

    if submit and point:
        result = get_result(point)
        if result != "-":
            st.session_state.history.append(result)
            st.session_state.suggestion = suggest_next(st.session_state.history)

# Hiển thị chuỗi kết quả
st.subheader("📊 Chuỗi cầu:")
if st.session_state.history:
    st.write(" ➡️ ".join(st.session_state.history))
else:
    st.write("Chưa có dữ liệu")

# Gợi ý tay tiếp theo
st.subheader("💡 Gợi ý:")
if st.session_state.suggestion:
    st.info(st.session_state.suggestion)

# Reset phiên
if st.button("🔄 Reset phiên"):
    st.session_state.history = []
    st.session_state.suggestion = ""
    st.success("Đã reset phiên!")
