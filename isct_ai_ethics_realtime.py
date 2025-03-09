import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import random
import time

# Define AI Agent Class for Real-Time Simulation
class ISCTAgent:
    """AI Agent for ethical negotiation using ISCT principles."""
    def __init__(self, name, hypernorm_weight=0.7, microsocial_contract_weight=0.3):
        self.name = name
        self.hypernorm_weight = hypernorm_weight
        self.microsocial_contract_weight = microsocial_contract_weight
        self.ethical_state = random.uniform(0, 1)  # Represents adherence to ethical norms
        self.history = []

    def negotiate(self, other_agent):
        """Simulates an ethical negotiation between two AI agents."""
        hypernorm_agreement = abs(self.ethical_state - other_agent.ethical_state) < 0.2
        microsocial_adaptation = (self.microsocial_contract_weight * self.ethical_state +
                                  other_agent.microsocial_contract_weight * other_agent.ethical_state) / 2

        if hypernorm_agreement:
            agreement = (self.ethical_state + other_agent.ethical_state) / 2
        else:
            agreement = microsocial_adaptation

        self.update_ethics(agreement)
        other_agent.update_ethics(agreement)

        self.history.append((other_agent.name, agreement))
        other_agent.history.append((self.name, agreement))

        return agreement

    def update_ethics(self, new_value):
        """Updates the ethical stance based on past negotiations."""
        self.ethical_state = (self.ethical_state + new_value) / 2

# Streamlit UI
st.title("🌍 ISCT-Based AI Ethics Negotiation - Live Tracker")

st.header("🔍 Why Cross-Cultural AI Ethics Conflicts Occur")
st.write("Cross-cultural AI ethics conflicts happen because AI agents trained in different cultural and legal settings interact globally.")
st.write("Key causes include:")
st.markdown("""
- **Divergent Ethical Frameworks**: AI ethics vary across societies (e.g., privacy vs. security).
- **Legal and Policy Variability**: Different AI laws create **regulatory conflicts**.
- **Cultural Philosophy Differences**: Western ethics favor **individual rights**, while Eastern ethics emphasize **collective harmony**.
- **Autonomous AI Decision-Making**: AI adapts based on **cultural biases in training data**.
""")

st.header("📌 Examples of AI Ethics Conflicts")
st.write("""
- **Social Media AI Moderation**: Free speech in the US vs. censorship in China.
- **Autonomous Vehicles**: AI prioritizing **drivers vs. pedestrians** in different countries.
- **AI Hiring Algorithms**: Merit-based hiring in the US vs. **social harmony hiring in Japan**.
- **Facial Recognition AI**: EU bans **public biometric data**, while other governments use it for security.
""")

st.header("🤖 How ISCT Helps Solve AI Ethics Conflicts")
st.write("""
**ISCT-based AI ethics negotiation follows these steps**:
1. **Check hypernorms** – Prevents AI from violating universal ethics.
2. **Evaluate microsocial contracts** – Ensures AI respects cultural norms.
3. **Negotiate using moral free space** – AI finds ethical compromises.
4. **Apply priority rules** – Resolves norm conflicts using ISCT logic.
5. **Reinforce ethical learning** – AI adapts over time.
""")

# User-selectable AI agent configurations
st.sidebar.subheader("Customize AI Agents")
num_agents = st.sidebar.slider("Number of AI Agents", min_value=3, max_value=10, value=5)
num_rounds = st.sidebar.slider("Number of Negotiation Rounds", min_value=5, max_value=50, value=10)

# Define Expanded AI Agents
agent_names = ["EU AI", "US AI", "China AI", "India AI", "Middle East AI", "Japan AI", "Africa AI"]
random.shuffle(agent_names)  # Shuffle agents for diversity

agents = [ISCTAgent(agent_names[i], random.uniform(0.5, 0.9), random.uniform(0.1, 0.5)) for i in range(num_agents)]

# Simulate AI Negotiations
agreements = []
ethical_states_over_time = []

progress_bar = st.progress(0)
status_text = st.empty()

for i in range(num_rounds):
    a, b = random.sample(agents, 2)
    agreement = a.negotiate(b)
    agreements.append((i + 1, agreement))
    ethical_states_over_time.append([agent.ethical_state for agent in agents])

    # Update progress bar
    progress_bar.progress((i + 1) / num_rounds)
    status_text.text(f"Running AI Negotiation Round {i+1}/{num_rounds}...")

    time.sleep(0.5)  # Simulate processing delay

# Plot Ethical Agreement Evolution
rounds, values = zip(*agreements)

st.subheader("📈 Ethical Agreement Trends")
fig1, ax1 = plt.subplots(figsize=(8, 5))
sns.lineplot(x=rounds, y=values, marker='o', linestyle='-', color='b', label="Ethical Agreement Value", ax=ax1)
ax1.set_xlabel("Negotiation Round")
ax1.set_ylabel("Ethical Agreement Value")
ax1.set_title("ISCT-Based AI Ethical Agreement Over Time")
ax1.legend()
ax1.grid(True)
st.pyplot(fig1)

# Heatmap for AI Ethical State Evolution
st.subheader("🌍 Ethical State Evolution Across AI Agents")
ethical_states_matrix = np.array(ethical_states_over_time)
fig2, ax2 = plt.subplots(figsize=(6, 5))
sns.heatmap(ethical_states_matrix, annot=True, cmap="coolwarm", xticklabels=[agent.name for agent in agents], yticklabels=range(1, num_rounds + 1), ax=ax2)
ax2.set_xlabel("AI Agents")
ax2.set_ylabel("Negotiation Round")
ax2.set_title("Ethical State Evolution Over Time")
st.pyplot(fig2)

st.success("Simulation Complete! 🎉")
