from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	@property
	def link(self):
		"""link commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_link'):
			from .Link import Link
			self._link = Link(self._core, self._cmd_group)
		return self._link

	def set(self, frequency: float, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: [SENSe]:PMETer<p>:FREQuency \n
		Snippet: driver.applications.k14Xnr5G.sense.pmeter.frequency.set(frequency = 1.0, powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param frequency: No help available
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SENSe:PMETer{powerMeter_cmd_val}:FREQuency {param}')

	def get(self, powerMeter=repcap.PowerMeter.Default) -> float:
		"""SCPI: [SENSe]:PMETer<p>:FREQuency \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.pmeter.frequency.get(powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: frequency: No help available"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SENSe:PMETer{powerMeter_cmd_val}:FREQuency?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
