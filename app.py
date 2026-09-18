import streamlit as st
from pathlib import Path

# =========================
# PAGE SETTINGS
# =========================

st.set_page_config(
    page_title="Cristian Joseph Turin | Portfolio",
    page_icon="💻",
    layout="wide"
)

import streamlit as st
from pathlib import Path

st.set_page_config(
    page_title="Cristian Joseph Turin | Portfolio",
    page_icon="💻",
    layout="wide"
)

# 👇 IBUTANG DINHI ANG MOBILE CSS
st.markdown("""
<style>

@media (max-width: 768px) {

    .block-container {
        padding-left: 20px;
        padding-right: 20px;
    }

    .hero-title {
        font-size: 36px;
    }

    img {
        max-width: 100%;
        height: auto;
    }

}

</style>
""", unsafe_allow_html=True)


# SUNOD NA ANG UBAN NIMONG CODE
# COLORS
# CUSTOM CSS
# ASSETS
# HOME
# ABOUT
# SKILLS
# PROJECTS
# EDUCATION
# CONTACT
# FOOTER

# =========================
# COLORS
# =========================

BG = "#0f1117"
CARD = "#181b24"
TEXT = "#ffffff"
MUTED = "#b8bcc8"
PURPLE = "#8b7cff"

# =========================
# CUSTOM CSS
# =========================

st.markdown(
    f"""
    <style>

    .stApp {{
        background-color: {BG};
        color: {TEXT};
    }}

    .block-container {{
        max-width: 1150px;
        padding-top: 30px;
        padding-bottom: 50px;
    }}

    p {{
        color: {MUTED};
        line-height: 1.7;
    }}

    h1, h2, h3, h4 {{
        color: {TEXT} !important;
    }}

    .stCaption {{
        color: {MUTED} !important;
    }}

    hr {{
        border-color: #303440;
    }}

    .card {{
        background-color: {CARD};
        padding: 28px;
        border-radius: 18px;
        border: 1px solid #292d38;
        margin-bottom: 20px;
    }}

    .hero-title {{
        font-size: 52px;
        font-weight: 700;
        line-height: 1.15;
        margin-bottom: 20px;
    }}

    .hero-small {{
        color: {PURPLE};
        font-weight: 700;
        letter-spacing: 2px;
        font-size: 15px;
    }}

    .purple {{
        color: {PURPLE};
    }}

    .skill-box {{
        background-color: {CARD};
        border: 1px solid #292d38;
        border-radius: 16px;
        padding: 22px;
        text-align: center;
        margin-bottom: 20px;
    }}

    .project-box {{
        background-color: {CARD};
        border: 1px solid #292d38;
        border-radius: 18px;
        padding: 25px;
        margin-bottom: 20px;
    }}

    .project-number {{
        color: {PURPLE};
        font-weight: 700;
        font-size: 14px;
        letter-spacing: 1px;
    }}

    .contact-box {{
        background-color: {CARD};
        border: 1px solid #292d38;
        border-radius: 20px;
        padding: 35px;
    }}

    .contact-box a {{
        color: {PURPLE};
        text-decoration: none;
    }}

    .contact-box a:hover {{
        text-decoration: underline;
    }}

    .footer {{
        text-align: center;
        padding: 25px;
    }}

    .footer a {{
        color: {PURPLE};
        text-decoration: none;
        font-weight: 600;
    }}

    .footer a:hover {{
        text-decoration: underline;
    }}

    .stButton > button {{
        background-color: {PURPLE};
        color: white;
        border: none;
        border-radius: 10px;
        padding: 10px 25px;
        font-weight: 600;
    }}

    .stButton > button:hover {{
        background-color: #7667ee;
        color: white;
    }}

    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# ASSETS
# =========================

ASSETS = Path("assets")

profile = ASSETS / "profile.jpg"
portfolio = ASSETS / "portfolio.jpg"
dashboard = ASSETS / "dashboard.jpg"


# =========================
# HEADER
# =========================

st.markdown(
    """
    <div class="card">
        <h2>
            Cristian<span class="purple">.</span>
        </h2>
        <p>Personal Portfolio</p>
    </div>
    """,
    unsafe_allow_html=True
)

# =========================
# QUOTE
# =========================

st.info(
    '"Who am I to judge others when I myself is an imperfect one"'
)

# =========================
# HOME
# =========================

left, right = st.columns([1.6, 1])

with left:

    st.markdown(
        '<div class="hero-small">HELLO, I\'M</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        """
        <div class="hero-title">
            Cristian Joseph
            <span class="purple">Turin</span>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write(
        "A college student interested in technology, "
        "web development, UI/UX design, and creating "
        "useful digital experiences."
    )

    st.markdown(
        """
        <a href="#my-projects">
            <button style="
                background-color:#8b7cff;
                color:white;
                border:none;
                padding:12px 25px;
                border-radius:10px;
                font-weight:bold;
                cursor:pointer;
                font-size:15px;
            ">
                View My Projects
            </button>
        </a>
        """,
        unsafe_allow_html=True
    )


with right:

    if profile.exists():

        st.image(
            str(profile),
            width=300
        )

    else:

        st.markdown(
            """
            <div class="card" style="text-align:center;">
                <div style="font-size:80px;">👨‍💻</div>
                <h3>Profile Photo</h3>
                <p>Add profile.jpg inside the assets folder.</p>
            </div>
            """,
            unsafe_allow_html=True
        )


# =========================
# ABOUT ME
# =========================

st.divider()

st.header("About Me")
st.caption("Get to know me and what I do.")

about1, about2 = st.columns(2)

with about1:

    st.markdown(
        """
        <div class="card">

        <h3>👋 Who I Am</h3>

        <p>
        I am Cristian Joseph Turin, a college student
        who is interested in technology and digital design.
        I enjoy learning how websites and applications
        are created.
        </p>

        <p>
        I am continuously improving my skills in
        programming, web development, and user interface design.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


with about2:

    st.markdown(
        """
        <div class="card">

        <h3>🎯 My Goal</h3>

        <p>
        My goal is to develop useful and easy-to-use
        digital experiences while continuing to improve
        my technical and creative skills.
        </p>

        <p>
        I want to gain more experience in developing
        websites and applications.
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )


# =========================
# SKILLS
# =========================

st.divider()

st.header("My Skills")
st.caption("Technologies and skills that I am learning and using.")

skills = [
    ("🌐", "HTML", "Building website structures"),
    ("🎨", "CSS", "Designing web interfaces"),
    ("🐍", "Python", "Programming and development"),
    ("🚀", "Streamlit", "Creating Python web applications"),
    ("📱", "UI/UX Design", "Designing user-friendly interfaces"),
    ("💻", "Web Development", "Creating functional websites")
]

columns = st.columns(3)

for i, skill in enumerate(skills):

    icon, name, description = skill

    with columns[i % 3]:

        st.markdown(
            f"""
            <div class="skill-box">

            <div style="font-size:38px;">
                {icon}
            </div>

            <h3>{name}</h3>

            <p>{description}</p>

            </div>
            """,
            unsafe_allow_html=True
        )


# =========================
# PROJECTS
# =========================

st.divider()

st.markdown(
    '<div id="my-projects"></div>',
    unsafe_allow_html=True
)

st.header("My Projects")
st.caption("Some of the projects and activities I have worked on.")

projects = [
    (
        "01",
        "Personal Portfolio",
        "A personal portfolio website designed to showcase my profile, skills, and projects.",
        "Python • Streamlit • HTML • CSS",
        portfolio
    ),
    (
        "02",
        "Student Dashboard",
        "A dashboard concept for presenting student information and useful academic features.",
        "UI Design • Web Development",
        dashboard
    )
]

project_columns = st.columns(2)

for i, project in enumerate(projects):

    number, title, description, technologies, image = project

    with project_columns[i % 2]:

        st.markdown(
            f"""
            <div class="project-box">

            <div class="project-number">
                PROJECT {number}
            </div>

            <h2>{title}</h2>

            </div>
            """,
            unsafe_allow_html=True
        )

        if image.exists():

            st.image(
                str(image),
                use_container_width=True
            )

        else:

            st.info(
                f"Add {image.name} inside the assets folder."
            )

        st.write(description)

        st.write(
            f"**Technologies:** {technologies}"
        )


# =========================
# EDUCATION
# =========================

st.divider()

st.header("Education")
st.caption("My educational background.")

st.markdown(
    """
    <div class="card">

    <h3>🎓 Elementary</h3>
    <p><strong>Bislig Central Elementary School</strong></p>

    <br>

    <h3>🏫 High School</h3>
    <p><strong>Bislig City National High School</strong></p>

    <br>

    <h3>🎓 College</h3>
    <p><strong>De la Salle John Bosco College</strong></p>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# CONTACT
# =========================

st.divider()

st.header("Contact Me")
st.caption("Let's connect and get in touch.")

st.markdown(
    """
    <div class="contact-box">

    <h2>Let's Work Together</h2>

    <p>
    If you want to know more about me, my skills,
    or my projects, feel free to contact me.
    </p>

    <p>
        📧 <strong>Email:</strong>
        <a href="mailto:Cristianturin7@gmail.com">
        Cristianturin7@gmail.com
        </a>
    </p>

    <p>
        📘 <strong>Facebook:</strong>
        <a href="https://www.facebook.com/cristian.joseph.turin.2025"
        target="_blank">
        Facebook
        </a>
    </p>

    <p>
        📸 <strong>Instagram:</strong>
        <a href="https://www.instagram.com/terdy.06/"
        target="_blank">
        Instagram
        </a>
    </p>

    </div>
    """,
    unsafe_allow_html=True
)


# =========================
# FOOTER
# =========================

st.divider()

st.markdown(
    "<h4 style='text-align: center;'>© 2026 Cristian Joseph Turin</h4>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align: center;'>Personal Portfolio • Built with Streamlit</p>",
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:

    st.link_button(
        "📘 Facebook",
        "https://www.facebook.com/cristian.joseph.turin.2025",
        use_container_width=True
    )

    st.link_button(
        "📸 Instagram",
        "https://www.instagram.com/terdy.06/",
        use_container_width=True
    )

    st.caption("Latest Updated: September 18, 2026")

