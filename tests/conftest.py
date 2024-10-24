import yaml


def load_requirements(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)["requirements"]


requirements = load_requirements('./doc/arc42/requirements.yaml')

test_results = {}


def pytest_runtest_makereport(item, call):
    """
    Hook to capture the result of each test.
    """
    if call.when == "call":  # Nur nach der Testausführung
        outcome = call.excinfo is None  # True, wenn der Test bestanden ist
        test_results[item.nodeid] = {
            "requirement_id": getattr(item.function, "requirement_id", None),
            "outcome": "passed" if outcome else "failed",
        }


def pytest_sessionfinish(session, exitstatus):  # pragma: no cover
    """
    Generate a Traceability Report after tests finish.
    """
    tested_requirements = set()
    traceability_report = []

    # Sammle alle Testergebnisse
    for item in session.items:
        result = test_results.get(item.nodeid, {})
        req_id = result.get("requirement_id")

        if req_id:
            tested_requirements.add(req_id)
            traceability_report.append({
                "test_name": item.name,
                "requirement_id": req_id,
                "test_result": result["outcome"]
            })

    # Anforderungen, die nicht getestet wurden
    all_requirements = set(requirements.keys())
    untested_requirements = all_requirements - tested_requirements

    # Generiere Bericht
    print("\nTraceability Report:")
    print("-------------------------------------------------")
    print("Tested Requirements:")
    for req_id in tested_requirements:
        print(f"- {req_id}: {requirements[req_id]['description']}")

    print("\nUntested Requirements:")
    for req_id in untested_requirements:
        print(f"- {req_id}: {requirements[req_id]['description']}")

    # Speichere den Bericht als YAML-Datei
    report = {
        "tested_requirements": list(tested_requirements),
        "untested_requirements": list(untested_requirements),
        "traceability": traceability_report
    }
    with open("traceability_report.yaml", "w") as file:
        yaml.dump(report, file, default_flow_style=False)

    print("\nTraceability Report saved as traceability_report.yaml.")
