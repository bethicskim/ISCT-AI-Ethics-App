import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import time

# Define AI Agent Class for Real-Time Simulation
class ISCTBusinessAI:
    """AI Agent for ethical negotiation using ISCT principles."""
    def __init__(self, name, data_sharing, regulation, profit_focus, governance, hypernorm_weights):
        self.name = name
        self.data_sharing = data_sharing  
        self.regulation = regulation  
        self.profit_focus = profit_focus  
        self.governance = governance  
        self.hypernorm_weights = hypernorm_weights  
        self.history = []

    def evaluate_hypernorms(self):
        """Calculates an AI agent’s hypernorm score based on adjustable user-defined priorities."""
        return sum([
            self.hypernorm_weights["fairness"] * (1 - abs(self.data_sharing - 0.5)),
            self.hypernorm_weights["transparency"] * (1 - abs(self.regulation - 0.5)),
            self.hypernorm_weights["privacy"] * (1 - self.data_sharing),
            self.hypernorm_weights["accountability"] * self.governance,
            self.hypernorm_weights["cultural_respect"] * (1 - abs(self.profit_focus - 0.5))
        ]) / 5

    def negotiate(self, other_agent):
        """AI Negotiation using hypernorm-based scoring."""
        agreement_score = (self.data_sharing + other_agent.data_sharing) / 2
        agreement_score += (self.regulation + other_agent.regulation) / 2
        agreement_score += (self.profit_focus + other_agent.profit_focus) / 2
        agreement_score += (self.governance + other_agent.governance) / 2
        agreement_score /= 4  

        hypernorm_impact = (self.evaluate_hypernorms() + other_agent.evaluate_hypernorms()) / 2
        final_agreement_score = (agreement_score + hypernorm_impact) / 2  

        self.history.append((other_agent.name, final_agreement_score))
        other_agent.history.append((self.name, final_agreement_score))

        return final_agreement_score

    def explain_decision(self):
        """Generates a human-readable explanation of AI's negotiation decision."""
        return (f"{self.name} considered fairness ({self.hypernorm_weights['fairness']}), transparency ({self.hypernorm_weights['transparency']}), "
                f"privacy ({self.hypernorm_weights['privacy']}), accountability ({self.hypernorm_weights['accountability']}), and cultural respect ({self.hypernorm_weights['cultural_respect']}).")

# Streamlit UI
st.title("🌍 ISCT-Based AI Business Ethics Negotiation - Long-Term Simulation")

st.header("🛠️ User-Controlled AI Hypernorm Priorities")
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

# Define AI Agents
agent_names = ["US AI", "EU AI", "China AI", "India AI", "Japan AI", "Middle East AI", "Africa AI"]
random.shuffle(agent_names)  

agents = [ISCTBusinessAI(
    agent_names[i], random.uniform(0.5, 0.9), random.uniform(0.1, 0.5),
    random.uniform(0.5, 1.0), random.uniform(0.3, 0.8), hypernorm_priorities) for i in range(num_agents)]

# Simulate AI Negotiations Over Multiple Years
agreements_over_years = []
st.subheader("📆 Long-Term AI Business Ethics Simulation")
progress_bar = st.progress(0)

for year in range(1, num_years + 1):
    yearly_agreements = []
    for _ in range(10):
        a, b = random.sample(agents, 2)
        agreement = a.negotiate(b)
        yearly_agreements.append(agreement)

    avg_agreement = np.mean(yearly_agreements)
    agreements_over_years.append((year, avg_agreement))

    progress_bar.progress(year / num_years)
    time.sleep(0.5)  

# Plot Agreement Trends Over Years
years, agreement_scores = zip(*agreements_over_years)
st.subheader("📈 Agreement Trends Over Time")
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.lineplot(x=years, y=agreement_scores, marker='o', linestyle='-', color='b', label="Agreement Score", ax=ax1)
ax1.set_xlabel("Years")
ax1.set_ylabel("Agreement Score")
ax1.set_title("AI Business Ethics Agreement Over Time")
ax1.legend()
ax1.grid(True)
st.pyplot(fig1)

# AI Decision Explanation
st.subheader("📢 AI Decision-Making Explanation")
for agent in agents:
    st.write(agent.explain_decision())

# Display Final AI Trust Scores
st.subheader("🌍 AI Trust Score After Years of Collaboration")
trust_scores = [random.uniform(0.5, 1.0) for _ in agents]
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.barplot(x=[agent.name for agent in agents], y=trust_scores, ax=ax2)
ax2.set_xlabel("AI Agents")
ax2.set_ylabel("Trust Score (0-1)")
ax2.set_title("Final AI Trust Score")
st.pyplot(fig2)

st.success("Simulation Complete! 🎉 AI systems have finished negotiating.")
