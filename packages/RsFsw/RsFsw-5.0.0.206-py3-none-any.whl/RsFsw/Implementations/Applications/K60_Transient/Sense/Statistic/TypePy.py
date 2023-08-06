from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, statistic_type: enums.StatisticType, window=repcap.Window.Default) -> None:
		"""SCPI: [SENSe]:STATistic<n>:TYPE \n
		Snippet: driver.applications.k60Transient.sense.statistic.typePy.set(statistic_type = enums.StatisticType.ALL, window = repcap.Window.Default) \n
		No command help available \n
			:param statistic_type: SELected | ALL SELected Only the selected hop/chirp from each sweep (capture) is included in the statistical evaluation. ALL All measured hops/chirps from each sweep (capture) are included in the statistical evaluation.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Statistic')
		"""
		param = Conversions.enum_scalar_to_str(statistic_type, enums.StatisticType)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:STATistic{window_cmd_val}:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.StatisticType:
		"""SCPI: [SENSe]:STATistic<n>:TYPE \n
		Snippet: value: enums.StatisticType = driver.applications.k60Transient.sense.statistic.typePy.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Statistic')
			:return: statistic_type: SELected | ALL SELected Only the selected hop/chirp from each sweep (capture) is included in the statistical evaluation. ALL All measured hops/chirps from each sweep (capture) are included in the statistical evaluation."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:STATistic{window_cmd_val}:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.StatisticType)
