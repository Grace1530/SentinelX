# SentinelX
## Software Requirements Specification (SRS)

### Project Title
**SentinelX: An Explainable AI-Based Intrusion Detection and Prevention Platform with an Integrated Cyber Attack Simulation Laboratory**

### Short Name
SentinelX

### Simulation Laboratory
AttackForge

### Version
1.0

### Document Status
Development Baseline

---

# 1. Introduction

## 1.1 Purpose

SentinelX is an AI-assisted cybersecurity platform designed to monitor
network traffic, identify suspicious and malicious network behavior,
provide explainable security alerts, support automated prevention
actions, and provide a controlled cyber attack simulation laboratory
for validating detection and response capabilities.

The platform combines network monitoring, machine learning,
explainable AI, threat intelligence, intrusion prevention,
visual analytics, incident management, and controlled attack
simulation into a unified security platform.

---

# 2. Problem Statement

Traditional network monitoring systems may generate large volumes
of security events that require manual investigation.

A basic intrusion detection system may identify suspicious traffic
but provide limited explanation about why the traffic was considered
malicious.

In addition, detection systems are difficult to demonstrate and
validate without a controlled environment capable of generating
known attack scenarios.

SentinelX addresses these challenges by combining:

- Network traffic monitoring
- Machine-learning-based detection
- Explainable security alerts
- Threat intelligence
- Automated prevention
- Security visualization
- Controlled attack simulation

The integrated AttackForge laboratory allows SentinelX to be
validated using authorized attack scenarios inside an isolated
environment.

---

# 3. Objectives

The primary objectives of SentinelX are:

1. Capture and monitor network traffic in real time.

2. Extract meaningful network features from captured traffic.

3. Detect supported malicious network behaviors using machine
   learning and rule-based analysis.

4. Provide confidence scores for machine-learning predictions.

5. Explain the major factors contributing to security detections.

6. Assign appropriate threat severity levels.

7. Generate security alerts and maintain an incident history.

8. Compare relevant indicators against configured threat
   intelligence information.

9. Automatically block selected malicious source IP addresses
   through the configured firewall.

10. Maintain configurable IP whitelists and blacklists.

11. Provide a professional SOC-style security dashboard.

12. Provide packet and alert investigation capabilities.

13. Provide controlled attack simulations through AttackForge.

14. Generate security reports in PDF, CSV, and JSON formats.

15. Maintain auditable records of detections and prevention actions.

16. Provide a reproducible platform suitable for academic research,
    demonstration, and cybersecurity learning.

---

# 4. Scope

## 4.1 Included in Version 1.0

SentinelX Version 1.0 includes:

- Live packet capture
- Packet parsing
- Network feature extraction
- Machine-learning-based traffic classification
- Supported attack detection
- Explainable AI output
- Threat severity assessment
- Threat intelligence lookup
- IP blacklist
- IP whitelist
- Automated IP blocking
- Firewall integration
- Security alerts
- Incident timeline
- SOC dashboard
- Packet inspection
- AttackForge simulation laboratory
- Security reports
- Persistent event logging
- Automated testing
- Technical documentation

---

# 5. Supported Detection Categories

Version 1.0 will focus on a defined and testable set of behaviors.

## 5.1 Normal Traffic

Traffic that does not meet the configured malicious
behavior criteria.

## 5.2 Port Scanning

Detection of repeated connection attempts against multiple
ports or hosts within a defined time window.

## 5.3 DoS / SYN Flood Behavior

Detection of abnormal volumes of connection requests or
SYN-related traffic patterns under controlled laboratory
conditions.

## 5.4 SSH Brute Force Behavior

Detection of repeated SSH authentication attempts when
corresponding traffic/log evidence is available.

## 5.5 Botnet-like / Anomalous Traffic

Detection of supported anomalous traffic patterns using
the selected dataset and feature representation.

> Note: SentinelX will only claim detection capabilities that
> are experimentally validated. Attack categories will not be
> advertised as universally detectable.

---

# 6. System Users

## 6.1 Security Analyst

Can:

- Monitor network activity
- Review alerts
- Investigate packets
- Analyze incidents
- Review threat intelligence
- Generate reports
- Review prevention actions

## 6.2 Administrator

Can:

- Configure the platform
- Manage trusted IPs
- Manage blocked IPs
- Configure detection settings
- Configure response policies

## 6.3 Student / Researcher

Can:

- Run controlled AttackForge scenarios
- Observe network behavior
- Analyze detections
- Compare model performance
- Review explanations
- Generate experimental reports

---

# 7. System Architecture

The logical processing pipeline shall be:

Network Traffic
        |
        v
Packet Capture Engine
        |
        v
Packet Parser
        |
        v
Feature Extraction Engine
        |
        v
AI Detection Engine
        |
        +--------------------+
        |                    |
        v                    v
Explainability        Threat Intelligence
        |                    |
        +---------+----------+
                  |
                  v
            Decision Engine
                  |
          +-------+-------+
          |               |
          v               v
        Alert             IPS
          |               |
          |               v
          |          Firewall Action
          |               |
          +-------+-------+
                  |
                  v
             Database
                  |
                  v
            SOC Dashboard
                  |
                  v
              Reports

AttackForge
     |
     v
Controlled Lab Traffic
     |
     v
Packet Capture Engine