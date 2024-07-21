'''我的首页'''
import streamlit as st
from PIL import Image

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区'])

#兴趣推荐页
def page_1(): 
    '''我的兴趣推荐'''
    with open('霞光.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('slogan.png')
    tab1,tab2,tab3,tab4 = st.tabs(['阿短的电影推荐','阿短的游戏推荐','阿短的书籍推荐','阿短的习题集推荐'])
    with tab1:
        st.write('小佳的电影推荐')
        st.write('-----------------------------')
    with tab2:
        st.write('阿短的游戏推荐')
        st.write('-----------------------------')
    with tab3:
        st.write('阿短的书籍推荐')
        st.write('-----------------------------')
    with tab4:
        st.write('阿短的习题集推荐')
        st.write('-----------------------------')




#图片处理工具
def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4 = st.tabs(['原色','改色1','改色2','改色3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))

#智能词典            
def page_3():
    '''我的智能词典'''
    pass


#留言区
def page_4():
    '''我的留言区'''
    pass

#图片处理工具
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img


if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()