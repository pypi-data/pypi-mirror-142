# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pydoc_markdown',
 'pydoc_markdown.contrib',
 'pydoc_markdown.contrib.loaders',
 'pydoc_markdown.contrib.processors',
 'pydoc_markdown.contrib.renderers',
 'pydoc_markdown.contrib.source_linkers',
 'pydoc_markdown.novella',
 'pydoc_markdown.util']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.3,<6.0',
 'click>=7.1,<9.0',
 'databind>=1.5.0,<2.0.0',
 'docspec-python>=2.0.0a1,<3.0.0',
 'docspec>=2.0.0a1,<3.0.0',
 'docstring-parser>=0.11,<0.12',
 'jinja2>=3.0.0,<4.0.0',
 'nr.util>=0.7.5,<1.0.0',
 'requests>=2.23.0,<3.0.0',
 'tomli>=2.0.0,<3.0.0',
 'tomli_w>=1.0.0,<2.0.0',
 'watchdog',
 'yapf>=0.30.0']

entry_points = \
{'console_scripts': ['pydoc-markdown = pydoc_markdown.main:cli'],
 'novella.markdown.preprocessors': ['pydoc = '
                                    'pydoc_markdown.novella.preprocessor:PydocTagPreprocessor'],
 'pydoc_markdown.interfaces.Loader': ['python = '
                                      'pydoc_markdown.contrib.loaders.python:PythonLoader'],
 'pydoc_markdown.interfaces.Processor': ['crossref = '
                                         'pydoc_markdown.contrib.processors.crossref:CrossrefProcessor',
                                         'filter = '
                                         'pydoc_markdown.contrib.processors.filter:FilterProcessor',
                                         'google = '
                                         'pydoc_markdown.contrib.processors.google:GoogleProcessor',
                                         'pydocmd = '
                                         'pydoc_markdown.contrib.processors.pydocmd:PydocmdProcessor',
                                         'smart = '
                                         'pydoc_markdown.contrib.processors.smart:SmartProcessor',
                                         'sphinx = '
                                         'pydoc_markdown.contrib.processors.sphinx:SphinxProcessor'],
 'pydoc_markdown.interfaces.Renderer': ['docusaurus = '
                                        'pydoc_markdown.contrib.renderers.docusaurus:DocusaurusRenderer',
                                        'hugo = '
                                        'pydoc_markdown.contrib.renderers.hugo:HugoRenderer',
                                        'jinja2 = '
                                        'pydoc_markdown.contrib.renderers.jinja2:Jinja2Renderer',
                                        'markdown = '
                                        'pydoc_markdown.contrib.renderers.markdown:MarkdownRenderer',
                                        'mkdocs = '
                                        'pydoc_markdown.contrib.renderers.mkdocs:MkdocsRenderer'],
 'pydoc_markdown.interfaces.SourceLinker': ['bitbucket = '
                                            'pydoc_markdown.contrib.source_linkers.git:BitbucketSourceLinker',
                                            'git = '
                                            'pydoc_markdown.contrib.source_linkers.git:GitSourceLinker',
                                            'gitea = '
                                            'pydoc_markdown.contrib.source_linkers.git:GiteaSourceLinker',
                                            'github = '
                                            'pydoc_markdown.contrib.source_linkers.git:GithubSourceLinker',
                                            'gitlab = '
                                            'pydoc_markdown.contrib.source_linkers.git:GitlabSourceLinker']}

setup_kwargs = {
    'name': 'pydoc-markdown',
    'version': '4.6.3',
    'description': 'Create Python API documentation in Markdown format.',
    'long_description': '# Pydoc-Markdown\n\n![Python versions](https://img.shields.io/pypi/pyversions/pydoc-markdown?style=for-the-badge)\n[![Pypi version](https://img.shields.io/pypi/v/pydoc-markdown?style=for-the-badge)](https://pypi.org/project/pydoc-markdown/)\n[![Build status](https://img.shields.io/github/workflow/status/NiklasRosenstein/pydoc-markdown/Python%20package?style=for-the-badge)](https://github.com/NiklasRosenstein/pydoc-markdown/actions)\n[![Gitter chat](https://img.shields.io/badge/Chat-On%20Gitter-%2386f4e4?style=for-the-badge)](https://gitter.im/NiklasRosenstein/pydoc-markdown)\n\nPydoc-Markdown is a tool to create Python API documentation in Markdown format. Instead of executing your Python\ncode like so many other documentation tools, it parses it using [docspec][] instead. To run Pydoc-Markdown, you\nneed to use at least Python 3.7.\n\n[>> Go to the Documentation][Documentation]\n\n  [contrib]: https://github.com/NiklasRosenstein/pydoc-markdown/blob/develop/.github/CONTRIBUTING.md\n  [docspec]: https://niklasrosenstein.github.io/docspec/\n  [Documentation]: https://niklasrosenstein.github.io/pydoc-markdown/\n  [MkDocs]: https://www.mkdocs.org/\n  [Novella]: https://niklasrosenstein.github.io/novella/\n  [Novella build backend]: https://niklasrosenstein.github.io/pydoc-markdown/usage/novella/\n\n### Installation\n\nI recommend to install Pydoc-Markdown using Pipx.\n\n    $ pipx install pydoc-markdown[novella]\n\n### Features\n\n* Understands multiple documentation styles (Sphinx, Google, Pydoc-Markdown specific) and converts them to properly\n  formatted Markdown\n* Can parse docstrings for variables thanks to [docspec][] (`#:` block before or string literal after the statement)\n* Generates links to other API objects per the documentation syntax (e.g. `#OtherClass` for the Pydoc-Markdown style)\n\n### News\n\nStarting with __4.6.0__, development focuses on integrating with [Novella][] and use it as a replacement for\ntool-specific renderers thus far provided directly by Pydoc-Markdown (i.e. integrations with MkDocs, Hugo and\nDocusuraus). Such integrations are/will be provided by Novella instead.\n\nWith the Novella integration, you can now place generated API content in Markdown format inline with your\nexisting Markdown documentation source files using `@pydoc` tags. Check out the [Documentation][] for more\ninformation on how to use Pydoc-Markdown with Novella.\n\nThe old style of using Pydoc-Markdown with a YAML or PyProject configuration to generate files and kick off the\nbuild is now deprecated but will be maintained for the foreseeable future (at least until the next major version\nbump). It is strongly recommended to migrate your existing projects to using the Novella build backend.\n\n### Contributing to Pydoc-Markdown\n\nAll contributions are welcome! Check out the [Contribution Guidelines][contrib].\n\n### Questions / Need help?\n\nFeel free to open a topic on [GitHub Discussions](https://github.com/NiklasRosenstein/pydoc-markdown/discussions)!\n',
    'author': 'Niklas Rosenstein',
    'author_email': 'rosensteinniklas@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
