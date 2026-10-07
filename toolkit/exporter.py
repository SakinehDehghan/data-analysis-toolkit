\"\"\"Report generation in Markdown and JSON.\"\"\"
import json
import os

def export_markdown_report(title, summaries, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    lines = [f"# {title}", "", "## Summary Statistics", ""]
    lines.append("| Metric | Count | Min | Max | Mean | Median | Std |")
    lines.append("|---|---|---|---|---|---|---|")
    for name, s in summaries.items():
        lines.append(f"| {name} | {s.get('count')} | {s.get('min')} | {s.get('max')} | {s.get('mean')} | {s.get('median')} | {s.get('std')} |")
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    return output_path

def export_json_report(data, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
    return output_path
