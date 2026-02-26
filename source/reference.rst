Reference
======================

Introduction
**********************

This reference provides a formal and complete description of the req language. It covers entity constructs, the expression language, traceability mechanisms, and compiler diagnostics, with syntax and examples for each.

This is not an introduction to req. Readers new to the language should start with the :ref:`overview-label` section and the Getting Started tutorial before consulting this reference.

This reference acts as the specification for the req language. It is the source of truth: any behavior in req tooling that contradicts this document can be considered a bug.

Only fully specified features are covered here. Draft or experimental functionality is not included. Features that are not yet implemented but fully specified have a special mention.

Prerequisites
**********************

The expression language covers a broad range of formal concepts. Familiarity with the following is helpful to make full use of it:

* Systems engineering, particularly :term:`MBSE` and languages such as SysML
* Requirements engineering, particularly functional and physical decomposition
* Formal logic, particularly `LTL <https://en.wikipedia.org/wiki/Linear_temporal_logic>`__ and `FOL <https://en.wikipedia.org/wiki/First-order_logic>`__
* Mathematics, particularly `set theory <https://en.wikipedia.org/wiki/Set_theory>`__

These are not strict prerequisites. Entity constructs and informal requirements can be used without any background in formal methods.
