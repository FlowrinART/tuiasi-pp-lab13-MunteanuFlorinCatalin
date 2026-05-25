# html_combiner.py
"""
Combinator de fișiere HTML.
"""

import re
from pathlib import Path


def extract_body(html: str) -> str:
    body_match = re.search(
        r"<body[^>]*>(.*?)</body>",
        html,
        flags=re.IGNORECASE | re.DOTALL
    )

    if body_match:
        return body_match.group(1).strip()

    cleaned = re.sub(
        r"<head[^>]*>.*?</head>",
        "",
        html,
        flags=re.IGNORECASE | re.DOTALL
    )
    cleaned = re.sub(r"</?html[^>]*>", "", cleaned, flags=re.IGNORECASE)
    cleaned = re.sub(r"</?body[^>]*>", "", cleaned, flags=re.IGNORECASE)

    return cleaned.strip()


def build_combined_html(bodies: list[str], source_names: list[str]) -> str:
    surse = ", ".join(source_names) if source_names else "Nicio sursă"

    continut_body = "\n".join(
        f"""<section class="source-block">
<h2>Sursa: {source_names[index]}</h2>
{body}
</section>"""
        for index, body in enumerate(bodies)
    )

    return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>HTML combinat</title>
    <meta name="description" content="Fișier combinat din: {surse}">
</head>
<body>
{continut_body}
</body>
</html>
"""


def combine_files(input_paths: list[str], output_path: str) -> None:
    bodies = list(
        map(
            lambda path: extract_body(Path(path).read_text(encoding="utf-8")),
            input_paths
        )
    )

    source_names = list(map(lambda path: Path(path).name, input_paths))

    combined_html = build_combined_html(bodies, source_names)

    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    Path(output_path).write_text(combined_html, encoding="utf-8")