from explainability.explainer import Explainer


def test_port_scan_explanation():
    explainer = Explainer()

    factors = explainer.explain(
        "PORT_SCAN",
        {
            "destination_port": 80,
            "tcp_syn": 1,
        },
    )

    assert len(factors) > 0