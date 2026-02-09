name: Build EXE

on: [push]

jobs:
  build:
    runs-on: windows-latest

    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.x'

      - name: Install dependencies
        run: pip install pyinstaller

      - name: Build EXE
        run: pyinstaller --onefile script.py

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: exe-file
          path: dist/*.exe
