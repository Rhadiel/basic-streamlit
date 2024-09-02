import streamlit as st

# Setting the title of the app
st.title("Welcome to My Portfolio!")

# Sidebar with navigation options
st.sidebar.title("Navigation")
st.sidebar.write("Use the options below to navigate through the portfolio.")
page = st.sidebar.radio("Go to", ["Home", "About Me", "Projects", "Contact"])

# Main content based on selected page
if page == "Home":
    st.header("Home")
    
    # Welcome message
    st.write("Welcome to my portfolio! I'm excited to share my journey and projects with you. Explore the various sections to learn more about me, my skills, and the work I've done.")
    
    # Introduction
    st.subheader("Who Am I?")
    st.write("""
    I'm Rhadiel, a Bachelor of Science in Information Technology student with a passion for web development and problem-solving. 
    This portfolio showcases my work and accomplishments in different areas of technology.
    """)
    
    # Fun metric display
    st.subheader("Current Focus")
    col1, col2, col3 = st.columns(3)
    col1.metric("Projects Completed", "8+", "3 this year")
    col2.metric("Learning Hours", "1500+", "50 this month")
    col3.metric("Coffee Consumed", "200+", "10 this week")
    
    # Progress bar for fun
    st.subheader("Portfolio Progress")
    st.write("Check out the progress I've made in building this portfolio!")
    progress = st.progress(80)
    st.write("80% Complete")
    
    # Button to encourage exploration
    if st.button("Explore My Projects"):
        st.write("Head over to the Projects section to see what I've been working on!")
    
elif page == "About Me":
    st.header("About Me")
    st.write("""
    Hello! My name is Rhadiel. I'm a passionate Bachelor of Science in Information Technology Student, 
    with experience in web development. I love working on projects that involve creativity, 
    problem-solving, and innovation. In this portfolio, you can find some of the projects I've 
    worked on and get to know a little more about me.
    """)
    st.image("Escario_1x1.jpg", caption='This is me!', use_column_width=True)

elif page == "Projects":
    st.header("Projects")
    st.write("""
    Here are a few projects I've worked on:

    1. **Project 1: Personal Website**
       - Built a personal website using HTML, CSS, and JavaScript.
       - Features: Responsive design, contact form, portfolio gallery.

    2. **Project 2: Inventory Management System**
       - Developed an inventory management system using JavaScript and React.
       - Features: Real-time inventory tracking, order management, and reporting.

    3. **Project 3: Clinic Booking System**
       - Created a clinic booking system using JavaScript and React.
       - Features: Appointment scheduling, patient management, and notifications.

    4. **Project 4: Hotel Booking System**
       - Built a hotel booking system using Java and MySQL.
       - Features: Room reservation, booking management, and customer reviews.
    """)
    # Chart
    st.subheader("Skills Over Time")
    skills_data = {
        "Year": ["2018", "2019", "2020", "2021", "2022"],
        "Python": [70, 75, 80, 85, 90],
        "JavaScript": [60, 65, 70, 75, 80],
    }
    st.line_chart(skills_data)

elif page == "Contact":
    st.header("Contact")
    st.write("""
    If you'd like to reach out to me, feel free to connect via LinkedIn, 
    GitHub, or send me an email at escariorhad@gmail.com.
    """)
    contact_button = st.button("Contact Me")

    if contact_button:
        st.write("Thank you for reaching out! I'll get back to you soon.")
    
    # Additional interactive elements
    st.subheader("Skill Level Assessment")
    skill_level = st.slider("Select your skill level (0 to 100):", min_value=0, max_value=100, value=50)
    st.write(f"Your selected skill level is: {skill_level}")

    st.subheader("Leave a Message")
    message = st.text_input("Type your message here:")
    if st.button("Submit Message"):
        st.write("Message submitted! Thank you!")

# Footer
st.write("Thank you for visiting my portfolio!")
