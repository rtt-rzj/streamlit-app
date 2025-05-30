import streamlit as st

st.title("🚀 我的项目集锦")
st.write("--- ")
st.write("以下是本人完成的一些项目：")

# 项目1: 宇宙最强代码注释生成器 (伪)
with st.expander("项目一：最强代码注释生成器", expanded=True):
    st.subheader("最强代码注释生成器")
    st.markdown("**目标**: 开发一个能自动为任何代码（包括Hello World）生成哲学级别深度注释的工具，让维护者怀疑人生。")
    st.markdown("**技术栈**: Python, NLTK, GPT-0.1")
    st.markdown("**我的角色**: 产品经理、首席架构师、唯一程序员兼测试。")
    st.link_button("🔗 源码围观 (不存在的)", "#")
    st.warning("项目状态：已放弃治疗")

# 项目2: AI 自动甩锅机器人
with st.expander("项目二：AI 自动甩锅机器人"):
    st.subheader("AI 自动甩锅机器人")
    st.markdown("**目标**: 训练一个AI模型，使其在任何程序出错时，都能迅速生成至少5条看起来非常专业的甩锅理由。")
    st.markdown("**技术栈**: TensorFlow, Keras, 大量甩锅语料库")
    st.markdown("**我的角色**: 甩锅语料收集员、模型调参工程师。")
    st.link_button("🔗 体验甩锅 (敬请期待)", "#")
    st.info("项目状态：灵感枯竭，暂停中")

# 项目3: 程序员鼓励师模拟器
with st.expander("项目三：程序员鼓励师模拟器"):
    st.subheader("程序员鼓励师模拟器")
    st.markdown("**目标**: 创建一个应用，能模拟不同风格的程序员鼓励师，在你写BUG的时候给予亲切的问候和鼓励。")
    st.markdown("**技术栈**: Streamlit, Python, 各种表情包API")
    st.markdown("**我的角色**: 首席表情包体验官、鼓励语撰写。")
    st.link_button("🔗 求鼓励 (暂未上线)", "#")
    st.success("项目状态：自娱自乐中")


st.divider()
# --- 页脚 ---
st.markdown("<div class='footer'>© 2025 RONG Zijian | 用 ❤️ 和 Streamlit 构建</div>", unsafe_allow_html=True)
