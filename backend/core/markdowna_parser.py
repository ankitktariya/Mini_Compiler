import re

def convert_markdown_to_html(md_text):
    html_lines = []
    in_code_block = False

    for line in md_text.split('\n'):
        line = line.rstrip()

        # Code block start/end
        if line.strip().startswith("```"):
            if not in_code_block:
                html_lines.append("<pre><code>")
                in_code_block = True
            else:
                html_lines.append("</code></pre>")
                in_code_block = False
            continue

        if in_code_block:
            html_lines.append(line)
            continue

        # Blockquote
        if line.startswith("> "):
            content = line[2:].strip()
            html_lines.append(f"<blockquote>{content}</blockquote>")
            continue

        # Heading
        if line.startswith("#"):
            hashes = len(line) - len(line.lstrip('#'))
            content = line.lstrip('#').strip()
            html_lines.append(f"<h{hashes}>{content}</h{hashes}>")
            continue

        # List item
        if line.startswith("- "):
            content = line[2:].strip()
        else:
            content = line

        # 🔁 Inline Conversions (respecting user links)
        content = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", content)      # Bold
        content = re.sub(r"\*(.+?)\*", r"<em>\1</em>", content)                  # Italic
        content = re.sub(r"`(.+?)`", r"<code>\1</code>", content)                # Inline code
        content = re.sub(r"!\[(.*?)\]\((.+?)\)", r"<img src='\2' alt='\1'>", content)  # Image
        content = re.sub(r"\[(.+?)\]\((.+?)\)", r"<a href='\2'>\1</a>", content)       # Link

        if line.startswith("- "):
            html_lines.append(f"<li>{content}</li>")
        elif content:
            html_lines.append(f"<p>{content}</p>")

    # Wrap <li> inside <ul>
    final_html = []
    in_list = False
    for line in html_lines:
        if line.startswith("<li>") and not in_list:
            final_html.append("<ul>")
            in_list = True
        elif not line.startswith("<li>") and in_list:
            final_html.append("</ul>")
            in_list = False
        final_html.append(line)
    if in_list:
        final_html.append("</ul>")

    return "\n".join(final_html)
