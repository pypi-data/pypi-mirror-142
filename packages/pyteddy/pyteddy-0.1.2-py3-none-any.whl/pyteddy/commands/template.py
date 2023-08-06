from .. import _db

import shelve
import string
import sys

from pathlib import Path

__module__ = sys.modules[__name__]

__default__ = {'$package_name': {'__init__.py': "\n__version__ = '0.0.0'\n"}, '.gitignore': '*.pyc\n\n*.egg-info/\nbuild/\ndist/\n', 'LICENSE': 'MIT License\n\nCopyright (c) 2022 $user_name\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.', 'pyproject.toml': '[build-system]\nrequires = [\n    "setuptools>=42",\n    "wheel"\n]\nbuild-backend = "setuptools.build_meta"\n', 'README.md': '## $package_name\n', 'requirements.txt': '', 'setup.cfg': '[metadata]\nname = $package_name\nversion = attr: $package_name.__version__\nauthor = $user_name\nauthor_email = $user_email\ndescription = \nlong_description = file: README.md\nlong_description_content_type = text/markdown\nurl = \nproject_urls =\n    Bug Tracker = \nclassifiers =\n    Programming Language :: Python :: 3\n    License :: OSI Approved :: MIT License\n    Operating System :: OS Independent\n\n[options]\npackage_dir =\n    = .\npackages = find:\npython_requires = >=3.9\n\n[options.packages.find]\nwhere = .\n', 'tests': {'__init__.py': 'import unittest\nimport $package_name\n'}}


def execute(**kwargs):
    subcommand = kwargs.pop('subcommand')
    getattr(__module__, subcommand)(**kwargs)


def load(*, name, path):
    path = Path(path)
    template = template_from_path(path)
    ckwargs = {name: template}
    _db.update('template', ckwargs)


def template_from_path(path: Path):
    """
    Recursively converts a path to a dictionary by reading all the files
    example:

    test/
        LICENSE ('license text')
        .gitignore ('#gitignore body')

    converts to:
        
    {
        'test': {
            'LICENSE': 'license text',
            '.gitignore': '#gitignore body',
        }
    }
    """

    if path.is_dir():
        dct = {}
        for sub_path in path.iterdir():
            dct[sub_path.name] = template_from_path(sub_path)

        return dct
    
    with open(path, 'r') as file:
        return file.read()



def create(name, path, context):
    if name == '__default__':
        if _db.get('template').get(name) is None:
            _db.update('template', {name: __default__})
            return

    path = Path(path)
    splitted_context = split_context(context)
    true_context = _db.get('config')

    true_context.update(splitted_context)

    template = _db.get('template')[name]

    relieved_template = relieve_template(template, true_context)

    create_path_from_template(path, relieved_template)


def create_path_from_template(path, template):
    for name, content in template.items():
        sub_path = path / name
        if type(content) is dict:
            sub_path.mkdir()
            create_path_from_template(sub_path, content)
        else:
            with open(sub_path, 'w') as file:
                file.write(content)
        


def split_context(context):
    if context is None:
        return {}

    splitted_context = {}
    for unit in context:
        key, value = unit.split('=')
        splitted_context[key] = value
    
    return splitted_context


def relieve_template(template, context):
    if type(template) is dict:
        return {relieve_template(name, context): relieve_template(content, context) for name, content in template.items()}

    return string.Template(template).substitute(context)


def delete(name):
    _db.delete('template', name)
