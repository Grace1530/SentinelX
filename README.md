# 🛡️ SentinelX

## Explainable AI-Based Cyber Defense Platform

> **See Every Packet. Stop Every Threat.**

SentinelX is an explainable AI-based intrusion detection and
prevention platform with an integrated cyber attack simulation
laboratory called **AttackForge**.

---

## 🚀 Core Capabilities

- Network packet monitoring
- Machine-learning-based intrusion detection
- Explainable AI
- Threat intelligence
- Intrusion prevention
- Security alerts
- SOC-style dashboard
- Incident investigation
- Automated reporting
- Controlled attack simulation

---

## ⚔️ AttackForge

AttackForge is SentinelX's integrated cybersecurity laboratory.

It provides controlled scenarios for:

- Port scanning
- SSH brute-force simulation
- Controlled SYN flood
- Controlled HTTP flood

All simulations are restricted to authorized laboratory
environments.

---

## 🧠 AI Detection

SentinelX evaluates:

- Random Forest
- XGBoost

Performance is measured using:

- Accuracy
- Precision
- Recall
- F1-score
- False-positive rate
- False-negative rate
- Detection latency

---

## 🏗️ Architecture

```text
Network
   ↓
Packet Capture
   ↓
Feature Extraction
   ↓
AI Detection
   ↓
Explainability
   ↓
Threat Intelligence
   ↓
Decision Engine
   ↓
IPS
   ↓
Database
   ↓
FastAPI
   ↓
React SOC Dashboard