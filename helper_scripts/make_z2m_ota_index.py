import argparse
import hashlib
import json
from pathlib import Path


BOARD_TO_MANUFACTURER_NAMES = {
    "TS0011": [
        '_TZ3000_qmi1cfuq',
        '_TZ3000_txpirhfq',
        '_TZ3000_ji4araar',
        'Tuya-TS0011-custom',
    ],
    "TS0011_END_DEVICE": [
        '_TZ3000_qmi1cfuq',
        '_TZ3000_txpirhfq',
        '_TZ3000_ji4araar',
        'Tuya-TS0011-custom',
    ],
    "TS0012": [
        '_TZ3000_jl7qyupf',
        '_TZ3000_nPGIPl5D',
        '_TZ3000_kpatq5pq',
        '_TZ3000_ljhbw1c9',
        '_TZ3000_4zf0crgo',
        'Tuya-CUSTOM',
        'Tuya-TS0012-custom',
    ],
    "TS0012_END_DEVICE": [
        '_TZ3000_jl7qyupf',
        '_TZ3000_nPGIPl5D',
        '_TZ3000_kpatq5pq',
        '_TZ3000_ljhbw1c9',
        '_TZ3000_4zf0crgo',
        'Tuya-CUSTOM',
        'Tuya-TS0012-custom',
    ],
    "TS0001": [
        '_TZ3000_skueekg3',
        'Tuya-TS0001-custom',
    ],
    "TS0002": [
        '_TZ3000_01gpyda5',
        '_TZ3000_bvrlqyj7',
        '_TZ3000_7ed9cqgi',
        '_TZ3000_zmy4lslw',
        '_TZ3000_ruxexjfz',
        '_TZ3000_4xfqlgqo',
        '_TZ3000_hojntt34',
        '_TZ3000_eei0ubpy',
        '_TZ3000_qaa59zqd',
        '_TZ3000_lmlsduws',
        '_TZ3000_lugaswf8',
        '_TZ3000_fbjdkph9',
        'Tuya-TS0002-custom',
    ],
    
}


def make_ota_index_entry(file: Path, base_url: str, board: str | None) -> dict[str, str | int]:
    data = file.read_bytes()
    res = {
        "fileName": file.name,
        "fileVersion": int.from_bytes(data[14:18], "little"),
        "fileSize": len(data),
        
        "url": f"{base_url}/{file}",
        "imageType": int.from_bytes(data[12:14], "little"),
        "manufacturerCode": int.from_bytes(data[10:12], "little"),
        "sha512": hashlib.sha512(data).hexdigest(),
        "otaHeaderString": data[20:52].decode('unicode_escape'), 
    }
    if board and board in BOARD_TO_MANUFACTURER_NAMES:
        res["manufacturerName"] = BOARD_TO_MANUFACTURER_NAMES[board]
    return res


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Zigbee2mqtt index json",
        epilog="Reads a zigbee image file and updates index.json")
    parser.add_argument("filename", metavar="INPUT", type=str, help="OTA filename")
    parser.add_argument("index_file", type=str, help="OTA index.json file")
    parser.add_argument("--base-url", required=False, help="Base url to use", 
                        default="https://github.com/romasku/tuya-zigbee-switch/raw/refs/heads/main")
    parser.add_argument("--board", required=False, help="Used to select manufacturerName list to avoid flashing wrong devices")

    args = parser.parse_args()

    entry = make_ota_index_entry(
        file=Path(args.filename),
        base_url=args.base_url,
        board=args.board,
    )
    index_file = Path(args.index_file)
    if index_file.exists():
        index_data = json.loads(index_file.read_text())
    else:
        index_data = []
    index_data = [
        it for it in index_data if
        (
            it.get("manufacturerName") != entry.get("manufacturerName")
            or it["manufacturerCode"] != entry["manufacturerCode"]    
            or it["imageType"] != entry["imageType"]
        ) 
    ]
    index_data.append(entry)
    index_file.write_text(json.dumps(
        index_data,
        indent=2,
    ))
    exit(0)