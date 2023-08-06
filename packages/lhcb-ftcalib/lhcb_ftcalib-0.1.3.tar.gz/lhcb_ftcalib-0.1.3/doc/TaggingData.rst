TaggingData module
==================

Every :class:`Tagger` object owns an object of type :class:`TaggingData` to keep track
of the tagging statistics and tagging performances. This data can be accessed under the 
`stats` member of a :class:`Tagger` object and does not need to be instantiated by hand.
In fact, it should not be instantiated by hand, as a Tagger objects updates
the internal data of its :class:`TaggingData` members.

Conventions
-----------

* A tagged event is an event with nonzero tagging decision

  **Edge cases**
    * :math:`\omega>0.5`: Counts as untagged and is truncated to :math:`\omega\equiv 0.5, d\equiv 0`.
    * :math:`\omega<0`: Counts as tagged but mistag is truncated to :math:`\omega\equiv 0`
      as otherwise link functions may crash and such values are not well motivated.
    * :math:`\omega\in(0, 0.5)\wedge d=0`: counts as untagged by the main definition.
    * :math:`\omega=0.5\wedge d\neq 0`: Events counts as tagged.
* A selected event is every event which the user has selected via the `selection` argument when constructing the tagger

.. autoclass:: TaggingData.TaggingData
   :members:
   :undoc-members:
   :show-inheritance:
