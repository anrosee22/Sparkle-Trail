# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['toggle_trail.py'],
    pathex=[],
    binaries=[],
    datas=[('sparkle_trail.py', '.'), ('sparkle_pink.png', '.'), ('sparkle_mint.png', '.'), ('sparkle_lilac.png', '.'), ('sparkle_yellow.png', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='toggle_trail',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['sparkle.ico'],
)
