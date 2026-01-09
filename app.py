import streamlit as st

st.set_page_config(page_title="IB MYP Daily Common Board", layout="centered")

st.title("📘 IB MYP Daily Common Board")
st.caption("Fast • Simple • Classroom Ready")

st.subheader("IB MYP Focus")

key_concept = st.selectbox(
    "Key Concept",
    ["Connections", "Change", "Relationships", "Form", "Identity",
     "Global Interactions", "Creativity", "Logic", "Time, Place & Space"]
)

related_concept = st.text_input("Related Concept (1–2 words)")
global_context = st.selectbox(
    "Global Context",
    [
        "Identities and relationships",
        "Orientation in space and time",
        "Personal and cultural expression",
        "Scientific and technical innovation",
        "Globalization and sustainability",
        "Fairness and development"
    ]
)

st.subheader("Daily Common Board")

benchmark = st.text_input("Florida Benchmark")

statement = st.text_area(
    "Statement of Inquiry",
    value=f"Students will understand that {key_concept.lower()} is developed through {related_concept or '________'} in the context of {global_context.lower()}."
)

inquiry = st.text_input("Inquiry Question")
learning_target = st.text_input("Learning Target (I can...)")
agenda = st.text_area("Agenda", placeholder="Bell Ringer → Inquiry → Practice → Reflection")

st.subheader("Ready-to-Post Common Board")

output = f"""
BENCHMARK:
{benchmark}

STATEMENT OF INQUIRY:
{statement}

INQUIRY QUESTION:
{inquiry}

LEARNING TARGET:
{learning_target}

AGENDA:
{agenda}
"""

st.text_area("Copy & Paste (Board or Slides)", output, height=260)
