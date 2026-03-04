.. _reference-markup-label:

Markup
======================

A *markup block* is a freeform text annotation written in Markdown. Markup blocks support
basic text formatting and can embed traceable references to other entities in the
specification.

A markup block appears in two positions:

* As the **body of a requirement** — placed after the ``is`` keyword, making the
  requirement informal (see :ref:`reference-requirement-label`).
* As a **standalone annotation** on any entity — placed before the entity keyword, it
  serves as freeform rationale or commentary.

.. code-block:: none
   :caption: Syntax

   @@ <RICH_TEXT|REFERENCE>* @@

.. code-block:: req
   :caption: Example — annotation and informal requirement body

   @@
     The **main propulsion unit** of the aircraft. See {System::Requirements::Thrust}
     for the associated constraints.
   @@
   part Engine
     let max_thrust in real [N]

     requirement ThrustBound is
       @@
         The {Engine::max_thrust} shall not exceed the structural limit
         at any operating altitude.
       @@
     requirement
   part

Format
**********************

Rich Text
~~~~~~~~~~~~~~~~~~~~~~

The body of a markup block is written in Markdown, conforming to the
`CommonMark <https://commonmark.org/>`_ specification.

Commonly used formatting elements include:

* Emphasis: ``*text*`` or ``_text_``
* Strong: ``**text**``
* Headings: ``# Heading``
* Inline code: `` `code` ``
* Unordered list: ``- item``
* Maths (LatEx): ``$ math $``

.. note::

   Not all CommonMark elements may be supported by every output format. Consult the
   tooling documentation for rendering details.

Reference
~~~~~~~~~~~~~~~~~~~~~~

A *reference* embeds a traceable link to another entity directly within a markup block.
The target is identified by its path (see :ref:`reference-reference-label`).

.. code-block:: none
   :caption: Syntax

   {PATH}

.. attention::

   Escape sequences for literal ``{``, ``}``, and ``@@`` within a markup body are not
   yet specified. The characters ``{`` and ``}`` are currently reserved for references.
