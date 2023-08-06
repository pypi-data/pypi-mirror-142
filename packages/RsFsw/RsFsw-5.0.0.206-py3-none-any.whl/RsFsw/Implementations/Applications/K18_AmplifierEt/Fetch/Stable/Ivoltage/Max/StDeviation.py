from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class StDeviation:
	"""StDeviation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stDeviation", core, parent)

	def get(self, voltage: enums.SelectionRangeB) -> float:
		"""SCPI: FETCh:STABle:IVOLtage:MAX:STDeviation \n
		Snippet: value: float = driver.applications.k18AmplifierEt.fetch.stable.ivoltage.max.stDeviation.get(voltage = enums.SelectionRangeB.ALL) \n
		No command help available \n
			:param voltage: No help available
			:return: result: No help available"""
		param = Conversions.enum_scalar_to_str(voltage, enums.SelectionRangeB)
		response = self._core.io.query_str(f'FETCh:STABle:IVOLtage:MAX:STDeviation? {param}')
		return Conversions.str_to_float(response)
