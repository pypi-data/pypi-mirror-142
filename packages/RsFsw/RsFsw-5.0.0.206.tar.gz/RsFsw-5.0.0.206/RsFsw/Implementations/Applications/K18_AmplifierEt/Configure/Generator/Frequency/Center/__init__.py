from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Center:
	"""Center commands group definition. 3 total commands, 2 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("center", core, parent)

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	@property
	def sync(self):
		"""sync commands group. 1 Sub-classes, 0 commands."""
		if not hasattr(self, '_sync'):
			from .Sync import Sync
			self._sync = Sync(self._core, self._cmd_group)
		return self._sync

	def set(self, frequency: float) -> None:
		"""SCPI: CONFigure:GENerator:FREQuency:CENTer \n
		Snippet: driver.applications.k18AmplifierEt.configure.generator.frequency.center.set(frequency = 1.0) \n
		This command defines the frequency of the generator. Make sure to synchronize with *OPC? or *WAI to make sure that the
		command was successfully applied on the generator before sending the next command. \n
			:param frequency: numeric value Unit: Hz
		"""
		param = Conversions.decimal_value_to_str(frequency)
		self._core.io.write(f'CONFigure:GENerator:FREQuency:CENTer {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:FREQuency:CENTer \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.generator.frequency.center.get() \n
		This command defines the frequency of the generator. Make sure to synchronize with *OPC? or *WAI to make sure that the
		command was successfully applied on the generator before sending the next command. \n
			:return: frequency: numeric value Unit: Hz"""
		response = self._core.io.query_str(f'CONFigure:GENerator:FREQuency:CENTer?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Center':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Center(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
