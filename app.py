import streamlit as st
from agent.mock_orchestrate import Orchestrator  


# Initialize Orchestrator
orchestrator = Orchestrator()

st.title("BIMSHI Store Dashboard 🧶")

# --- Show Current Inventory ---
st.header("Current Inventory")
inventory = orchestrator.get_inventory()
for item, qty in inventory.items():
    st.write(f"{item}: {qty} pcs")

# --- Update Stock ---
st.header("Update Stock")
item_to_update = st.selectbox("Select Item", list(inventory.keys()))
qty_change = st.number_input("Quantity to Add/Subtract", min_value=-100, max_value=100, value=0)
if st.button("Update Stock"):
    orchestrator.update_stock(item_to_update, qty_change)
    st.success(f"{item_to_update} stock updated!")
    st.experimental_rerun()

# --- Generate Insights ---
st.header("Analytics Insights")
if st.button("Generate Insights"):
    insights = orchestrator.get_insights()
    for key, val in insights.items():
        st.write(f"{key}: {val}")

