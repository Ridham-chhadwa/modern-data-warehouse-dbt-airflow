from config import REPORTS_DIR


def create_quality_report(raw: dict, clean: dict) -> str:
    REPORTS_DIR.mkdir(exist_ok=True)

    lines = [
        "# Data Quality Report",
        "",
        "| Table | Raw Records | Clean Records | Removed | Raw Missing | Clean Missing | Raw Duplicates | Clean Duplicates |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]

    for table in raw:
        raw_df = raw[table]
        clean_df = clean[table]

        lines.append(
            f"| {table} | {len(raw_df)} | {len(clean_df)} | {len(raw_df) - len(clean_df)} | "
            f"{int(raw_df.isna().sum().sum())} | {int(clean_df.isna().sum().sum())} | "
            f"{int(raw_df.duplicated().sum())} | {int(clean_df.duplicated().sum())} |"
        )

    report_path = REPORTS_DIR / "data_quality_report.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")

    return str(report_path)