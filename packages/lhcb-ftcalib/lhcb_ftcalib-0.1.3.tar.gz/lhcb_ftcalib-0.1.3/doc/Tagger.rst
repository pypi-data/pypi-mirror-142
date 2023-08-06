Tagger module
=============

In ftcalib, a :class:`TaggerBase` object is a collection of Tagging data sufficient to
perform or apply a flavour tagging calibration. A tagger stores its own
calibration function in the member `func`. Two Tagger classes :class:`Tagger` and
:class:`TargetTagger` are derived from :class:`TaggerBase` (which should never be
instantiated as it is supposed to be purely virtual). :class:`Tagger` is used to run a
flavour tagging calibration while :class:`TargetTagger` is supposed to load a
calibration from file and apply it to some target data, hence the name.

.. autoclass:: Tagger.TaggerBase
   :members:
   :show-inheritance:

.. autoclass:: Tagger.Tagger
   :members:
   :undoc-members:
   :show-inheritance:
