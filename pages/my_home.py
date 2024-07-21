'''我的主页'''
import streamlit as st
from PIL import Image
import wordcloud
import matplotlib.pyplot as plt
import base64
page = st.sidebar.radio('江北联校潮汐终端', ['联校官方推荐', '图片处理工具', '资料查询终端', '终端留言区'])

def img_change(img,rc,gc,bc):
            width,height=img.size
            img_array=img.load()
            for x in range(width):
                for y in range(height):
                    r=img_array[x,y][rc]
                    g=img_array[x,y][gc]
                    b=img_array[x,y][bc]
                    img_array[x,y]=(r,g,b)
            return img
def ciyvn(str):
    w=wordcloud.WordCloud(font_path='fangzheng.TTF')
    w.generate(str)
    w.to_file('shortstory.png')
    img = Image.open('shortstory.png')
    return img
def page_1():
    '''联校官方推荐'''
    with open('主页面.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('2024-07-17 191848.png')
    st.write('联校官方动漫推荐')
    st.write(':orange[(十分推荐)]')
    st.write('《物理魔法使马修》    《孤独摇滚》    《时光代理人》')
    st.write(':orange[(推荐)]')
    st.write('《罗小黑战记》    《凹凸世界》')
    st.write('-----------------------------')
    st.write('联校官方游戏推荐')
    st.write(':orange[(十分推荐)]')
    st.write('《脑叶公司》    《Minecraft（我的世界）')
    st.write(':orange[(推荐)]')
    st.write('《赛博朋克2077》    《原子之心》')
    st.write('-----------------------------')
    st.write('联校官方书籍推荐')
    st.write(':orange[(十分推荐)]')
    st.write('《江北联校》')
    st.write(':orange[(推荐)]')
    st.write('《记忆传授人》    《历史刺绣人》    《森林送信人》')
    st.write('-----------------------------')
    st.write('联校官方习题集推荐')
    st.write(':orange[(你居然想内卷？！！？没门！好好听老师上课！)]')
    st.write('-----------------------------')

def page_2():
    '''图片处理工具'''
    with open('选题.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('2024-07-17 191848.png')
    st.write(':orange[图片改色小工具]')
    st.write('-----------------------------')
    uploaded_file=st.file_uploader('上传图片',type=['png','jpg','jpeg'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10 = st.tabs(['原色','改色1','改色2','改色3','改色4','改色5','改色6','改色7','改色8','改色9'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
    else:
        pass
    st.write('-----------------------------')
    st.write(':orange[词云生成小工具]')
# 上传文件
    uploaded_file = st.file_uploader("Choose a file")
     
    if uploaded_file is not None:
        # 将上传的文件转换成文本
        string_data = uploaded_file.read().decode("utf-8")
        st.image(ciyvn(string_data))
    else:
        pass

def page_3():
    '''资料查询终端'''
    with open('选题.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('2024-07-17 191848.png')
    st.write('-----------------------------')
    st.write('施工中')
    st.write('-----------------------------')
    st.write('尽请期待')
    st.write('-----------------------------')

def page_4():
    '''终端留言区'''
    with open('选题.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('2024-07-17 191848.png')
    st.write('-----------------------------')
    st.write('施工中')
    st.write('-----------------------------')
    st.write('尽请期待')
    st.write('-----------------------------')

if page == '联校官方推荐':
    page_1()
elif page == '图片处理工具':
    page_2()
elif page == '资料查询终端':
    page_3()
elif page == '终端留言区':
    page_4()
