#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Flow Overview 다이어그램 교체 스크립트

사용법:
    python3 update_diagram.py 새로운다이어그램.svg

새로 만든 SVG 파일을 지정하면, 웹페이지 폴더의 Flow_Overview.svg를
덮어써서 자동으로 화면에 반영됩니다. (별도 코드 수정 필요 없음)

같은 폴더에서 실행하는 걸 기본으로 하며, 다른 경로에 있는 폴더를
지정하고 싶으면 두 번째 인자로 대상 폴더 경로를 넘기면 됩니다.

예:
    python3 update_diagram.py ~/Downloads/새로운다이어그램.svg
    python3 update_diagram.py ~/Downloads/새로운다이어그램.svg /path/to/webpage/folder
"""

import sys
import shutil
from pathlib import Path

TARGET_FILENAME = "Flow_Overview.svg"

def main():
    if len(sys.argv) < 2:
        print("사용법: python3 update_diagram.py <새로운 SVG 파일 경로> [웹페이지 폴더 경로]")
        sys.exit(1)

    src = Path(sys.argv[1]).expanduser().resolve()
    dest_dir = Path(sys.argv[2]).expanduser().resolve() if len(sys.argv) >= 3 else Path(__file__).parent.resolve()
    dest = dest_dir / TARGET_FILENAME

    if not src.exists():
        print(f"[오류] 원본 파일을 찾을 수 없습니다: {src}")
        sys.exit(1)

    if src.suffix.lower() != ".svg":
        print(f"[경고] SVG 파일이 아닌 것 같습니다: {src.name} (계속 진행합니다)")

    if not dest_dir.exists():
        print(f"[오류] 대상 폴더가 존재하지 않습니다: {dest_dir}")
        sys.exit(1)

    shutil.copyfile(src, dest)
    print(f"완료: {src.name} -> {dest}")
    print("브라우저에서 새로고침(캐시 강제 새로고침 Ctrl+Shift+R 권장)하면 바로 반영됩니다.")

if __name__ == "__main__":
    main()
