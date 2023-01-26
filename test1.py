import pandas as pd
import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

'''streamlit run C:/Users/FrankLao/PycharmProjects/pythonProject/programme/research/Streamlit_learn/test1.py'''

matplotlib.rc('font',family = 'AR PL UMing CN') #用matplotlib显示中文字符

#1. st.write() 类似于print()，在网页上打印出内容
st.write('1. st.write()')
#用pandas输出数据为表格
st.write(pd.DataFrame({
    '第一列':[1,2,3,4],
    '第二列':[10,20,30,40]}
))

#2. st.line_chart() #生成折线图
st.write('2. st.line_chart()')
chart_data = pd.DataFrame(
    np.random.randn(20,3), #随机生成20行，3列数据
    columns=['a','b','c']  #三种数据的名称分别为a,b,c
)
st.line_chart(chart_data) #将上面的数据以折线图展示

#3. st.map() #显示经纬度
st.write('3. st.map()')
map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50,50] + [37.76,-122.4],
    columns = ['latitude','longitude']
)
st.map(map_data)

#4. st.slider() #生成一个滑动条（默认为0到100）
st.write('4. st.slider()')
x = st.slider('x') #给滑动条起名，在滑动时会给x定义一个值
st.write(x,'square is',pow(x,2))  #输出x计算结果

#5. st.text_input() #提供一个文本框给你输入内容
st.write('5. st.text_input()')
st.text_input('your name',key='name') #'your name'属于lable是一个输入提示，key是一个id
#显示输入的值，原封不动在输入框下面显示出输入的值
st.session_state.name

#6. st.checkbox() #勾选框
st.write('6. st.checkbox()')
if st.checkbox('Show Dataframe') is True: #当'Show Dataframe'这个勾选框被勾选时
    chart_data = pd.DataFrame(
        np.random.randn(20,3),
        columns=['a','b','c']
    )
    #chart_data 也可以直接写这个英文就显示
    st.write(chart_data) #显示出这个内容

#7. st.selectbox() #下拉选项
st.write('7. st.selectbox()')
df = pd.DataFrame({ #定义一个系列选项
    '第1列':[1,2,3,4]
})
option = st.selectbox(label='Which number do you like best?',options=df['第1列'])
st.write('you selected:',option) #显示出用户选择的选项

#8. st.siderbar #侧边栏 #在网页左上角显示一个可以点击的箭头，点击之后弹出侧边栏
st.write('8. st.sidebar')
add_selectbox = st.sidebar.selectbox(
    '通讯方式选择',
    ('微信','QQ','手机','邮件')
)
st.write('下拉选项:',add_selectbox)
#在侧边栏中添加一个滑动条
add_slider = st.sidebar.slider(
    '选择一个范围的值',
    0.0,100.0,(25.0,75.0)
)
st.write('值的范围:',add_slider)

#9. st.radio()单选
st.write('10. st.radio()')
left_column,right_column = st.columns(2) #设置两条列
#左边列设置
left_column.button('Press me!') #左边列设置一个按钮，写有'Press me!'
#右边列设置
with right_column:
    chosen = st.radio( #右边列设置一个单选，title,选项
        '手机品牌',
        ('苹果','华为','小米','三星')
    )
    st.write(f'你选择的品牌是:{chosen}')

#10. st.progress() 进度条 #让用户知道进度的情况
st.write('10. st.progress()')
import time
st.write('模拟长时间的计算')
#添加placeholder
latest_iteration = st.empty()
bar = st.progress(0) #生成一个条，从0开始计
for i in range(100):
    #更新进度条
    #页面中每发生一次点击则更新一次进度条
    latest_iteration.text(f'Iteration{i+1}') #进度条中显示的文本
    bar.progress(i+1) #条中显示的数字为i+1
    time.sleep(0.1) #暂停0.1秒
st.write('运行结束')

#11. st.file_uploader() 上传文件、图片等
st.write('11. st.file_uploader()')
#让用户上传文件
upload_file = st.file_uploader(
    label = '上传数据集CSV文件' #label可以理解为提示信息
)

if upload_file is not None: #如果用户上传了文件，不为空
    df = pd.read_csv(upload_file) #读取这个文件
    st.success('上传文件成功') #提示信息，文件上传成功
else:
    st.stop() #退出

#选择横坐标和纵坐标属性
x_var = st.selectbox(
    label = '选择横坐标的属性',
    options = ['bill_length_nm','bill_depth_mm','flipper_length_mm']
)

y_var = st.selectbox(
    label = '选择纵坐标的属性',
    options=['bill_length_mm','bill_depth_mm','flipper_length_mm']
)

sns.set_style('darkgrid')
markers = {'Adelie':'s',
           'Gentoo':'x',
           'Chinstrap':'o'}

fig,ax = plt.subplots()
ax = sns.scatterplot(data=df,
                     x=x_var,
                     y=y_var,
                     hue='species',
                     markers=markers,
                     style='species')
plt.xlabel(x_var)
plt.ylabel(y_var)
plt.title('Penguins Scatter Plot')
st.pyplot(fig)









