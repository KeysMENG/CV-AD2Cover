# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_all

datas = []
binaries = []
hiddenimports = []
hiddenimports += [
    'docx',
    'docx.api',
    'docx.opc',
    'docx.oxml',
    'docx.parts',
    'docx.parts.document',
    'docx.parts.numbering',
    'docx.parts.styles',
    'docx.parts.settings',
    'docx.parts.coreprops',
    'docx.parts.image',
    'docx.parts.header',
    'docx.parts.footer',
    'docx.parts.footnotes',
    'docx.parts.endnotes',
    'docx.parts.comments',
    'docx.parts.fonttable',
    'docx.parts.websettings',
    'docx.parts.theme',
    'docx.parts.customprops',
    'docx.parts.customxml',
    'docx.parts.styleswitheffects'
]
# 收集 streamlit 依赖
tmp_ret = collect_all('streamlit')
datas += tmp_ret[0]; binaries += tmp_ret[1]; hiddenimports += tmp_ret[2]

# 收集 python-docx 依赖
docx_ret = collect_all('docx')
datas += docx_ret[0]; binaries += docx_ret[1]; hiddenimports += docx_ret[2]

a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
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
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
