from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, signal_source: enums.SignalSourceB) -> None:
		"""SCPI: INPut:SELect \n
		Snippet: driver.applications.k6Pulse.inputPy.select.set(signal_source = enums.SignalSourceB.ABBand) \n
		This command selects the signal source for measurements, i.e. it defines which connector is used to input data to the R&S
		FSW. If no additional input options are installed, only RF input or file input is supported. For R&S FSW85 models with
		two RF input connectors you must select the input connector to configure first using method RsFsw.Applications.K10x_Lte.
		InputPy.TypePy.set. \n
			:param signal_source: No help available
		"""
		param = Conversions.enum_scalar_to_str(signal_source, enums.SignalSourceB)
		self._core.io.write(f'INPut:SELect {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SignalSourceB:
		"""SCPI: INPut:SELect \n
		Snippet: value: enums.SignalSourceB = driver.applications.k6Pulse.inputPy.select.get() \n
		This command selects the signal source for measurements, i.e. it defines which connector is used to input data to the R&S
		FSW. If no additional input options are installed, only RF input or file input is supported. For R&S FSW85 models with
		two RF input connectors you must select the input connector to configure first using method RsFsw.Applications.K10x_Lte.
		InputPy.TypePy.set. \n
			:return: signal_source: No help available"""
		response = self._core.io.query_str(f'INPut:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.SignalSourceB)
