import streamlit as st

st.title("📬 与我联系")
st.write("--- ")
st.write("非常乐意与您交流！您可以通过以下方式找到我：")

col1, col2 = st.columns(2)
with col1:
    st.subheader("社交媒体")
    st.markdown("📧 **邮箱**: [rtt_rzj@163.com](mailto:rtt_rzj@163.com)")
    st.markdown("💼 **LinkedIn**: [Richard Rong](https://linkedin.com/in/richard-rong-bb8847350/)")
    st.markdown("💻 **GitHub**: [rtt-rzj](https://github.com/rtt-rzj)")
with col2:
    st.subheader("留言给我")
    with st.form("contact_form"):
        name = st.text_input("你的名字")
        email = st.text_input("你的邮箱")
        message = st.text_area("你想说的话")
        submit_button = st.form_submit_button("发送消息")
        if submit_button:
            if name and email and message:
                st.success(f"感谢 {name}！你的消息已收到（模拟）。")
            else:
                st.error("请填写所有必填项。")

st.divider()
# --- 页脚 ---
st.markdown("<div class='footer'>© 2025 RONG Zijian | 用 ❤️ 和 Streamlit 构建</div>", unsafe_allow_html=True)
