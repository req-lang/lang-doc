.. _reference-label:

Reference
======================

Introduction
**********************

This reference provides a formal and complete description of the req language. It covers entity constructs, the expression language, traceability mechanisms, and compiler diagnostics, with syntax and examples for each.

This is not an introduction to req. Readers new to the language should start with the :ref:`overview-label` section and the :ref:`getting-started-label` tutorial before consulting this reference.

This reference acts as the specification for the req language. It is the source of truth: any behavior in req tooling that contradicts this document can be considered a bug. Particularly, the reference specifies:

* The formal syntax of the language
* The semantics for each concept of the language.


Note that this reference is therefore a good starting point to understand the https://github.com/req-lang/reqtool implementation.

Only fully specified features are covered here. Draft or experimental functionality is not included. Features that are not yet implemented but fully specified have a special mention.


.. toctree::
  :maxdepth: 1
  :caption: Contents:

  reference/entities

Prerequisites
**********************

The expression language covers a broad range of formal concepts. Familiarity with the following is helpful to make full use of it:

* Systems engineering, particularly :term:`MBSE` and languages such as SysML
* Requirements engineering, particularly functional and physical decomposition
* Formal logic, particularly `LTL <https://en.wikipedia.org/wiki/Linear_temporal_logic>`__ and `FOL <https://en.wikipedia.org/wiki/First-order_logic>`__
* Mathematics, particularly `set theory <https://en.wikipedia.org/wiki/Set_theory>`__

These are not strict prerequisites. Entity constructs and informal requirements can be used without any background in formal methods.

Conventions
**********************

* A *mandatory property* is expressed as an **affirmative phrase**, e.g. "The document starts with a package." It should be read as "the document shall start with a package", meaning any conforming implementation must respect the property.

* An *optional property* is expressed as an **affirmative phrase using the modal may**, e.g. "The expression may have a type." It should be read as "the expression may or may not have a type." A conforming implementation must handle both cases.

A syntax notation is used throughout this reference to describe the formal grammar of the language. It is intended to be more readable than BNF while remaining unambiguous:

* ``LABEL`` (uppercase) represents a defined language concept
* ``<LABEL_A | LABEL_B>`` represents a choice between two alternatives
* ``LABEL?`` indicates zero or one occurrence, ``LABEL*`` zero or more, ``LABEL+`` one or more
* All other tokens are literal
