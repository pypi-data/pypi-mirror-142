from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mtime:
	"""Mtime commands group definition. 3 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mtime", core, parent)

	@property
	def average(self):
		"""average commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_average'):
			from .Average import Average
			self._average = Average(self._core, self._cmd_group)
		return self._average

	def set(self, arg_0: enums.Duration, powerMeter=repcap.PowerMeter.Default) -> None:
		"""SCPI: [SENSe]:PMETer<p>:MTIMe \n
		Snippet: driver.applications.k9X11Ad.sense.pmeter.mtime.set(arg_0 = enums.Duration.LONG, powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param arg_0: No help available
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
		"""
		param = Conversions.enum_scalar_to_str(arg_0, enums.Duration)
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		self._core.io.write(f'SENSe:PMETer{powerMeter_cmd_val}:MTIMe {param}')

	# noinspection PyTypeChecker
	def get(self, powerMeter=repcap.PowerMeter.Default) -> enums.Duration:
		"""SCPI: [SENSe]:PMETer<p>:MTIMe \n
		Snippet: value: enums.Duration = driver.applications.k9X11Ad.sense.pmeter.mtime.get(powerMeter = repcap.PowerMeter.Default) \n
		No command help available \n
			:param powerMeter: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pmeter')
			:return: arg_0: No help available"""
		powerMeter_cmd_val = self._cmd_group.get_repcap_cmd_value(powerMeter, repcap.PowerMeter)
		response = self._core.io.query_str(f'SENSe:PMETer{powerMeter_cmd_val}:MTIMe?')
		return Conversions.str_to_scalar_enum(response, enums.Duration)

	def clone(self) -> 'Mtime':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Mtime(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
