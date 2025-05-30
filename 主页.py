import streamlit as st

# --- 页面配置 ---
st.set_page_config(
    page_title="RONG Zijian的数字空间",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- 自定义 CSS ---
st.markdown("""
<style>
    /* --- 全局与容器 --- */
    .stApp {
        /* background: linear-gradient(to bottom right, #f0f2f6, #e0e4e8); /* 尝试渐变背景 */
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1000px; /* 限制主内容区最大宽度，使其更集中 */
        margin: auto; /* 居中 */
    }
    /* --- 卡片基础样式 --- */
    .custom-card {
        background-color: #ffffff;
        border-radius: 12px; /* 更大的圆角 */
        padding: 20px 25px; /* 调整内边距 */
        box-shadow: 0 6px 12px rgba(0,0,0,0.08); /* 更柔和的阴影 */
        margin-bottom: 25px;
        transition: all 0.3s ease-in-out;
        border: 1px solid #e0e0e0; /* 细边框 */
        height: 100%; /* 让卡片在列中高度一致 (如果列内只有卡片) */
    }
    .custom-card:hover {
        box-shadow: 0 8px 16px rgba(0,0,0,0.12);
        transform: translateY(-3px);
    }
    /* --- 文本与标题 --- */
    h1, h2, h3, h4 {
        color: #333; /* 深色文本 */
    }
    h1 {
        font-size: 2.5em;
        font-weight: 700;
        text-align: center; /* 页面大标题居中 */
        margin-bottom: 0.5em;
    }
    h3.user-intro {
        text-align: center;
        font-size: 1.6em;
        margin-bottom: 0.3em;
    }
    p.user-caption {
        text-align: center;
        font-size: 1em;
        color: #555;
        margin-bottom: 1.5em;
    }
    h4.card-title {
        font-size: 1.3em;
        color: #FF4B4B; /* 主题色用于小标题 */
        margin-bottom: 0.8em;
        border-bottom: 2px solid #ffe0e0; /* 标题下划线 */
        padding-bottom: 0.3em;
    }
    /* --- 右侧个人信息卡片 --- */
    .profile-card-content {
        display: flex;
        flex-direction: column; /* 垂直排列 */
        align-items: center; /* 水平居中 */
        text-align: center; /* 文本居中 */
        height: 100%; /* 尝试让内容撑满卡片 */
        justify-content: space-between; /* 内容在卡片内部分散对齐 */
    }
    .profile-image-wrapper {
        margin-top: 10px; /* 图片与卡片顶部的距离 */
        margin-bottom: 15px;
    }
    .profile-image-wrapper img {
        width: 130px; /* 调整头像大小 */
        height: 130px;
        border-radius: 50%;
        object-fit: cover; /* 确保图片不变形 */
        border: 4px solid #FF4B4B;
        padding: 4px;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    .profile-name {
        font-size: 1.3em;
        font-weight: 600;
        margin-bottom: 5px;
        color: #222;
    }
    .profile-motto {
        font-size: 0.9em;
        color: #555;
        margin-bottom: 15px;
        flex-grow: 1; /* 让座右铭占据多余空间，将提示信息推到底部 */
    }
    .profile-card-content .stAlert {
        width: 100%; /* 让提示信息宽度与卡片一致 */
        margin-top: auto; /* 将提示信息推到卡片底部 */
    }
    /* --- 技能标签 --- */
    .skills-card-content {
        text-align: center; /* 标签整体居中 */
    }
    .skill-tag {
        display: inline-block;
        background-color: #e9ecef; /* 更中性的背景 */
        color: #495057; /* 搭配的文字颜色 */
        padding: 8px 15px;
        border-radius: 20px; /* 更圆润的标签 */
        margin: 6px;
        font-size: 0.9em;
        font-weight: 500;
        transition: background-color 0.2s, color 0.2s;
    }
    .skill-tag:hover {
        background-color: #FF4B4B;
        color: white;
    }
    /* --- 关于本站列表 --- */
    .about-list ul {
        list-style-type: none; /* 去掉默认的点 */
        padding-left: 0;
    }
    .about-list li {
        margin-bottom: 12px; /* 增加列表项间距 */
        font-size: 1.0em;
        color: #444;
        display: flex; /* 使用 flex 对齐图标和文本 */
        align-items: center; /* 垂直居中对齐 */
    }
    .about-list li svg {
        min-width: 16px; /* 固定图标宽度，防止文本换行时图标移动 */
        margin-right: 10px; /* 图标和文本间距 */
        color: #FF4B4B; /* 列表图标颜色 */
    }
    /* --- 页脚 --- */
    .footer {
        text-align: center;
        padding: 20px 0;
        color: #777;
        font-size: 0.9em;
        border-top: 1px solid #eee;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# --- 页面头部 ---
st.markdown("<h1>🚀 欢迎来到我的数字空间</h1>", unsafe_allow_html=True)
st.markdown("<h3 class='user-intro'>你好，我是 RONG Zijian 👋</h3>", unsafe_allow_html=True)
st.markdown("<p class='user-caption'>一位热情的学生，专注于学好Machine Learning in Marketing</p>", unsafe_allow_html=True)
st.divider()


col1_html = """
<div class="custom-card">
    <h4 class="card-title">✨ 关于本站</h4>
    <p>这个网站是使用 Streamlit 构建的，旨在分享我的学习笔记、项目经验和一些个人思考。
    我热衷于探索新技术，并乐于将所学应用于实际问题的解决。</p>
    <br>
    <strong>在这里你可以找到：</strong>
    <div class="about-list">
        <ul>
            <li><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-pencil-fill" viewBox="0 0 16 16"><path d="M12.854.146a.5.5 0 0 0-.707 0L10.5 1.793 14.207 5.5l1.647-1.646a.5.5 0 0 0 0-.708l-3-3zm.646 6.061L9.793 2.5 3.293 9H3.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.5h.5a.5.5 0 0 1 .5.5v.207l6.5-6.5zm-7.468 7.468A.5.5 0 0 1 6 13.5V13h-.5a.5.5 0 0 1-.5-.5V12h-.5a.5.5 0 0 1-.5-.5V11h-.5a.5.5 0 0 1-.5-.5V10h-.5a.499.499 0 0 1-.175-.032l-.179.178a.5.5 0 0 0-.11.168l-2 5a.5.5 0 0 0 .65.65l5-2a.5.5 0 0 0 .168-.11l.178-.178z"/></svg> 我的技术博客和教程</li>
            <li><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-lightbulb-fill" viewBox="0 0 16 16"><path d="M2 6a6 6 0 1 1 10.174 4.31c-.203.196-.359.4-.453.619l-.762 1.769A.5.5 0 0 1 10.5 13h-5a.5.5 0 0 1-.46-.302l-.761-1.77a1.964 1.964 0 0 0-.453-.618A6 6 0 0 1 2 6zm3 8.5a.5.5 0 0 1 .5-.5h5a.5.5 0 0 1 0 1l-.224.447a1 1 0 0 1-.894.553H6.618a1 1 0 0 1-.894-.553L5.5 15a.5.5 0 0 1-.5-.5z"/></svg> 我参与或独立完成的项目案例</li>
            <li><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-globe-americas" viewBox="0 0 16 16"><path d="M8 0a8 8 0 1 0 0 16A8 8 0 0 0 8 0ZM2.04 4.326c.325 1.329 2.532 2.54 3.717 3.19.48.263.793.434.743.484-.03.028-.15.028-.213.009-.11-.036-.253-.086-.41-.146-1.532-.588-2.923-.89-3.841-.95-.036-.003-.076-.003-.115-.003a6.97 6.97 0 0 1 0-1.705c.041-.003.083-.003.125-.003.162 0 .324.006.484.02zM3.81 9.825c.07-.172 1.137-1.424 2.564-2.157.144-.073.287-.14.418-.202.13-.064.25-.12.354-.174.106-.055.2-.098.282-.132.082-.033.15-.055.21-.069.06-.014.114-.023.158-.027.044-.003.083-.003.121-.003s.077 0 .121.003c.044.004.098.013.158.027.06.014.128.036.21.069.082.034.176.077.282.132.104.054.224.11.354.174.13.063.274.13.418.202 2.654 1.424 2.507 2.37 2.468 2.494a6.979 6.979 0 0 1-1.005 2.704.964.964 0 0 0-.189-.299l-.001-.002c-.002-.002-.005-.005-.007-.007l-.004-.005c-.01-.01-.02-.02-.03-.03-.02-.02-.04-.038-.06-.056-.07-.06-.14-.12-.21-.175a2.498 2.498 0 0 0-3.468 0c-.07.055-.14.115-.21.175-.02.018-.04.036-.06.056-.01.01-.02.02-.03.03l-.004.005c-.002.002-.005-.005-.007.007l-.001.002a.964.964 0 0 0-.189.299 6.978 6.978 0 0 1-1.005-2.704c-.039-.124.188-1.07 2.468-2.494Z"/></svg> 一些关于 生成代码 和 摸鱼 的分享</li>
        </ul>
    </div>
    <br>
    <p>希望这些内容能对你有所启发！</p>
</div>
"""
st.markdown(col1_html, unsafe_allow_html=True) # 确保 col1_html 在这里被调用前已定义

st.divider()

# --- 技能栈 --- 
st.markdown("<h3 style='text-align:center; margin-bottom:1em;'>🎯 我的技能栈</h3>", unsafe_allow_html=True)
skills_html = '<div class="custom-card skills-card-content">'
skills = ["一本正经地胡说八道", "快速召唤外卖", "在DDL前反复横跳", "专业抬杠运动员", "摸鱼大师", "表情包富翁", "熬夜冠军", "拖延症晚期患者", "反向种草小能手", "退堂鼓表演艺术家"]
for skill in skills:
    skills_html += f'<span class="skill-tag">{skill}</span>'
skills_html += '</div>'
st.markdown(skills_html, unsafe_allow_html=True)

# --- 页脚 ---
st.markdown("<div class='footer'>© 2025 RONG Zijian | 用 ❤️ 和 Streamlit 构建</div>", unsafe_allow_html=True)
