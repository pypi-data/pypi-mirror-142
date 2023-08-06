from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Length:
	"""Length commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("length", core, parent)

	@property
	def mode(self):
		"""mode commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_mode'):
			from .Mode import Mode
			self._mode = Mode(self._core, self._cmd_group)
		return self._mode

	def set(self, length: float) -> None:
		"""SCPI: [SENSe]:ADEMod:ZOOM:LENGth \n
		Snippet: driver.sense.ademod.zoom.length.set(length = 1.0) \n
		The command allows you to define the length of the time domain zoom area for the analog-demodulated measurement data in
		the specified window manually. If the length is defined manually using this command, the zoom mode is also set to manual. \n
			:param length: Unit: S Length of the zoom area in seconds.
		"""
		param = Conversions.decimal_value_to_str(length)
		self._core.io.write(f'SENSe:ADEMod:ZOOM:LENGth {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:ADEMod:ZOOM:LENGth \n
		Snippet: value: float = driver.sense.ademod.zoom.length.get() \n
		The command allows you to define the length of the time domain zoom area for the analog-demodulated measurement data in
		the specified window manually. If the length is defined manually using this command, the zoom mode is also set to manual. \n
			:return: length: Unit: S Length of the zoom area in seconds."""
		response = self._core.io.query_str(f'SENSe:ADEMod:ZOOM:LENGth?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'Length':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Length(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
