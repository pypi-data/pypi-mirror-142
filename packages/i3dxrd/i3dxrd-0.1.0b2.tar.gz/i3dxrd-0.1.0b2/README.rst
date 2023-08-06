Project intended to replace the ImageD11 interface, using the ImageD11 core functions.
A class Dataset is created to initialise the data and apply any needed functionalities.
All the widgets are created using silx and Qt. To define the workflow an Orange3 add-on is
implemented.

For more about ImageD11 please visit: https://i3dxrd.readthedocs.io/en/latest/

It is recommended to create a virtual environment to avoid conflicts between dependencies (https://docs.python.org/3/library/venv.html).

.. code-block:: bash

    python3 -m venv /path/to/new/virtual/environment

    source /path/to/new/virtual/environment/bin/activate

*Note: To deactivate the environment call:* :code:`deactivate`

Then, you can install darfix with all its dependencies:

.. code-block:: bash

    pip install i3dxrd[full]

To install darfix with a minimal set of dependencies run instead:

.. code-block:: bash

    pip install i3dxrd

Start the GUI and make sure darfix appears as an add-on:

.. code-block:: bash

    orange-canvas

To install from sources:
------------------------

.. code-block:: bash

    git clone https://gitlab.esrf.fr/XRD/i3dxrd.git
    cd i3dxrd
    pip install .[full]

To test the orange workflow run:

.. code-block:: bash

	orange-canvas orangecontrib/i3dxrd/tutorials/example_workflow.ows
