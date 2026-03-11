req language
======================

req is a *requirements-as-code* language: specifications can be written in plain natural
language or formal mathematical expressions — and both are valid in the same file.
This is *progressive formalization*: start with English, formalize only what benefits from
machine checking.

Start with the :doc:`Getting Started guide <tutorials/getting-started>`.

What is req?
**********************

req is a *progressively formal* specification language:

* **Requirements as the primary unit** — requirements capture expectations and assumptions,
  from stakeholder needs to detailed system properties.
* **Progressive formalization** — informal natural language and formal expressions coexist
  in the same file. Formalize incrementally, only where it adds value.
* **Explicit definitions** — attributes and parts give requirements a shared vocabulary,
  enabling cross-references, traceability, and compiler-checked consistency.
* **Formal expression language** — arithmetic, logic, temporal operators, and set theory
  for precise, machine-checkable constraints.

req aims to express the core specifications of a project from stakeholder needs to detailed
engineering properties. It provides lightweight constructs without enforcing a
concept-heavy framework.

.. code-block:: req
   :caption: Progressive formalization — informal and formal requirements in the same file

    @@
      The most **famous** example in the coding world...
    @@
    package Hello_World
      part Model
        part Output
          let value in text
          let ready in boolean
        part
      part
    
      package Requirements
        requirement Print is
          @@
            When {Hello_World::Output::ready},
            {Hello_World::Output::value} shall be equal to 'Hello World'
          @@
        requirement

        @@
          This is *progressive formalization* of {Hello_World::Requirements::Print}

          # Comments

          It wasn't *clear* enough in informal syntax according to John
        @@
        # sil 4 #
        requirement Print_Formal
        refines Hello_World::Requirements::Print
        is
          when
            Hello_World::Output::ready then Hello_World::Output::value = 'Hello World'
          end
        requirement
      package
    package

Features
**********************

* Agnostic and lightweight *specification structure* — no modeling framework imposed

* Clear *problem space description* — requirements state what the system must do,
  not how it does it

* *Requirement as the primary semantic unit* — the specification flows through requirements
  from stakeholder needs to detailed properties

* *MBSE-compatible* — based on core mathematical properties rather than graphical diagrams

* *Interoperable* — designed for straightforward translation to SysML v2, formal languages,
  and simulation tools

* *Incremental adoption* — start from existing Word or Excel documents; formalize gradually

* *Vendor lock-in eliminated* — specifications live in plain-text source files,
  not ALM databases

.. note::

   req is under active development. The language and this documentation are subject to
   change. See the :doc:`Language Reference <reference>` for the current stable
   specification.

.. toctree::
  :maxdepth: 1
  :caption: Contents:

  tutorials.rst
  overview.rst
  glossary.rst
  reference.rst
  tooling.rst

