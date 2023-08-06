from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:POWer:SEM:AMPower:AUTO \n
		Snippet: driver.applications.k14Xnr5G.sense.power.sem.amPower.auto.set(state = False) \n
		This command selects how the R&S FSW determines the power of a medium range base station.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a medium range base station ([SENSe:]POWer:CATegory) . \n
			:param state: ON | 1 Automatically determines the Tx power. OFF | 0 Define a Tx power manually with [SENSe:]POWer:SEM:AMPower.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:POWer:SEM:AMPower:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:SEM:AMPower:AUTO \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.power.sem.amPower.auto.get() \n
		This command selects how the R&S FSW determines the power of a medium range base station.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a medium range base station ([SENSe:]POWer:CATegory) . \n
			:return: state: ON | 1 Automatically determines the Tx power. OFF | 0 Define a Tx power manually with [SENSe:]POWer:SEM:AMPower."""
		response = self._core.io.query_str(f'SENSe:POWer:SEM:AMPower:AUTO?')
		return Conversions.str_to_bool(response)
