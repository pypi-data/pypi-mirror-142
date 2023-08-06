# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pypme']

package_data = \
{'': ['*']}

install_requires = \
['numpy-financial>=1.0.0,<2.0.0', 'pandas>=1.4.1,<2.0.0', 'xirr>=0.1.8,<0.2.0']

setup_kwargs = {
    'name': 'pypme',
    'version': '0.1.2',
    'description': 'Python library for PME (Public Market Equivalent) calculation',
    'long_description': "# pypme – Python library for PME (Public Market Equivalent) calculation\n\nBased on the [Modified PME\nmethod](https://en.wikipedia.org/wiki/Public_Market_Equivalent#Modified_PME).\n\n## Example\n\n```python\nfrom pypme import verbose_xpme\nfrom datetime import date\n\npmeirr, assetirr, df = verbose_xpme(\n    dates=[date(2015, 1, 1), date(2015, 6, 12), date(2016, 2, 15)],\n    cashflows=[-10000, 7500],\n    prices=[100, 120, 100],\n    pme_prices=[100, 150, 100],\n)\n```\n\nWill return `0.5525698793027238` and  `0.19495150355969598` for the IRRs and produce this\ndataframe:\n\n![Example dataframe](images/example_df.png)\n\nNotes:\n- The `cashflows` are interpreted from a transaction account that is used to buy from an\n  asset at price `prices`.\n- The corresponding prices for the PME are `pme_prices`.\n- The `cashflows` is extended with one element representing the remaining value, that's\n  why all the other lists (`dates`, `prices`, `pme_prices`) need to be exactly 1 element\n  longer than `cashflows`.\n\n## Variants\n\n- `xpme`: Calculate PME for unevenly spaced / scheduled cashflows and return the PME IRR\n  only. In this case, the IRR is always annual.\n- `verbose_xpme`: Calculate PME for unevenly spaced / scheduled cashflows and return\n  vebose information.\n- `pme`: Calculate PME for evenly spaced cashflows and return the PME IRR only. In this\n  case, the IRR is for the underlying period.\n- `verbose_pme`: Calculate PME for evenly spaced cashflows and return vebose\n  information.\n\n## Garbage in, garbage out\n\nNote that the library will only perform essential sanity checks and otherwise just works\nwith what it gets, also with nonsensical data. E.g.:\n\n```python\nfrom pypme import verbose_pme\n\npmeirr, assetirr, df = verbose_pme(\n    cashflows=[-10, 500], prices=[1, 1, 1], pme_prices=[1, 1, 1]\n)\n```\n\nResults in this df and IRRs of 0:\n\n![Garbage example df](images/garbage_example_df.png)\n\n## References\n\n- [Google Sheet w/ reference calculation](https://docs.google.com/spreadsheets/d/1LMSBU19oWx8jw1nGoChfimY5asUA4q6Vzh7jRZ_7_HE/edit#gid=0)\n- [Modified PME on Wikipedia](https://en.wikipedia.org/wiki/Public_Market_Equivalent#Modified_PME)\n",
    'author': 'ymyke',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ymyke/pypme',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<3.10',
}


setup(**setup_kwargs)
