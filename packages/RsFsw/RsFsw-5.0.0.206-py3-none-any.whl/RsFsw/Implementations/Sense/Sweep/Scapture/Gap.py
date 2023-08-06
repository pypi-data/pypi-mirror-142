from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gap:
	"""Gap commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gap", core, parent)

	def set(self, seg_cap_gap_len: int) -> None:
		"""SCPI: [SENSe]:SWEep:SCAPture:GAP \n
		Snippet: driver.sense.sweep.scapture.gap.set(seg_cap_gap_len = 1) \n
		No command help available \n
			:param seg_cap_gap_len: No help available
		"""
		param = Conversions.decimal_value_to_str(seg_cap_gap_len)
		self._core.io.write(f'SENSe:SWEep:SCAPture:GAP {param}')

	def get(self) -> int:
		"""SCPI: [SENSe]:SWEep:SCAPture:GAP \n
		Snippet: value: int = driver.sense.sweep.scapture.gap.get() \n
		No command help available \n
			:return: seg_cap_gap_len: No help available"""
		response = self._core.io.query_str(f'SENSe:SWEep:SCAPture:GAP?')
		return Conversions.str_to_int(response)
