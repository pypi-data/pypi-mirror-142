from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 6 total commands, 4 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def offset(self):
		"""offset commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_offset'):
			from .Offset import Offset
			self._offset = Offset(self._core, self._cmd_group)
		return self._offset

	@property
	def factor(self):
		"""factor commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_factor'):
			from .Factor import Factor
			self._factor = Factor(self._core, self._cmd_group)
		return self._factor

	@property
	def sweep(self):
		"""sweep commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sweep'):
			from .Sweep import Sweep
			self._sweep = Sweep(self._core, self._cmd_group)
		return self._sweep

	@property
	def coupling(self):
		"""coupling commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_coupling'):
			from .Coupling import Coupling
			self._coupling = Coupling(self._core, self._cmd_group)
		return self._coupling

	def set(self, frequency: float, externalGen=repcap.ExternalGen.Nr1) -> None:
		"""SCPI: SOURce:EXTernal<gen>:FREQuency \n
		Snippet: driver.source.external.frequency.set(frequency = 1.0, externalGen = repcap.ExternalGen.Nr1) \n
		This command defines a fixed source frequency for the external generator. This command is only valid if External
		Generator Control (R&S FSW-B10) is installed. \n
			:param frequency: Source frequency of the external generator. Unit: HZ
			:param externalGen: optional repeated capability selector. Default value: Nr1
		"""
		param = Conversions.decimal_value_to_str(frequency)
		externalGen_cmd_val = self._cmd_group.get_repcap_cmd_value(externalGen, repcap.ExternalGen)
		self._core.io.write(f'SOURce:EXTernal{externalGen_cmd_val}:FREQuency {param}')

	def get(self, externalGen=repcap.ExternalGen.Nr1) -> float:
		"""SCPI: SOURce:EXTernal<gen>:FREQuency \n
		Snippet: value: float = driver.source.external.frequency.get(externalGen = repcap.ExternalGen.Nr1) \n
		This command defines a fixed source frequency for the external generator. This command is only valid if External
		Generator Control (R&S FSW-B10) is installed. \n
			:param externalGen: optional repeated capability selector. Default value: Nr1
			:return: frequency: Source frequency of the external generator. Unit: HZ"""
		externalGen_cmd_val = self._cmd_group.get_repcap_cmd_value(externalGen, repcap.ExternalGen)
		response = self._core.io.query_str(f'SOURce:EXTernal{externalGen_cmd_val}:FREQuency?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
