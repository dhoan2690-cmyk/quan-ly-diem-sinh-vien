import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Quản lý điểm sinh viên",
    page_icon="📚",
    layout="wide"
)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")

data = {
    "Họ tên": [
        "Nguyễn Văn An", "Trần Thị Bình",
        "Lê Văn Cường", "Phạm Thị Dung",
        "Hoàng Văn Em", "Vũ Thị Giang",
        "Đỗ Văn Hùng", "Bùi Thị Hoa",
        "Đặng Văn Khánh", "Ngô Thị Lan"
    ],
    "Chuyên cần": [9, 8, 7, 10, 6, 8, 9, 7, 5, 8],
    "Giữa kỳ": [8, 9, 6, 9, 5, 7, 8, 8, 4, 9],
    "Cuối kỳ": [9, 9, 7, 10, 4, 8, 9, 7, 5, 8]
}

df = pd.DataFrame(data)

# Tính điểm tổng kết
df["Tổng kết"] = (
    df["Chuyên cần"] * 0.1
    + df["Giữa kỳ"] * 0.3
    + df["Cuối kỳ"] * 0.6
).round(2)

# Xếp loại
def xep_loai(diem):
    if diem >= 8.5:
        return "Giỏi"
    elif diem >= 7:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    return "Yếu"

df["Xếp loại"] = df["Tổng kết"].apply(xep_loai)

# Bảng điểm
st.subheader("Bảng điểm 10 sinh viên")
st.dataframe(df, use_container_width=True)

# Thống kê
st.subheader("Thống kê lớp")

c1, c2, c3, c4 = st.columns(4)

c1.metric("Điểm trung bình", f"{df['Tổng kết'].mean():.2f}")
c2.metric("Số sinh viên đạt", f"{(df['Tổng kết'] >= 5).sum()}/10")

sv_max = df.loc[df["Tổng kết"].idxmax()]
sv_min = df.loc[df["Tổng kết"].idxmin()]

c3.metric("Điểm cao nhất", f"{sv_max['Tổng kết']:.2f}")
c4.metric("Điểm thấp nhất", f"{sv_min['Tổng kết']:.2f}")

st.write("Sinh viên cao điểm nhất:", sv_max["Họ tên"])
st.write("Sinh viên thấp điểm nhất:", sv_min["Họ tên"])

# Chọn sinh viên
st.subheader("Tra cứu sinh viên")
ten = st.selectbox("Chọn sinh viên", df["Họ tên"].tolist())
sv = df[df["Họ tên"] == ten].iloc[0]

st.write("Điểm chuyên cần:", sv["Chuyên cần"])
st.write("Điểm giữa kỳ:", sv["Giữa kỳ"])
st.write("Điểm cuối kỳ:", sv["Cuối kỳ"])
st.write("Điểm tổng kết:", sv["Tổng kết"])
st.write("Xếp loại:", sv["Xếp loại"])

# Biểu đồ
st.subheader("Biểu đồ điểm tổng kết")
st.bar_chart(df.set_index("Họ tên")["Tổng kết"])

# Thông tin người tạo
st.divider()

st.markdown(
    """
    <div style="text-align: center; color: gray; font-size: 12px;">
        Người tạo:Đoàn Trương Huy Hoàn <br>
        MSSV: 052208004433
    </div>
    """,
    unsafe_allow_html=True
)
