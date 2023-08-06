from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class UsePort:
	"""UsePort commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("usePort", core, parent)

	def set(self, power_source: enums.PowerSource) -> None:
		"""SCPI: SOURce:VOLTage:USEPort \n
		Snippet: driver.applications.k30NoiseFigure.source.voltage.usePort.set(power_source = enums.PowerSource.VSUPply) \n
		No command help available \n
			:param power_source: No help available
		"""
		param = Conversions.enum_scalar_to_str(power_source, enums.PowerSource)
		self._core.io.write(f'SOURce:VOLTage:USEPort {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.PowerSource:
		"""SCPI: SOURce:VOLTage:USEPort \n
		Snippet: value: enums.PowerSource = driver.applications.k30NoiseFigure.source.voltage.usePort.get() \n
		No command help available \n
			:return: power_source: No help available"""
		response = self._core.io.query_str(f'SOURce:VOLTage:USEPort?')
		return Conversions.str_to_scalar_enum(response, enums.PowerSource)
