from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class AmPower:
	"""AmPower commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("amPower", core, parent)

	@property
	def auto(self):
		"""auto commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_auto'):
			from .Auto import Auto
			self._auto = Auto(self._core, self._cmd_group)
		return self._auto

	def set(self, power: float) -> None:
		"""SCPI: [SENSe]:POWer:SEM:AMPower \n
		Snippet: driver.applications.k14Xnr5G.sense.power.sem.amPower.set(power = 1.0) \n
		This command defines the power of a medium range base station.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a medium range base station ([SENSe:]POWer:CATegory) .
			- Select manual definition of Tx power ([SENSe:]POWer:SEM:AMPower:AUTO) . \n
			:param power: numeric value Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'SENSe:POWer:SEM:AMPower {param}')

	def get(self) -> float:
		"""SCPI: [SENSe]:POWer:SEM:AMPower \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.power.sem.amPower.get() \n
		This command defines the power of a medium range base station.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a medium range base station ([SENSe:]POWer:CATegory) .
			- Select manual definition of Tx power ([SENSe:]POWer:SEM:AMPower:AUTO) . \n
			:return: power: numeric value Unit: dBm"""
		response = self._core.io.query_str(f'SENSe:POWer:SEM:AMPower?')
		return Conversions.str_to_float(response)

	def clone(self) -> 'AmPower':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = AmPower(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
