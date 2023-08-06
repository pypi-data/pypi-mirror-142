from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	# noinspection PyTypeChecker
	def get(self) -> enums.CalibrationState:
		"""SCPI: DIAGnostic:SERVice:CALibration:DUE:STATe \n
		Snippet: value: enums.CalibrationState = driver.diagnostic.service.calibration.due.state.get() \n
		No command help available \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:CALibration:DUE:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.CalibrationState)
