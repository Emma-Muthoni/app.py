import streamlit as st

# 1. App Header & Title
st.title("🎓 OUK Student Performance Portal")
st.write("Enter your grades below to dynamically calculate your final semester marks.")

# 2. Interactive Input Fields (Users type directly on the website)
student_name = st.text_input("Student Name:", value="Robison")
current_score = st.number_input("Current Exam Score (%):", min_value=0, max_value=100, value=80)
bonus_points = st.slider("Select Awarded Bonus Points:", min_value=0.0, max_value=20.0, value=8.5, step=0.5)

# 3. The Math Logic
final_score = current_score + bonus_points

# 4. Display the results visually using web elements
st.markdown("---")
st.subheader("📊 Final Evaluation Report")

st.info(f"**Student Profile:** {student_name}")

if final_score >= 50:
    st.success(f"🎉 **Status: Passed!** Final calculated mark is **{final_score}%**")
else:
    st.error(f"⚠️ **Status: Review Needed.** Final calculated mark is **{final_score}%**")
