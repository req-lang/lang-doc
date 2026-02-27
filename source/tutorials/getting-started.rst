.. _getting-started-label:

Getting started
======================

This tutorial walks you through the initial setup of the req language tools and the writing of your first specification.

Prerequisites
**********************

The language and tools are straightforward to use, but it is preferable that you are familiar with:

* The use of the terminal, PowerShell for Windows and sh for macOS and Linux
* The use of an :term:`IDE`, VSCode preferentially

It is recommended that you have VSCode installed on your machine. You can download it `here <https://code.visualstudio.com/>`__.

Setup
**********************

This section will guide you through the installation of the required tools to start specifying with the req language.

.. note::

   To perform an advanced setup refer to the tooling section of this documentation.

reqtool
~~~~~~~~~~~~~~~~~~~~~~

reqtool is the only binary you will need to install. It is a general utility program that we will use to check the validity of a specification.

To install reqtool, open a terminal and copy the command below:

 .. tab-set::

     .. tab-item:: Linux / macOS
        :sync: unix

        .. code-block:: bash

            curl -fsSL https://raw.githubusercontent.com/req-lang/reqtool/main/install.sh | sh

     .. tab-item:: Windows
        :sync: win

        .. code-block:: powershell

            irm https://raw.githubusercontent.com/req-lang/reqtool/main/install.ps1 | iex


Authentication might be required to finalize the setup. Once it is done you should be able to run the following command:

.. code-block:: bash

   reqtool help

A help message should be displayed indicating the available commands and the usage of the program.

req-vscode
~~~~~~~~~~~~~~~~~~~~~~

This is the VSCode extension that provides syntax coloring and other features for editing specifications in the IDE. It is recommended that you use it for this tutorial.


#. Go to the extension releases https://github.com/req-lang/req-vscode/releases
#. Download the `req-vscode.vsix` file
#. Follow the `official instructions <https://code.visualstudio.com/docs/configure/extensions/extension-marketplace#_install-from-a-vsix>`__ to install a .vsix extension

Open a new text file and save it with the .req extension. Copy the following code into the newly created file:

.. code-block:: req
   :caption: Template code

    package System
      part Model
      part

      package Requirements
      package
    package

If everything works, you should see the keywords and labels highlighted.

.. hint::

   This code represents the standard structure of most specifications in req. You will likely use it as a starting point very often.

Your first specification
**********************

In this section we will set up a basic workflow so you understand how to work with req.

Use the checker
~~~~~~~~~~~~~~~~~~~~~~

Create a new file named `intro.req`. Copy-paste the above req code into this file. Then open a terminal at the directory where the file is located and execute the following command:

.. code-block:: bash

  reqtool check intro.req

You should see a single line output saying something like:

.. code-block:: bash

  All done in 64.20us

The ``check`` command performed a verification of the file ``intro.req`` to diagnose any issues.

.. note::

   The VSCode extension performs checks automatically on save. The command line interface is used here for clarity.

Adding a requirement
~~~~~~~~~~~~~~~~~~~~~~

Within the ``Requirements`` package, add the following:


.. code-block:: req

  requirement Maximum_temperature is
    @@
      The system temperature shall be less than 30C
    @@
  requirement

This passes the check and looks like most requirements you have written in Excel or any ALM tool.

While this is a perfectly valid way to use req, in the next section you will understand what the preferred approach is and why it matters.

Adding an attribute
~~~~~~~~~~~~~~~~~~~~~~

Consider the following question: what if several requirements deal with temperature and you want to identify exactly which ones?

This question comes up naturally when searching for contradictions or analyzing the impact of a change.
The notion of :ref:`reference-attribute-label` and :ref:`reference-part-label` was introduced precisely for this. Let's add an attribute under the ``Model`` part:

.. code-block:: req

   let temperature in real [C]

And now let's use this attribute:

.. code-block:: req

  requirement Maximum_temperature is
    @@
      The {System::Model::temperature} shall be less than 30C
    @@
  requirement

``Maximum_temperature`` is now explicitly linked to ``temperature``. There is no need to search the specification manually to find requirements related to the concept of system temperature.

.. hint::

  When extracting a part or an attribute reference, always prefer the narrowest scope. In the above requirement, we could have written ``The {System} temperature shall be less than 30C``, but that would lose precision: the requirement constrains a specific attribute, not the system as a whole.

Your first diagnostic
~~~~~~~~~~~~~~~~~~~~~~

For the sake of demonstration, delete the ``temperature`` attribute we just created and run ``reqtool check intro.req``.

The command outputs an error message that looks like this:

.. code-block:: bash

   Reference not found: System::Model::temperature
    8:7

This is a *diagnostic* established during the check, indicating that the requirement (line 8, column 7) references something that does not exist.

The ``check`` command acts like a compiler for your specifications. A wide variety of diagnostics can be reported; a description of each is available in the :doc:`Language Reference </reference>`.

Switching to formal
~~~~~~~~~~~~~~~~~~~~~~

The requirement we wrote is valid and makes the specification easy to browse. Two things can still be improved:

#. Writing the requirement in plain English adds boilerplate that carries no mathematical meaning.
#. We lose the precise semantics of what we expect from the attribute.

Formal notation addresses both: expressions are concise, and each formal requirement in req is implicitly a *shall* statement.

By preserving the mathematical meaning of the requirement, the compiler can also detect formal contradictions and catch an entirely different class of errors.

Let's rewrite our requirement in formal notation:

.. code-block:: req

  requirement Maximum_temperature is
      System::Model::temperature < 30
  requirement

If we had mistakenly written:

.. code-block:: req

  requirement Maximum_temperature is
      System::Model::temperature < false
  requirement

The ``check`` command would report:

.. code-block:: bash

    Expected Number got Boolean
        8:35

This is first-class type checking applied to your specification.

Make a refinement
~~~~~~~~~~~~~~~~~~~~~~

So far we have written a single requirement. When working with multiple requirements, it is common to make the relationships between them explicit. Here is how to do that in req.

Let's add a higher-level requirement than the one we have been working with:

.. code-block:: req

  requirement Bound_temperature is
    @@
      The {System::Model::temperature} shall be bound.
    @@
  requirement

Now let's express the traceability link using ``refines``. Modify the ``Maximum_temperature`` requirement:

.. code-block:: req

  requirement Maximum_temperature
  refines System::Requirements::Bound_temperature
  is
      System::Model::temperature < 30
  requirement

Complete example
~~~~~~~~~~~~~~~~~~~~~~

Once done, you should end up with the following content in ``intro.req``:

.. code-block:: req

    package System
      part Model
        let temperature in real [C]
      part

      package Requirements
        requirement Bound_temperature is
          @@
            The {System::Model::temperature} shall be bound.
          @@
        requirement

        requirement Maximum_temperature
        refines System::Requirements::Bound_temperature
        is
          System::Model::temperature < 30
        requirement
      package
    package

This specification should pass the ``check`` with no diagnostics.

Wrapping up
**********************

In this tutorial you learned how to set up the toolchain for the req language and make use of the compiler diagnostics.
You were introduced to the most common workflow:

1. Write in plain English
2. Extract attributes and parts from the requirements
3. Formalize and trace where relevant
4. Check and fix via ``reqtool check``

You have built a specification that is:

* Formal, with mathematical and logical properties that are enforced by the compiler
* Easily browsable, traceable, and analyzable
