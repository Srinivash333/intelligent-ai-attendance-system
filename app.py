import streamlit as st

def main():

    st.set_page_config(
        page_title="AI Attendance System",
        page_icon="📸",
        layout="centered"
    )

    # Title
    st.title("AI Powered Attendance System")

    # User input
    name = st.text_input("Enter Student Name")

    # Buttons
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Mark Attendance", type="primary", use_container_width=True):
            st.success(f"Attendance Marked for {name}")

    with col2:
        if st.button("Exit", type="secondary", use_container_width=True):
            st.warning("Session Closed")

    # AI Attendance Image using HTML
    st.markdown("""
    <div style="text-align:center; margin-top:30px;">
        <img 
            src="https://images.unsplash.com/photo-1522075469751-3a6694fb2f61?q=80&w=1200&auto=format&fit=crop"
            width="700"
            style="border-radius:15px;"
        >
        <h2 style="color:#4CAF50;">
            Face Recognition Attendance System
        </h2>
        <p>
            AI based smart attendance using facial recognition technology.
        </p>
    </div>
    """, unsafe_allow_html=True)

main()