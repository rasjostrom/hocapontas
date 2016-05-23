Installation
------------
At the command line:

``pip install hocapontas``

Or clone the repo at
`GitHub <https://github.com/rasjostrom/hocapontas.git>`_ and check the
requirements.txt file.


Requirements
~~~~~~~~~~~~

hocapontas relies on the `DBC <https://en.wikipedia.org/wiki/Design_by_contract>`_ library `PyContracts <https://pypi.python.org/pypi/PyContracts>`_ to enforce parameter types and return values based on doc string
properties like ``:type parameter: int`` or ``:rtype: dict`` (which
means free type checking just by documentating your code).
