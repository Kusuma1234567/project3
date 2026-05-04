import streamlit as st
st.title("My App")
from database import init_db, insert_request, get_all_requests, update_status
from priority import detect_priority
from notification import send_email
from database import add_reply
from notification import send_reply_email

# Initialize DB
init_db()

st.set_page_config(page_title="Certificate Priority System", layout="wide")

st.title("📄 Smart Certificate Priority Prediction System")

menu = ["New Request", "Admin Dashboard"]
choice = st.sidebar.selectbox("Menu", menu)

# ---------------------------
# USER REQUEST PAGE
# ---------------------------
if choice == "New Request":
    st.subheader("Submit Certificate Request")

    name = st.text_input("Enter Name")
    email = st.text_input("Enter Email")
    message = st.text_area("Enter Request Message")

    if st.button("Submit Request"):
        if name and email and message:
            priority = detect_priority(message)

            insert_request(name, email, message, priority)

            st.success(f"Request Submitted Successfully!")
            st.info(f"Detected Priority: {priority}")

        else:
            st.error("Please fill all fields")

# ---------------------------
# ADMIN DASHBOARD
# ---------------------------
elif choice == "Admin Dashboard":

    st.subheader("All Requests")

    data = get_all_requests()

    for row in data:
        req_id, name, email, message, priority, status,reply = row

        st.write("----")
        st.write(f"ID: {req_id}")
        st.write(f"Name: {name}")
        st.write(f"Email: {email}")
        st.write(f"Message: {message}")
        st.write(f"Priority: {priority}")
        st.write(f"Status: {status}")
        st.write(f"Reply: {reply}")

        reply_text = st.text_input(f"Reply for Request ID {req_id}", key=f"reply_{req_id}")

        if st.button(f"Send Reply {req_id}", key=f"send_reply_{req_id}"):
            if reply_text:
                add_reply(req_id, reply_text)
                send_reply_email(email, name, reply_text)
                st.success("Reply sent successfully!")

        col1, col2 = st.columns(2)

        with col1:
            if st.button(f"Mark Ready {req_id}", key=f"mark_ready_{req_id}"):
                update_status(req_id, "Ready")

                sent = send_email(email, name, priority)

                if sent:
                    st.success("Notification Sent!")
                else:
                    st.warning("Status updated but email failed")
