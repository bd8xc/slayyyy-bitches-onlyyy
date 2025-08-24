import streamlit as st
import random

# Title
st.title("📊 My Mini Dashboard")

# Simulate fake analytics data
steps_today = random.randint(3000, 12000)
revenue_today = round(random.uniform(5000, 15000), 2)
new_users = random.randint(10, 100)
open_tickets = random.randint(1, 20)

# Display metrics
st.metric("👟 Steps Today", f"{steps_today} steps")
st.metric("💰 Revenue Today", f"₹{revenue_today}")
st.metric("🧑‍💻 New Users", f"{new_users}")
st.metric("🛠️ Open Support Tickets", f"{open_tickets}")

# Add a bar chart
st.subheader("📈 Revenue Over Past Week")
week_data = [random.uniform(5000, 15000) for _ in range(7)]
st.bar_chart(week_data)

# Add a line chart for steps
st.subheader("👣 Steps Over Past Week")
steps_data = [random.randint(3000, 12000) for _ in range(7)]
st.line_chart(steps_data)

# Add a table
st.subheader("🧾 Sample User Data")
st.table({
    "Name": ["Amit", "Sara", "Ravi"],
    "Email": ["amit@example.com", "sara@example.com", "ravi@example.com"],
    "Signups": [True, True, False]
})
