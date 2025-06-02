import streamlit as st

st.title("😄 心情驿站")
st.write("--- ")

# --- 互动功能：心情选择器 ---
st.subheader("今日心情如何？")
mood_options = ["元气满满", "有点小丧", "只想摸鱼", "灵感爆发"] # 心情选项
selected_mood = st.selectbox("选择你今天的心情：", mood_options)

if selected_mood == "元气满满":
    st.balloons()
    st.success(f"太棒了！保持这份**{selected_mood}**的心情，今天也是高效的一天！")
elif selected_mood == "有点小丧":
    st.snow()
    st.info(f"没关系，**{selected_mood}**只是暂时的。来，给你一个虚拟的抱抱！🤗")
elif selected_mood == "只想摸鱼":
    st.warning(f"理解万岁！**{selected_mood}**的时候，不如看看这些项目找找乐子？😉")
elif selected_mood == "灵感爆发":
    st.success(f"哇哦！**{selected_mood}**的你，是不是又有什么新点子了？快去实现吧！✨")

st.divider()
# --- 页脚 ---
st.caption("<div class='footer'>© 2025 RONG Zijian | 用 ❤️ 和 Streamlit 构建</div>", unsafe_allow_html=True)
