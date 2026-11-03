"""Reproduce the exact R3 DLL from an existing official 0.2.0 DLL.

No downloads, game discovery, installation, process access, or system changes.
This writes only the explicitly named NEW output file. Python 3 standard library.
"""
from pathlib import Path
import argparse
import hashlib
import json


def patched_bytes(source, recipe):
    digest = hashlib.sha256(source).hexdigest().upper()
    if digest != recipe['source_sha256']:
        raise ValueError('Wrong input DLL version/hash; no output written')
    output = bytearray(source)
    used = set()
    for change in recipe['changes']:
        offset = change['offset']
        old, new = bytes.fromhex(change['old']), bytes.fromhex(change['new'])
        if offset < 0 or len(old) != len(new) or offset + len(old) > len(source):
            raise ValueError('Invalid patch bounds')
        if source[offset:offset + len(old)] != old:
            raise ValueError('Original bytes do not match patch recipe')
        positions = set(range(offset, offset + len(old)))
        if used.intersection(positions):
            raise ValueError('Overlapping patch ranges')
        used.update(positions)
        output[offset:offset + len(new)] = new
    if hashlib.sha256(output).hexdigest().upper() != recipe['patched_sha256']:
        raise ValueError('Patched DLL hash mismatch; no output written')
    return bytes(output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('input', type=Path)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.input.resolve() == args.output.resolve() or args.output.exists():
        parser.error('Output must be a new file, separate from the input')
    recipe = json.loads((Path(__file__).parent / 'core-port-manifest.json').read_text())
    result = patched_bytes(args.input.read_bytes(), recipe)
    with args.output.open('xb') as stream:
        stream.write(result)
    print('Created verified R3 DLL:', args.output)
