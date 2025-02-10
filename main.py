import streamlit as st
import pandas as pd
import time
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import numpy as np
st.title("Welcome To Streamlit")
st.subheader(" Let's Explore the Features and Functionalities of the Streamlit")
st.markdown(":ghost::pencil:"*15)
st.markdown("-----")
st.header("Lets Explore The Code:")
st.code("""
        a = "hello Worls!
        print(a)
        for i in range(20):
            print(f"2 * {i} = {2*i}")
        """,line_numbers=True,language="python")
st.success("Done")
st.markdown("-----")
st.markdown("### Lets Explore Some Input Fields :star:")
Name = st.text_input("Name")
Password = st.text_input("Password",type="password",placeholder="Enter Password")
Date = st.date_input("Enter Date Of Birth")
Time = st.time_input("Select Time Of Birth")
Age = st.number_input("Select Your Age",min_value=1,max_value=80,placeholder="Age Matters")
City = st.select_slider("City",["AP","TG","KRNTK","ALAPADU","GDVD","TPG"])
Rating = st.slider("Distance",0,100)
Gender = st.radio("Gender",["Male","Female"])
col1,col2 = st.columns(2)
with col1:
    Languages = st.selectbox("Languages Known",["Telugu","English","Hindi"])
with col2:
    Programming = st.multiselect("Programming Languages",["Java","Python","Django","C","C++","PHP","SQL","POWER-BI"])
Show_details = st.toggle("Show Details")
st.divider()
if Show_details:
    st.success(f"""Name : {Name} \n Passwors : {Password} 
               \n Date : {Date} 
               \n Time : {Time} 
               \n Age : {Age} 
               \n City : {City}
               \n Gender : {Gender}
               \n Languages : {Languages} 
               \n Programs Learned : {Programming}""")

st.markdown("## Loading The Data")
def load(data)-> pd.DataFrame:
    return pd.read_excel(data)
df = load("IT.xls")
df.columns = df.iloc[5]
df = df[6:].reset_index(drop=True)
# st.table(df)
st.markdown("##### IT Dept Academic List")
st.dataframe(df)
st.markdown("------")
st.markdown("##### Data Editor")
st.data_editor(df)

st.divider()
st.header("Media")
img = st.image("sasilogo.png",caption="Sasi Logo")
Audio = st.audio("I-Wanna-Be-Yours.mp3",format="audio/mp3")
tab1,tab2=st.tabs(["Click","Monument Memory"])
with tab1:
    if st.button("Lets Take A Picture"):
        cam = st.camera_input("Click To Capture")
        if cam:
            with open(f"one.png","wb") as f:
                f.write(cam.getbuffer())
                st.success("Image Saved")
        else:
            st.warning("Image Not Saved")
with tab2:
    if st.button("Want To See IT Memory :ghost:"):
        st.video("it.mp4",format="video/mp4",autoplay=True)
st.balloons()
st.snow()
st.divider()
st.markdown("### Lets Explore Some Advance Features")
tab1,tab2,tab3 = st.tabs(["Insight","ChatBot - > IT","Visualize A File"])
with tab1:
    if (st.button("Want to See Top 10 IT Students ",icon='🔎')):
        df["FinalCGPA"] = pd.to_numeric(df["FinalCGPA"])
        st.dataframe(df.nlargest(10,"FinalCGPA"))
        
        df.columns = df.columns.str.strip()
    
        # Replace empty values with NaN and fill them appropriately
        df.fillna(0, inplace=True)
            
        # Convert numerical columns to appropriate types
        gpa_columns = [col for col in df.columns if "GPA" in col]
        backlog_columns = [col for col in df.columns if "Backlogs" in col]
        df[gpa_columns] = df[gpa_columns].apply(pd.to_numeric, errors='coerce')
        df[backlog_columns] = df[backlog_columns].apply(pd.to_numeric, errors='coerce')
            
        st.write("## Student Performance Overview")
            
        # Line Chart - GPA Progression for a Selected Student
        st.subheader("GPA Progression")
        student = st.selectbox("Select Student", df["Name"].unique())
        student_data = df[df["Name"] == student]
        if not student_data.empty:
            st.line_chart(student_data[gpa_columns].T)
        
        # Bar Chart - Final CGPA Distribution
        st.subheader("Final CGPA Distribution")
        st.bar_chart(df,x="Name",y="FinalCGPA")

        
  
            
with tab2:
    def stream(data):
        for word in data.split():
            yield word + " "
            time.sleep(0.2)
            
    prompt = st.chat_input("Ask Me Anything")
    if prompt:
        res = f"you Ask For {prompt} but I only Know About a Person in IT is Anil named as *LE-01* , *Titulu* "
        with st.chat_message("user"):
            st.write_stream(stream(res))
with tab3:
    fileup = st.file_uploader("Choose A File To Visualize",type="csv")
    if fileup:
        st.dataframe(pd.read_csv(fileup))






