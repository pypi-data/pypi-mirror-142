from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:LIST:SWEep:COUNt:MULTiplier:STATe \n
		Snippet: driver.applications.k40PhaseNoise.sense.listPy.sweep.count.multiplier.state.set(state = False) \n
		This command turns a multiplier that is applied to the average count in each half decade on and off. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:LIST:SWEep:COUNt:MULTiplier:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:LIST:SWEep:COUNt:MULTiplier:STATe \n
		Snippet: value: bool = driver.applications.k40PhaseNoise.sense.listPy.sweep.count.multiplier.state.get() \n
		This command turns a multiplier that is applied to the average count in each half decade on and off. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'SENSe:LIST:SWEep:COUNt:MULTiplier:STATe?')
		return Conversions.str_to_bool(response)
