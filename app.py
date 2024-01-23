import streamlit as st
from database import connect_2_db
from pymongo import MongoClient

def main():    
    st.set_page_config(page_title="Send feedback", page_icon=":penguin:")
    st.title('Share your feedback, questions, ideas')

    # this markdown is for hiding "github" button
    st.markdown("<style>#MainMenu{visibility:hidden;}</style>", unsafe_allow_html=True)
    st.markdown("<style>footer{visibility: hidden;}</style>", unsafe_allow_html=True)
    st.markdown("<style>header{visibility: hidden;}</style>", unsafe_allow_html=True)
    st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob, .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137, .viewerBadge_text__1JaDK{display: none;} 
    </style>
    """,
    unsafe_allow_html=True
    )

    feedback = st.text_input("Please write your feedback")
    if st.button('Submit'):
        if feedback:
            feedbacks = connect_2_db()
            feedbacks.insert_one({"feedback": feedback})
            st.success('Thank you for your feedback!')
        else:
            st.warning("Please write your feedback")


if __name__ == '__main__':
    main()