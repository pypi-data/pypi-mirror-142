from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.RepeatedCapability import RepeatedCapability
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands
	Repeated Capability: FreqOffset, default value after init: FreqOffset.Nr1"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)
		self._cmd_group.rep_cap = RepeatedCapability(self._cmd_group.group_name, 'repcap_freqOffset_get', 'repcap_freqOffset_set', repcap.FreqOffset.Nr1)

	def repcap_freqOffset_set(self, freqOffset: repcap.FreqOffset) -> None:
		"""Repeated Capability default value numeric suffix.
		This value is used, if you do not explicitely set it in the child set/get methods, or if you leave it to FreqOffset.Default
		Default value after init: FreqOffset.Nr1"""
		self._cmd_group.set_repcap_enum_value(freqOffset)

	def repcap_freqOffset_get(self) -> repcap.FreqOffset:
		"""Returns the current default repeated capability for the child set/get methods"""
		# noinspection PyTypeChecker
		return self._cmd_group.get_repcap_enum_value()

	def set(self, denominator: float, freqOffset=repcap.FreqOffset.Default) -> None:
		"""SCPI: SOURce:EXTernal:FREQuency:OFFSet<of> \n
		Snippet: driver.applications.k30NoiseFigure.source.external.frequency.offset.set(denominator = 1.0, freqOffset = repcap.FreqOffset.Default) \n
		No command help available \n
			:param denominator: Unit: HZ
			:param freqOffset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Offset')
		"""
		param = Conversions.decimal_value_to_str(denominator)
		freqOffset_cmd_val = self._cmd_group.get_repcap_cmd_value(freqOffset, repcap.FreqOffset)
		self._core.io.write(f'SOURce:EXTernal:FREQuency:OFFSet{freqOffset_cmd_val} {param}')

	def get(self, freqOffset=repcap.FreqOffset.Default) -> float:
		"""SCPI: SOURce:EXTernal:FREQuency:OFFSet<of> \n
		Snippet: value: float = driver.applications.k30NoiseFigure.source.external.frequency.offset.get(freqOffset = repcap.FreqOffset.Default) \n
		No command help available \n
			:param freqOffset: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Offset')
			:return: denominator: Unit: HZ"""
		freqOffset_cmd_val = self._cmd_group.get_repcap_cmd_value(freqOffset, repcap.FreqOffset)
		response = self._core.io.query_str(f'SOURce:EXTernal:FREQuency:OFFSet{freqOffset_cmd_val}?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Offset':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Offset(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
