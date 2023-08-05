OPICS Quickstart
================

Installing OPICS
----------------

Installing from pypi
~~~~~~~~~~~~~~~~~~~~

The easiest way to install OPICS is using pip pypi:

.. code:: console


   pip install opics

Installing from source
~~~~~~~~~~~~~~~~~~~~~~

Download the OPICS source code.

.. code:: console


   git clone https://github.com/jaspreetj/opics

Install the OPICS package using ``pip``.

.. code:: console


   pip install -e ./opics

Once the package is installed, it can be imported using:

.. code:: ipython3

    import opics

OPICS Libraries
---------------

Listing available libraries
~~~~~~~~~~~~~~~~~~~~~~~~~~~

The package does not come with any component libraries pre-installed.
You can select and download available libraries from the library
catalogue.

.. code:: ipython3

    library_catalogue = opics.libraries.library_catalogue
    
    print(f"Available Libraries: {[_ for _ in library_catalogue.keys()]} ")

Downloading libraries
~~~~~~~~~~~~~~~~~~~~~

The OPICS libraries are downloaded by passing in ``library_name``,
``library_url``, and ``library_path`` to the
``libraries.download_library`` module. The module returns ``True`` if
the library is downloaded successfully.

.. code:: ipython3

    library = library_catalogue["ebeam"]
    
    
    import os
    installation_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop\\delete') 
    
    opics.libraries.download_library(
        library_name=library["name"],
        library_url=library["dl_link"],
        library_path=installation_path,
    )
    
    # reload libraries
    import importlib
    importlib.reload(opics.libraries)

List installed libraries
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    opics.libraries.installed_libraries

List library components
~~~~~~~~~~~~~~~~~~~~~~~

.. code:: ipython3

    opics.libraries.ebeam.components_list

Remove libraries
~~~~~~~~~~~~~~~~

Any of the installed libraries can be removed using the
``libraries.remove_library`` module.

.. code:: ipython3

    opics.libraries.remove_library("ebeam")
    
    importlib.reload(opics.libraries)
    
    print(opics.libraries.installed_libraries)

.. code:: ipython3

    #reinstall ebeam library
    opics.libraries.download_library(
        library_name=library["name"],
        library_url=library["dl_link"],
        library_path=installation_path,
    )
    
    importlib.reload(opics.libraries)
    
    print(opics.libraries.installed_libraries)

Library components
~~~~~~~~~~~~~~~~~~

Let’s take a look at the library components.

.. code:: ipython3

    ebeam_lib = opics.libraries.ebeam

Listing library components

.. code:: ipython3

    ebeam_lib.components_list

Let’s take a look inside a component for more information on its
parameters and layout, such as port locations.

.. code:: ipython3

    ebeam_lib.Y?

Setting up a simulation
-----------------------

The network module is used to define a circuit, add and connect
components. The network module takes ``network_id`` and ``f`` as inputs.
If no ``f`` or frequency data points specified, the network module uses
the default value specified in ``opics.globals.F``.

.. code:: ipython3

    from opics import Network
    from opics.globals import C
    import numpy as np
    
    freq = np.linspace(C * 1e6 / 1.5, C * 1e6 / 1.6, 2000)
    circuit = Network(network_id="circuit_name", f=freq)

Once an empty network is defined. We can start by adding components.

.. code:: ipython3

    input_gc = circuit.add_component(ebeam_lib.GC)
    y = circuit.add_component(ebeam_lib.Y)
    wg2 = circuit.add_component(ebeam_lib.Waveguide, params=dict(length=0e-6))
    wg1 = circuit.add_component(ebeam_lib.Waveguide, params={"length":15e-6})
    y2 = circuit.add_component(ebeam_lib.Y)
    output_gc = circuit.add_component(ebeam_lib.GC)

We can also define custom port names for components for easy reference.

.. code:: ipython3

    input_gc.set_port_reference(0, "input_port")
    output_gc.set_port_reference(0, "output_port")

Connect components using the ``Network.connect`` module.

.. code:: ipython3

    circuit.connect(input_gc, 1, y, 0)
    circuit.connect(y, 1, wg1, 0)
    circuit.connect(y, 2, wg2, 0)
    circuit.connect(y2, 0, output_gc, 1)
    circuit.connect(wg1, 1, y2, 1)
    circuit.connect(wg2, 1, y2, 2)

Simulate the network/circuit

.. code:: ipython3

    circuit.simulate_network()

Plot the simulated response

.. code:: ipython3

    circuit.sim_result.plot_sparameters(show_freq=False)

An interactive plot can be spawned by enabling the interactive option.

.. code:: ipython3

    circuit.sim_result.plot_sparameters(show_freq=False, interactive=True)
