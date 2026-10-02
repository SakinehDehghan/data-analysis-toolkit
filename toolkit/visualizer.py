\"\"\"ASCII-based lightweight visualization tools.\"\"\"

def render_ascii_bar(label, value, max_val, bar_length=25):
    ratio = (value / max_val) if max_val > 0 else 0
    filled = int(ratio * bar_length)
    bar = '█' * filled + '░' * (bar_length - filled)
    return f"{label.ljust(15)} | {bar} {value}"
