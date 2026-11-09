@echo off
rem Builds dist\Bound.exe (single-file installer + launcher).
rem Requires Python 3 with pyinstaller and pillow, and the payload\ folder (see README).
cd /d "%~dp0" || exit /b 1
if not exist payload\emulator\shadPS4.exe ( echo Missing payload\emulator\shadPS4.exe & exit /b 1 )
if not exist payload\extractor\pkg_extractor.exe ( echo Missing payload\extractor\pkg_extractor.exe & exit /b 1 )
python make_icon.py assets\app.ico || exit /b 1
python -m PyInstaller --noconfirm --clean --onefile --windowed --name Bound ^
  --icon assets\app.ico ^
  --add-data "assets;assets" ^
  --add-data "payload;payload" ^
  --hidden-import PIL.Image ^
  bound_pc.py || exit /b 1
echo BUILD OK: %~dp0dist\Bound.exe
