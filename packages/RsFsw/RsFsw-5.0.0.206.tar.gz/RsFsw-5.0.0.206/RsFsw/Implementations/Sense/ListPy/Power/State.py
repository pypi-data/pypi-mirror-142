from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: enums.OffState) -> None:
		"""SCPI: [SENSe]:LIST:POWer:STATe \n
		Snippet: driver.sense.listPy.power.state.set(state = enums.OffState.OFF) \n
		This command turns the List Evaluation off. \n
			:param state: OFF | 0
		"""
		param = Conversions.enum_scalar_to_str(state, enums.OffState)
		self._core.io.write(f'SENSe:LIST:POWer:STATe {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.OffState:
		"""SCPI: [SENSe]:LIST:POWer:STATe \n
		Snippet: value: enums.OffState = driver.sense.listPy.power.state.get() \n
		This command turns the List Evaluation off. \n
			:return: state: OFF | 0"""
		response = self._core.io.query_str(f'SENSe:LIST:POWer:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.OffState)
