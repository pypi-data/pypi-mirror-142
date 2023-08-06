from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:POWer:SEM:OBANd:STATe \n
		Snippet: driver.applications.k10Xlte.sense.power.sem.oband.state.set(state = False) \n
		This command turns SEM limits defined for specific operating bands on and off.
			INTRO_CMD_HELP: Effects of this command \n
			- Selecting a base station category to test against becomes unavailable ([SENSe:]POWer:SEM:CATegory) . \n
			:param state: ON | OFF | 1 | 0 You can select an operating band with [SENSe:]POWer:SEM:OBANd.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:POWer:SEM:OBANd:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:SEM:OBANd:STATe \n
		Snippet: value: bool = driver.applications.k10Xlte.sense.power.sem.oband.state.get() \n
		This command turns SEM limits defined for specific operating bands on and off.
			INTRO_CMD_HELP: Effects of this command \n
			- Selecting a base station category to test against becomes unavailable ([SENSe:]POWer:SEM:CATegory) . \n
			:return: state: ON | OFF | 1 | 0 You can select an operating band with [SENSe:]POWer:SEM:OBANd."""
		response = self._core.io.query_str(f'SENSe:POWer:SEM:OBANd:STATe?')
		return Conversions.str_to_bool(response)
