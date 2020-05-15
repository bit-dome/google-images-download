
import gooey
gooey_root = os.path.dirname(gooey.__file__)



a = Analysis([r'google_images_download.py'],
             pathex=[r'D:\Users\bit\Desktop\Google_Image_Download\google-images-download\google_images_download'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             )
pyz = PYZ(a.pure)

options = [('u', None, 'OPTION')]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          options,        
          name='bit_google_images_downloader',
          debug=False,
          strip=None,
          upx=True,
          console=True,
          )