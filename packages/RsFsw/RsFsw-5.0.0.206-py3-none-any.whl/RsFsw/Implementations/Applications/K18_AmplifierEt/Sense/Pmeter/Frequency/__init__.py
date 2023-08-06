from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


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

	def set(self, frequency: float) -> None:
		"""SCPI: [SENSe]:PMETer:FREQuency \n
		Snippet: driver.applications.k18AmplifierEt.sense.pmeter.frequency.set(frequency = 1.0) \n
		This command defines the frequency of the power sensor. \n
			:param frequency: The available value range is specified in the data sheet of the power sensor in use. Unit: HZ
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'SENSe:PMETer:FREQuency {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:PMETer:FREQuency \n
		Snippet: value: float = driver.applications.k18AmplifierEt.sense.pmeter.frequency.get() \n
		This command defines the frequency of the power sensor. \n
			:return: frequency: The available value range is specified in the data sheet of the power sensor in use. Unit: HZ"""
		response = self._core.io.query_str(f'SENSe:PMETer:FREQuency?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Frequency':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Frequency(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
