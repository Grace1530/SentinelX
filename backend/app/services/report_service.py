from backend.app.database.repository import repository


def create_report(
    report_type: str,
    report_format: str,
    file_path: str,
    generated_by: str = "system",
    incident_id: int | None = None,
) -> int:
    query = """
        INSERT INTO reports (
            report_type,
            format,
            file_path,
            generated_by,
            incident_id
        )
        VALUES (?, ?, ?, ?, ?)
    """

    return repository.execute(
        query,
        [
            report_type,
            report_format,
            file_path,
            generated_by,
            incident_id,
        ],
    )