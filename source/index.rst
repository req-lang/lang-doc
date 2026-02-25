Language
======================

Welcome to the req language official documentation website!

What is req ?
**********************

The *req* is a *progressively formal* systems specification language:

* *Description language* that aims at gathering requirements and goals for a given project in a single source files set.

* *Embeds markdown*, allows to use all markdown constructs to provide rich information such as images, diagrams, table and maths.

* *Explicit definitions* of terms within the specification. This makes extracting a glossary and ontology easy and provides a single source of truth for all the wording.

* *Formal syntax* at its core to write *formal properties* of the system, allowing for units, maths and logic.

The req language aims to express the *core specifications* of a project from stakeholder needs and goals to detailed engineering and design. It provides basic but powerful structural semantics, allowing for a hierarchy of *definitions*, *parts* and *requirements*.

.. code-block:: req

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

* Agnostic and lightweight *specification structure semantics*

* Mainly focus on clear and transpilable *problem space description*

* *Requirement is the primary semantic unit* of specification

* *Lightweight MBSE approach*, based on core mathematical properties rather than diagrams

* Made for both *easy export and import* and *human-readability*

* Incremental adoption, from already existing documents

* *Token-efficient* approach for LLM

* *Eliminates vendor lock-in* as requirements are not in ALM but in plain-text source files 

.. note:: The language is still under active development and this documentation is subject to change in the near future.

.. toctree::
  :maxdepth: 1
  :caption: Contents:

  overview.rst
  glossary.rst
