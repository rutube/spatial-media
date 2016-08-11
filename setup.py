from distutils.core import setup
try:
    copy("bin/spatial_media.py", "bin/spatial_media")
except (OSError, IOError):
    pass


setup(name='spatialmedia',
      version='2.1a1',
      description='Specifications and tools for 360 video and spatial audio.',
      author='Google Inc',
      license='Apache License 2.0',
      url='https://github.com/google/spatial-media',
      packages=['spatialmedia', 'spatialmedia.mpeg'],
      scripts=['bin/spatial_media']
)
