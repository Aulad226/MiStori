import streamlit as stm
import streamlit as st
import datetime
import openai
from streamlit_option_menu import option_menu
from streamlit_cognito_auth import CognitoAuthenticator


#Coding for views from here
stm.set_page_config(page_title="MiStori", page_icon="📗", layout="wide")
#Coding for Nab bar
selected = option_menu(
        menu_title = None,
        options = ["Home", "Story", "Contact us"],
        icons = ["house", "book", "envelope"],
        menu_icon = "cast",
        default_index=0,
        orientation = "horizontal",
        styles = {
            "container": {"padding":"0!important", "background-color":"#262730"},
            "icon": {"color":"orange", "font-size": "25px"},
            "nav-link":{
                "font-size" : "20px",
                "text-align": "left",
                "margin": "0px",
                "--hover-color": "#8A5353",
            },
            "nav-link-selected": {"background-color": "#D66464"},
        },
    ) 

#Coding for home page from here
if selected == "Home":
 hour = datetime.datetime.now().hour

 if hour < 12:
    greeting = "Good morning"
 elif hour < 18:
    greeting = "Good afternoon"
 else:
    greeting = "Good evening"

# Print the greeting message
 stm.subheader(f"{greeting} And welcome...👋")
 stm.write("MiStori is an innovative AI-powered platform that enables individuals to effortlessly recount the stories of their loved ones. This platform has a scalable business model that has the potential to appeal to a vast market, including older individuals who possess valuable stories and knowledge. Developing MiStori requires front-end and back-end development, as well as the implementation of AI video editing technology, database management, video uploading and storage, and website development.")
#Genrate sroey form from here
if selected == "Story":
 def main():
    stm.title('Lets get introduced')
    name = stm.text_input('Who do you want to interview?')
    dob = stm.text_input('Birthdate', placeholder='dd/mm/yyyy')
    # Get a list of all countries and cities
    countries = ['Australia', 'United States', 'China']
    cities = {  
    'Australia': ['Sydney', 'Melbourne', 'Brisbane','Perth','Adelaide','Australian Capital Territory','Darwin','Hobart'],
    'United States': ['New York ', 'Los Angeles', 'Chicago','Houston'],
    'China': ['Anhui', 'Beijing', 'Chongqing','Fujian','Gansu','Guangdong','Guangxi','Guizhou']
}
    # Create a dropdown list for countries
    country = stm.selectbox('Country', countries)
    if country:
       city = stm.selectbox('City', cities[country])
    qualification = stm.selectbox('Highest level of qualification?',('','Highschool', 'Diploma', 'Bachelor', 'Master', 'PhD'))
    relationship = stm.selectbox('Relationship to the person?',('','Grandparent', 'Parent', 'Children', 'Cousin', 'Spouse/Partner', 'In-law'))

    col1, col2, col3 = stm.columns(3)
    with col1:
        work_industry = stm.text_input('Industry of work?')
    with col2:
        work_role = stm.text_input('Role of work?')
    with col3:
        work_organization = stm.text_input('Organization of employment?')
    achievements = stm.text_input('What are some of their notable achievements?', help="Those could be from any aspect of life")
    about = stm.selectbox('What do you want this story to be about?',('','Personal background and development','Career and professional life','Personal relationships and life events','Social and cultural context','Personal growth and transformation','Financial journey','Community involvement','Mentors and influencers','Family heritage and genealogy'))
    gpt_prompt=f"You will create a storyline in fashion of person's bio and 15 dynamic interview questions. The interview questions will change depending on the inputs from 11 variables. These interview questions will be structured to bring out as much wisdom and emotion as possible and will strongly relate to the context provided by the 11 variables. The variables are:{name}{dob}{country}{city}{qualification}{relationship}{work_industry}{work_role}{work_organization}{achievements}{about}"   

    if stm.button('Proceed'):
        openai.api_key= API_KEY
        with stm.spinner('Generating the storyline and questions for you now...'):
            response = openai.Completion.create(
              model="text-davinci-003",
              prompt= gpt_prompt,
              temperature=0.7,
              max_tokens=256,
              top_p=1,
              frequency_penalty=0,
              presence_penalty=0
            )
        questions = response['choices'][0]['text']
        stm.write(questions)

 if __name__ == "__main__":
    main()
#Contact us page coding from here
if selected == "Contact us":
# Subtitle
 stm.subheader("We appreciate your feedback and look forward to hearing from you!")

# Text
 stm.markdown("""
 MiStori is a fun and engaging way to create stories. It is a great way to let your imagination run wild, and it is also a great way to improve your writing skills..
 """)

# Contact information
 stm.markdown("""
 If you would like to learn more about us, please visit our website at [website address]. You can also contact us at [email address] or [phone number].

 If you have any feedback for us, please fill out the form below.
 """)

# Feedback form
 name = stm.text_input("Your name", placeholder="your full name")
 email = stm.text_input("Your email address")
 feedback = stm.text_area("Your feedback")

# Submit button
 if stm.button("Submit feedback"):
    stm.markdown("""
    Thank you for your feedback! We will review it and get back to you as soon as possible.
    """)

"---"

#Adding code for footer here

footer_container = stm.container()

with footer_container:
   col1, col2, col3 = stm.columns((2,1,1))

   with col1:
      stm.subheader("Mission")

      stm.markdown("<p>MiStori is a platform that empowers everyone to share their stories. We believe that stories have the power to connect, inspire, and make us feel understood. We are committed to helping people tell their stories and making the world a better place.</p>", unsafe_allow_html=True)

   with col2:
      stm.subheader("Policies")
      stm.markdown('<a>Privacy Policy </a>', unsafe_allow_html=True)
      stm.markdown('<a>Terms and Conditions </a>', unsafe_allow_html=True)
      stm.subheader("Support")
      stm.markdown('<a>Support forum</a>', unsafe_allow_html=True)
      stm.markdown('<a>FAQ page </a>', unsafe_allow_html=True)
   with col3:
      stm.subheader("Contact info")
      stm.markdown("Email: xyz@MiStori.com", unsafe_allow_html=True)
      stm.markdown("<p>Mobile: 04xxxxxxx", unsafe_allow_html=True)
      stm.markdown("<p>Address: Darwin City, NT 0800", unsafe_allow_html=True)
      stm.subheader("Social Apps")
      stm.markdown("<a href='https://www.facebook.com/'>Facebook</a>", unsafe_allow_html= True)
      stm.markdown("<a>Linkedin</a>", unsafe_allow_html=True)
      stm.markdown("<a>Twitter</a>", unsafe_allow_html=True)

#Below codes are for the Developer address
stm.markdown("<br>", unsafe_allow_html=True)
stm.markdown("<h5>Developed by True Blue IT Services 2023", unsafe_allow_html=True)


#Hiding Default MainMenu and Footer
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """ 
stm.markdown(hide_st_style, unsafe_allow_html=True)
 
