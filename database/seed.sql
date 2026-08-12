INSERT OR IGNORE INTO threat_intelligence (
    indicator,
    indicator_type,
    threat_type,
    confidence,
    source,
    description,
    mitre_technique
)
VALUES
(
    '192.0.2.10',
    'IP',
    'TEST_INDICATOR',
    1.0,
    'SENTINELX_TEST_DATA',
    'Reserved documentation/test IP.',
    NULL
);