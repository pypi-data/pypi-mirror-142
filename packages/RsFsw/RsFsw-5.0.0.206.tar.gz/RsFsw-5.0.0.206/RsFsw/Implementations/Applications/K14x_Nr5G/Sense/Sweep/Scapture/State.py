from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:SWEep:SCAPture:STATe \n
		Snippet: driver.applications.k14Xnr5G.sense.sweep.scapture.state.set(state = False) \n
		This command turns segmented capture on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select external of IF power trigger source (TRIGger[:SEQuence]:SOURce<ant>) . \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SWEep:SCAPture:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWEep:SCAPture:STATe \n
		Snippet: value: bool = driver.applications.k14Xnr5G.sense.sweep.scapture.state.get() \n
		This command turns segmented capture on and off.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select external of IF power trigger source (TRIGger[:SEQuence]:SOURce<ant>) . \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:SWEep:SCAPture:STATe?')
		return Conversions.str_to_bool(response)
