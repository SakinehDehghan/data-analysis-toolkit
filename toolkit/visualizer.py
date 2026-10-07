\"\"\"ASCII-based lightweight visualization tools.\"\"\"

def render_ascii_bar(label, value, max_val, bar_length=25):
    ratio = (value / max_val) if max_val > 0 else 0
    filled = int(ratio * bar_length)
    bar = '█' * filled + '░' * (bar_length - filled)
    return f"{label.ljust(15)} | {bar} {value}"

def render_ascii_histogram(values, bins=5):
    if not values:
        return "No data to render."
    min_v, max_v = min(values), max(values)
    step = (max_v - min_v) / bins if max_v != min_v else 1
    counts = [0] * bins
    for v in values:
        idx = min(int((v - min_v) / step), bins - 1)
        counts[idx] += 1
    max_c = max(counts) if max(counts) > 0 else 1
    lines = []
    for i in range(bins):
        range_label = f"[{min_v + i*step:.1f} - {min_v + (i+1)*step:.1f}]"
        lines.append(render_ascii_bar(range_label, counts[i], max_c))
    return '\n'.join(lines)

def render_comparison_chart(metric_dict):
    max_val = max(metric_dict.values()) if metric_dict else 1
    output = []
    for k, v in metric_dict.items():
        output.append(render_ascii_bar(str(k), v, max_val))
    return '\n'.join(output)

def render_box_summary(name, summary):
    return f"--- {name} ---\nMin: {summary.get('min')}, Median: {summary.get('median')}, Max: {summary.get('max')}\n"
