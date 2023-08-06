from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Distance:
	"""Distance commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("distance", core, parent)

	def set(self, bandwidth: enums.TuningRange) -> None:
		"""SCPI: DIAGnostic:SERVice:INPut:MC[:DISTance] \n
		Snippet: driver.diagnostic.service.inputPy.mc.distance.set(bandwidth = enums.TuningRange.SMALl) \n
		This command selects the distance of the peaks of the microwave calibration signal for calibration of the YIG filter.
		This command is only available for instrument models R&S FSW13/26. \n
			:param bandwidth: WIDE | SMALl SMALl Small offset of combline frequencies. WIDE Wide offset of combline frequencies.
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.TuningRange)
		self._core.io.write(f'DIAGnostic:SERVice:INPut:MC:DISTance {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.TuningRange:
		"""SCPI: DIAGnostic:SERVice:INPut:MC[:DISTance] \n
		Snippet: value: enums.TuningRange = driver.diagnostic.service.inputPy.mc.distance.get() \n
		This command selects the distance of the peaks of the microwave calibration signal for calibration of the YIG filter.
		This command is only available for instrument models R&S FSW13/26. \n
			:return: bandwidth: WIDE | SMALl SMALl Small offset of combline frequencies. WIDE Wide offset of combline frequencies."""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:INPut:MC:DISTance?')
		return Conversions.str_to_scalar_enum(response, enums.TuningRange)
