# 🛡️ SentinelX

## Explainable AI-Based Network Intrusion Detection & Prevention Platform

> **Detect. Explain. Correlate. Respond.**

SentinelX is a machine-learning-based network security platform that monitors network traffic, extracts behavioral features, detects suspicious activity, explains detections, calculates risk, generates alerts, correlates alerts into incidents, and supports controlled prevention actions.

The project combines machine-learning-based intrusion detection, flow analysis, explainability, risk and decision management, alert and incident management, intrusion prevention, attack simulation, an isolated Kali Linux security lab, and real network traffic validation.

---

## 🎯 What SentinelX Does

```text
Network Traffic
      ↓
Packet Capture
      ↓
Flow Tracking
      ↓
Feature Extraction
      ↓
Machine Learning
      ↓
Explainability
      ↓
Risk & Decision Engine
      ↓
Alert
      ↓
Incident Correlation
      ↓
Prevention
```

The goal is to move from **traffic → detection → investigation → response**.

---

## 🚀 Core Features

### 🔍 Network Traffic Analysis

SentinelX processes:
- Source and destination IP addresses
- Source and destination ports
- Protocol
- Packet length
- TCP flags
- TTL
- Flow-level statistics

### 🔄 Flow Tracking

SentinelX maintains:
- Packet count
- Byte count
- SYN count
- ACK count
- RST count
- FIN count
- Unique destination ports

### 🤖 Machine Learning Detection

SentinelX currently uses a trained **Random Forest classifier**.

Current detection classes:

```text
NORMAL
PORT_SCAN
SSH_BRUTE_FORCE
SYN_FLOOD
HTTP_FLOOD
```

The model produces a prediction and confidence score.

### 🧠 Explainability

Supporting behavioral factors can include:

```text
Multiple destination ports observed
Repeated TCP SYN activity observed
High packet volume observed
```

### ⚖️ Risk & Decision Engine

The decision layer evaluates:
- Detection type
- Confidence
- Severity
- Risk score
- Whitelist state
- Response policy

Possible responses:

```text
MONITOR
ALERT
ALERT_ONLY
BLOCK
```

### 🚨 Alert Management

Alerts can contain:
- Detection type
- Source IP
- Severity
- Confidence
- Risk score
- Explanation
- Status
- Timestamp

### 📋 Incident Management

Incident lifecycle:

```text
OPEN
 ↓
INVESTIGATING
 ↓
CONTAINED
 ↓
RESOLVED
```

### 🔗 Incident Correlation

Repeated alerts from the same ongoing event can update an existing incident.

```text
PORT_SCAN Alert
PORT_SCAN Alert
PORT_SCAN Alert
        ↓
   ONE INCIDENT
        ↓
   Alert Count = 3
```

### 🛡️ Intrusion Prevention

SentinelX includes a prevention layer that can perform controlled blocking actions when the decision policy requires it. Detection, alerting, and prevention can be enabled independently during testing.

---

# ⚔️ AttackForge

**AttackForge** is SentinelX's integrated controlled attack-simulation environment.

Current scenarios include:
- Port scan simulation
- SSH brute-force simulation
- SYN flood simulation
- HTTP flood simulation

AttackForge is used for controlled testing, detection validation, regression testing, prevention validation, and authorized demonstrations.

---

# 🐧 Kali Linux Security Lab

SentinelX was connected to an isolated VMware Kali Linux laboratory using a **VMnet1 Host-only network**.

```text
┌──────────────────────────┐
│       Kali Linux         │
│      192.168.83.129      │
│                          │
│   Nmap / Scapy / Sensor  │
└────────────┬─────────────┘
             │
          VMnet1
       Host-only Network
             │
             ▼
┌──────────────────────────┐
│      Windows Host        │
│      192.168.83.1        │
│      SentinelX API       │
└──────────────────────────┘
```

---

# 📡 Kali Packet Sensor

A Python-based sensor uses **Scapy** to capture packets from Kali's `eth0` interface and extract:

```text
Source IP
Destination IP
Source Port
Destination Port
Protocol
Packet Length
TCP Flags
TTL
Interface
```

Pipeline:

```text
Kali eth0
   ↓
Scapy
   ↓
Kali Packet Sensor
   ↓
SentinelX FastAPI
   ↓
Detection Pipeline
```

---

# 🔄 Real-Traffic Validation

The validated packet-processing path is:

```text
Real Network Traffic
        ↓
Kali eth0
        ↓
Scapy
        ↓
Packet Sensor
        ↓
SentinelX API
        ↓
Flow Tracking
        ↓
Feature Extraction
        ↓
Random Forest
        ↓
Explanation
        ↓
Decision
        ↓
Alert
        ↓
Incident
        ↓
Optional Prevention
```

Controlled Nmap traffic was used during real-traffic validation. Observed classifications included `PORT_SCAN`, `SYN_FLOOD`, and `NORMAL`.

---

# ✅ Validation Results

Current regression result:

```text
42 passed
```

Testing includes:
- AI engine
- AI inference
- Detection API
- Feature extraction
- Flow features
- Explainability
- Decision engine
- IPS engine
- Packet capture
- AttackForge
- Pipeline API
- Sentinel pipeline
- Threat intelligence
- Incident services
- Training pipeline

---

# 🛡️ Prevention Validation

A controlled AttackForge port-scan scenario was tested with prevention enabled.

Example result:

```text
Packets processed : 20
Detections        : 14
Blocked           : 10
Prevention        : Enabled
Status            : COMPLETED
```

---

# 🏗️ System Architecture

```text
                         SENTINELX
                              │
                              ▼
                    ┌──────────────────┐
                    │  Packet Capture  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │  Flow Tracking   │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌───────────────────┐
                    │ Feature Extraction│
                    └────────┬──────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   ML Inference   │
                    │  Random Forest   │
                    └────────┬─────────┘
                             │
                ┌────────────┼────────────┐
                │            │            │
                ▼            ▼            ▼
        Explainability   Risk Engine   Threat Intel
                │            │            │
                └────────────┼────────────┘
                             ▼
                    ┌──────────────────┐
                    │ Decision Engine  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌───────────────────┐
                    │ Alerts / Incidents│
                    └─────────┬─────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  IPS / Response  │
                    └────────┬─────────┘
                             │
                             ▼
                           SQLite
                             │
                             ▼
                          FastAPI
```

---

# 🧰 Technology Stack

**Programming:** Python, SQL, Bash, PowerShell

**Backend:** FastAPI, Pydantic

**Machine Learning:** Scikit-learn, Random Forest

**Networking & Security:** Kali Linux, Scapy, tcpdump, Nmap, VMware, VMnet1

**Database:** SQLite

**Testing:** Pytest

**API:** Swagger UI, OpenAPI

---

# 📁 Project Structure

```text
SentinelX/
├── ai_engine/
├── attackforge/
├── backend/
├── decision_engine/
├── explainability/
├── feature_extraction/
├── ips_engine/
├── packet_capture/
├── sensors/
├── threat_intelligence/
├── datasets/
├── database/
├── reports/
├── docs/
├── research/
├── scripts/
├── tests/
├── demo/
│   └── video/
│       ├── sentinelx-demo-landscape.mp4
│       └── sentinelx-demo-vertical.mp4
├── README.md
└── .gitignore
```

---

# 🎥 Demo

## Landscape Demo

[▶ Watch SentinelX Demo](demo/video/sentinelx-demo-landscape.mp4)

## Vertical / Mobile Demo

[▶ Watch Vertical Demo](demo/video/sentinelx-demo-vertical.mp4)

The demonstration highlights:

```text
Kali Security Lab
       ↓
Real Traffic
       ↓
Packet Capture
       ↓
ML Detection
       ↓
Alert
       ↓
Incident
       ↓
Prevention Validation
```

---

# ⚙️ Running SentinelX

## Clone the repository

```bash
git clone https://github.com/Grace1530/SentinelX.git
cd SentinelX
```

## Install dependencies

```bash
pip install -r requirements.txt
```

## Start the backend

Local development:

```bash
uvicorn backend.app.main:app --host 127.0.0.1 --port 8000 --reload
```

Swagger:

```text
http://127.0.0.1:8000/docs
```

For the isolated Kali laboratory:

```bash
uvicorn backend.app.main:app --host 192.168.83.1 --port 8000
```

## Run tests

```bash
python -m pytest
```

Expected current result:

```text
42 passed
```

## Start the Kali packet sensor

```bash
sudo python3 ~/sentinelx_sensor/sensor.py
```

## Controlled Nmap test

```bash
nmap -sS -T2 -p 1-100 192.168.83.1
```

Only perform security testing against systems and networks you own or are explicitly authorized to test.

---

# 🔬 Development & Validation Approach

```text
1. Build backend components
        ↓
2. Train and integrate ML model
        ↓
3. Add feature extraction and flow tracking
        ↓
4. Add explainability and decision logic
        ↓
5. Add alerts and incident management
        ↓
6. Add AttackForge simulation
        ↓
7. Build isolated Kali lab
        ↓
8. Capture real traffic using Scapy
        ↓
9. Feed traffic into SentinelX
        ↓
10. Validate detection and prevention
        ↓
11. Run automated regression tests
```

---

# 📌 Project Status

## Completed

- ✅ Machine-learning detection
- ✅ Flow tracking
- ✅ Feature extraction
- ✅ Explainability
- ✅ Risk and decision engine
- ✅ Alert management
- ✅ Incident management
- ✅ Incident correlation
- ✅ AttackForge
- ✅ IPS / prevention
- ✅ FastAPI backend
- ✅ Kali packet sensor
- ✅ Real-traffic validation
- ✅ Automated testing
- ✅ GitHub demo assets

## Validation

- ✅ 42 automated tests passing
- ✅ Real Kali traffic processed
- ✅ Controlled Nmap traffic tested
- ✅ Alert creation tested
- ✅ Incident correlation tested
- ✅ Prevention workflow tested

---

# ⚠️ Project Scope

SentinelX is a **student/research security engineering project** and is not presented as a replacement for enterprise IDS/IPS products.

Model behavior can vary between synthetic training traffic and real-world traffic.

Future improvements can include:

- Larger real-world datasets
- Model calibration
- Better false-positive reduction
- Additional detection techniques
- Improved threat-intelligence integration
- More advanced SOC visualization
- Production-oriented deployment

---

# 👩‍💻 Author

## Grace Angela

Computer Science student focused on cybersecurity, network security, machine learning, and practical security engineering.

SentinelX combines:

```text
Machine Learning
+
Network Security
+
Linux
+
Security Automation
+
Backend Engineering
```

---

# 🔗 Project Links

**GitHub**

https://github.com/Grace1530/SentinelX

**LinkedIn**

Add your LinkedIn profile here.

---

# ⭐ SentinelX

> **Detect. Explain. Correlate. Respond.**
