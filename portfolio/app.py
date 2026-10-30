import streamlit as st
import pandas as pd
import numpy as np


st.set_page_config(
    page_title="Gave C. Hontiveros | Portfolio & Autobiography",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "feedback_submitted" not in st.session_state:
    st.session_state.feedback_submitted = False
if "interactive_rating" not in st.session_state:
    st.session_state.interactive_rating = 5

# Custom CSS for polished design (Extra Component: Theme / Custom CSS)
st.markdown("""
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 700;
        color: #1E3A8A;
        margin-bottom: 0px;
    }
    .sub-title {
        font-size: 1.1rem;
        color: #4B5563;
        margin-bottom: 1.5rem;
    }
    .card {
        padding: 1.2rem;
        border-radius: 10px;
        background-color: #F8FAFC;
        border: 1px solid #E2E8F0;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# SIDEBAR NAVIGATION & CONTROLS
with st.sidebar:
    st.image("portfolio/Selfie.jpg", caption="Gave C. Hontiveros", use_container_width=True)
    st.markdown("### **Gave C. Hontiveros**")
    st.markdown("**Program:** BS Computer Science")
    st.markdown("**Section:** G5")
    st.markdown("---")
    
    st.subheader("🧭 Navigation")
    page_selection = st.radio(
        "Go to section:",
        ["About & Autobiography", "Skills & Analytics", "Projects Portfolio", "Interactive Zone", "Contact & Feedback"]
    )
    
    st.markdown("---")
    st.subheader("⚙️ Page Settings")
    display_milestones = st.checkbox("Show Milestones Timeline", value=True)
    skill_filter = st.selectbox(
        "Filter Skills Category",
        ["All Skills", "Software Engineering", "Cloud & Cybersecurity", "Data Science"]
    )
    
    st.markdown("---")
    st.caption("Submitted for CSIT340 Activity | 2026")


# ABOUT & AUTOBIOGRAPHY
if page_selection == "About & Autobiography":
    st.markdown('<p class="main-title">Gave C. Hontiveros</p>', unsafe_allow_html=True)
    st.markdown('<p class="sub-title">BS Computer Science — Section G5 | Student ID: 23-3742-867</p>', unsafe_allow_html=True)
    
    col_img, col_bio = st.columns([1, 2])
    
    with col_img:
        st.image(
            "https://via.placeholder.com/300x350.png?text=Gave+C.+Hontiveros", 
            caption="Gave C. Hontiveros — CS Student",
            use_container_width=True
        )
    
    with col_bio:
        st.subheader("👋 Biography")
        st.write("""
        Hello! I am a passionate Computer Science student dedicated to building scalable full-stack applications, 
        exploring cloud architecture, and diving into cybersecurity and data science. My journey in technology 
        is driven by curiosity and a desire to engineer practical, real-world solutions that bridge technical complexity 
        and user-centered design.
        """)
        st.write("""
        When I am not developing platforms or solving cybersecurity challenges, I enjoy studying foreign languages, 
        analyzing complex data structures, and collaborating on systems architecture projects.
        """)
    
    st.markdown("---")
    st.header("📖 Autobiography & Background")
    
    tab_bg, tab_edu, tab_interests = st.tabs(["🏛️ Background", "🎓 Education", "💡 Interests"])
    
    with tab_bg:
        st.write("""
        Growing up with a fascination for computers and logical problem-solving, I began programming early on. 
        My journey started with simple scripts and evolved into designing complete multi-tier enterprise software, 
        exploring how backend systems seamlessly connect with intuitive mobile and web interfaces.
        """)
    
    with tab_edu:
        st.markdown("**Cebu Institute of Technology - University**")
        st.write("Bachelor of Science in Computer Science")
        st.write("*Relevant Coursework:* Software Engineering, Data Science & Machine Learning, AWS Cloud Foundations, Cryptography & Cybersecurity, ServiceNow Platform Development, Foreign Languages (Japanese).")
    
    with tab_interests:
        st.write("""
        - **Full-Stack Engineering:** Java Spring Boot, Next.js, TypeScript, Kotlin Android.
        - **Cloud & DevOps:** AWS Infrastructure, IAM, Cost Explorer, EC2 & S3 Deployment.
        - **Data & AI:** K-Means Clustering, Association Rule Mining, Data Pipelines in Pandas.
        - **Cybersecurity:** Cipher Analysis, Modular Arithmetic, and CTF Challenge Solving.
        """)

    if display_milestones:
        st.markdown("---")
        st.subheader("🏆 Key Milestones")
        st.markdown("""
        - **2026:** Engineered STATHIS v2.5 Architecture — A multi-tier fitness system using Spring Boot, Next.js, and Kotlin.
        - **2026:** Completed Advanced ServiceNow & AWS Cloud Foundations Certifications/Coursework.
        - **2026:** Conducted Data Science Research on Machine Learning Clustering & Classification Algorithms.
        - **2026:** Solved multi-category CTF challenges across Cryptography and Web Exploitation.
        """)

# SKILLS & ANALYTICS
elif page_selection == "Skills & Analytics":
    st.header("⚡ Technical Skills & Proficiency")
    st.write("Below is a breakdown of my self-assessed technical proficiencies across core domains.")
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Core Language", "Java / Kotlin", "Advanced")
    m2.metric("Web Frameworks", "Spring / Next.js", "Proficient")
    m3.metric("Cloud Platform", "AWS / Cloud", "Intermediate")
    m4.metric("Data Science", "Pandas / Scikit", "Intermediate")
    
    st.markdown("---")
    
    skills_data = {
        "Skill": ["Java (Spring Boot)", "Next.js / React", "Kotlin (Android)", "AWS Cloud", "Python (Data Science)", "Cryptography & CTF", "ServiceNow Dev"],
        "Category": ["Software Engineering", "Software Engineering", "Software Engineering", "Cloud & Cybersecurity", "Data Science", "Cloud & Cybersecurity", "Software Engineering"],
        "Proficiency (%)": [92, 88, 85, 80, 84, 78, 82],
        "Years Experience": [3, 2, 2, 1, 2, 1, 1]
    }
    df_skills = pd.DataFrame(skills_data)
    
    if skill_filter != "All Skills":
        filtered_df = df_skills[df_skills["Category"] == skill_filter]
    else:
        filtered_df = df_skills
        
    col_table, col_chart = st.columns([1, 1])
    
    with col_table:
        st.subheader("📋 Skills Summary Table")
        st.dataframe(filtered_df, use_container_width=True)
        
        csv_data = filtered_df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="📥 Download Skills CSV Data",
            data=csv_data,
            file_name="gave_hontiveros_skills.csv",
            mime="text/csv"
        )
        
    with col_chart:
        st.subheader("📊 Proficiency Chart")
        chart_data = filtered_df.set_index("Skill")[["Proficiency (%)"]]
        st.bar_chart(chart_data)

# PROJECTS PORTFOLIO
elif page_selection == "Projects Portfolio":
    st.header("🛠️ Featured Projects")
    st.write("A selection of my recent software architecture, data science, and cloud deployment projects.")
    
    # Project 1
    with st.expander("🏋️ Project 1: STATHIS — Multi-Tier Health & Fitness Platform", expanded=True):
        st.markdown("**Role:** Lead Systems Architect & Full-Stack Developer")
        st.markdown("**Tools Used:** Java Spring Boot, Next.js, Kotlin, PostgreSQL, Docker")
        st.write("""
        STATHIS is a full-featured fitness ecosystem built with a robust Spring Boot backend API, 
        a modern Next.js web application dashboard, and a native Kotlin Android client. It incorporates adaptive 
        exercise recommendations, user schedule management, and real-time form evaluation.
        """)
        st.markdown("[View Repository on GitHub](https://github.com/G-A-V-E)")

    # Project 2
    with st.expander("📊 Project 2: Unsupervised Data Clustering & Analysis Suite"):
        st.markdown("**Role:** Data Science Developer")
        st.markdown("**Tools Used:** Python, Pandas, Scikit-Learn, Jupyter, Matplotlib")
        st.write("""
        Conducted extensive exploratory data analysis and unsupervised machine learning models, implementing 
        K-Means clustering, DBSCAN, and SLINK algorithms. Automated evaluation metrics to analyze cluster 
        cohesion and optimal hyperparameter selection.
        """)
        st.markdown("[View Data Science Notebooks](https://github.com/G-A-V-E)")

    # Project 3
    with st.expander("☁️ Project 3: AWS Cloud Architecture & IAM Policy Suite"):
        st.markdown("**Role:** Cloud Systems Administrator")
        st.markdown("**Tools Used:** AWS EC2, S3, IAM, AWS Cost Explorer, CLI")
        st.write("""
        Designed secure multi-tier cloud infrastructure configurations adhering to the AWS Well-Architected Framework. 
        Implemented granular IAM access control policies, automated cost tracking with AWS Cost Explorer, and optimized 
        resource provisioning with Reserved Instances.
        """)
        st.markdown("[View Infrastructure Docs](https://github.com/G-A-V-E)")

# INTERACTIVE ZONE
elif page_selection == "Interactive Zone":
    st.header("🎛️ Interactive Streamlit Showcase")
    st.write("Demonstrating interactive Streamlit widgets integrated with real-time feedback logic.")
    
    st.subheader("1. Project Focus Filter")
    tech_stack = st.multiselect(
        "Select technologies you are interested in discussing:",
        ["Java / Spring", "React / Next.js", "Kotlin", "AWS Cloud", "Python / Data Science", "Cybersecurity"],
        default=["Java / Spring", "AWS Cloud"]
    )
    if tech_stack:
        st.info(f"Selected focus areas: **{', '.join(tech_stack)}**")
        
    st.markdown("---")
    
    st.subheader("2. Self-Assessment Interactive Adjuster")
    hours_studied = st.slider("Hours spent coding per week:", min_value=5, max_value=60, value=25, step=5)
    st.write(f"At **{hours_studied} hours/week**, estimated yearly output: **{hours_studied * 52} hours** of engineering practice!")

# CONTACT & FEEDBACK
elif page_selection == "Contact & Feedback":
    st.header("📬 Contact & Visitor Feedback")
    st.write("Have feedback or want to get in touch? Send a message using the form below.")
    
    # Extra Component: Form
    with st.form(key="contact_form", clear_on_submit=True):
        st.subheader("Send a Message")
        
        col_f1, col_f2 = st.columns(2)
        with col_f1:
            user_name = st.text_input("Your Name *")
        with col_f2:
            user_email = st.text_input("Your Email *")
            
        subject = st.selectbox("Topic", ["General Inquiry", "Project Collaboration", "Feedback", "Other"])
        message = st.text_area("Your Message *")
        
        rating = st.slider("Rate this Streamlit Portfolio App (1-10):", 1, 10, 10)
        
        submit_button = st.form_submit_button(label="🚀 Submit Feedback")
        
    if submit_button:
        if user_name.strip() == "" or user_email.strip() == "":
            st.error("Please fill in all required fields (Name and Email).")
        else:
            st.session_state.feedback_submitted = True
            st.success(f"Thank you, **{user_name}**! Your message regarding **'{subject}'** has been received.")
            st.balloons()  # Extra visual touch
            
    if st.session_state.feedback_submitted:
        st.info("ℹ️ You have submitted feedback during this session. Thank you for visiting!")


st.markdown("---")
st.caption("© 2026 Gave C. Hontiveros | BSIT | Built with Streamlit")
