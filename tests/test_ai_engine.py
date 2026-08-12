from ai_engine.model_config import SUPPORTED_CLASSES


def test_supported_classes_exist():
    assert "NORMAL" in SUPPORTED_CLASSES
    assert "PORT_SCAN" in SUPPORTED_CLASSES
    assert "SSH_BRUTE_FORCE" in SUPPORTED_CLASSES
    assert "SYN_FLOOD" in SUPPORTED_CLASSES
    assert "HTTP_FLOOD" in SUPPORTED_CLASSES