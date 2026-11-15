"""Run without network access or third-party packages."""
import ast
from html.parser import HTMLParser
from pathlib import Path

source = (Path(__file__).parent / 'verify_network.py').read_text()
parser = next(node for node in ast.parse(source).body if isinstance(node, ast.ClassDef) and node.name == 'Document')
namespace = {'HTMLParser': HTMLParser}
exec(compile(ast.Module(body=[parser], type_ignores=[]), '<document-parser>', 'exec'), namespace)
Document = namespace['Document']
cases = [
    ('page title ignores SVG chart and point titles', '<html><head><title>Expected page title</title></head><body><svg><title>Chart</title><circle><title>Point</title></circle></svg></body></html>', 'Expected page title'),
    ('page title decodes character references', '<html><head><title>A &amp; B</title></head><body><svg><title>Chart</title></svg></body></html>', 'A & B'),
    ('SVG title cannot substitute for a missing page title', '<html><head></head><body><svg><title>Chart only</title></svg></body></html>', ''),
]
for label, html, expected in cases:
    assert Document(html).title == expected, label
    print('PASS ' + label)
print(str(len(cases)) + ' verifier parser tests passed')
