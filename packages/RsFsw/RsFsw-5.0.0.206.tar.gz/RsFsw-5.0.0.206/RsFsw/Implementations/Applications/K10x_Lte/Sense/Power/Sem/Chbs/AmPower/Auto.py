from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:POWer:SEM:CHBS:AMPower:AUTO \n
		Snippet: driver.applications.k10Xlte.sense.power.sem.chbs.amPower.auto.set(state = False) \n
		This command turn automatic detection of the TX channel power on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select medium range base stations ([SENSe:]POWer:SEM:CATegory) .
		When you turn off automatic detection, you can define the TX channel power manually with [SENSe:]POWer:SEM:CHBS:AMPower. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:POWer:SEM:CHBS:AMPower:AUTO {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:SEM:CHBS:AMPower:AUTO \n
		Snippet: value: bool = driver.applications.k10Xlte.sense.power.sem.chbs.amPower.auto.get() \n
		This command turn automatic detection of the TX channel power on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select medium range base stations ([SENSe:]POWer:SEM:CATegory) .
		When you turn off automatic detection, you can define the TX channel power manually with [SENSe:]POWer:SEM:CHBS:AMPower. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:POWer:SEM:CHBS:AMPower:AUTO?')
		return Conversions.str_to_bool(response)
