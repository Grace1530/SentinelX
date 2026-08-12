# SentinelX
## Database Design

## 1. Database

SQLite — Version 1.0

Database file:

sentinelx.db

---

## 2. Entity Relationship Overview

```text
PACKETS
   │
   ├──────────────► ALERTS
   │                    │
   │                    ▼
   │                INCIDENTS
   │                    │
   │                    ▼
   │                RESPONSES
   │
   └──────────────► ATTACK_SIMULATIONS

THREATS
   │
   └──────────────► ALERTS

THREAT_INTELLIGENCE
   │
   └──────────────► THREATS

BLOCKED_IPS
   │
   └──────────────► RESPONSES

REPORTS
   │
   └──────────────► INCIDENTS