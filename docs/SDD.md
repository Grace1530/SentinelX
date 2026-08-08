# SentinelX
## Software Design Document (SDD)

### Project
SentinelX: An Explainable AI-Based Intrusion Detection and Prevention Platform with an Integrated Cyber Attack Simulation Laboratory

### Version
1.0

---

# 1. System Architecture

SentinelX follows a modular architecture consisting of:

1. Network Capture Layer
2. Processing Layer
3. AI Detection Layer
4. Explainability Layer
5. Threat Intelligence Layer
6. Decision Layer
7. Prevention Layer
8. Persistence Layer
9. API Layer
10. Presentation Layer
11. AttackForge Laboratory

---

# 2. High-Level Architecture

```text
                    ┌──────────────────────┐
                    │      NETWORK         │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  PACKET CAPTURE      │
                    │      ENGINE           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ PACKET PARSER        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │ FEATURE EXTRACTION   │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │   AI DETECTION       │
                    │      ENGINE           │
                    └───────┬───────┬──────┘
                            │       │
                    ┌───────▼──┐ ┌──▼──────────────┐
                    │EXPLAIN-  │ │THREAT           │
                    │ABILITY   │ │INTELLIGENCE     │
                    └───────┬──┘ └──────┬──────────┘
                            │            │
                            └──────┬─────┘
                                   ▼
                    ┌──────────────────────┐
                    │   DECISION ENGINE     │
                    └──────────┬───────────┘
                               │
                    ┌──────────┴──────────┐
                    ▼                     ▼
          ┌──────────────────┐   ┌──────────────────┐
          │ ALERT MANAGEMENT  │   │   IPS ENGINE     │
          └────────┬─────────┘   └────────┬─────────┘
                   │                      │
                   └──────────┬───────────┘
                              ▼
                    ┌──────────────────────┐
                    │      DATABASE        │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    FASTAPI LAYER     │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │    SOC DASHBOARD     │
                    └──────────────────────┘


             ┌──────────────────────────────┐
             │        ATTACKFORGE          │
             │   Controlled Lab Simulator  │
             └──────────────┬───────────────┘
                            │
                            ▼
                     LAB NETWORK TRAFFIC
                            │
                            └──────► PACKET CAPTURE