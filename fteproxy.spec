# -*- mode: python -*-
a = Analysis(['./bin/fteproxy'],
             pathex=['.','fte'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
            )
pyz = PYZ(a.pure,
          level=9)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='fteproxy',
          debug=False,
          strip=True,
          upx=True,
          console=True)
