.. _reference-entities-label:

Entity
======================

An *entity* is a specification object that structures the specification.
In a document interpretation, entities are analogous to sections and subsections.
In a model interpretation, entities are model elements that either constrain or define the :term:`SOI` or its environment.

Structure
**********************

A .req specification starts with a :ref:`reference-package-label`, which is called the *root* and is the parent of all other entities in the specification.
The specification forms a tree from the root down to leaf entities.

.. note::

  It is common to place the constraint section — :ref:`reference-package-label` and :ref:`reference-requirement-label` — and the definition section — :ref:`reference-part-label` and :ref:`reference-attribute-label` — as direct children of the root.

.. attention::

  Multi-file specifications are not yet supported. All entities referenced in a specification must be defined in the same source file.

Identification
**********************

Identifier
~~~~~~~~~~~~~~~~~~~~~~

Each entity has an *identifier* that can only be composed of:

* alphanumeric characters ``[0-9a-zA-Z]``
* the underscore symbol ``_``

An identifier cannot start with a numeric character.

.. note::

   Naming conventions are introduced for each entity type in the sections below.

Path
~~~~~~~~~~~~~~~~~~~~~~

A *path* is the concatenation of identifiers separated by ``::``, e.g. ``Specification::System::Wheel``.
Each entity has an *absolute path* that lists each identifier from the root to the entity itself.

.. note::

   Each entity is uniquely identified by its path. Two entities cannot share the same path.

.. _reference-reference-label:

Reference
~~~~~~~~~~~~~~~~~~~~~~

A *reference* is a mention of a path present in the specification.

.. note::

  References are commonly used in :ref:`reference-markup-label` and :ref:`reference-expression-label`.

The *scope* is the set of all entities that can be referenced. Each entity in scope is identified by a unique path — no duplication is allowed.

When resolving a reference, the following rules are evaluated in order:

1. The reference matches an identifier of a direct child of the parent entity
2. The reference is a full path from root to entity
3. The reference is the suffix of an imported path

Imports
~~~~~~~~~~~~~~~~~~~~~~

A :ref:`reference-package-label` or :ref:`reference-part-label` may have *imports* that allow references to be shortened.
Adding an import brings a *prefix* into scope that is merged with references at resolution time — see :ref:`reference-reference-label`.

.. code-block:: none
   :caption: Syntax

   import PATH

.. _reference-requirement-label:

Requirement
**********************

A *requirement* is an expectation or an assumption about the :term:`SOI` or its environment.
An implementation satisfies a specification if and only if all requirements are met in the assumed environment.


.. code-block:: none
   :caption: Syntax

   requirement IDENTIFIER
   (<refines|derives|specializes> PATH)*
   is
    <MARKUP|EXPRESSION>
   requirement

Requirements can either be *formal* by using an boolean expression:

.. code-block:: req
   :caption: Example of a formal requirement

   requirement Keep_temperature_low_on_summer is
    when is_summer then temperature < 30
    end
   requirement

Or *informal* by using a markup:

.. code-block:: req
   :caption: Example of an informal requirement

   requirement Keep_temperature_low_on_summer is
   @@
    When this {is_summer}, the {temperature} should be strictly less than 30
   @@
   requirement

.. _reference-requirement-constraint-label:

Constraint
~~~~~~~~~~~~~~~~~~~~~~

Each requirement may *constrain* either a :ref:`reference-part-label` or an :ref:`reference-attribute-label`.

.. attention::

   The specification of how the constrained entity is determined from a requirement body is forthcoming. For expression requirements, it is derived from the attributes referenced in the expression. For markup requirements, it is determined by the implementation.

.. _reference-requirement-traceability-label:

Traceability
~~~~~~~~~~~~~~~~~~~~~~

*Traceability* is a directed link between requirements. Unlike free-form trace links, each traceability keyword in req carries a defined semantic that constrains how requirements may be related:

#. *Refinement* (``refines``) — the child requirement adds detail or stronger conditions to what the parent requires. The parent's intent still holds; the child narrows it. Both requirements constrain the same entity.
#. *Specialization* (``specializes``) — the child requirement applies to a specific subset of situations covered by the parent. The situations are meant to be selected via configuration management. Both requirements constrain the same entity.
#. *Derivation* (``derives``) — the child requirement was produced from the parent through a design or allocation decision. No constraint compatibility is implied; the constrained entities may differ.

.. _reference-package-label:

Package
**********************

A *package* is a container element that provides a *viewpoint* for requirements. Packages can be nested to provide a hierarchy between viewpoints.

.. code-block:: none
   :caption: Syntax

   package IDENTIFIER
    <PACKAGE|PART|REQUIREMENT>
   package


.. _reference-attribute-label:

Attribute
**********************

.. _reference-part-label:

Part
**********************
