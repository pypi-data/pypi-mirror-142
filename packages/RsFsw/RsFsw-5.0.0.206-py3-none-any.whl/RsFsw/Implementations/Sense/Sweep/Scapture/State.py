from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, seg_cap_state: bool) -> None:
		"""SCPI: [SENSe]:SWEep:SCAPture[:STATe] \n
		Snippet: driver.sense.sweep.scapture.state.set(seg_cap_state = False) \n
		No command help available \n
			:param seg_cap_state: No help available
		"""
		param = Conversions.bool_to_str(seg_cap_state)
		self._core.io.write(f'SENSe:SWEep:SCAPture:STATe {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWEep:SCAPture[:STATe] \n
		Snippet: value: bool = driver.sense.sweep.scapture.state.get() \n
		No command help available \n
			:return: seg_cap_state: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:SCAPture:STATe?')
		return Conversions.str_to_bool(response)
