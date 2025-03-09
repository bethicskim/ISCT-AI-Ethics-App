import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import time

# ==============================
# 🌍 Detailed Explanations: How This AI Simulation Works
# ==============================
st.title("🌍 ISCT AI Business Ethics Negotiation Simulation")

st.header("📢 Understanding This Simulation")
st.write("""
This simulation models **how AI agents from different countries and businesses negotiate ethical agreements** 
before launching a joint **international AI-powered business project**. It demonstrates:
- How **AI decision-making differs** across cultures.
- How **global AI teams can find common ethical ground**.
- The role of **ISCT (Integrative Social Contracts Theory)** in resolving ethical conflicts.
""")

# ==============================
# 🏛️ AI Personalities & Hypernorm Priorities
# ==============================
st.sidebar.subheader("🎭 Choose AI Personality Type")
ai_personality = st.sidebar.selectbox(
    "AI Negotiation Style",
    ["Balanced", "Aggressive", "Cooperative"]
)

st.header("🔄 Adjust AI Ethical Priorities")
st.write("Modify how AI agents prioritize different ethical principles before negotiations start.")

hypernorm_priorities = {
    "fairness": st.slider("Fairness Priority", 0.0, 1.0, 0.8),
    "transparency": st.slider("Transparency Priority", 0.0, 1.0, 0.7),
    "privacy": st.slider("Privacy Priority", 0.0, 1.0, 0.9),
    "accountability": st.slider("Accountability Priority", 0.0, 1.0, 0.6),
    "cultural_respect": st.slider("Cultural Respect Priority", 0.0, 1.0, 0.75),
}

st.sidebar.subheader("⚙️ Simulation Settings")
num_agents = st.sidebar.slider("Number of AI Agents", min_value=3, max_value=10, value=5)
num_years = st.sidebar.slider("Simulation Duration (Years)", min_value=1, max_value=10, value=5)

# ==============================
# 🤖 AI Agent Class with Personalities
# ==============================
class ISCTBusinessAI:
    """AI Agent for ethical negotiation using ISCT principles."""
    def __init__(self, name, personality, hypernorm_weights):
        self.name = name
        self.personality = personality
        self.hypernorm_weights = hypernorm_weights
        self.history = []
        self.trust_score = random.uniform(0.5, 1.0)
    
    def negotiate(self, other_agent):
        """AI Negotiation using hypernorm-based scoring."""
        if self.personality == "Aggressive":
            agreement_score = max(0, 1 - abs(self.trust_score - other_agent.trust_score) * 0.5)
        elif self.personality == "Cooperative":
            agreement_score = min(1, (self.trust_score + other_agent.trust_score) / 1.8)
        else:  # Balanced
            agreement_score = (self.trust_score + other_agent.trust_score) / 2
        
        self.trust_score += random.uniform(-0.05, 0.1)
        other_agent.trust_score += random.uniform(-0.05, 0.1)

        self.history.append((other_agent.name, agreement_score))
        other_agent.history.append((self.name, agreement_score))

        return agreement_score
    
    def explain_decision(self):
        """Generates a human-readable explanation of AI's negotiation decision."""
        return f"{self.name} ({self.personality}) negotiated with {len(self.history)} AI partners, focusing on fairness ({self.hypernorm_weights['fairness']}), transparency ({self.hypernorm_weights['transparency']}), and privacy ({self.hypernorm_weights['privacy']})."

# ==============================
# 🎯 Run the AI Business Ethics Simulation
# ==============================
st.subheader("🎯 Run the AI Business Ethics Simulation")
st.write("Watch AI agents negotiate ethical business agreements over time.")

# Define AI Agents
agent_names = ["US AI", "EU AI", "China AI", "India AI", "Japan AI", "Middle East AI", "Africa AI"]
random.shuffle(agent_names)

agents = [ISCTBusinessAI(agent_names[i], ai_personality, hypernorm_priorities) for i in range(num_agents)]

progress_bar = st.progress(0)
agreements_over_years = []

for year in range(1, num_years + 1):
    yearly_agreements = [random.uniform(0.4, 0.9) for _ in range(num_agents)]
    avg_agreement = np.mean(yearly_agreements)
    agreements_over_years.append((year, avg_agreement))

    progress_bar.progress(year / num_years)
    time.sleep(0.5)

# ==============================
# 📈 Display Business Agreement Trends Over Time
# ==============================
st.subheader("📈 AI Business Ethics Agreement Over Time")
years, agreement_scores = zip(*agreements_over_years)
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.lineplot(x=years, y=agreement_scores, marker='o', linestyle='-', color='b', label="Agreement Score", ax=ax1)
ax1.set_xlabel("Years")
ax1.set_ylabel("Agreement Score")
ax1.set_title("AI Business Ethics Agreement Trends")
ax1.legend()
ax1.grid(True)
st.pyplot(fig1)

# ==============================
# 📜 AI Negotiation Summaries
# ==============================
st.subheader("📜 AI Negotiation Summaries")
for agent in agents:
    st.write(agent.explain_decision())

# ==============================
# 💬 AI Chat: Ask AI About Its Decisions
# ==============================
st.subheader("💬 Ask AI About Its Decisions")
user_input = st.text_input("Ask an AI agent about its negotiation strategy:")

if user_input:
    chosen_agent = random.choice(agents)
    response = f"🤖 {chosen_agent.name} says: '{chosen_agent.explain_decision()}'"
    st.write(response)

st.success("Simulation Complete! 🎉 AI systems have finished negotiating.")
