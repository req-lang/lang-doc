Core Concepts
======================

This section aims at defining the most relevant concepts to understand what composes a req specification.
Definitions here are intended as an introduction; refer to the language reference for a more in-depth treatment.
Once familiar with the getting started example, this section acts as a basic cheatsheet to start designing systems with .req

.. note::

   In the context of the req language, the term *specification* means a .req file, that can contain information about the system of interest, as well as its environment.

Entity
**********************

The term *entity* refers to specification objects that provide structure to the specification. An entity has several functions:

* Hold meta-information about the underlying artifact
* Provide hierarchy and separation to the specification
* Entity-specific functions, explained in the following sections

A specification is simply a tree of entities. Entities can be gathered into two categories: *constraining* and *defining* entities.
Two flows are possible when writing a specification:

* Start by constraining (i.e. write :ref:`concept-requirement-label`) to fix the expectations on the system without modeling
* Start by defining (i.e. write :ref:`concept-attribute-label` and :ref:`concept-part-label`) to model the structure of the system

.. attention::

   While the terminology used mimics the SysMLv2 terminology in order to ease understanding, there is not yet a guarantee of exact matching between the two. Furthermore, the req terminology is subject to change.

.. note::

  Tags can be used to represent project, domain or management specific data such as change-requests, validation-method, priority, ...

.. _concept-requirement-label:

Requirement
~~~~~~~~~~~~~~~~~~~~~~

The *requirement* is the base constraining entity. It can either be written in natural language:

.. code-block:: req
   :caption: Example of natural language requirement

   requirement Ensure_sensor_temperature is
    @@
      The {System::Sensor::temperature} shall be maintained below 30C
    @@
   requirement

Or expressed using formal syntax:

.. code-block:: req
   :caption: Example of formal requirement

   requirement Ensure_sensor_temperature is
      System::Sensor::temperature < 30
   requirement

A requirement expresses a constraint on the system that can either be an expectation or an assumption. Typical examples are:

* Stakeholder needs
* High-level system requirements
* Detailed equipment properties
* Behavioral modeling

Requirements can include references to definitions, :ref:`concept-part-label` or :ref:`concept-attribute-label`. Requirements can be linked with each other via traceability (explained in the dedicated reference section), the most common link being ``refines``. 

.. code-block:: req
   :caption: Example of traceability 

   requirement Ensure_sensor_temperature_formal
   refines Ensure_sensore_temperature_informal is
      System::Sensor::temperature < 30
   requirement

.. note::

   Formal requirements are expected to be boolean expressions forming a verifiable statement about the system.

.. _concept-package-label:

Package
~~~~~~~~~~~~~~~~~~~~~~

A *package* is a collection of sub-packages and requirements. A package gathers the constraints expressed by requirements under a viewpoint.

.. code-block:: req
   :caption: Typical package usage

    package Measuring
      package Measure_gas_composition
        requirement Measure_NO2 is
          @@ ... @@
        requirement

        requirement Measure_CO is
          @@ ... @@
        requirement
      package
    package

Packages partition requirements according to a *thematic breakdown*: functional, abstractions level, allocations, ... 
Breakdown strategies can be combined to split the specification in the most convenient way.

.. note:: Packages can be considered as the sections and sub-sections of the specification.

.. _concept-attribute-label:

Attribute
~~~~~~~~~~~~~~~~~~~~~~

An *attribute* is the base defining entity. An attribute represents any valued property that is relevant to the specification.

.. code-block:: req
   :caption: Basic attribute definition

    let current_speed in real [m/s]
    let has_overspeed in boolean

Typical use cases for an attribute are system dynamic state, system parameter, constants...

.. note::

   Attributes are meant to be used in formal :ref:`concept-requirement-label` in order to express properties that can benefit from advanced checking.

.. _concept-part-label:

Part
~~~~~~~~~~~~~~~~~~~~~~

A *part* is a collection of sub-parts and attributes. A part gathers the definitions expressed by attributes into a cohesive unit.
Unlike :ref:`concept-package-label`, it is common to use a part without any children just to introduce a *concept* relevant to the specification.

.. code-block:: req
   :caption: Typical part usage

    part Passenger
    part

    part TrainCar
      let current_speed in real [m/s]
      let has_overspeed in boolean
      part Wheels
        let diameter in real [cm]
      part
    part

The part can typically be used to partition the system in the following ways:

* A physical decomposition of the system into sub-systems or sub-equipment
* A conceptual decomposition, via subsumption — i.e. B is an aspect of A
* A functional decomposition, mirroring the functional decomposition of :ref:`concept-package-label`\ s

The parts form a partition of the attributes, and more generally of the concepts relevant to the specification.

.. note::

   Parts can be considered as the sections and sub-sections of the glossary.


Expression
**********************

An *expression* is the object used to define formal requirements. An expression has a syntax which is a mix of logic and mathematics, and is used to express the property that must hold to satisfy a requirement.

.. code-block:: req
   :caption: Typical expression

    requirement Trigger_EB_on_absolute_overspeed is
      forall t in TrainUnit such that t::speed > 100
        when t::operation /= SpecialOps then rising t::trigger_emergency_breaking
        end
      end

Expressions are typically used when:

* More clarity is needed to express a requirement precisely
* Exporting to another format is required for verification or simulation
* Diagnosing consistency issues on a given requirement or attribute

.. note:: The expression language is explained in more depth in the dedicated reference page.

Wrapping up
**********************

The req requires a reduced subset of concepts to be effective. It is output-focused, in the sense that during authoring of the specification one can always understand what a document produced from these specifications could look like.

The language is accessible to any stakeholder without requiring specific software or a priori knowledge of modeling, but still allows for rigorous semantics and specialized modeling methodologies via tags or specific design patterns if required.

The syntax is meant to be lightweight and simple, yet powerful when it comes to formal expressions.
