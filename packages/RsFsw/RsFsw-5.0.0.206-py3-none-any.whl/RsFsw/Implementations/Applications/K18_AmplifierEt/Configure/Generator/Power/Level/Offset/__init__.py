from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	@property
	def ledState(self):
		"""ledState commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_ledState'):
			from .LedState import LedState
			self._ledState = LedState(self._core, self._cmd_group)
		return self._ledState

	def set(self, level: float) -> None:
		"""SCPI: CONFigure:GENerator:POWer:LEVel:OFFSet \n
		Snippet: driver.applications.k18AmplifierEt.configure.generator.power.level.offset.set(level = 1.0) \n
		This command defines a mathematical level offset for the signal generator (for example to take external attenuation into
		account) . Make sure to synchronize with *OPC? or *WAI to make sure that the command was successfully applied on the
		generator before sending the next command. \n
			:param level: numeric value Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(level)
		self._core.io.write(f'CONFigure:GENerator:POWer:LEVel:OFFSet {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:GENerator:POWer:LEVel:OFFSet \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.generator.power.level.offset.get() \n
		This command defines a mathematical level offset for the signal generator (for example to take external attenuation into
		account) . Make sure to synchronize with *OPC? or *WAI to make sure that the command was successfully applied on the
		generator before sending the next command. \n
			:return: level: numeric value Unit: dBm"""
		response = self._core.io.query_str(f'CONFigure:GENerator:POWer:LEVel:OFFSet?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Offset':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Offset(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
