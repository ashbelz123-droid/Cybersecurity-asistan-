def generate_report(target, scan_result):
    report = f"""
    Security Report for {target}

    Status: {scan_result.get('status')}

    Issues:
    """

    for issue in scan_result.get("issues", []):
        report += f"- {issue}\n"

    return report
