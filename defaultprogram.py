import streamlit as st
from PIL import Image
st.markdown('''
<style>
	h1 {
		font-size: 56px;
		text-align: center;
		text-transform: uppercase;
		font-family: 'Felix Titling', serif;
	}
	h2 {
		font-size: 42px;
		text-align: center;
		text-transform: uppercase;
		font-family: 'Felix Titling', serif;
	}
	p {
		font-size: 20px;
		text-align: left;
		padding-left: 80px;
		padding-right: 80px;
		text-transform: uppercase;
		font-family: 'Felix Titling', serif;
	}
	img {
  		border: 5px solid #ddd;
  		border-radius: 12px;
  		padding: 5px;
	}

	[data-testid="stAppViewContainer"] > .main {
		background-image: url("https://images.pexels.com/photos/1090977/pexels-photo-1090977.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1");
		background-size: 100vw 100vh;
                background-position: center;  
                background-repeat: no-repeat;
	}</style>
''', unsafe_allow_html=True)
st.title('_Bosco_ Is :blue[cool]:sunglasses::+1:')
st.write('good text')
st.header('bosco')
if st.checkbox('yes or no'):
        st.success(' testing')
st.image(Image.open('image.png'),width=300)
st.image(Image.open('image.png'),width=200)
if st.checkbox('diplay/no display'):
        st.success('displaying')
        st.image(Image.open('image.png'),width=500)
select = st.selectbox('favorites',['bhindi','veg','egg','chicken',])
if select == 'chicken':
        st.success('good choice brother')
elif select == 'bhindi':
        st.header('perform example')
if(st.button('click me')):
        st.success('thanks for clicking')
if(st.button('click me for test')):
        st.success('clicked')
else:
	st.success('you did not click')
st.write('check out this [link](https://youtube.com)')
st.write('check out this [link](https://google.com)')
st.write('check out this [link](bhindi.com)')
numbertest=""
if(st.button('button with int')):
        numbertest="clicked"
if(st.button('button set int to 0')):
        numbertest="clicked 2nd one"
st.text(numbertest)
st.header('thanks for visiting')
st.divider()
st.markdown('''
<p>very good text inserted by using the insert html command of bosco</p><br><h1>same with this heading</h1>
''', unsafe_allow_html=True)
st.text_area("","asdasfafagegwehhrhr\nasdasdasdasdad\nasdasd")
newcheckboxfunction = st.checkbox('new checkbox function')
if newcheckboxfunction  :
        st.success('clicked')
else:
        st.success('no click')
st.text_area("created by gui","nice text")
st.text_area("working","another test")
st.divider()
battton = st.checkbox('battton')
st.text_area("BOSCO","ASD")
st.divider()
st.divider()
st.divider()
st.title('bosco')
st.divider()
st.divider()
st.divider()
new = st.button('new')#buttonnew
text='check'#change vartext
if new :#if/checkvar
	st.write(text)
check = st.checkbox('check')#checkboxcheck
newtext='box'#change/declare varnewtext
if check :#if/checkvar
        st.image(Image.open('image.png'),width=200)
area=st.text_area("text area","area")#text areaarea
choose = st.selectbox('choose an option',['option1','option2','option3','option4'])#selectorchoose
if choose =='option1':#if/checkvar
        st.success('out')#output
click_me = st.checkbox('click_me')#checkboxclick_me
if click_me:#if/checkvar
	st.success('checker clicked')#output
st.link_button('link_button', '#bosco') #link button link_button
st.link_button('bosco', '#bosco') #link button bosco
chaakbox = st.checkbox('chaakbox')#checkboxchaakbox
if chaakbox:#if/checkvar
        st.divider()#divider

sel = st.selectbox('selector',['1', '2', '3', '4', '5'])      #selectorsel
if sel==2:      #if/checkvar
        st.divider()#      divider
