
# Need to clean up all the functions and stuff, make it actually organized
import streamlit as st
import pandas as pd
import numpy as np

# Harassment Version Variable
harassmentVar = False

# Functions

def button():
    if st.button("Click me!"):
        st.balloons()
        st.snow()
        st.toast("Hi friend! Did you miss me?...")
        st.text("Woah! Where did that come from?")
        return

def doYouAgree():
    st.text("Do you agree?")
    iAgree = st.checkbox("I agree")
    iDontAgree = st.checkbox("I don't agree, you are being a big baby")
    if iAgree == True and iDontAgree == True:
        st.text("")
        st.markdown("**Stop trying to cheat the system, you only get one opinion!**")
        global harassmentVar
        harassmentVar = True
        return
    if iAgree == True:
        st.text("")
        st.markdown("**Thank you for understanding!**")
        return
    if iDontAgree == True:
        st.text("")
        st.markdown("**I don't like you anymore. I will find new ways to harass you.**")
        harassmentVar = True
        return
    else:
        return

def toggle():
    # Initialize the variable in session state so it persists across reruns
    if "cueingAppNumber" not in st.session_state:
        st.session_state.cueingAppNumber = 0
    
    # Create the toggle widget ONCE and store its current value
    toggle_active = st.toggle("Cueing app...")

    # Check the stored value of the single toggle
    if toggle_active and st.session_state.cueingAppNumber < 1 and harassmentVar == True:
        st.toast("Let's do this poopy pants!")
        st.session_state.cueingAppNumber += 2
    if toggle_active and st.session_state.cueingAppNumber < 1:
        st.toast("Let's do this!")
        st.session_state.cueingAppNumber += 2
        return

    if not toggle_active:
        return

def name():
    nameInput = st.text_input("Name")
    if nameInput and harassmentVar == True:
        st.text("Did you actually type your name? Wow, I am surprised considering you are a...")
        st.image("stinkyPoopImage.jpeg")
        return
    
    if nameInput:
        st.text("Did you actually type your name? Wow, I did not think you would do that. Anyway...")
        return

def oldVYoung():
    answerToAge = st.selectbox("Are you young or old", ["Select", "young", "old"])
    if answerToAge == '' and harassmentVar == True:
        st.markdown("**Hurry up already, I don't have all day to wait for your answer!**")
        return
    
    if answerToAge == 'Select' and harassmentVar == False:
        st.text("")
        return
   
    if answerToAge == 'young' and harassmentVar == True:
        st.text("Well, you know what they say, younger people suck.")
        return
    
    if answerToAge == 'old' and harassmentVar == True:
        st.text("Well, you know what they say, old is not gold")
        return
    
    if answerToAge == 'young':
        st.text("Nice! Everyone likes being young.")
        return
    
    if answerToAge == 'old':
        st.text("If you picked old, that's okay. Age is just a state of mind.")
        return

# No longer broken! Fully fixed now!
def pickANumber():
    threeChoicesCounter = 0

    if threeChoicesCounter < 3:
        if "pANsliderList" not in st.session_state:
            st.session_state.pANsliderList = []

        pANslider = st.slider("", 0, 100)

        if pANslider:
            st.session_state.pANsliderList.append(pANslider)

        threeChoicesCounter = int(len(st.session_state.pANsliderList))
        #st.text(", ".join(map(str, number_list)))
        #st.text(", ".join(map(str, st.session_state.pANsliderList)))
        st.text("Your current number is " + str(pANslider) + ". You have previously select the following numbers: " + ", ".join(map(str, st.session_state.pANsliderList)))
    
    if threeChoicesCounter >= 3:
        st.text("Dude! It is just a number! Just pick one, this doesn't have to have any deeper meaning.")
        st.text("Or does it...")
    
    else:
        return

def wantToSeeAChart():
    yesCheckbox = st.checkbox("Yes")
    noCheckbox = st.checkbox("No")
    if yesCheckbox and noCheckbox and harassmentVar == True:
        st.text("Stop trying to cheat the system! You are really acting like a ...")
        st.image("stinkyPoopImage.jpeg")
        harassmentVar == True
        return st.text(harassmentVar)
    
    # return is not returning the st.text(harassmentVar and there is no sign that harassmentVar is changing, can not use global var more than once)
    if yesCheckbox and harassmentVar == True:
        st.text("That is perfect, because even though you are a turd, you are going to see one.")
        return
    
    if noCheckbox and harassmentVar == True:
        st.text("Honestly this answer doesn't surprise me, considering you are a ...")
        st.image("stinkyPoopImage.jpeg")
        return
    
    if yesCheckbox and noCheckbox:
        st.text("Stop trying to cheat the system!")
        return
    
    if yesCheckbox:
        st.text("Perfect, because you are going to see one anyway")
        return
    
    if noCheckbox:
        st.text("Too bad because you are going to see one anyway!")
        return
    
def car(): 
    answerToCar = st.selectbox("Do you think self driving cars are cool?", ["Select","Yes, I think they are cool.", "No, I am a lame-o and do not think self driving cars are cool."])

    if answerToCar == 'Yes, I think they are cool.' and harassmentVar == True:
        st.text("Me too! Though you are still a ...")
        st.image("stinkyPoopImage.jpeg")
        return
    
    if answerToCar == 'Select' and harassmentVar == True:
        st.markdown("**Well answer the question!!!**")
        return
    
    if answerToCar == 'No, I am a lame-o and do not think self driving cars are cool.' and harassmentVar == True:
        st.text("Wow! First turd now lame-o. You are a piece of work.")
        return

    if answerToCar == 'Yes, I think they are cool.':
        st.text("Me too!")
        return
    
    if answerToCar == 'Select':
        st.text("")
        return
    
    else:
        st.text("Well, the answer speaks for itself...")
        return

def poopPin():
    if harassmentVar == True:
        poopyPlace = pd.DataFrame({"lat": [35.251091], "lon": [-112.187714]})
        st.map(poopyPlace)
        st.link_button("You should check this place out, you will be able to connect with your people!", "https://en.wikipedia.org/wiki/Poozeum")
        return
    else:
        st.map()
        return

# Start of the normal app part

st.title("Hello World!")
st.markdown("As you can see, this is my first Streamlit App")
st.markdown("Isn't is :rainbow[CRAZY]?")


st.subheader("I don't know if you can tell...")
st.markdown("But I really don't know what I am doing :)")

button()

# Column Set for I am trying ...
col1, col2 = st.columns(2)
with col1:
    st.subheader("I am trying...", divider='rainbow')
with col2:
    st.subheader("But this crap is hard!", divider='rainbow')

doYouAgree()

# Sidebar
with st.sidebar:
    st.header("About app")
    st.write("It is a terrible, stream of conciousness, overthetop and yet underwelling app.(If you attack me on my grammer, I will come for you)")

    if harassmentVar == True:
        st.write("")
        st.write("Enjoy the harassment version of the app!")

st.text("")
st.text("Wait! Text exist? Let me use that instead of the markdown stuff.")
st.header("Simply put", divider='rainbow')
st.text("I don't know what to build, so lets just see where this takes us :)")
st.text("")

st.header("Welcome to my...", divider='rainbow')
st.text("")
st.markdown("> “Stream of consciouness app that most certainly will not be any good, but learning starts from being brave enough to produce it anyway.” — *Me*")
st.text("")
st.text("Wow! That was a mouthfull.")

toggle()

st.text("")
st.text("")
st.text("")

st.header("Lets start with the basics..., so what's your name", divider='rainbow')

name()

st.header("Are you young or old", divider='rainbow')

oldVYoung()

st.header("Pick a number", divider='rainbow')

pickANumber()

st.text("")
st.text("")
st.text("")


st.header("Lets talk more about you!", divider='rainbow')
st.text("")
st.text("JK! We've talked about you enough - don't want to give you the scaries!")
st.text("")

st.header("Want to see a chart?", divider='rainbow')
st.text("")


wantToSeeAChart()

#st.text("Well if you didn't check it, you are out of luck, cause you are going to see one anyway.")


st.text("")
st.text("")

# Changed the oringial code to x = x + 10; could we used the slider feature and call a function instead of text when translating to factorial app?
col1, col2 = st.columns(2)
with col1:
    x = st.slider("Choose an x value", 1, 10)
with col2:
    st.write("The value of :rainbow[***x***] is", x+10)


#This is a random chart
#Upgrade Idea, we import real data and change it to a topic we care about and go off on a tagent
st.subheader("This is my chart!")
chart_data = pd.DataFrame(np.random.randn(20,3), columns=("First column", "Second column", "Third column"))
st.area_chart(chart_data)

st.header("Anyway, if you didn't find the chart impressive enough...", divider='rainbow')

st.text("Here is an image for your troubles")

st.text("This is an image of a self driving car, isn't cool!")
st.image("selfDrivingCar.jpeg")

car()

st.header("If that is still not impressive to you...", divider='rainbow')

st.text("Here is a map")
#st.map()

poopPin()

st.header("If that is still not impressive to you...", divider='rainbow')

st.subheader("You are out of luck, because I have nothing else")
st.text("I hope you enjoyed my disfunctional, poor quality app. (Don't worry, you won't hurt my feelings if you think it is awful)")
st.text("Thank you to StreamLit and DataProfessor for helping me learn some of the basics")

st.subheader("Until next time...")
