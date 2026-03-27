from __future__ import annotations

import json
import sys
from pathlib import Path

# Petit contournement utile dans certains environnements où torchvision
# pose un problème au chargement. Il est sans effet si tout fonctionne.
try:
    import torch.library

    _orig_register_fake = torch.library.register_fake

    def _safe_register_fake(opname):
        def decorator(func):
            try:
                return _orig_register_fake(opname)(func)
            except RuntimeError:
                return func
        return decorator

    torch.library.register_fake = _safe_register_fake
except Exception:
    pass

from ultralytics import YOLO


def results_to_json(results, output_json: Path) -> None:
    result = results[0]
    names = result.names
    boxes = result.boxes

    detections: list[dict] = []
    for i in range(len(boxes)):
        cls_id = int(boxes.cls[i].item())
        conf = float(boxes.conf[i].item())
        x1, y1, x2, y2 = [float(v) for v in boxes.xyxy[i].tolist()]

        detections.append(
            {
                'class_id': cls_id,
                'class_name': names[cls_id],
                'confidence': round(conf, 4),
                'bbox_xyxy': {
                    'x1': round(x1, 2),
                    'y1': round(y1, 2),
                    'x2': round(x2, 2),
                    'y2': round(y2, 2),
                },
            }
        )

    payload = {
        'source_image': str(result.path),
        'num_detections': len(detections),
        'detections': detections,
    }

    output_json.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding='utf-8')


def main() -> int:
    if len(sys.argv) != 2:
        print('Usage: python detect_yolo.py <image>')
        return 1

    image_path = Path(sys.argv[1])
    if not image_path.exists():
        print(f'Image introuvable : {image_path}')
        return 1

    try:
        model = YOLO('yolov8n.pt')
        results = model.predict(
            source=str(image_path),
            save=True,
            project='runs/detect',
            name='predict',
            exist_ok=True,
            verbose=False,
        )

        save_dir = Path(results[0].save_dir)
        output_json = save_dir / 'detections.json'
        results_to_json(results, output_json)

        print(f'Image annotée : {save_dir / image_path.name}')
        print(f'JSON généré   : {output_json}')
        return 0
    except Exception as exc:
        print(f'Erreur YOLO : {exc}')
        print("Astuce : vérifie que 'ultralytics' est installé et que le modèle yolov8n.pt peut être téléchargé.")
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
