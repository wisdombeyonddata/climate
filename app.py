import streamlit as st


st.sidebar.write('Hello World!')

planet = st.sidebar.selectbox('Select your favourite planet: ', ('Venus', 'Earth', 'Mars'))
epsilon = 1
sigma = 5.67E-8  


if planet == 'Venus':
    st.sidebar.image('venus.jpg', width=200)
    st.sidebar.write('This is a small introduction text about Venus, she has got it oh oh baby she got it!')
    st.sidebar.write('Fun facts about Venus:')
    L = 2600          # Watts/m2
    albedo = 0.7
    real_T = 700
    
if planet == 'Earth':
    st.sidebar.image('earth.jpg', width=200)
    st.sidebar.write('This is a small introduction text about earth, our home')
    L = 1350          # Watts/m2
    albedo = 0.3

if planet == 'Mars':
    st.image('mars.jpg', width=500)
    st.write('This is a small introduction text about mars, Elons baby!')
    L = 600          # Watts/m2
    albedo = 0.15

# do calculations
T = (L*(1-albedo)/(4*epsilon*sigma))**(1/4)

st.header('Model Formulation')
#st.markdown($\frac{L (1-\alpha)}{4 \epsilon \sigma}$)

st.header('Model Input')
if st.checkbox('What is albedo?'):
    st.write('Albedo measures .... help!')

if st.checkbox('What is L?'):
    st.write('L measures .... help!')

st.write(f'The albedo of {planet} is {albedo} and the other thingy is {L}')
st.write('Source here')

st.header('Lets Model!')
st.write(f'Temperatur on planet {planet} is according to our model {round(T)} K')

st.header('Model Evaluation')
st.write(f'Actual temperature on planet {planet} is {real_T} K')
difference = abs(real_T-T)
st.write(f'This is a {round(difference)} K difference')

if difference >200:
    st.write('too bad')