.. _reference-expression-label:

Expression
======================

An *expression* is a typed formal statement that evaluates to a value.
Expressions are present in two cases:

* In formal :ref:`reference-requirement-label` to express a property that must hold 
* In :ref:`reference-attribute-label` definition to express the domain of the attribute

An expression composes several :ref:`reference-attribute-label`\ s in order to:

* Define a *formal property* that must hold considering the domain on the involved attributes
* Constrain an attribute to narrow its definition domain

.. attention ::

   An expression is not algorithm, there is no instruction or succession occurring in expressions, only properties that shall held.


Formalism
**********************

The req uses several formalism in conjunction to produce expressions:

* Predicate logic: ``and``, ``or``, ...
* :term:`FOL`\ : ``forall``, ``exists``, ...
* :term:`LTL`\ : ``eventually``, ...
* set theory\ : ``includes``, ``in``, ...
* common mathematics: algebra, functions, ...

.. note ::

  While this is a reduced subset of what can be required in a specification, the language can still be extented with other constructs.
  The language is driven by expressivity and as such, as long as a construct can be written in formal notation and it is revelant for systems engineers, it might be included.

Literals
**********************

Numbers
~~~~~~~~~~~~~~~~~~~~~~

Numbers are written in decimal format and might use exponential notation.

.. code-block:: req
   :caption: Example of numbers 

    2
    3.14
    10e7
 
A special keyword is reserved of infinite values ``infinity``.

.. note ::

   No distinction is made between integer or real numbers. Fractional numbers are considered operators and not litterals.

Boolean
~~~~~~~~~~~~~~~~~~~~~~

True and false predicates, denoted ``true`` or ``false``.

.. code-block:: req
   :caption: Example of boolean

    true
    false


Undefined
~~~~~~~~~~~~~~~~~~~~~~

A value that is explicetly not specified, denoted ``undefined``.

.. code-block:: req
   :caption: Example of boolean

    undefined


.. note ::

   Undefined values are useful when relaxing an expression when certain conditions are met


Set
~~~~~~~~~~~~~~~~~~~~~~

The set literal allows to create ad-hoc defined set with a finite number of element:

.. code-block:: none 
   :caption: Syntax of set 

    undefined


