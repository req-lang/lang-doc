.. _use-cases-label:

Use Cases
======================

This section illustrates four situations where req brings concrete value. Each use case is
independent — you can start with any of them. The greatest benefit comes from combining them,
following the natural progression from structured text to formal, machine-checked specifications.

Text-Based Specifications
****************************

**The pain.** Word and Excel are the default starting point for system specifications.
They work for small teams on short programs. As the specification grows, familiar problems appear:

* Changes are hard to review — a modified cell or a tracked change in Word gives no context
  about what the requirement means or what else was affected.
* References between requirements are informal and break silently — renaming a term does not
  update every mention of it elsewhere in the document.
* Filtering and searching are manual — extracting all requirements that concern a particular
  subsystem or interface requires reading the entire document.

**With req.** The specification lives in plain text files. A version control system (git)
provides line-level diffs, branching, and pull-request workflows out of the box. Explicit
cross-references are checked by the checker: a broken link is a defect, not a broken
hyperlink discovered months later in a review.

.. code-block:: req
   :caption: A minimal text-based specification

   package Brake_System
     @@
       The **braking system** is responsible for decelerating the vehicle
       safely under all operating conditions. See {Brake_System::Brake} for
       the detailed requirements.
     @@
     package Brake
       requirement Stop_distance is
         @@
           The vehicle shall reach a complete stop within the certified
           stopping distance for the current operating speed.
         @@
       requirement
     package
   package

A reference such as ``{BrakeSystem::Brake}`` is resolved during check. If the target
entity is renamed or moved, the checker reports the defect immediately.

Traceability and Impact Analysis
************************************

**The pain.** Requirements do not exist in isolation. Stakeholder needs decompose into
system requirements, which decompose into subsystem constraints, which derive from design
decisions. In Word or database-based tools, these relationships are maintained as free-text
fields or manual link tables — fragile, hard to query, and routinely outdated.

**With req.** Traceability is expressed in the language itself. The ``refines``,
``specializes``, and ``derives`` keywords establish typed links between requirements that
the checker verifies. When a parent requirement changes, every dependent requirement is
immediately visible without consulting a separate traceability matrix.

.. code-block:: req
   :caption: Traceability between requirement levels

   package System
     part Vehicle
        speed in real [km/h]
        mass in real [kg]
        breaking_force in real [N]
        max_deceleration in real [m/s^2]
     part

     part TractionControl
     part

     requirement Max_Speed is 
        Vehicle::speed <= 250 
      requirement

     package Powertrain
       requirement Traction_Control refines Max_Speed is
         @@
           The {TractionControl} system shall prevent wheel slip from
           causing the vehicle to exceed its maximum {Vehicule::speed}.
         @@
       requirement
     package

     package Brakes
       requirement Brake_Authority derives Max_Speed is
         Vehicle::braking_force >= Vehicle::mass * Vehicle::max_deceleration
       requirement
     package

   package

The requirement ``Brake_Authority`` is derived from ``Max_Speed`` by a design
decision: the braking system must be sized to enforce the speed constraint. This
relationship is machine-readable, queryable, and checked for reference validity by
the checker.

Progressive Formalization
****************************

**The pain.** Writing formal requirements upfront requires committing to a full formal
model before the system is well understood. Teams that try this stall. Teams that do not try it stay in informal prose forever. 
The choice has historically been to keep formal on separated tools for very specific concerns.

**With req.** Informal and formal requirements coexist in the same file and the same
package. A requirement can start as prose and be formalized incrementally, requirement
by requirement, as the design stabilizes and the relevant attributes are defined.

.. code-block:: req
   :caption: Informal and formal requirements side by side

   package Brake_System
     part Brake
       let stopping_distance_ref in real [m]
       let stopping_distance in real [m]
       let speed in real [km/h]
     part

    requirement Brake_performance is
      @@
        {Brake} performance shall be verified across the full speed range
        according to the certified braking performance table.
      @@
    requirement

    requirement Cold_brake_margin is
      Brake::stopping_distance <= 1.2 * Brake::stopping_distance_ref
    requirement
   package

``Brake_performance`` remains informal — the full table is not yet modeled formally.
``Cold_brake_margin`` is formal and type-checked. Both are valid in the same file.
The checker checks what can be checked and leaves the rest to the engineer's judgment.

.. note::

   Formalizing a requirement requires that the attributes it references are declared with
   ``let`` in the enclosing scope. Formalization and attribute declaration go hand in hand:
   writing a formal constraint is also an act of defining the system's state variables, parameters and interface.

Incremental Structure
****************************

**The pain.** Model-based systems engineering tools require upfront modeling investment:
define blocks, interfaces, viewpoints, and stereotypes before writing a single requirement.
This overhead causes many teams to abandon structured approaches entirely.

**With req.** Structure grows from the specification itself. A flat list of requirements
can be reorganized incrementally into :ref:`reference-part-label` and
:ref:`reference-attribute-label` as the system decomposition becomes clearer — without
switching tools or restructuring the entire document.

.. code-block:: req
   :caption: A structured specification grown incrementally

   package Aircraft
     part System 
      limit_load in real [N]
      fuel_consumption in real [kg/s]
     part 

     part Engine
       let max_thrust in real [N]
       let fuel_flow in real [kg/s]
     part

     part Airframe
       let max_structural_load in real [N]
     part

     requirement Thrust_bound is 
       max_thrust <= 50000 
     requirement

     requirement Fuel_efficiency is
       @@
         {System::fuel_consumption} at maximum continuous thrust shall not exceed
         the certified {Engine::fuel_flow} limit.
       @@
     requirement

     requirement Structural_Limit is
       Airframe::max_structural_load <= System::limit_load
     requirement
   package

The ``Engine`` and ``Airframe`` parts define the system components decomposition. Their ``let``
attributes are the typed interface between the system model and the formal requirements.
A team can reach this structure incrementally — one part and one attribute at a time —
starting from a single flat package with informal requirements.

Tool Integration
****************************

**Today.** ``reqtool check`` parses the specification, resolves all cross-references, and
type-checks every formal expression. This 
operation catch a class of specification errors — broken references, type mismatches,
undefined identifiers — that no word processor or spreadsheet can detect.

.. note::

   The current scope of ``reqtool check`` is type checking and reference resolution.
   It does not detect contradictory requirements or verify that properties hold over
   a system model. These are directions of future development.

**Roadmap.** Because formal req expressions are grounded in standard formalisms
(:term:`LTL`, :term:`FOL`, set theory), they can in principle be translated to inputs
for simulation monitors, model checkers, or formal provers, provided the target tool
supports the relevant formalism. Export formats (including :term:`ReqIF` for exchange
with existing ALM tools) are planned but not yet available.

Wrapping Up
****************************

The four use cases above are not mutually exclusive. The recommended path is to start
wherever the current pain is greatest: replace a Word document with structured markup,
add typed attributes to an existing informal specification, formalize one critical
requirement at a time. Each step produces value independently; together they form a
machine-checkable, traceable, version-controlled specification.

To get started, see the :ref:`getting-started-label` tutorial.
