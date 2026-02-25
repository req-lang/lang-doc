.. _language-landscape-label:
Language Landscape
======================

This section aims to compare the req language with other candidates with respect to the requirements engineering activity and engineering data management.

This section serves as:

* A refined category definition for the req language
* An explanation of why req should exist and how it differs from any other category
* An overview of the kinds of language that req should be translated to

Modeling languages
**********************

For the purpose of this comparison, SysMLv2 is taken as representative of modeling languages, though the discussion also applies to other languages in the category.

SysMLv2 is mainly focused on **solution space description**: its primary design goal is to describe elements of solutions such as state machines, actions and interfaces within a specific thinking framework.
This framework can be refined as required to narrow it down to a concrete methodology or approach.

The req is mainly focused on **problem space description**, providing a way to describe system features using equations and mathematical properties.

Formalizing a requirement in SysMLv2 requires a significant amount of upfront boilerplate modeling to be used efficiently: constraints must be linked via ``satisfy`` relationships, and the constraint body can either be fully formal or plain-text documentation only, with no cross-references.

Drawbacks
~~~~~~~~~~~~~~~~~~~~~~

* Steep learning curve due to the variety of concepts
* Concepts inherited from software engineering add boilerplate
* Either fully opt-in or opt-out, difficult to provide a hybrid document/model description
* Formal semantics difficult to understand

Advantages
~~~~~~~~~~~~~~~~~~~~~~

* Out-of-the-box concepts to design systems
* Highly customizable semantics
* Graphical description

.. note:: The req is planned to be interoperable with SysMLv2 in the sense that requirements may be translated from/to SysMLv2.

Formal languages
**********************

A formal language is defined here as a language based on maths and logic to express formal properties that can be proven. Notable examples are Alloy, TLA+ and Prolog.

Formal languages have historically been developed as **proof-ready languages**. This design choice causes the semantics encoded to be notoriously hard to read and understand.

One should keep in mind that requirements and systems specifications must be readable by non-specialist engineers or even non-engineers. Therefore, clarity is an important consideration.

Drawbacks
~~~~~~~~~~~~~~~~~~~~~~

* Very difficult to read and understand
* Proof coverage varies widely between formal languages
* Hard to link with actual requirements or engineering concepts

Advantages
~~~~~~~~~~~~~~~~~~~~~~

* Mathematically correct semantics out-of-the-box
* Precise verification algorithms


.. note:: The req takes the following approach: if it can be written using maths or logic, then it should be writable in req. Some expressions may be translated to formal languages but this is not always the case. Expressiveness is the priority, but some expressions may not be sound and therefore will not have a way to be proven.

Markup languages
**********************

Markdown and AsciiDoc are good examples: they provide good content structure (via headings), referencing and link features, and above all, rich text features.

The req language is essentially a markup language with enhanced structural semantics — more adapted to systems engineering than headings — along with powerful references and mathematical expressions.

Drawbacks
~~~~~~~~~~~~~~~~~~~~~~

* No identifier semantics, nor traceability
* No formal constraints on property types of elements
* No export to machine-readable structure


Advantages
~~~~~~~~~~~~~~~~~~~~~~

* Out-of-the-box document generation
* Simpler format understandable by non-technical users
* Easy formatting of images, diagrams, ...

.. note:: It should be straightforward to export a req specification to any markup language.


Simulation languages
**********************

Modelica, MATLAB and Simulink are common candidates. These languages excel at providing approximations of a solution in order to evaluate behavior. They are generally not provided with a powerful testing framework to monitor properties on simulation runs.

The req language is the missing component to bring requirements verification within simulations. It should be possible to translate a formal property into a verifier component or a script within a simulation.

Drawbacks
~~~~~~~~~~~~~~~~~~~~~~

* Only focused on the solution space
* Sometimes requires thinking in terms of algorithms and instructions
* Subject to approximations or limitations due to simulation mechanics
* No structural semantics

Advantages
~~~~~~~~~~~~~~~~~~~~~~

* Advanced and concrete modeling
* Continuous and discrete modeling

.. note:: Formal req requirements represent properties that must hold during all simulation sequences featuring the enabling conditions of the requirements.

Wrapping Up
**********************

The req language is a middle ground between all the above-mentioned language categories. It attempts to focus primarily on requirements authoring, clarity and verifiability.

In this matter, none of the above-mentioned language categories provides both convenience, precision and non-engineer understandability.

One of the main design goals of the req language is to provide a great balance between these three aspects. All the above-mentioned languages have served as sources of inspiration.

.. note:: A special mention to the FORM-L language, which has established strong groundings for the formal requirements-as-code approach, and is the main source of inspiration for the req language.
