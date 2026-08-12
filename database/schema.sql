PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS packets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME NOT NULL,
    source_ip TEXT,
    destination_ip TEXT,
    source_port INTEGER,
    destination_port INTEGER,
    protocol TEXT,
    packet_length INTEGER,
    tcp_flags TEXT,
    ttl INTEGER,
    interface TEXT,
    flow_id TEXT
);

CREATE INDEX IF NOT EXISTS idx_packets_timestamp
ON packets(timestamp);

CREATE INDEX IF NOT EXISTS idx_packets_source_ip
ON packets(source_ip);

CREATE INDEX IF NOT EXISTS idx_packets_destination_ip
ON packets(destination_ip);

CREATE INDEX IF NOT EXISTS idx_packets_flow_id
ON packets(flow_id);


CREATE TABLE IF NOT EXISTS threats (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    indicator TEXT NOT NULL,
    indicator_type TEXT NOT NULL,
    threat_type TEXT,
    severity TEXT,
    source TEXT,
    description TEXT,
    mitre_technique TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_threats_indicator
ON threats(indicator);


CREATE TABLE IF NOT EXISTS alerts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME NOT NULL,
    source_ip TEXT,
    destination_ip TEXT,
    source_port INTEGER,
    destination_port INTEGER,
    protocol TEXT,
    detection_type TEXT NOT NULL,
    severity TEXT NOT NULL,
    confidence REAL,
    risk_score REAL,
    explanation TEXT,
    mitre_technique TEXT,
    status TEXT DEFAULT 'OPEN',
    packet_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (packet_id)
        REFERENCES packets(id)
        ON DELETE SET NULL
);

CREATE INDEX IF NOT EXISTS idx_alerts_timestamp
ON alerts(timestamp);

CREATE INDEX IF NOT EXISTS idx_alerts_source_ip
ON alerts(source_ip);

CREATE INDEX IF NOT EXISTS idx_alerts_detection_type
ON alerts(detection_type);

CREATE INDEX IF NOT EXISTS idx_alerts_severity
ON alerts(severity);

CREATE INDEX IF NOT EXISTS idx_alerts_status
ON alerts(status);


CREATE TABLE IF NOT EXISTS incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    incident_id TEXT UNIQUE,
    title TEXT NOT NULL,
    attack_type TEXT,
    severity TEXT,
    source_ip TEXT,
    status TEXT DEFAULT 'OPEN',
    first_seen DATETIME,
    last_seen DATETIME,
    alert_count INTEGER DEFAULT 0,
    resolution TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE IF NOT EXISTS blocked_ips (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ip_address TEXT UNIQUE NOT NULL,
    reason TEXT,
    detection_type TEXT,
    severity TEXT,
    blocked_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    expires_at DATETIME,
    firewall TEXT,
    active BOOLEAN DEFAULT 1
);

CREATE INDEX IF NOT EXISTS idx_blocked_ips_address
ON blocked_ips(ip_address);


CREATE TABLE IF NOT EXISTS attack_simulations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    scenario TEXT NOT NULL,
    target TEXT NOT NULL,
    start_time DATETIME,
    end_time DATETIME,
    status TEXT,
    expected_detection TEXT,
    actual_detection TEXT,
    detected BOOLEAN,
    confidence REAL,
    severity TEXT,
    response TEXT,
    result TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_simulations_scenario
ON attack_simulations(scenario);

CREATE INDEX IF NOT EXISTS idx_simulations_start_time
ON attack_simulations(start_time);


CREATE TABLE IF NOT EXISTS threat_intelligence (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    indicator TEXT NOT NULL,
    indicator_type TEXT,
    threat_type TEXT,
    confidence REAL,
    source TEXT,
    first_seen DATETIME,
    last_seen DATETIME,
    description TEXT,
    mitre_technique TEXT
);

CREATE INDEX IF NOT EXISTS idx_threat_intelligence_indicator
ON threat_intelligence(indicator);


CREATE TABLE IF NOT EXISTS system_events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp DATETIME NOT NULL,
    event_type TEXT,
    severity TEXT,
    component TEXT,
    message TEXT,
    details TEXT
);


CREATE TABLE IF NOT EXISTS reports (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    report_type TEXT,
    format TEXT,
    file_path TEXT,
    generated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    generated_by TEXT,
    incident_id INTEGER,

    FOREIGN KEY (incident_id)
        REFERENCES incidents(id)
        ON DELETE SET NULL
);