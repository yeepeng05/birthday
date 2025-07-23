from PIL import Image
import streamlit as st


def main():
    create_web()  


def create_web():
    # 更改背景颜色
    st.markdown(
    """
    <style>
    .stApp {
        background-image: linear-gradient(180deg, white 0%, wheat 100%) !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

    CORRECT_PASSWORD ='780730'
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if not st.session_state.authenticated:
        audio = open('flute.mp3', 'rb')
        st.audio(audio, autoplay=True, loop=True)
        st.markdown("""
        <style>
            .password-box {
                background-color: transparent;
                padding: 30px;
                border-radius: 10px;
            }
            .password-title {
                color: black;
                font-size: 24px;
                margin-bottom: 20px;
            }
            .error-msg {
                color: red !important;
                font-weight: bold;
            }
    </style>
    <div class="password-box">
            <div class="password-title">🔐 请输入专属密码</div>
    </div>
    """, unsafe_allow_html=True)
    
        password = st.text_input("", type="password", key="pwd_input")
    
        if st.button("解锁", key="pwd_btn"):
            if password == CORRECT_PASSWORD:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.markdown('<p class="error-msg">✖ 密码错误，请重试</p>', 
                        unsafe_allow_html=True)
        st.stop()

    # 气球特效
    st.balloons()
    # 音乐特效
    audio = open('happybirthday.mp3', 'rb')
    st.audio(audio, autoplay=True, loop=True)

    # 中文字体设置
    st.markdown(
    '''
    <style>
    .chinese_font {
        font-family: 'KaiTi' !important;
        font-size: 45px !important;
        color: salmon;
    }
    </style>
    <p class='chinese_font'>妈咪生日快乐！</p>
    ''',
    unsafe_allow_html=True
    )
        
    # 英文字体设置（pyfiglet和art只能在灰色背景呈现！）
    st.markdown(
    '''
    <style>
    .chinese_font {
        font-size: 55px !important;
        color: salmon;
    }
    </style>
    <p class='chinese_font'>ℌ𝔞𝔭𝔭𝔶 𝔅𝔦𝔯𝔱𝔥𝔡𝔞𝔶 ❤</p>
    ''',
    unsafe_allow_html=True
    )

    left, right = st.columns(2)  # 将页面分成两列     

    with left:
        # 1. 指定本地图片文件夹路径
        photos = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg']
        st.markdown('<span style="color: black; font-size: 20px;">点击+解锁更多照片~ </span>', unsafe_allow_html=True)
        index = st.number_input('', min_value=1, max_value=len(photos), step=1)
        st.image(photos[index-1], use_container_width=True)
            
    with right:  
        st.image("_love.png", width=200)
        st.image('_cake.png', width=200)


def turn_qr():
    qr = segno.make_qr("https://streamlit.io")
    qr.to_artistic(
        background=str(bg_path),
        target="art_qr.png",
        scale=15,
        border=2,
        light=None  # 透明背景
    )
    
    # 显示结果
    st.image("art_qr.png", caption="你的艺术二维码")
    st.download_button("下载", open("art_qr.png", "rb"), "my_qr.png")

if __name__ == '__main__':
    main()
