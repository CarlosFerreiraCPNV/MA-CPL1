from __future__ import annotations

import mimetypes
import sys
from email import policy
from email.parser import BytesParser
from pathlib import Path


def is_image(part) -> bool:
    content_type = part.get_content_type()
    if content_type.startswith('image/'):
        return True
    filename = part.get_filename()
    if filename:
        guessed, _ = mimetypes.guess_type(filename)
        return bool(guessed and guessed.startswith('image/'))
    return False


def extract_first_image(eml_path: Path, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)

    with eml_path.open('rb') as f:
        msg = BytesParser(policy=policy.default).parse(f)

    for part in msg.iter_attachments():
        if not is_image(part):
            continue

        filename = part.get_filename() or 'image_attachment'
        ext = Path(filename).suffix or '.jpg'
        safe_name = Path(filename).stem.replace(' ', '_') + ext
        out_path = output_dir / safe_name
        out_path.write_bytes(part.get_payload(decode=True))
        return out_path

    raise FileNotFoundError('Aucune pièce jointe image trouvée dans le fichier .eml.')


def main() -> int:
    if len(sys.argv) != 2:
        print('Usage: python extract_attachment.py <mail.eml>')
        return 1

    eml_path = Path(sys.argv[1])
    if not eml_path.exists():
        print(f'Fichier introuvable : {eml_path}')
        return 1

    try:
        saved = extract_first_image(eml_path, Path('attachments'))
        print(f'Image extraite : {saved}')
        return 0
    except Exception as exc:
        print(f'Erreur : {exc}')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
