from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Reference:
	"""Reference commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("reference", core, parent)

	@property
	def meastoRef(self):
		"""meastoRef commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_meastoRef'):
			from .MeastoRef import MeastoRef
			self._meastoRef = MeastoRef(self._core, self._cmd_group)
		return self._meastoRef

	def set(self, ref_value: float, trace=repcap.Trace.Default) -> None:
		"""SCPI: CONFigure:ADEMod:RESults:ACV:DETector<det>:REFerence \n
		Snippet: driver.configure.ademod.results.acv.detector.reference.set(ref_value = 1.0, trace = repcap.Trace.Default) \n
		No command help available \n
			:param ref_value: No help available
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
		"""
		param = Conversions.decimal_value_to_str(ref_value)
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		self._core.io.write(f'CONFigure:ADEMod:RESults:ACV:DETector{trace_cmd_val}:REFerence {param}')

	def get(self, trace=repcap.Trace.Default) -> float:
		"""SCPI: CONFigure:ADEMod:RESults:ACV:DETector<det>:REFerence \n
		Snippet: value: float = driver.configure.ademod.results.acv.detector.reference.get(trace = repcap.Trace.Default) \n
		No command help available \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
			:return: ref_value: No help available"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		response = self._core.io.query_str(f'CONFigure:ADEMod:RESults:ACV:DETector{trace_cmd_val}:REFerence?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Reference':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Reference(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
