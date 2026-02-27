.. _reference-entities-label:

Entity
======================

An *entity* is a specification object that represent the structure of the specification.
In a document interpretation of the specification, entities are analogous to section and sub-section.
In a model interpretation, the entities are model elements that can either be *constraining* or *defining* the :term:`SOI`

Document structure
**********************

A .req specification starts with a :ref:`reference-package-label` which is the called the *root* and is the parent of any other entity contained in the specification.
The specification forms a tree starting from the root down to leaf entities.

It is common to separate the constraint section represented by :ref:`reference-package-label` / :ref:`reference-requirement-label` and definition the :ref:`reference-part-label` / :ref:`reference-attribute-label` at the highest level of the specification, meaning just beneath root.

.. attention::

  .req documents cannot reference each other for now, all the information regarding a specification must be contained in a single source file.


Encoding
~~~~~~~~~~~~~~~~~~~~~~

.req document are encoded using ASCII format but this is subject to change in the near future.

Identification
**********************

Identifier
~~~~~~~~~~~~~~~~~~~~~~

Each entity have an *identifier*, that can only be composed of:

* alphanumeric characters ``[0-9a-Z]``
* the underscore symbol ``_``

.. note ::

   Naming conventions are introduced for each type of reference.

An identifier cannot start with a numeric character. 

Path
~~~~~~~~~~~~~~~~~~~~~~

A *path* is the concatenation of identifiers separated by ``::``, ex. ``Specification::System::Wheel``.
Each entity have an *absolute path* that is lists each identifier from root to the entity itself.

.. note ::

   Each entity is uniquely identified by its path, two entities can't have the same path.
  

.. _reference-reference-label:

Reference
~~~~~~~~~~~~~~~~~~~~~~

A *reference* is a mention to a path present in the specification. References are commonly used in :ref:`reference-markup-label` and :ref:`reference-expression-label`.

The *scope* is the set of all entities that can be referenced, scope contains only distinct entities that are referenced by unique path, no duplication is allowed.

More precisely, when determining the entity for a given reference the following hypotheses are evaluated in order:

1. The reference is a label from the parent element
2. The reference is a full path from root to element      
3. The reference is is the suffix of an imported path

Imports
~~~~~~~~~~~~~~~~~~~~~~

A :ref:`reference-package-label` or :ref:`reference-part-label` may have *imports* that allows to shorten reference in code. Adding an import brings to scope a *prefix* that is be merged with actual references, cf. :ref:`reference-reference-label`.


.. _reference-requirement-label:

Requirement
**********************

.. _reference-package-label:

Package
**********************

.. _reference-attribute-label:

Attribute
**********************

.. _reference-part-label:

Part
**********************
