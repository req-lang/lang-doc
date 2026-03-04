.. _reference-expression-label:

Expression
======================

An *expression* is a typed formal statement that evaluates to a value.
Expressions are present in two cases:

* In formal :ref:`reference-requirement-label` to express a property that must hold
* In :ref:`reference-attribute-label` definition to express the domain of the attribute

An expression composes several :ref:`attributes <reference-attribute-label>` in order to:

* Define a *formal property* that must hold considering the domain of the involved attributes
* Constrain an attribute to narrow its definition domain

.. attention::

   An expression is not an algorithm. There are no instructions or sequences of actions —
   only properties that must hold.


Formalism
**********************

req uses several formalisms in conjunction to produce expressions:

.. list-table:: Allowed formalisms
   :header-rows: 1

   * - Name
     - Examples
   * - Propositional logic
     - ``and``, ``or``
   * - :term:`LTL` (discrete-time)
     - ``eventually``, ``globally``
   * - :term:`FOL`
     - ``forall``, ``exists``
   * - Set theory
     - ``includes``, ``in``
   * - Common algebra
     - ``+``, ``-``


.. note::

   The current set of formalisms is a deliberate subset of what a specification may require.
   req will progressively be extended with additional constructs: the guiding criterion is
   that any new construct must be expressible in standard formal notation and relevant for
   systems engineers.


The :ref:`attributes <reference-attribute-label>` used in expression are considered time-dependent function.
More precisely, let's suppose an attribute is defined by a requirement to be:

.. math::

   x = f(y, z)

Where :math:`f` denotes an expression. It is assumed that :math:`x`, :math:`y` and :math:`z` are function of time ie.


.. math::

   \forall t\ x(t) = f(y(t), z(t))

As a corollary :math:`x` is constant if and only if :math:`y` and :math:`z` are constants (literals for instance).

.. note::

  Unless explicitely stated by temporal operators, the attributes constraints hold for all :math:`t`, meaning during the whole lifecycle, for all operating conditions. One can further refine the modeling of the operating conditions or lifecycle by introducing attributes to discriminate between those. 


Type system
**********************

The *type* of an expression defines which operators can be applied to it.
An :ref:`attribute <reference-attribute-label>` has a type that is inferred from its domain definition.

Operators in req are strictly discriminated by type: applying an operator to an incompatible is not allowed.

If a type cannot be inferred, the expression has the type *undefined*, which is not a true
type but denotes the absence of typing information.

.. attention::

   While there is currently no mechanism to define a custom type, this is subject to change.


.. _reference-type-number-label:

Number
~~~~~~~~~~~~~~~~~~~~~~

The type ``Number`` covers all numerical values, including integers and real numbers.
No distinction is made between them in the type system.

.. _reference-type-boolean-label:

Boolean
~~~~~~~~~~~~~~~~~~~~~~

The type ``Boolean`` is applied to any boolean expression.

.. _reference-type-set-label:

Set
~~~~~~~~~~~~~~~~~~~~~~

The type ``Set`` is applied to any expression that evaluates to a set.
Sets are homogeneous in the sense that they can only contain elements of the same type.

Literals
**********************

A *literal* is a value written directly in the expression source.

Numbers
~~~~~~~~~~~~~~~~~~~~~~

Numbers are written in decimal format and may use exponential notation.

.. code-block:: none 
   :caption: Example of numbers

    2
    3.14
    10e7

``infinity`` represents an infinite value. Values are of type :ref:`reference-type-number-label`.

.. note::

   No distinction is made between integers and real numbers at the type level.
   Fractional expressions such as ``1/3`` are evaluated as arithmetic operations, not
   written as decimal literals.

Boolean
~~~~~~~~~~~~~~~~~~~~~~

The Boolean literals ``true`` and ``false`` represent the two truth values.

.. code-block:: none 
   :caption: Booleans

    true
    false

Values are of type :ref:`reference-type-boolean-label`.

Undefined
~~~~~~~~~~~~~~~~~~~~~~

The literal ``undefined`` represents a value that has been explicitly left unspecified.

.. code-block:: req
   :caption: undefined

    undefined

.. note::

   Undefined values are useful for relaxing a constraint when certain conditions are met.

Set
~~~~~~~~~~~~~~~~~~~~~~

The set literal allows creating an ad-hoc set with a finite number of elements:

.. code-block:: none
   :caption: Syntax of set

   { <EXPRESSION (, EXPRESSION)+|EXPRESSION?> }

.. code-block:: req
   :caption: Example of set literal

   {1, 2, 3}

Values are of type :ref:`reference-type-set-label`. Expressions must have the same type.

Built-in set
~~~~~~~~~~~~~~~~~~~~~~

A built-in set is a keyword that denotes a well-known set:

.. code-block:: none
   :caption: Built-in sets

   real
   boolean
   integer

.. note::

   Built-in sets are most commonly used as the domain of an
   :ref:`attribute <reference-attribute-label>`.

Values are of type :ref:`reference-type-set-label`. Element type varies according to the built-in set.

Operators
**********************

An *operator* is an expression that contains one or several attributes or literals.
Each operator is described with a formal equivalent which allows to translate the req expression into a logical and mathematical expression.

.. note::

   The convention will be that ``x`` and ``y`` represents values which are not domains (sets), whereas ``X`` and ``Y`` represents domains.

Arithmetic
~~~~~~~~~~~~~~~~~~~~~~

Arithmetic operators act on :ref:`reference-type-number-label` and evaluate to :ref:`reference-type-number-label`.

.. list-table:: Arithmetic operators
   :header-rows: 1

   * - Syntax
     - Description
     - Formal equivalence
   * - ``x + y``
     - Addition
     - :math:`x + y`
   * - ``x - y``
     - Subtraction
     - :math:`x - y`
   * - ``x * y``
     - Multiplication
     - :math:`x \cdot y`
   * - ``x / y``
     - Division
     - :math:`x / y`
   * - ``x % y``
     - Remainder
     - :math:`x \bmod y`
   * - ``x ^ y``
     - Exponentiation
     - :math:`x^{y}`
   * - ``-x``
     - Unary negation
     - :math:`-x`
   * - ``+x``
     - Unary identity
     - :math:`+x`
   * - ``x!``
     - Factorial
     - :math:`x!`

Comparison
~~~~~~~~~~~~~~~~~~~~~~

Comparison operators act on :ref:`reference-type-number-label` and evaluate to
:ref:`reference-type-boolean-label`.

.. list-table:: Comparison operators
   :header-rows: 1

   * - Syntax
     - Description
     - Formal equivalence
   * - ``x = y``
     - True if x and y are equal
     - :math:`x = y`
   * - ``x /= y``
     - True if x and y are not equal
     - :math:`x \neq y`
   * - ``x < y``
     - True if x is strictly less than y
     - :math:`x < y`
   * - ``x > y``
     - True if x is strictly greater than y
     - :math:`x > y`
   * - ``x <= y``
     - True if x is less than or equal to y
     - :math:`x \leq y`
   * - ``x >= y``
     - True if x is greater than or equal to y
     - :math:`x \geq y`

Propositional logic
~~~~~~~~~~~~~~~~~~~~~~

Propositional logic operators act on :ref:`reference-type-boolean-label` and evaluate to :ref:`reference-type-boolean-label`.

.. list-table:: Propositional logic operators
   :header-rows: 1

   * - Syntax
     - Description
     - Formal equivalence
   * - ``x and y``
     - True if both x and y are true
     - :math:`x \wedge y`
   * - ``x or y``
     - True if at least one of x or y is true
     - :math:`x \vee y`
   * - ``x xor y``
     - True if exactly one of x or y is true
     - :math:`x \oplus y`
   * - ``x implies y``
     - True if x is false or x and y are true
     - :math:`x \Rightarrow y`
   * - ``x iff y``
     - True if x and y have the same truth value
     - :math:`x \Leftrightarrow y`
   * - ``not x``
     - True if x is false
     - :math:`\neg x`

Set
~~~~~~~~~~~~~~~~~~~~~~

The following operators act on :ref:`reference-type-set-label` and evaluate to :ref:`reference-type-set-label`.

.. list-table:: Set algebra operators
   :header-rows: 1

   * - Syntax
     - Description
     - Formal equivalence
   * - ``X union Y``
     - Elements belonging to X or Y
     - :math:`X \cup Y`
   * - ``X intersection Y``
     - Elements belonging to both X and Y
     - :math:`X \cap Y`
   * - ``X difference Y``
     - Symmetric difference of X and Y 
     - :math:`X \Delta Y = X \cup Y \backslash X \cap Y`
   * - ``X complement Y``
     - Elements of Y that are not in X
     - :math:`Y \backslash X`

The following operators act on :ref:`reference-type-set-label` and evaluate to :ref:`reference-type-boolean-label`.

.. list-table:: Set predicate operators
   :header-rows: 1

   * - Syntax
     - Description
     - Formal equivalence
   * - ``x in X``
     - True if x is an element of X
     - :math:`x \in X`
   * - ``X includes Y``
     - True if Y is a subset of X
     - :math:`Y \subseteq X`


Temporal logic
~~~~~~~~~~~~~~~~~~~~~~

Temporal logic operators act on :ref:`reference-type-boolean-label` and evaluate to
:ref:`reference-type-boolean-label`. They express properties over a discrete sequence
of time steps. See :term:`LTL` for the underlying formalism.

.. list-table:: Temporal logic operators
   :header-rows: 1

   * - Syntax
     - Description
     - Formal equivalence
   * - ``always x``
     - True if x holds at every future time step
     - :math:`\square x`
   * - ``eventually x``
     - True if x holds at some future time step
     - :math:`\lozenge x`
   * - ``previously x``
     - True if x held at the immediately preceding time step
     - :math:`\ominus x`
   * - ``rising x``
     - True at the first time step where x becomes true
     - :math:`\neg x_{t-1} \wedge x_{t}`
   * - ``falling x``
     - True at the first time step where x becomes false
     - :math:`x_{t-1} \wedge \neg x_{t}`
   * - ``x since y``
     - True if x has been true at every step since the last step where y was true
     - :math:`x \,\mathcal{S}\, y`

.. note::

   The notion of time step does not refer to a particular time division and sampling, one can consider that time steps are just an arbitrary division that splits continuous time into event points that changes states (ie. the value of the attributes).

Aggregator
~~~~~~~~~~~~~~~~~~~~~~

An *aggregator*  take a list of arguments and evaluates to a single value. 

.. code-block:: none
   :caption: Syntax

   <all|any> EXPRESSION (, EXPRESSION)* end

.. list-table:: Aggregators
   :header-rows: 1

   * - Syntax
     - Description
     - Formal equivalence
   * - ``all x1, x2, ... end``
     - True if all arguments are true
     - :math:`\bigwedge x_i`
   * - ``any x1, x2, ... end``
     - True if at least one argument is true
     - :math:`\bigvee x_i`

.. note::

   Boolean aggregators are the list counterparts of ``and`` and ``or``: ``all e1, e2 end`` is
   equivalent to ``e1 and e2``, and ``any e1, e2 end`` is equivalent to ``e1 or e2``.

Conditional
**********************

A *conditional* is a notation for expressing a requirement that depends on one or more conditions.
It is a direct equivalent of a propositional pattern and does not add expressive power — only readability.

Branch
~~~~~~~~~~~~~~~~~~~~~~

The *branch* conditional is an expression whose content depends on a condition:

.. code-block:: none
   :caption: Syntax

    if EXPRESSION then EXPRESSION
    (else EXPRESSION)?
    end

.. code-block:: req
   :caption: Example of if

    requirement R is
     if doors_open then speed = 0
     else speed < 25
     end
    requirement

Let :math:`c` denote the condition, :math:`x` the consequence (the expression when the condition is true) and :math:`y` the fallback.
The if-else expression is strictly equivalent to:

.. math::

   (c \Rightarrow x) \wedge (\neg c \Rightarrow y)

If the else branch is not defined, :math:`y` is taken equal to true by convention, that is, the expression becomes:

.. math::

  c \Rightarrow x

All expressions must be of type :ref:`reference-type-boolean-label`.

When
~~~~~~~~~~~~~~~~~~~~~~

The *when* conditional is an expression governed by a set of unordered conditions:

.. code-block:: none
   :caption: Syntax

    when
      EXPRESSION then EXPRESSION
      (, EXPRESSION then EXPRESSION)*
      (otherwise EXPRESSION)?
    end

.. code-block:: req
   :caption: Example of when

    requirement R is
     when
      doors_open then speed = 0,
      weather_is_bad then speed < 10,
      otherwise speed < 25
     end
    requirement

Let :math:`c_i` denote the conditions, :math:`x_i` the consequences for each condition and :math:`y` the fallback. The when expression is strictly equivalent to:

.. math::

  \left(\bigwedge_i c_i \Rightarrow x_i\right) \wedge \left(\left(\bigwedge_i \neg c_i\right) \Rightarrow y\right)

If the otherwise branch is not defined, :math:`y` is taken equal to true by convention, which simplifies the expression:

.. math::

  \bigwedge_i c_i \Rightarrow x_i


All expressions must be of type :ref:`reference-type-boolean-label`.

.. note::

  This construct is particularly useful when multiple conditions govern a requirement simultaneously —
  for instance, when specifying an event-action mechanism such as a state machine.

Quantifiers
**********************

A *quantifier* is an expression that evaluates over the elements of a set.
By convention, in this section, :math:`x` denotes the identifier, :math:`X` the domain (expression after the ``in``), :math:`P(x)` the filter (expression after the ``such that``). 

.. _reference-forall-label:

Forall
~~~~~~~~~~~~~~~~~~~~~~

The *forall* quantifier is strictly equivalent to the universal quantifier of first-order logic :math:`\forall`.

.. code-block:: none
   :caption: Syntax

    forall IDENTIFIER in EXPRESSION (such that EXPRESSION)?
      EXPRESSION
    end

.. code-block:: req
   :caption: Example of forall

    requirement R is
      forall t in train_units such that t::speed = 0
        t::alarm_triggered
      end
    requirement

The expression evaluates to :ref:`reference-type-boolean-label`.
Denote the body expression :math:`Q(x)`; the forall block is strictly equivalent to:

.. math::

   \forall x \in X,\ P(x) \Rightarrow Q(x)

When the ``such that`` clause is omitted, :math:`P(x)` is taken equal to :math:`\text{true}`, which simplifies to:

.. math::

   \forall x \in X,\ Q(x)

.. note::

   If the domain is empty, ``forall`` evaluates to ``true`` (vacuous truth).

.. _reference-exists-label:

Exists
~~~~~~~~~~~~~~~~~~~~~~

The *exists* quantifier is strictly equivalent to the existential quantifier of first-order logic :math:`\exists`.

.. code-block:: none
   :caption: Syntax

    exists IDENTIFIER in EXPRESSION
      such that EXPRESSION
    end

.. code-block:: req
   :caption: Example of exists

    requirement R is
      exists t in train_units such that t::ready_for_departure
      end
    requirement

The expression evaluates to :ref:`reference-type-boolean-label`.
Unlike ``forall``, ``exists`` has no body expression: the ``such that`` clause is the predicate.
The exists block is strictly equivalent to:

.. math::

   \exists x \in X,\ P(x)

.. note::

   If the domain is empty, ``exists`` evaluates to ``false``.

.. _reference-select-label:

Select
~~~~~~~~~~~~~~~~~~~~~~

The *select* quantifier has no first-order logic equivalent. It expresses the choice of an element within a set.

.. code-block:: none
   :caption: Syntax

    select IDENTIFIER in EXPRESSION (such that EXPRESSION)?
      (<maximizes|minimizes> EXPRESSION)?
    end

.. code-block:: req
   :caption: Example of select

    requirement R is
      closest_plane = select p in managed_planes
        minimizes p::distance_to_runway_threshold
      end
    requirement

The expression evaluates to an element drawn from the input domain. The optional ``maximizes`` or ``minimizes`` part is called the *optimizer*.

.. attention::

   If the input domain is empty, the evaluation of the select is undefined.

Denote :math:`a` the value the select block evaluates to and :math:`f(x)` the optimizer expression.
Suppose the optimizer is a maximization; :math:`a` has the following property:

.. math::

  a \in X \wedge a = \underset{x \in X,\, P(x)}{\mathrm{argmax}}\ f(x)

The minimization case is symmetric:

.. math::

  a \in X \wedge a = \underset{x \in X,\, P(x)}{\mathrm{argmin}}\ f(x)

When no optimizer is specified, the select only guarantees:

.. math::

  a \in X

.. note::

   The choice is non-deterministic. Using the non-optimized form is useful to constrain intermediate
   attributes or quantities that serve as inputs to other requirements.
