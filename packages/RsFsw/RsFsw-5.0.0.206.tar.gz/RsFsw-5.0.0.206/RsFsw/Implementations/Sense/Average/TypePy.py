from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, mode: enums.AverageModeB) -> None:
		"""SCPI: [SENSe]:AVERage:TYPE \n
		Snippet: driver.sense.average.typePy.set(mode = enums.AverageModeB.LINear) \n
		This command selects the trace averaging mode. \n
			:param mode: LOGarithmic The logarithmic power values are averaged. LINear The power values are averaged before they are converted to logarithmic values. POWer The power level values are converted into unit Watt prior to averaging. After the averaging, the data is converted back into its original unit.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AverageModeB)
		self._core.io.write(f'SENSe:AVERage:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AverageModeB:
		"""SCPI: [SENSe]:AVERage:TYPE \n
		Snippet: value: enums.AverageModeB = driver.sense.average.typePy.get() \n
		This command selects the trace averaging mode. \n
			:return: mode: LOGarithmic The logarithmic power values are averaged. LINear The power values are averaged before they are converted to logarithmic values. POWer The power level values are converted into unit Watt prior to averaging. After the averaging, the data is converted back into its original unit."""
		response = self._core.io.query_str(f'SENSe:AVERage:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.AverageModeB)
