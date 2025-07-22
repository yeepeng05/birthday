import turtle as t
from PIL import Image
from rembg import remove
import streamlit as st
import qrcode, segno

class Draw:
    def love():
        t.setup(600, 600)
        t.pencolor('red')
        t.fillcolor('lightcoral')
        t.begin_fill()
        t.left(90)
        t.circle(100, 180)
        t.circle(200, 180)
        t.circle(100, 180)
        t.end_fill()

        # 储存照片
        canvas = t.Screen().getcanvas()
        canvas.postscript(file='love.eps')

    
    def cake():
        # 蛋糕基地
        t.setup(600, 600)
        t.pencolor('tan')
        t.fillcolor('tan')
        t.penup()
        t.fd(100)
        t.right(90)
        t.pendown()
        t.begin_fill()
        t.pendown()
        t.fd(100)
        t.right(90)
        t.fd(200)
        t.right(90)
        t.fd(90)
        t.right(90)
        t.fd(200)
        t.end_fill()

        # 开始撒可可粉
        t.pencolor('saddlebrown')
        t.fillcolor('saddlebrown')
        t.left(90)
        t.begin_fill()
        t.fd(10)
        t.left(90)
        t.fd(200)
        t.left(90)
        t.fd(10)
        t.end_fill()
        t.pensize(10)
        t.penup()
        t.fd(10)
        for _ in range(2):
            t.left(90)
            t.fd(5)
            t.pendown()
            t.fd(185)
            t.right(90)
            t.penup()
            t.fd(20)
            t.right(90)
            t.pendown()
            t.fd(185)
            t.left(90)
            t.penup()
            t.fd(20)
        t.pendown()
        t.right(90)
        t.fd(5)
        t.right(180)
        t.fd(193)

        # 蜡烛
        t.pensize(1)
        t.penup()
        t.goto(0, 0)
        t.pencolor('firebrick')
        t.fillcolor('firebrick')
        t.left(180)
        t.fd(5)
        t.right(90)
        t.pendown()
        t.begin_fill()
        t.fd(50)
        t.right(90)
        t.fd(10)
        t.right(90)
        t.fd(50)
        t.end_fill()

        # 烛火
        t.penup()
        t.goto(7, 57)
        t.left(180)
        t.pencolor('yellow')
        t.fillcolor('yellow')
        t.pendown()
        t.begin_fill()
        t.circle(7, -180)
        t.goto(0, 73)
        t.goto(7, 57)
        t.end_fill()
        t.hideturtle()
        # 储存照片
        canvas = t.Screen().getcanvas()
        canvas.postscript(file='cake.eps')


def main():
    '''
    Draw.love()
    Draw.cake()
    turn_img()
    removebg()
    '''
    create_web()
    turn_qr()
    

def turn_img():
    # 转换格式为png
    img = Image.open('love.eps')
    img.save('love.png')

    img = Image.open('cake.eps')
    img.save('cake.png')



def removebg():
    # 弄掉照片背景
    with open('love.png', 'rb') as inp:
        with open('_love.png', 'wb') as outp:
            outp.write(remove(inp.read())) 

    
    with open('cake.png', 'rb') as inp:
        with open('_cake.png', 'wb') as outp:
            outp.write(remove(inp.read()))


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
        font-size: 65px !important;
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
        font-size: 65px !important;
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
        photos = ['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg']
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