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
		"""SCPI: [SENSe]:POWer:RLEVel:VERify[:STATe] \n
		Snippet: driver.applications.k40PhaseNoise.sense.power.refLevel.verify.state.set(state = False) \n
		This command turns level verification on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:POWer:RLEVel:VERify:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:POWer:RLEVel:VERify[:STATe] \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.sense.power.refLevel.verify.state.get() \n
		This command turns level verification on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:POWer:RLEVel:VERify:STATe?')
		return Conversions.str_to_bool(response)
