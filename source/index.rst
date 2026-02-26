req language official website!
======================

This website contains the documentation of the language constitued by:

* Getting started and advanced tutorials
* Comprehensive language specification
* Introduction to the language philosophy and design 

What is req ?
**********************

The *req* is a *progressively formal* specification language:

* *Description language* that aims at gathering requirements and model for a given project.

* *Embeds markdown*, to provide rich information such as images, diagrams, table and maths.

* *Explicit definitions usage*, to extracting a glossary and ontology and use it within requirements.

* *Formal syntax* at its core to write *formal properties* of the system, allowing for units, maths and logic.

The req language aims to express the *core specifications* of a project from stakeholder needs and goals to detailed engineering and design. It provides simple but powerful constructs, allowing for modeling without enforcing a concept heavy-framework.

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

* Mainly focus on clear *problem space description*

* *Requirement is the primary semantic unit* of specification

* *MBSE approach*, based on core mathematical properties rather than diagrams

* Made for both *easy translation* other languages and *human-readability*

* Facilitates incremental adoption, from already existing documents

* *Token-efficient* approach for LLM

* *Eliminates vendor lock-in* as requirements are not in ALM but in plain-text source file

.. note:: The language is still under active development and this documentation is subject to change in the near future.

.. toctree::
  :maxdepth: 2
  :caption: Contents:

  tutorials.rst
  overview.rst
  glossary.rst
  reference.rst
