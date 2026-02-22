.. highlight:: shell

============
Installation
============

Follow the steps below to install ``py-ipld-dag`` on your platform.

**Linux / macOS / Windows**

1. Create a Python virtual environment:

   .. code-block:: sh

       python -m venv venv

2. Activate the virtual environment:

   - **Linux / macOS**

     .. code-block:: sh

         source venv/bin/activate

   - **Windows (cmd)**

     .. code-block:: batch

         venv\Scripts\activate.bat

   - **Windows (PowerShell)**

     .. code-block:: powershell

         venv\Scripts\Activate.ps1

3. Install ``py-ipld-dag``:

   .. code-block:: sh

       python -m pip install py-ipld-dag

Development install (from source)
---------------------------------

For a development setup (run tests, build docs, contribute), see the
:doc:`contributing` guide. Use ``uv pip install --group dev -e .`` (or
``pip install --group dev -e .`` with pip >= 25.1) after cloning the
`repository <https://github.com/ipld/py-ipld-dag>`_.
