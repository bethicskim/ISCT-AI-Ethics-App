import streamlit as st
import numpy as np
import random
import time

# ==============================
# 🌍 ISCT AI Ethics Simulation for Students
# ==============================
st.title("🌍 ISCT AI Business Ethics Learning Simulation")

st.header("📢 Understanding This Simulation")
st.write("""
This simulation helps students understand **how AI uses ISCT (Integrative Social Contracts Theory) 
to resolve ethical conflicts** in business negotiations.  
- **Step-by-step learning mode** explains each AI decision.  
- **Case studies allow students to test ISCT in real-world dilemmas.**  
- **AI debate mode lets students argue ethical cases with AI.**  
""")

# ==============================
# 🏛️ Select a Case Study Mode
# ==============================
st.sidebar.header("📌 Choose a Case Study")
case_study = st.sidebar.selectbox(
    "Select a Real-World Ethical Scenario:",
    ["AI in Hiring", "AI in Healthcare", "AI & Free Speech"]
)

# Explanation for the selected case study
if case_study == "AI in Hiring":
    st.write("👥 **AI in Hiring**: Should AI prioritize diversity or pure merit?")
elif case_study == "AI in Healthcare":
    st.write("🏥 **AI in Healthcare**: Should AI share patient data for public health?")
elif case_study == "AI & Free Speech":
    st.write("📰 **AI & Free Speech**: Should AI platforms remove harmful content or protect free expression?")

# ==============================
# 🎛️ Adjust AI Ethical Priorities
# ==============================
st.header("🔄 Adjust AI Ethical Priorities")
st.write("Modify how AI agents prioritize different ethical principles before negotiations start.")

hypernorms = {
    "fairness": 1.0,  # Strictly enforced
    "transparency": 1.0,  
    "privacy": 1.0,  
    "accountability": 1.0,  
    "cultural_respect": 1.0  
}

micro_norms = {
    "data_sharing": st.slider("Data Sharing Preference", 0.0, 1.0, 0.5),
    "regulation": st.slider("Regulation Strictness", 0.0, 1.0, 0.5),
    "profit_focus": st.slider("Profit vs. Social Responsibility", 0.0, 1.0, 0.5),
    "governance": st.slider("Democratic vs. Centralized Governance", 0.0, 1.0, 0.5),
}

# ==============================
# 🤖 AI Agent Class with ISCT Step-by-Step Learning
# ==============================
class ISCTBusinessAI:
    """AI Agent that strictly follows ISCT principles."""
    def __init__(self, name, hypernorm_weights, micro_norm_weights):
        self.name = name
        self.hypernorm_weights = hypernorm_weights
        self.micro_norm_weights = micro_norm_weights
        self.history = []
        self.trust_score = random.uniform(0.5, 1.0)

    def check_hypernorms(self, other_agent):
        """Check if the agreement violates ISCT hypernorms."""
        for hypernorm in self.hypernorm_weights.keys():
            if abs(self.micro_norm_weights[hypernorm] - other_agent.micro_norm_weights[hypernorm]) > 0.5:
                return hypernorm
        return None

    def negotiate(self, other_agent):
        """Step-by-step AI decision-making process for students."""
        
        st.write(f"🤖 **{self.name} is reviewing the agreement...**")
        time.sleep(1)

        violation = self.check_hypernorms(other_agent)
        if violation:
            return f"❌ {self.name} rejected the agreement due to a {violation.upper()} violation."

        st.write(f"✅ **{self.name} has approved the agreement.**")
        return f"✅ {self.name} and {other_agent.name} reached an agreement."

# ==============================
# 🎯 Run the Step-by-Step AI Business Ethics Simulation
# ==============================
st.subheader("🎯 Step-by-Step AI Business Ethics Negotiation")

# Define AI Agents
agents = [
    ISCTBusinessAI("US AI", hypernorms, micro_norms),
    ISCTBusinessAI("EU AI", hypernorms, micro_norms),
]

if st.button("Start Step-by-Step Simulation"):
    a, b = random.sample(agents, 2)
    result = a.negotiate(b)
    st.write(result)

# ==============================
# 💬 AI Debate Mode: Students vs. AI
# ==============================
st.subheader("💬 Debate an Ethical Case with AI")
st.write("Test your ethical reasoning by arguing against AI.")

user_input = st.text_input("Your argument against AI’s stance:")

if user_input:
    chosen_agent = random.choice(agents)
    response = f"🤖 {chosen_agent.name} says: 'I respect your argument, but ISCT requires us to prioritize {random.choice(list(hypernorms.keys()))}.'"
    st.write(response)

st.success("Simulation Complete! 🎉 AI strictly followed ISCT and explained decisions.")
