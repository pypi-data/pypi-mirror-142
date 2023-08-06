from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, state: enums.SweepStatisticMode) -> None:
		"""SCPI: [SENSe]:SWEep:STATistics:MODE \n
		Snippet: driver.applications.k18AmplifierEt.sense.sweep.statistics.mode.set(state = enums.SweepStatisticMode.IQAVeraging) \n
		Sets and queries the statistics mode. \n
			:param state: IQAVeraging | TRACe
		"""
		param = Conversions.enum_scalar_to_str(state, enums.SweepStatisticMode)
		self._core.io.write(f'SENSe:SWEep:STATistics:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SweepStatisticMode:
		"""SCPI: [SENSe]:SWEep:STATistics:MODE \n
		Snippet: value: enums.SweepStatisticMode = driver.applications.k18AmplifierEt.sense.sweep.statistics.mode.get() \n
		Sets and queries the statistics mode. \n
			:return: state: IQAVeraging | TRACe"""
		response = self._core.io.query_str(f'SENSe:SWEep:STATistics:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.SweepStatisticMode)
