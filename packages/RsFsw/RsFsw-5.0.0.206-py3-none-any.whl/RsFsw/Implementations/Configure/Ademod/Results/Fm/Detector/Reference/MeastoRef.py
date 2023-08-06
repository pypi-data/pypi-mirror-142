from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal.RepeatedCapability import RepeatedCapability
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class MeastoRef:
	"""MeastoRef commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: RefMeasurement, default value after init: RefMeasurement.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("meastoRef", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_refMeasurement_get', 'repcap_refMeasurement_set', repcap.RefMeasurement.Nr1)

	def repcap_refMeasurement_set(self, refMeasurement: repcap.RefMeasurement) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to RefMeasurement.Default
		Default value after init: RefMeasurement.Nr1"""
		self._cmd_group.set_repcap_enum_value(refMeasurement)

	def repcap_refMeasurement_get(self) -> repcap.RefMeasurement:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, trace=repcap.Trace.Default, refMeasurement=repcap.RefMeasurement.Default) -> None:
		"""SCPI: CONFigure:ADEMod:RESults:FM:DETector<det>:REFerence:MEAStoref<t> \n
		Snippet: driver.configure.ademod.results.fm.detector.reference.meastoRef.set(trace = repcap.Trace.Default, refMeasurement = repcap.RefMeasurement.Default) \n
		Sets the reference value to be used for relative demodulation results to the currently measured value on the specified
		trace for all relative detectors. If necessary, the detectors are activated. A reference value 0 would provide infinite
		results and is thus automatically corrected to 0.1. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
			:param refMeasurement: optional repeated capability selector. Default value: Nr1 (settable in the interface 'MeastoRef')
		"""
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		refMeasurement_cmd_val = self._cmd_group.get_repcap_cmd_value(refMeasurement, repcap.RefMeasurement)
		self._core.io.write(f'CONFigure:ADEMod:RESults:FM:DETector{trace_cmd_val}:REFerence:MEAStoref{refMeasurement_cmd_val}')

	def set_with_opc(self, trace=repcap.Trace.Default, refMeasurement=repcap.RefMeasurement.Default, opc_timeout_ms: int = -1) -> None:
		trace_cmd_val = self._cmd_group.get_repcap_cmd_value(trace, repcap.Trace)
		refMeasurement_cmd_val = self._cmd_group.get_repcap_cmd_value(refMeasurement, repcap.RefMeasurement)
		"""SCPI: CONFigure:ADEMod:RESults:FM:DETector<det>:REFerence:MEAStoref<t> \n
		Snippet: driver.configure.ademod.results.fm.detector.reference.meastoRef.set_with_opc(trace = repcap.Trace.Default, refMeasurement = repcap.RefMeasurement.Default) \n
		Sets the reference value to be used for relative demodulation results to the currently measured value on the specified
		trace for all relative detectors. If necessary, the detectors are activated. A reference value 0 would provide infinite
		results and is thus automatically corrected to 0.1. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param trace: optional repeated capability selector. Default value: Tr1 (settable in the interface 'Detector')
			:param refMeasurement: optional repeated capability selector. Default value: Nr1 (settable in the interface 'MeastoRef')
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:ADEMod:RESults:FM:DETector{trace_cmd_val}:REFerence:MEAStoref{refMeasurement_cmd_val}', opc_timeout_ms)

	def clone(self) -> 'MeastoRef':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = MeastoRef(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
