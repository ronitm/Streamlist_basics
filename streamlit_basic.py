import streamlit as st
import pandas as pd

st.title('Hello world :100:')

'Displaying using magic :smile:'

# TEXT INPUT
name = st.text_input('Your name')
url = st.text_input('linkedin profile')
org = st.text_input('Organization')
if url :
    st.write(f'Hello {name}!')
    st.write(f'Profile = {url}!')
    st.write(f'Org =  {org}!')

st.text_area('Description')

x = st.number_input('Enter a number',min_value=1, max_value=99, step=1)
st.write(f'The current number is {x}')
st.divider()

# Button
clicked = st.button('Submit')
if clicked:
    'Thank you for submitting your request'

# CheckBox
agree = st.checkbox('I agree', value=True)
if agree:
    'Great, you agreed'

df = pd.DataFrame({'Name':['Anne','Mario','Doug'],
                   'Age' :[30,25,40]
                   })
if st.checkbox('Show data'):
    st.write(df)

# RADIO
pets = ['cats','dogs','fish']
pet = st.radio('Favorite pet', pets, index = 1)
st.write(f'Your favorite pet: {pet}')



st.divider()
# Dropdown select box
cities=['London','Paris','Madrid','Berlin']
city = st.selectbox('Your city', cities, index = 1)
st.write(f'You live in {city}')

st.multiselect('choose a planet',['Jupiter', 'Mars', 'neptune'])

# SLIDER
x= st.slider('x', value=15, min_value=12, max_value=78, step=3)
st.write(f'x is {x}')
st.select_slider('Pick a mark', ['Bad', 'Good', 'Excellent'])

# FIle uploader
uploaded_file = st.file_uploader('Upload your file:', type=['txt','csv','pdf','xlsx'])
if uploaded_file:
    st.write(uploaded_file)
    if uploaded_file.type == 'text/plain':
        from io import StringIO
        stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
        string_data = stringio.read()
        st.write(string_data)
    elif uploaded_file.type == 'text/csv':
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.write(df)
    elif uploaded_file.type == 'xlsx':
        import pandas as pd
        df = pd.read_excel(uploaded_file)
        st.write(df)
    else:
        import PyPDF2
        reader = PyPDF2.PdfReader(uploaded_file)
        st.write(reader.pages[0].extract_text())

# Camera Input
#camera_photo = st.camera_input('Take a photo')
#if camera_photo:
#    st.image(camera_photo)

# Display any image
#st.image('https://pbs.twimg.com/profile_images/1589007733226844160/i5-iIoSc_400x400.jpg')
#st.audio('audio.mp3')
st.video('https://www.youtube.com/watch?v=kiMTRQXBol0')

# SIdebar
my_select_box = st.sidebar.selectbox('Select country of operations',['US','Canada','Mexico'])

# Columns
left_column, right_column = st.columns(2)
import random
data=[random.random() for _ in range(100)]

with left_column:
    st.subheader('A chart')
    st.line_chart(data)

right_column.subheader('Data')
right_column.write(data[:10])


# Progress Bar