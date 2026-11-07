#!/usr/bin/env python3
"""Phase 8 source-to-PDF preflight. Verifies structure and readability, not novelty."""
from pathlib import Path
from hashlib import sha256
import json
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
PAIRS = [
    ('manuscript', 'Absolute_Luck_Phase6_Manuscript', 10, 5),
    ('essay', 'Absolute_Luck_Phase7_Essay', 5, 5),
]
results = {}
for folder, stem, expected_pages, expected_figures in PAIRS:
    directory = ROOT / folder
    source = directory / (stem + '.tex')
    pdf = directory / (stem + '.pdf')
    assert source.is_file() and pdf.is_file(), (source, pdf)
    latex = source.read_text(encoding='utf8')
    refs = re.findall(r'\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}', latex)
    assert len(refs) == expected_figures, (folder, refs)
    for ref in refs:
        fig = (directory / ref)
        assert fig.is_file() and fig.stat().st_size > 500, fig
        assert (fig.parent / (fig.stem + '.svg')).is_file(), fig
        assert (fig.parent / (fig.stem + '.png')).is_file(), fig
    assert pdf.stat().st_size > 100_000, (folder, pdf.stat().st_size)
    info = subprocess.check_output(['pdfinfo', str(pdf)], text=True)
    m = re.search(r'^Pages:\s+(\d+)', info, re.M)
    assert m and int(m.group(1)) == expected_pages, (folder, m and m.group(1))
    rendered_text = subprocess.check_output(['pdftotext', str(pdf), '-'], text=True)
    for term in ['Absolute Luck', 'probability', '200']:
        assert term.lower() in rendered_text.lower(), (folder, term)
    # Verifies PDF isn't an image-only/blank artifact.
    assert len(rendered_text.strip()) > 3000, (folder, len(rendered_text))
    results[folder] = {
        'pages': expected_pages,
        'figure_references_resolved': len(refs),
        'pdf_sha256': sha256(pdf.read_bytes()).hexdigest(),
        'pdf_bytes': pdf.stat().st_size,
        'extractable_text_characters': len(rendered_text),
    }
print(json.dumps({'status': 'PASS', 'checks': results, 'scope': 'technical PDF/source reproducibility; not external peer review'}, indent=2))
