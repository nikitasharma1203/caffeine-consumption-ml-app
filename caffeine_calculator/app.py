import streamlit as st
import pandas as pd

st.set_page_config(page_title="Caffeine Intake Calculator", layout="wide")

st.markdown("""
    <style>
    body {
        background-color: #f5f1e6;
    }
    .main {
        background-color: #f5f1e6;
    }
    h1, h2, h3 {
        color: #4b2e2e;
    }
    .stButton>button {
        background-color: #6f4e37;
        color: white;
        border-radius: 10px;
        padding: 8px 16px;
        border: none;
    }
    .stButton>button:hover {
        background-color: #4b2e2e;
        color: #fff;
    }
    .css-1d391kg {
        background-color: #e8dcc7;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
# ☕ Brew. Sip. Track.

### *"Because every cup tells a story: make sure yours stays balanced."*
---
""")

caffeine_data = {
    "Tea": {"Dwarkesh": 37.86, "Girnar": 25, "Lipton": 23.25, "Red Label": 48,
        "Taj": 58.8, "Tata": 37, "Tetley": 33, "Tulsi": 0, "Waghbakri": 20,
        "Others(Regular tea)": 35.36, "Others(Green tea)": 30},
    "Coffee": {
        "Amul": 70, "Nescafe": 60, "Bru": 80, "Davidoff": 57, "Ajay": 38,
        "MSU Nescafe": 24.08, "Continental": 62, "Starbucks": 73, "Sunrise": 90,
        "Others(Regular)": 55, "Others(Black)": 75
    },
    "Energy Drink": {
        "Red Bull": 30, "Monster": 36, "Mountain Dew": 54, "Coca cola": 38,
        "Sting": 29, "Others": 31}}

if "drinks" not in st.session_state:
    st.session_state["drinks"] = pd.DataFrame(columns=["Type", "Brand", "Size", "Servings", "Caffeine_mg"])

st.sidebar.header("☕ Add Your Drink")

weight = st.sidebar.number_input("Your Weight (kg):", min_value=30, value=70)
drink_type = st.sidebar.selectbox("Drink Type:", list(caffeine_data.keys()))
brand = st.sidebar.selectbox("Brand:", list(caffeine_data[drink_type].keys()))
size = st.sidebar.number_input("Cup Size (ml):", min_value=50, step=50, value=250)
servings = st.sidebar.number_input("Servings:", min_value=1, value=1)

caffeine_per_100ml = caffeine_data[drink_type][brand]
caffeine_per_cup = (caffeine_per_100ml / 100) * size

st.sidebar.markdown(f"**☕ Per Cup:** `{caffeine_per_cup:.2f} mg`")


if st.sidebar.button("➕ Add Drink"):
    caffeine_amount = caffeine_per_cup * servings
    new_row = {
        "Type": drink_type,
        "Brand": brand,
        "Size": size,
        "Servings": servings,
        "Caffeine_mg": round(caffeine_amount, 2)
    }
    st.session_state["drinks"] = pd.concat(
        [st.session_state["drinks"], pd.DataFrame([new_row])],
        ignore_index=True
    )

if st.sidebar.button("🔄 Reset Session"):
    st.session_state["drinks"] = pd.DataFrame(
        columns=["Type", "Brand", "Size", "Servings", "Caffeine_mg"]
    )


st.subheader("📋 Your Coffee Log")

if st.session_state["drinks"].empty:
    st.info("No drinks added yet ☕")
else:
    st.dataframe(st.session_state["drinks"], use_container_width=True)


if st.button("📊 Analyze My Intake"):

    total_caf = st.session_state["drinks"]["Caffeine_mg"].sum()
    limit = 2.5 * weight

    st.subheader("📊 Results")

    progress = min(total_caf / limit, 1.0)
    st.progress(progress)

    st.write(f"**Total Caffeine:** {total_caf:.2f} mg")
    st.write(f"**Safe Limit:** {limit:.2f} mg")

    if total_caf < limit:
        st.success("✅ You're in the safe zone. Enjoy your brew!")
    elif total_caf == limit:
        st.warning("⚖️ Right at the edge. Maybe skip the next cup?")
    else:
        st.error("🚨 Too much caffeine! Time to switch to water.")
