from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.CorrectionMode) -> None:
		"""SCPI: [SENSe]:CORRection:LOSS:CALibration:MODE \n
		Snippet: driver.applications.k30NoiseFigure.sense.correction.loss.calibration.mode.set(mode = enums.CorrectionMode.SPOT) \n
		This command selects the input loss mode. \n
			:param mode: SPOT | TABLe SPOT Uses a constant calibration loss value for all measurement points (see [SENSe:]CORRection:LOSS:CALibration:SPOT) . TABLe Uses the contents of the calibration loss table.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.CorrectionMode)
		self._core.io.write(f'SENSe:CORRection:LOSS:CALibration:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.CorrectionMode:
		"""SCPI: [SENSe]:CORRection:LOSS:CALibration:MODE \n
		Snippet: value: enums.CorrectionMode = driver.applications.k30NoiseFigure.sense.correction.loss.calibration.mode.get() \n
		This command selects the input loss mode. \n
			:return: mode: SPOT | TABLe SPOT Uses a constant calibration loss value for all measurement points (see [SENSe:]CORRection:LOSS:CALibration:SPOT) . TABLe Uses the contents of the calibration loss table."""
		response = self._core.io.query_str(f'SENSe:CORRection:LOSS:CALibration:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.CorrectionMode)
