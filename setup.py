from distutils.core import setup
from distutils.command.install_scripts import install_scripts as _install_scripts
from distutils.file_util import move_file

import os

class install_scripts(_install_scripts):
    def run(self):
        _install_scripts.run(self)

        for old in self.get_outputs():
            new = os.path.splitext(old)[0]
            # move_file doesn't have a way to tell it to overwrite, so remove
            # the existing copy to accomplish the same thing.
            if os.path.isfile(new) and os.path.exists(new):
                os.unlink(new)
            move_file(old, new)

setup(cmdclass={"install_scripts": install_scripts},
      name='pykickstart', version='3.3',
      description='Python module for manipulating kickstart files',
      author='Chris Lumens', author_email='clumens@redhat.com',
      url='http://fedoraproject.org/wiki/pykickstart',
      scripts=['tools/ksvalidator.py', 'tools/ksflatten.py', 'tools/ksverdiff.py', 'tools/ksshell.py'],
      packages=['pykickstart', 'pykickstart.commands', 'pykickstart.handlers'],
      package_data={'': ['*.pyi']},
      data_files=[('share/man/man1', ['docs/ksvalidator.1', 'docs/ksflatten.1', 'docs/ksverdiff.1',
                                      'docs/ksshell.1'])])
