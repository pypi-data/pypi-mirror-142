from setuptools import find_packages, setup

setup(
    name='wagtail_colour_picker_enoki',
    version='0.3.2',
    author='Enoki-Studio',
    author_email='theo@enoki-studio.com',
    url='http://pypi.python.org/pypi/wagtail_colour_picker_enoki/',
    license='LICENSE.txt',
    description='WagtailColorPickerByEnoki',
    long_description='Wagtail colors picker with draftailJs',
    long_description_content_type='text/markdown',
    include_package_data=True,
    packages=find_packages(),
    keywords=['wagtail', 'draftjs', 'colour', 'picker', 'accent', 'design'],
)
