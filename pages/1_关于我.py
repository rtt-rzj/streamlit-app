import streamlit as st
from PIL import Image
import os
# 可选：如果这个页面也需要特定的页面配置，可以再次调用，但通常主app.py的配置会全局生效
# st.set_page_config(page_title="关于我", page_icon="👨‍💻")

st.title("👨‍💻 关于我")
st.write("--- ")

col1, col2 = st.columns([1,1.5])
with col1:
    image_path = os.path.join("images", "1.png")
    if os.path.exists(image_path):
        image = Image.open(image_path)
        col1.image(image, width=250)
    else:
        col1.warning("Profile image not found")
    st.markdown("**RONG Zijian**")
    st.markdown("📍 HONG KONG, China")

with col2:
    st.subheader("我是谁？")
    st.write("""
    我是一个对 生成代码 和 摸鱼 充满热情的砖家。
    拥有0.5年的 [Ctrl+C/Ctrl+V] 经验，我致力于 [让BUG无处遁形，或者至少让它们看起来像是特性]。
    我坚信 [只要咖啡管够，Nothing is impossible]。
    """
    )
    st.subheader("技能栈")
    skills = {
        "Python (入门到放弃再到入门)": 80,
        "Streamlit (CV工程师)": 70,
        "数据分析 (一本正经地胡说八道)": 60,
        "机器学习 (调包侠)": 50,
        "续命咖啡因依赖": 99
    }
    for skill, percentage in skills.items():
        st.write(f"{skill}")
        st.progress(percentage)

st.subheader("兴趣爱好")
st.markdown("""
- 📚 阅读 (最近在读 《如何假装看懂代码》)
- ✈️ 旅行 (最近在看 《流浪地球》)
- 🎵 音乐 (最近在听 《周杰伦》)
- 🎮 游戏 (最近沉迷于 《原神》)
- 🎨 绘画 (最近在学 《Adobe Photoshop》)
""")

st.divider()
# --- 页脚 ---
st.markdown("<div class='footer'>© 2025 RONG Zijian | 用 ❤️ 和 Streamlit 构建</div>", unsafe_allow_html=True)
