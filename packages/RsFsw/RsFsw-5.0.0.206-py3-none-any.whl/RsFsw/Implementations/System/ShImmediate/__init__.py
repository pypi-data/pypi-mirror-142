from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ShImmediate:
	"""ShImmediate commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("shImmediate", core, parent)

	@property
	def state(self):
		"""state commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_state'):
			from .State import State
			self._state = State(self._core, self._cmd_group)
		return self._state

	def set(self, hw_update: enums.EventOnce) -> None:
		"""SCPI: SYSTem:SHIMmediate \n
		Snippet: driver.system.shImmediate.set(hw_update = enums.EventOnce.ONCE) \n
		Executes any received remote commands that cause changes to the hardware and have not been executed yet due to a
		SYST:SHIM:STAT OFF command. \n
			:param hw_update: No help available
		"""
		param = Conversions.enum_scalar_to_str(hw_update, enums.EventOnce)
		self._core.io.write(f'SYSTem:SHIMmediate {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.EventOnce:
		"""SCPI: SYSTem:SHIMmediate \n
		Snippet: value: enums.EventOnce = driver.system.shImmediate.get() \n
		Executes any received remote commands that cause changes to the hardware and have not been executed yet due to a
		SYST:SHIM:STAT OFF command. \n
			:return: hw_update: No help available"""
		response = self._core.io.query_str(f'SYSTem:SHIMmediate?')
		return Conversions.str_to_scalar_enum(response, enums.EventOnce)

	def clone(self) -> 'ShImmediate':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = ShImmediate(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
