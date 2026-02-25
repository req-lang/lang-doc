Language Landscape
======================

This section aims to compare the req language with other candidates with respect to the requirement engineering activity and engineering data management.

Think of this section as both a:

* Refined category definition for the req language
* A "why" req should exists, how it is different from any other category
* An overview of the kind of language that the req should be transpiled to

Modeling languages
**********************

Let's assume modeling language means SysMLv2, one might find that the discussion also applies to other language.

The SysMLv2 is mainly focused on **solution space description**, its primary design goal is to describing elements of solutions such as state machines, actions, ... in a specific thinking framework. 
This framework can be refined as required to narrow down the thinking framework to a concrete methodology or framework.

The req is a mainly focused on **problem space description** providing a way for describing some model features using equations and mathematical properties.

Formalizing a requirement in SysMLv2 requires a lot of upfront boilerplate modeling to be used efficiently, constraint, link via satisfy, and the constraint can either be totally formal or doc only with pure plain-text (no references).

Drawbacks
~~~~~~~~~~~~~~~~~~~~~~

* Steep learning curve because of the variety of concepts
* Concepts inherited from software engineering adding boilerplate
* Either opt-in or out, difficult to provide a hybrid document/model description
* Formal semantics difficult to understand

Advantages
~~~~~~~~~~~~~~~~~~~~~~

* Out-of-the-box abstract concept to design systems
* Highly customizable semantics 
* Graphical description

.. note:: The req is planned to be interoperable with SysMLv2 in the sense that requirements might be translated from/to SysMLv2

Formal languages
**********************

By formal language, we mean a language that is based on maths and logic to express formal properties that can be proven. Notorious examples are Alloy, TLA+ or Prolog.

The formal language have historical been developed as **proof ready language**, this design choice causes the semantics encoded to be notoriously hard to read and understand.

One might keep in mind that requirements and systems specification shall be read by non-specialists engineers or even non-engineers. Therefore, clarity might be an important point.

Drawbacks
~~~~~~~~~~~~~~~~~~~~~~

* Very difficult to read and understand
* Proof coverage varies wildly between formal languages
* Hard to link with actual requirements or engineering concepts

Advantages
~~~~~~~~~~~~~~~~~~~~~~

* Mathematically correct semantics out-of-the-box
* Precise verification algorithms


.. note:: The req takes the following approach: if it can be written using maths or logic, then it should be writable in req. Some expressions might be translated to some formal languages but it is not always the case. Expressiveness is the priority but some expressions might not be sound and therefore will not have a way to be proven.

Markup languages
**********************

Markdown or asciidoc are good examples, they all provide good content structure (via heading), some referencing and link features, and above all, rich text features.

The req language is basically a markup language with enhanced structure semantics (more adapted to systems engineering than headings), powerful references and maths.

Drawbacks
~~~~~~~~~~~~~~~~~~~~~~

* No identifier semantics, neither traceability
* No formal constraints on properties types of an elements
* No export to machine-readable structure


Advantages
~~~~~~~~~~~~~~~~~~~~~~

* Out-of-the-box document generation
* Simpler format understandable by non-technical
* Easy formatting of images, diagrams, ...

.. note:: It should be easy to export a req specification to any markup language


Simulation languages
**********************

Modelica, Matlab, Simulink are common candidates. These languages excel at providing approximations of a solution in order to evaluate behavior. They are generally not provided with a powerful testing framework to monitor properties on the simulation runs.

The req language is the missing component to bring requirements verification within simulations. It should be possible to translate a formal property into a verifier component or a script within a simulation

Drawbacks
~~~~~~~~~~~~~~~~~~~~~~

* Only focuses on solution space
* Sometimes requires to think algorithms and instructions
* Subject to approximations or limitations due to simulation mechanics
* No structural semantics

Advantages
~~~~~~~~~~~~~~~~~~~~~~

* Advanced and concrete modeling
* Continuous and discrete modeling 

.. note:: req formal requirements represents properties that must hold during all simulation sequences featuring the enabling conditions of the requirements. 

Wrapping Up
**********************

The req language is a middle-ground between all the above mentioned language categories. It attempts to focus primarily on requirements edition, clarity and verifiability.

In this matter, none of the above mentioned language category provide both convenience, precision and non-engineer understandability. 

The main design goal of the req language is to provide a great balance between these three aspects. Note that all the above mentioned languages have been source of inspiration.

.. note:: A special mention to the FORM-L language, which has established strong groundings for the formal requirements as code approach, and is the main source of inspiration for the req language.
