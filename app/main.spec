# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

import os
import mtcnn
import cv2

datas = [
  (os.path.join(os.path.dirname(mtcnn.__file__), 'data/mtcnn_weights.npy'), 'mtcnn/data/'),
  (os.path.join(os.path.dirname(cv2.__file__), 'data/*'), 'cv2/data/')
]

a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=datas,
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
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
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None )
