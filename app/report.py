def generate_report(target, result):
    report = f"Security Report for {target}\n\n"

    if "issues" in result:
        report += "Issues Found:\n"
        for issue in result["issues"]:
            report += f"- {issue}\n"
    else:
        report += "No issues found."

    return report
