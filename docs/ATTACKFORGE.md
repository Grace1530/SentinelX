# SentinelX
## AttackForge — Cyber Attack Simulation Laboratory

## 1. Purpose

AttackForge is the controlled cyber attack simulation laboratory
integrated into SentinelX.

Its purpose is to generate authorized network activity so that
SentinelX can validate:

- Detection
- Explainability
- Alerting
- Threat classification
- Prevention
- Incident recording
- Reporting

AttackForge shall operate only against explicitly authorized
laboratory targets.

---

# 2. Architecture

```text
AttackForge UI
      │
      ▼
Scenario Manager
      │
      ▼
Target Validation
      │
      ▼
Simulation Engine
      │
      ▼
Authorized Lab Target
      │
      ▼
Generated Network Traffic
      │
      ▼
SentinelX Packet Capture
      │
      ▼
Feature Extraction
      │
      ▼
AI Detection
      │
      ▼
Explainability
      │
      ▼
Decision Engine
      │
      ├──────────────► Alert
      │
      └──────────────► IPS
                         │
                         ▼
                      Firewallok d