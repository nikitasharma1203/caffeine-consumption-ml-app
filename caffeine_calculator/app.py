# caffeine_dashboard.py
# ☕ Caffeine Intake Calculator (Multi-Drink Session)

import streamlit as st
import pandas as pd

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="Caffeine Intake Calculator", layout="wide")
st.title("☕ Caffeine Intake Calculator (Multi-Drink Session)")

# -------------------------------
# CAFFEINE DATA (mg per 100ml)
# -------------------------------
caffeine_data = {
    "Tea": {
        "Dwarkesh": 37.86, "Girnar": 25, "Lipton": 23.25, "Red Label": 48,
        "Taj": 58.8, "Tata": 37, "Tetley": 33, "Tulsi": 0, "Waghbakri": 20,
        "Others(Regular tea)": 35.36, "Others(Green tea)": 30
    },
    "Coffee": {
        "Amul": 70, "Nescafe": 60, "Bru": 80, "Davidoff": 57, "Ajay": 38,
        "MSU Nescafe": 24.08, "Continental": 62, "Starbucks": 73, "Sunrise": 90,
        "Others(Regular)": 55, "Others(Black)": 75
    },
    "Energy Drink": {
        "Red Bull": 30, "Monster": 36, "Mountain Dew": 54, "Coca cola": 38,
        "Sting": 29, "Others": 31
    }
}

# -------------------------------
# SESSION STATE FOR DRINKS
# -------------------------------
if "drinks" not in st.session_state:
    st.session_state["drinks"] = pd.DataFrame(columns=["Type", "Brand", "Size", "Servings", "Caffeine_mg"])

# -------------------------------
# SIDEBAR INPUTS
# -------------------------------
st.sidebar.header("Add a Drink")

weight = st.sidebar.number_input("Your Weight (kg):", min_value=30, value=70)
drink_type = st.sidebar.selectbox("Drink Type:", list(caffeine_data.keys()))
brand = st.sidebar.selectbox("Select Brand:", list(caffeine_data[drink_type].keys()))
size = st.sidebar.number_input("Cup Size (ml):", min_value=50, step=50, value=250)
servings = st.sidebar.number_input("Servings:", min_value=1, value=1)

# -------------------------------
# CALCULATE CAFFEINE PER CUP
# -------------------------------
caffeine_per_100ml = caffeine_data[drink_type][brand]
caffeine_per_cup = (caffeine_per_100ml / 100) * size
st.sidebar.write(f"☕ Caffeine per cup: {caffeine_per_cup:.2f} mg")

# -------------------------------
# BUTTONS
# -------------------------------
if st.sidebar.button("Add Drink"):
    caffeine_amount = caffeine_per_cup * servings
    new_row = {
        "Type": drink_type,
        "Brand": brand,
        "Size": size,
        "Servings": servings,
        "Caffeine_mg": round(caffeine_amount, 2)
    }
    st.session_state["drinks"] = pd.concat([st.session_state["drinks"], pd.DataFrame([new_row])], ignore_index=True)

if st.sidebar.button("🔄 Refresh Session"):
    st.session_state["drinks"] = pd.DataFrame(columns=["Type", "Brand", "Size", "Servings", "Caffeine_mg"])

# -------------------------------
# MAIN PANEL
# -------------------------------
st.subheader("Drinks Summary")
st.dataframe(st.session_state["drinks"])

if st.sidebar.button("Calculate Total"):
    total_caf = st.session_state["drinks"]["Caffeine_mg"].sum()
    limit = 2.5 * weight

    st.subheader("Results")
    st.write(f"☕ Total Caffeine Consumed: {total_caf:.2f} mg")

    if total_caf < limit:
        st.success(f"✅ You're within the safe limit of {limit:.2f} mg.")
    elif total_caf == limit:
        st.info("⚖️ You're exactly at the recommended limit.")
    else:
        st.error(f"⚠️ Warning: You exceeded the safe limit of {limit:.2f} mg!")
