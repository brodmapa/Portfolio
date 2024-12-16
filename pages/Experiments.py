import streamlit as st
import pandas as pd
import logic.utils as utls

# --- Adding New Topics ---
# When adding new topics, paste the elif statement and 
# make sure that the topic is the same in select box and if statement

st.set_page_config(page_title="Image Gallery", layout="wide", page_icon="lol", initial_sidebar_state="auto")
page = st.sidebar.selectbox("Select a Project", [
    "Overview",
    "Data Platform Engineering",
    "Weather Prediction", 
    "Visualising Sexual Harassment UK", 
    "Hybrid Animation for Neural Nets"])

# --- Overview ---
if page == "Overview":
    st.title("Project Overview")
    st.write("""In this section I present a selection of the projects i have worked on. 
             With each project you will find a attributed year and context sourrounding the project. Do note
             that these experiments are not edited post submission and are not meant to be run in web.
             If you are looking for anything specific, feel free to check the table below:""")

    data = {'Project': ['Weather Prediction', 'Visualising Sexual Harassment UK', 'Hybrid Animation for Neural Nets'],
            'Date': [25, 30, 35],
            'Area': ['Study', 'Study', 'Work']}

    df = pd.DataFrame(data)
    styled_df = df.style.highlight_max(axis=0, color='darkgreen')
    st.dataframe(styled_df)

# --- Data Platform Engineering ---
elif page == "Data Platform Engineering":
    st.title("Home Page")
    st.write("Welcome to the Home Page!")
    st.code("""
import pandas as pd

# Create a DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35]}
df = pd.DataFrame(data)

# Display the DataFrame
print(df)
""", language='python')

# --- Weather Prediction ---
elif page == "Weather Prediction":
    st.title("Home Page")
    st.write("Welcome to the Home Page!")

    html_file = "./sources/experiments_.html"

    with open(html_file, "r") as f:
        html_content = f.read()

    st.components.v1.html(html_content, height=38500, scrolling=False)

# --- Sexual Harassment UK ---
elif page == "Visualising Sexual Harassment UK":
    col1, col2 = st.columns([3, 1])  # Adjust column widths (3:1 ratio)
    with col2:
        st.info("""This project was created for the
        Data visualisation course during May 2024.""")
        st.info("This project was part of the Master Degree Program: Data Science - FH Kiel")
    with col1:
        st.markdown("""
    <h1>Harassment in Numbers (UK - 2023)</h1>
    <blockquote>
        For more information on data collection and methodology, refer to the <a href="https://www.ons.gov.uk/peoplepopulationandcommunity/crimeandjustice/bulletins/experiencesofharassmentinenglandandwales/december2023">original article</a>.
    </blockquote>
    <p>The CSEW (Crime Survey for England and Wales) gathered information on experiences of harassment in different age groups all throughout England and Wales. This article serves to break down these numbers and trends to reflect as objectively as possible on the increasing issue of harassment.</p>
    <p>Data has been gathered from the ONS (Office for National Statistics). For further information, it is advised to visit their website or contact them directly.</p>""",unsafe_allow_html=True)

    st.markdown("""
    <p>When discussing the issue of harassment, significant attention has to be paid to the complex nature of the topic summarized below. Participants in the CSEW surveys were aged 16 or older by the time of questioning and summarized their experience with harassment in the past year.</p>
    <h3>Non-Sexual Harassment</h3>
    <ul>
        <li>Comments or behavior of a threatening, hurtful, or abusive nature directed at you in public.</li>
        <li>Messages or calls of a threatening, hurtful, or abusive nature (including posts online).</li>
        <li>Threatening, hurtful, or abusive graffiti about you (not shown in tables due to disclosure restraints).</li>
    </ul>
    <h3>Sexual Harassment</h3>
    <ul>
        <li>Unwanted messages or calls of a sexual nature.</li>
        <li>Inappropriate sexual jokes, comments, or gestures.</li>
        <li>Unwanted relationship attempts.</li>
        <li>Sexually explicit pictures or videos being taken, shared, or threatened to be shared without permission.</li>
        <li>Unwanted touching in either a sexual or non-sexual way.</li>
        <li>Someone indecently exposing themselves in person or online (flashing).</li>
    </ul>
    <h3>71% of harassers are estimated to be strangers</h3>
    <p>This was concluded based on the representative number of participants in the questionnaire and their personal relationship with the predator. The trend clearly indicates a tendency toward harassment originating with people you do not have a very close relationship with.The authors data additionally reveals that 82.6% of non-sexual harassment happens in person, while only 66.8% of sexual harassment happens in person. Sexual online harassment in an online space increases in likelihood from 15.3% to 29.1%. Considering the influence of online spaces toward harassment, as shown by studies conducted in America [2], this issue cannot fully contribute to the impact of online spaces in which regulations for abusive behaviors are not sufficiently enforced.</p>
    <p>Instead, the crime survey for 2023 indicates strongly that in-person harassment by strangers is the most prevalent form of harassment.</p>""", unsafe_allow_html=True)

    st.image(utls.imagerise("./images/Data_Viz/2.png",[800,800]), caption="Resized Kitten Image")


    st.markdown("""<h3>Overall distribution of harassment shows specific trends & differences for each gender</h3>
    <p>Similarity trends in the relationship of victim toward perpetrator for both genders appear to make room for gender-based differences when considering the likelihood of harassment. Throughout their lifespan, women are more likely to be harassed for any reason than the overall values of people show. Noticably, in later stages of life, the downward trend appears to shift, which appears especially significant for English and Welsh males. The government report itself does not indicate reasons for this periodic increase and subsequent decrease in harassment likelihood.</p>""",unsafe_allow_html=True)
    st.image(utls.imagerise("./images/Data_Viz/1.png",[1098, 450]), caption="""Note: Overall harassment refers to the combined values of male & female population. Experience of any harassment calculated where a respondent has stated that they experienced at least one type of behaviour listed as either non-sexual or sexual.""")


    st.markdown("""<h3>23% of women aged 16-24 are predicted to experience sexual harassment in any given year</h3>
    <p>Continuing further on the age-related tendencies in male and female harassment, the change in harassment over the course of life can be further divided into sexual and non-sexual.
        While women appear to suffer consistently more or equally from harassment at almost every stage and aspect, the trend does not always appear consistent. Considering the strongest influences of harassment at an early age toward later stages of life, the temporary increase in non-sexual (general) harassment in men clearly outgrows and even surpasses female sexual harassment. This sharp increase in male victims appears to be the first 10-year period where any kind of harassment between men and women is equally comparable.</p>""",unsafe_allow_html=True)
    st.image(utls.imagerise("./images/Data_Viz/3.png",[1098,450]), caption="""Note: Values of male sexual harassment at 65 - 1.2%; Non sexual harassment female are between - 2.8%; Estimates provided are based on questions where respondents were prompted with different behaviours. Questions were separated into ‘non-sexual’ and ‘sexual’ harassment categories.
        Experience of non-sexual harassment calculated where a respondent has stated that they experienced at least one type of behaviour listed in the non-sexual harassment types.
        Experience of sexual harassment calculated where a respondent has stated that they experienced at least one type of behaviour listed in the sexual harassment types.""")

    st.markdown("""<h3>35 to 44 is the age range, when the most prevalent harassment appears to slow down</h3>
        <p>Looking more closely into the scenarios proposed by the data, at least two obvious points can be drawn:
        1) Harassment decreases with age, although not always consistently.
        2) Hurtful and inappropriate behaviors do not seem to be a simple age trend but continue throughout adulthood.</p>""",unsafe_allow_html=True)
    st.image(utls.imagerise("./images/Data_Viz/4.png",[1098,450]), caption="""Percentages may not sum to 100% as respondents could select multiple response options.
        Specific datapoints had to be retrospectively added, since they aren’t available to the public.These include:
        indecent exposure - age 16- 19, 55+ sexually explicit videos - age 45 - 54
        [2] - including comments or gestures
        [3] - including calls of sexual nature
        [4] - Messages or calls of a threatening, hurtful or abusive nature (including things posted online)
        [5] - Comments or behaviour of a threatening, hurtful or abusive nature directed at you in public
        [6] - to you (flashing) either in person or online
        [7] - in either a sexual or non-sexual way
        [8] - taken, shared or threatened to be shared without your permission""")


    st.markdown("""<h3>The people who experience the most harassment share with authorities the least</h3>
    <p>While further information is provided on victims perceptions of the reasons behind their harassment and the relevant locations in which harassment happens, the original article already provides an in- depth analysis of the Crime Survey for England and Wales between October 2022 and March 2023. Instead, the survey itself should also be put under close inspection, seeing as it is inherently likely that biases and harassment are considered to occur relatively more often than they are reported.</p>""",unsafe_allow_html=True)
    st.image(utls.imagerise("./images/Data_Viz/5.png",[1098,450]), caption="""[2] - Experience of Any Harassment for both genders
        Survey participants describe the unweighted base, which refers to all respondents who were shown the harassment module.
        Number of participants not equal for all parts of the survey presented thus far. Varying participant amounts found in relationship to perpetrator. Value for 16-24 year olds artificially created from mean of 16-19 & 20-24 age groups.64 years old most people have experienced harassment""")
    st.markdown("""<p>Considering the survey participants, a steep difference, while not found in relation to the participating genders, is clearly found in age distributions. The staggering difference between underage, adult, and elderly
        participants appears to correspond to the severity of experiencing harassment. While it is absolutely possible to be sheer coincidence, there is an argument to be made for either lack of support for or knowledge about harassment related crime cases in young adults. Both reasons provided might begin to contextualise this trend, but are in no way proven or based on emperical evidence. Further research or authors comments on this subject matter might give additional insights into this pattern. For further information and analysis please refer to the original source linked below.</p>""",unsafe_allow_html=True)
    st.markdown("""
    <h3>This post has been created by Paul Brodmann | 26th June 2024.</h3>
    <ul>
        <li>Unwanted relationship attempts</li>
        <li>[1] - „Experiences of harassment in England and Wales: December 2023“, Nick Stripe, https://www.ons.gov.uk/ peoplepopulationandcommunity/crimeandjustice/bulletins/experiencesofharassmentinenglandandwales/december2023#glossary, Last Accessed: 21st June 2024</li>
        <li>[2] - „The State of Online Harassment“, Emilia A Vogels, https://www.pewresearch.org/internet/2021/01/13/the-state-of-online-harassment/, Last Accessed: 21st June 2024</li>
    </ul>
""", unsafe_allow_html=True)

# --- Hybrid Animation for Neural Nets ---
elif page == "Hybrid Animation for Neural Nets":
    st.title("Page 2")
    st.write("This is Page 2!")

