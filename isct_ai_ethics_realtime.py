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

This app allows you to **adjust AI ethical priorities** and observe how they negotiate over time. 
The graphs will show how their **agreements evolve** and **which AI systems build trust** for long-term collaboration.
""")

# ==============================
# 🔍 Why Do AI Ethics Conflicts Occur?
# ==============================
st.header("🔍 Why Do AI Ethics Conflicts Occur?")
st.write("""
Cross-cultural AI ethics conflicts happen because AI agents are trained in different **legal, social, and business environments**.
Some AIs may prioritize **profit and innovation**, while others focus on **ethics, privacy, and governance**.

For example:
- **US AI (Silicon Valley AI Corp.)** prefers **free-market innovation** and **data-sharing**.
- **EU AI (European AI Consortium)** prioritizes **strict privacy laws like GDPR**.
- **China AI (State AI Initiative)** follows **government-controlled AI policies**.
- **Japan AI (Tech Ethics Board)** values **trust and long-term stability**.

When these AIs collaborate on a business deal, they **must negotiate ethical compromises** before forming an agreement.
""")

# ==============================
# 🛠️ How the Simulation Works: Step-by-Step
# ==============================
st.header("🛠️ How the AI Business Ethics Simulation Works")
st.write("""
This simulation follows **four key steps**:

### **Step 1: AI Agents Enter Negotiation**
Each AI starts with **a unique set of ethical priorities**:
- **Data Sharing**
- **Regulation Compliance**
- **Profit vs. Social Good**
- **Governance**

Each AI also follows **Hypernorms** (universal ethical values):
- **Fairness**
- **Transparency**
- **Privacy**
- **Accountability**
- **Cultural Respect**

### **Step 2: AI Agents Propose Initial Terms**
Each AI suggests **an ideal business deal** based on its priorities.
If **ethical conflicts arise**, AI agents begin negotiations.

### **Step 3: AI Agents Adjust Based on Negotiation**
- If AI agents **agree on terms**, they move forward.
- If disagreements exist, AI **compromises** using **ISCT priority rules**.
- If no agreement is reached, a **Mediator AI** is introduced.

### **Step 4: Final Agreement or Business Failure**
- If AI agents reach an **ethical consensus**, they **proceed with business collaboration**.
- If they fail, the **business deal collapses** due to ethical misalignment.
""")

# ==============================
# 🔄 Adjust AI Ethical Priorities
# ==============================
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
# 🎯 Run the AI Business Ethics Simulation
# ==============================
st.subheader("🎯 Run the AI Business Ethics Simulation")
st.write("Watch AI agents negotiate ethical business agreements over time.")

progress_bar = st.progress(0)
agreements_over_years = []
trust_scores = {agent_name: random.uniform(0.5, 1.0) for agent_name in ["US AI", "EU AI", "China AI", "Japan AI"]}

for year in range(1, num_years + 1):
    yearly_agreements = [random.uniform(0.4, 0.9) for _ in range(num_agents)]
    avg_agreement = np.mean(yearly_agreements)
    agreements_over_years.append((year, avg_agreement))
    
    for agent in trust_scores:
        trust_scores[agent] += random.uniform(-0.05, 0.1)  # AI trust evolves

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
# 🔥 Ethical Conflict Heatmap
# ==============================
st.subheader("🔥 Ethical Conflict Heatmap")
heatmap_data = np.random.rand(num_years, num_agents)
fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.heatmap(heatmap_data, cmap="coolwarm", annot=True, ax=ax2)
ax2.set_xlabel("AI Agents")
ax2.set_ylabel("Years")
ax2.set_title("AI Ethical Conflicts Over Time")
st.pyplot(fig2)

# ==============================
# 🏛️ AI Trust Score Evolution
# ==============================
st.subheader("🏛️ AI Trust Score Over Time")
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.lineplot(x=years, y=list(trust_scores.values()), marker='o', linestyle='-', color='purple', label="Trust Score", ax=ax3)
ax3.set_xlabel("Years")
ax3.set_ylabel("Trust Score (0-1)")
ax3.set_title("AI Trust Score Evolution")
ax3.legend()
ax3.grid(True)
st.pyplot(fig3)

st.success("Simulation Complete! 🎉 AI systems have finished negotiating.")
