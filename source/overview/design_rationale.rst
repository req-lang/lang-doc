Design Rationale
======================

This section explains the core design decision that have been made during the development of the req language.
These key decisions explain why req looks the way it does, what it deliberately sacrifices and what problems are considered out of scope.

This rationale is opinionated and made to be challenged on future versions of the language. The main intent is to provide constitutional decisions and derive core characteristics that will guide the whole language design.

.. note:: This section focuses on pure language related design decision. Governance and methodology is considered out of scope.


.. _document-model-bridge-label:
Documents-model bridge
**********************

*The req aims at providing a way to bridge between document-based systems engineering and model-based systems engineering.*

Observation
~~~~~~~~~~~~~~~~~~~~~~

While model based approach are getting more and more popular, one can observe that modeling becomes less and less connected to the actual engineering artifacts that are produced by engineers during system lifecycle.

Basically, :ref:`MBSE` nowadays feels like drawing boxes and arrows rather than thinking the systems. Translating these models to other engineers adds overload and creates friction which kills the benefits of the modeling effort.

More precisely, model based systems engineering requires to leverage concepts that are getting further away from actual engineering, thus making adoption by engineers more difficult and using it quite abstract. 

Another interesting point is that despite the claimed raise of models, systems lifecycle is still governed by requirements and documents. One of the primary role of any modeler software is to provide document generation. This can be explained by several facts:

* Not every stakeholder understands the diagram or models, and should not be expected to 
* Not every system property, assumption or goal can be relevantly represented as a diagram
* Systems are primarily designed from requirements living in one or several contracts
* The system architecture and design should reflect the expectations of the contracts

Decisions
~~~~~~~~~~~~~~~~~~~~~~

The req language takes the following approach: start with already existing documents, gather those into req specifications, model as you go by introducing concepts and definitions from the bare text.

The key concepts and terms are then explicitly referenced within the specification and the relation between those arises from the text. This is your actual model, no need to introduce labeled arrows and boxes. And since it starts from your actual documents, one can understand purely by reading text without being provided with a complex framework.

.. note::  In concrete terms, you start with the sentence "The system shall have a temperature of 30C", then you extract "System" and "temperature" and put in glossary. Finally you rephrase `The System::temperature shall be equal to 30C`.


Limitations
~~~~~~~~~~~~~~~~~~~~~~

While this approach provides a lot of flexibility and makes modeling occur with no effort, it is still preferable to standardize the terminology and provide things such as requirements boilerplate to have a sound model. With SysML in contrast a significant part of the terminology and boilerplate is avoided thanks to concepts standardization.

To mitigate this fact, it is preferable to rigorously define boilerplate and terminology as early as possible during the specification effort. Patterns such as :term:`EARS` in conjunction with standardized ontology and rich glossary are the alternative way to go.

Requirements-centric
**********************

*The req provides a single atomic concept to model every property of the system: the requirements.*

.. note:: By requirements we mean every expectation or assumption that is stated in a specification.

Observation
~~~~~~~~~~~~~~~~~~~~~~

As stated in the previous section, systems are primarily designed on a contractual basis, which make the organization developing the systems accountable for the satisfaction of contract requirements.

While it seems that state-of-the-art model are gaining traction in the matter of being legal basis and justification for requirements satisfaction, this is not consensual and models often requires to be backed by plain text statements that explicitly states what is required from a diagram or model artifact.

Furthermore, when it comes to stakeholder needs, one can observe that diagrams are often very subjective and language such as BPML are just basic sentences decomposition, so why not just write the sentence and extract the diagrams when convenient ? Often, requirements start as back-of-the-envelope sentences acknowledged during meetings and having a requirement-centric approach captures this fact.

At the opposite of the design process, when it comes to detailed design expectations, the requirements satisfaction is often evaluate by:

1. Refining requirements to match the adequate level of detail for verification
2. Determining a test procedure for the requirements

Considering the first aspect, the set of modeling abstraction that could capture all the required concepts to match any domain specific detailed requirements is extremely broad and it is unrealistic to design a language trying to achieve that.

Decisions
~~~~~~~~~~~~~~~~~~~~~~

Considering what have been stated above, the req language will essentially articulate specifications around requirements. But allowing these to be as precise and refined as possible, read the :ref:`progressively-formal-label` part in order to better understand how this could be achieved.

The specification flows from high to low level requirements via explicit traceability links, expectation chain is preserved while each stakeholder can write his expectations in the language that is the most adequate.

This allows to keep the set of concepts required to understand the req as small as possible, and therefore simplifies learning.

Limitations
~~~~~~~~~~~~~~~~~~~~~~

The first limitation is that duplication of concept can quickly appear, imagine the following example, the marketing team denotes a sub-system attribute "available power", while the mechanical engineering team already uses another term but refer to the same concept. How can the two teams be triggered about the fact that they are implicitly manipulating the same concept ?

The mitigation for that reveals an advantage, as the req language provide first-class definitions of concepts and terms, one can browse each concept even if those are not coming from the same domain and challenge the duplication. The process encourages stakeholder to raise questions whenever concept are unclear, which elicits knowledge and make definitions explicit.

Another limitation is that the language currently does not allow for differentiation between goals, needs, expectations and other characteristics of requirements. This might be quite confusing for a reader to understand why an expectation should be meet and where it comes from even with traceability.

The current mitigation regarding that matter is to use the provided tagging system to add meta-information about a requirement and keep clear the intent of the requirement.

.. note:: This limitation is one of the most significative weakness of the req language and might be addressed in the future version via expecation/assumption mechanisms.

.. _progressively-formal-label:
Progressively-formal
**********************

*The req language allows to write plain English as well as pure formal requirements, with the least amount limitation regarding the formalism used.*

.. note:: Here formal means, logics and maths, including set theory, discrete and (continuous planned) temporal logics, ...

Observation
~~~~~~~~~~~~~~~~~~~~~~

As observed in the :ref:`language-landscape-label` section, whether we are considering formal or modeling languages, each comes with a restricted set of abstraction and often its own custom constructs to provide formal expressiveness. For example SysMLv2 has action, states, port, interfaces, ... TLA+ is closer to pure maths but designed around model-checking rather than requirements expressiveness.

While this is justified by the need of providing consistent tooling such a execution and graphs for SysMLv2 or model checking for TLA+, this is one of the most important adoption killer. When a systems engineer faces the question of formalism, it will have the following choices:

1. Select a concept heavy SysML, maybe with a framework, but being restricted and require customization to extend syntax
2. Select a task-focused language such as TLA+ but being restricted on the semantics 
3. Use English everywhere and deal with specific aspects latter on a case-by-case basis

In the first case, having the adequate level of expressiveness requires a heavy upfront effort at organization scale and the benefits are only expected on the long run, after several projects, considering that nothing will be obsolete by the time reuse happens. And while some framework and customization might already be in place in the organization, these are still a liability of the organization cause it requires customized tooling, documentation, ...

The second choice is difficult to justify since pure formal language are notoriously difficult to handle and are not designed to cover the variety of case required by systems engineering. Engineers will end up with a variety of formal models targeting specific needs but with no clear source of truth or indication on provenance. Again, this is a liability and it is worth the effort when dealing with very specific cases such as safety critical systems.

Sadly, the third choice is the most pragmatic one, while being ambiguous, mostly unprovable and poorly machine-readable, it is this only formalism that guarantees for systems engineers that every stakeholder will be able to express itself with no limitation and that can gather all the systems specification.

This is one of the key observation regarding actual state-of-the-art :term:`MBSE` and surrounding topics, there is no one to govern them all language that permits broad adoption while retaining both machine-readable and human-readable semantics.

Decisions
~~~~~~~~~~~~~~~~~~~~~~

The decision seems quite simple but has deep implications: what can be written using maths, logic or English, should be writable in req. While this statement seems very bold at first, it has to be understood more like a long term design direction.

In practice, the goal is to provide the ability to the express 20% of the actual maths and logic syntax that makes up for 80% of the requirements. This will progressively eliminates the need to use English for requirements while keeping it for high-level specifications or very specific aspects of the specification. Thus, providing as unambiguous requirements as possible, as early as possible in the system lifecycle.

Another key decision is that the formalism that is used for the formal req language should be as easy to read and close to English as possible. Reading or writing a formal requirement should be encouraged and should require the least amount of cognitive effort. In other words, it should be natural to use it.

Think of the language as a common interface between other language that are more specific or oriented around a particular aspect, the req should be translatable into any of those formats.


.. note:: Lets take a concrete example, above we rephrased an example requirements `System::temperature shall be equal to 30C`, using the req we will simply use `System::temperature = 30`. Here the unit is explicit from the definition of `temperature` but could also be made explicit from the expression. This kind of requirements are the bread and butter of specification and we proceed by analogy with this case to discover the 20% relevant percent of formal syntax.

  An arithmetic constraint on a physical quantity, a simple temporal invariant, or a boolean condition already covers the vast majority of verifiable requirements in embedded systems.

Limitations
~~~~~~~~~~~~~~~~~~~~~~

The first limitation that comes is that rich expressiveness allows for the author the write unsound expressions or that have no way to be proven. In other words, the set of syntactically valid expressions is expected to be much greater than the set of semantically valid expressions.

This is mitigated by the fact that the tooling around req should be able to detect unsound expressions such as tautologies, contradictory facts, unsatisfactory expressions, ... Furthermore, this limitation can also be perceived as an advantage considering that the author would have written this expression in English with no warning or guard whereas here, the syntax first constraints the expressions, then the tooling analyzes it, which is much richer.

Another limitation is that while part of the specification can be made provable and tested in simulation, some will not because of unsoundness (as explained above) or because of theoretical limits of computability. 

There is no actual mitigation regarding that fact, but since req should be translatable, it should check whether an expression is reaching any kind of theoretical limits that blocks its translation. This provides a guard regarding the computability aspects of the verification for a given expression.


Text-first
**********************

*req focuses on giving a comprehensive pure text representation of a requirements specification, with no graphical annotations*

Observation
~~~~~~~~~~~~~~~~~~~~~~

While requirements have almost always been managed by databases, one could argue that this causes several issues:

* Vendor-locking from requirements management vendor software
* Hard to browse requirements and structure for LLM
* Performance (speed) penalty when processing requirements 
* Difficulty to represent expressions, references in text, ...
* Hard to use agile (git) based workflows for specification review, configuration management, ...

This point is clearly acknowledged by practitioners and is discussed since the development of SysMLv2. But what is less consensual is the presence or not of graphical annotation. One can observe that graphical annotation are annoying to manage via git and that most of the time it is vendor related information that strongly depends on the client software.

Furthermore, when it comes to developing editors or a graphical notation, it is often observed that a lot of time is lost drawing and moving graphical elements for presentation purposes rather than doing actual thinking on the system.

Decision
~~~~~~~~~~~~~~~~~~~~~~

The req will be purely text based and graphical representation are the responsibility of the client software that reads the specification. Furthermore the format used for the req language will focus only on specification information that is worth being version controlled.

Limitations
~~~~~~~~~~~~~~~~~~~~~~

It might be harder to develop a graphical notation as it has been done for SysMLv2, the req language takes starts from the opposite, text-first then maybe graphics.

Another drawback is that meta-information related to an element of the language could a priori not be parsed easily by the req tooling. Specific formats that might be used (JSON, programming language, ...) in the meta part of the specs will be considered plain-text.

Wrapping up
**********************

From the grounding decisions explained above, it appears that the req language will have the following desired characteristics:

* *Agnostic* do neither provide or impose any specific modeling or writing framework
* *Expressiveness-focused* do not enforce formal expressions, encourage usage progressively, from English to maths
* *Verifiable* formal requirements could be verifiable by translating to adequate software
* *Source of truth* by its gathering nature, the req can provide a requirements source of truth 
* *Human-readable* source files should contain mostly English or formal but simple to read expressions
* *Machine-readable* source files have enough structure to be well interpreted by a compiler or an LLM
* *Interoperable* should offer straightforward ways to translate to most of the language cited in :ref:`language-landscape-label`
