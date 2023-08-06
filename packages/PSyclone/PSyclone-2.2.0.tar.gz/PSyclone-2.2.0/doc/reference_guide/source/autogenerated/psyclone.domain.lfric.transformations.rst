=========================================
``psyclone.domain.lfric.transformations``
=========================================

.. automodule:: psyclone.domain.lfric.transformations

   .. contents::
      :local:


Submodules
==========

.. toctree::

   psyclone.domain.lfric.transformations.lfric_alg_trans
   psyclone.domain.lfric.transformations.lfric_extract_trans
   psyclone.domain.lfric.transformations.lfric_invokecall_trans
   psyclone.domain.lfric.transformations.lfric_loop_fuse_trans

.. currentmodule:: psyclone.domain.lfric.transformations


Classes
=======

- :py:class:`LFRicExtractTrans`:
  Dynamo0.3 API application of ExtractTrans transformation     to extract code into a stand-alone program. For example:

- :py:class:`LFRicLoopFuseTrans`:
  Dynamo0.3 API specialisation of the

- :py:class:`LFRicInvokeCallTrans`:
  Transform a generic PSyIR representation of an Algorithm-layer

- :py:class:`LFRicAlgTrans`:
  Transform a generic PSyIR representation of the Algorithm layer to


.. autoclass:: LFRicExtractTrans
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: LFRicExtractTrans
      :parts: 1

.. autoclass:: LFRicLoopFuseTrans
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: LFRicLoopFuseTrans
      :parts: 1

.. autoclass:: LFRicInvokeCallTrans
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: LFRicInvokeCallTrans
      :parts: 1

.. autoclass:: LFRicAlgTrans
   :members:

   .. rubric:: Inheritance
   .. inheritance-diagram:: LFRicAlgTrans
      :parts: 1
