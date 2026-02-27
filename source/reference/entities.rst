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

Meta-information
**********************

Each entity is provided with *meta-information* that is meant to provide additional context on the entity.

Comment
~~~~~~~~~~~~~~~~~~~~~~

A *comment* is additional information about a given entity. Any entity can be provided with a comment; the comment may be interpreted differently depending on the kind of entity.


.. code-block:: req
   :caption: Example of comment 
    
   @@
   # Rationale 

   After client meeting, format fits the most for the desired application...
   @@
   requirement Significant_digit_and_format is
    @@
      The {System} shall use decimal format with 2 significant digits 
    @@
   requirement


.. note::

  A common practice is to always provide :ref:`concept-part-label` and :ref:`concept-attribute-label` with a comment that acts as a definition. :ref:`concept-requirement-label` comments can be used as rationale.


Tags
~~~~~~~~~~~~~~~~~~~~~~

A *tag* is meta-information about a given entity, organized as a key-value pair. Any entity can be provided with tags and the value is optional.
Tags are useful to specify additional information about an entity:


.. code-block:: req
   :caption: Example of tag 
    
   # verification proof #
   # priority high #
   requirement Perfection is
    @@
      The {System} shall be perfect 
    @@
   requirement


.. note::

  Tags can be used to represent project, domain or management specific data such as change-requests, validation-method, priority, ...



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

Requirements can either be *formal* by using a Boolean expression:

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

A *package* is a container element that provides a namespace for requirements. Packages can be nested to provide a hierarchy between concern areas.

.. code-block:: none
   :caption: Syntax

   package IDENTIFIER
    <PACKAGE|PART|REQUIREMENT|IMPORT>*
   package

Packages are used to provide a *thematic breakdown* of requirements.

.. code-block:: req
   :caption: Example of a package

   package Room_Control
     package Temperature_Control  
      requirement Keep_temperature_low_on_summer is
        @@ ... @@
      requirement
     package

     package Humidity_Control
     package
   package


A :ref:`reference-requirement-label` belongs to one and only one package. Packages form a requirements partitioning of the system:

* **Function**, activity or operational breakdown of requirements
* **Non-functional** requirements, included either as function sub-packages or a separate package
* **Level of detail**: business, system, equipment, ...

.. note::

   A package can contain :ref:`reference-part-label`, common use case is the root package that contain a root part.

.. _reference-attribute-label:

Attribute
**********************

An *attribute* is a named quantity of the specification that can be assigned a value. 

.. code-block:: none
   :caption: Syntax

   let IDENTIFIER (in DOMAIN)? ([ UNIT ])? 


An attribute can represent several aspects of a system:

* A **state variable** of the specification that can evolve over time
* A **constant parameter** or external input
* An **event** relevant to the specification

.. code-block:: req
   :caption: Example of a set of attributes 

   part Airplane
      let current_speed in real [m/s]
      let wingspan in real [m]
      let has_landed in boolean
    part

An attribute has semantic *type*, inferred by the compiler from its domain and the expressions in which it appears. The type determines which operations are applicable to the attribute.

Domain
~~~~~~~~~~~~~~~~~~~~~~

A *domain*, is the mathematical set of the allowed values of an attribute. It is defined first via an expression having the type ``Set`` in the attribute definition. 

Formal requirements (see :ref:`reference-requirement-label`) constrain attributes. All constraints on an attribute must be *satisfiable* for the specification to be consistent.
More precisely, each constraint narrows the domain of the attribute; if the domain becomes empty the specification is unsatisfiable.

.. note::

   As the number of constraints on an attribute grows, their intersection narrows. An empty intersection means the constraints are contradictory and the specification is unsatisfiable.


Unit
~~~~~~~~~~~~~~~~~~~~~~

A physical *unit* can be provided to numerical attributes

.. attention:: 

  For now, units are freeform labels and are not validated by the compiler.

.. _reference-part-label:

Part
**********************

A *part* is a container element that provides a namespace for attributes and nested parts.
Parts can be nested to represent a physical or conceptual decomposition of the :term:`SOI`
and its environment. This hierarchical structure is called an :term:`ontology`.

.. code-block:: none
   :caption: Syntax

   part IDENTIFIER
    <ATTRIBUTE|PART|IMPORT>*
   part

Parts are typically used to partition a system in the following ways:

* **Physical decomposition** — the system is broken down into sub-systems or sub-equipment.
* **Conceptual decomposition** — B is a functional or logical aspect of A, without implying physical separation.

.. code-block:: req
   :caption: Example of a part

   part Airplane
     let current_speed in real [m/s]
     let has_overspeed in boolean
     part Wings
       let wingspan in real [m]
     part
   part

Unlike :ref:`reference-package-label`, it is common to use a part with no children to
introduce a *concept* relevant to the specification. A part, even with no children, allows for a concept to be named and referenced in requirements before
its attributes are defined.

Informal requirements (see :ref:`reference-requirement-label`) on parts serve as high-level
constraints that can be progressively formalized as the specification matures.

.. note::

   In a more general sense, a part represents an *aspect* of the system under
   consideration — either a grouping of physical characteristics (geometry, mass, speed)
   or functional characteristics (behavior, capability, mode).
