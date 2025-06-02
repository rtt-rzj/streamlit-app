import streamlit as st
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(page_title="宇宙猫咪数据洞察", page_icon="🌌😼")

st.markdown("# 🌌😼 宇宙猫咪数据洞察")
st.write("--- ")
st.write(
    """欢迎来到宇宙猫咪的多维数据探索中心！"""
)

# 创建宇宙猫咪的“科学”数据
@st.cache_data
def create_cosmic_cat_data(num_cats=150):
    # 零食偏好（X轴）: 1=小鱼干, 2=猫薄荷宇宙射线, 3=喵星罐头, 4=反物质猫条
    snack_preference_score = np.random.uniform(1, 4, num_cats)
    
    # 跳跃高度（Y轴, 单位：光年/喵秒²）
    jump_height = snack_preference_score * np.random.uniform(0.5, 2, num_cats) + np.random.normal(0, 0.5, num_cats)
    jump_height = np.clip(jump_height, 0.1, 10) # 确保跳跃高度在合理（？）范围内

    # 呼噜声频率（Z轴, 单位：赫兹/宇宙尘埃密度）
    purr_frequency = (snack_preference_score**0.5 + jump_height**0.3) * np.random.uniform(50, 200, num_cats) + np.random.normal(0,10,num_cats)
    purr_frequency = np.clip(purr_frequency, 20, 1000)

    # 猫咪品种（颜色）
    cat_breed = np.random.choice(['星际短毛', '银河长毛', '量子暹罗', '虫洞布偶'], num_cats)
    
    # 尾巴长度（点大小, 单位：秒差距）
    tail_length = np.random.rand(num_cats) * 5 + 1 # 尾巴长度在1到6秒差距之间

    data = pd.DataFrame({
        '零食偏好指数': snack_preference_score,
        '跳跃高度 (光年/喵秒²)': jump_height,
        '呼噜声频率 (赫兹/宇宙尘埃密度)': purr_frequency,
        '宇宙猫咪品种': cat_breed,
        '尾巴长度 (秒差距)': tail_length
    })
    return data

df_cosmic_cats = create_cosmic_cat_data()

st.subheader("宇宙猫咪零食偏好、跳跃与呼噜声多维探索平台")
st.write("警告：以下数据由喵星科学家通过非严谨观测获得。请旋转图表，揭示宇宙猫咪的秘密！")

fig_cosmic_cats = px.scatter_3d(df_cosmic_cats, 
                                x='零食偏好指数', 
                                y='跳跃高度 (光年/喵秒²)', 
                                z='呼噜声频率 (赫兹/宇宙尘埃密度)', 
                                color='宇宙猫咪品种',
                                size='尾巴长度 (秒差距)',
                                opacity=0.75,
                                title="喵的宇宙：零食、跳跃与呼噜声的神秘关联",
                                labels={
                                    '零食偏好指数':'最爱零食指数 (1-4分)', 
                                    '跳跃高度 (光年/喵秒²)':'最大跳跃高度 (光年/喵秒²)', 
                                    '呼噜声频率 (赫兹/宇宙尘埃密度)':'呼噜声基频 (赫兹/尘埃)',
                                    '宇宙猫咪品种': '尊贵品种',
                                    '尾巴长度 (秒差距)': '尾巴长度 (秒差距)'
                                },
                                height=700,
                                color_discrete_sequence=px.colors.qualitative.Pastel # 使用柔和一些的颜色
                               )

fig_cosmic_cats.update_layout(
    legend=dict(
        title_text='猫咪品种',
        orientation="h",
        yanchor="bottom",
        y=1.02,
        xanchor="right",
        x=1
    ),
    margin=dict(l=0, r=0, b=0, t=50),
    scene = dict(
        xaxis_title='最爱零食指数 (越高越爱)',
        yaxis_title='跳跃能力 (越高越能跳)',
        zaxis_title='呼噜声魔力 (越高越治愈)'
    )
)

st.plotly_chart(fig_cosmic_cats, use_container_width=True)

st.write("--- ")
st.success("恭喜你！你刚刚观看了宇宙中最先进的猫咪数据分析！")
st.caption("数据来源：喵星人跨维度研究中心（M.C.R.C.）")

st.divider()
# --- 页脚 ---
st.caption("<div class='footer'>© 2025 RONG Zijian | 用 ❤️ 和 Streamlit 构建</div>", unsafe_allow_html=True)
