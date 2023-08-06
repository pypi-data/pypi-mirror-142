# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['thag', 'thag.runners']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'thag',
    'version': '0.0.2',
    'description': 'GUI toolkit for building GUI toolkits (and create beautiful applications for mobile, web, and desktop from a single python3 codebase)',
    'long_description': '# THAG : "[T]he [H]TML [A]ttributs [G]UI"\n\nThe descendant of [gtag](https://github.com/manatlan/gtag) ... but :\n\n * Not tied to [guy](https://github.com/manatlan/guy)\n * Able to be used in anything which can display html/js/css (pywebview, cefpython3, a browser, ....)\n * A lot lot lot better and simpler (better abstractions/code/concepts)\n * "intelligent rendering" (redraw only component with states changes)\n\nIt\'s a GUI toolkit for building GUI toolkits ;-)\n\n[Changelog](changelog.md)\n\n**Thag** provides somes [`runners`](thag/runners) ootb. But they are here just for the show. IRL, you should build your own, for your needs.\n\n## In French\nSorte de FWK (orienté composants), où on code (coté backend) des objets python (en fait des objets "Tag"), qui ont une representation HTML avec des interactions, qui peuvent s\'executer dans tout ce qui est capable d\'afficher du html/js/css (pywebview, cefpython3, a browser, ....)\n\nLes "interactions" sont des actions émanants de la partie front vers le back, pour synchroniser l\'état de l\'objet (côté back), et retourner sa nouvelle représentation front.\nLa nature de ces interactions dépendent du `runner` utilisé (browser>ajax|websocket, guy>Websocket, pywebview>inproc)\n\nLe fwk permet surtout de fabriquer ses composants ... et il faudrait utiliser ces composants dans une appli.\n\nAutant le fwk permet des interactions avec js/front ... autant, il ne faudrait pas en faire dans les composants finaux : l\'idée, c\'est d\'abstraire toutes interactions js : de manière à ce que ça soit totallement transparent dans les composants finaux.\n\n',
    'author': 'manatlan',
    'author_email': 'manatlan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/manatlan/thag',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
