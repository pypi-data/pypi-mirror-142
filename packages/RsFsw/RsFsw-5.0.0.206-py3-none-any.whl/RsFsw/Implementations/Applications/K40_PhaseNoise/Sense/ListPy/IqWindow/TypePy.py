from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, window_function: enums.WindowFunction) -> None:
		"""SCPI: [SENSe]:LIST:IQWindow:TYPE \n
		Snippet: driver.applications.k40PhaseNoise.sense.listPy.iqWindow.typePy.set(window_function = enums.WindowFunction.BHARris) \n
		No command help available \n
			:param window_function: No help available
		"""
		param = Conversions.enum_scalar_to_str(window_function, enums.WindowFunction)
		self._core.io.write(f'SENSe:LIST:IQWindow:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.WindowFunction:
		"""SCPI: [SENSe]:LIST:IQWindow:TYPE \n
		Snippet: value: enums.WindowFunction = driver.applications.k40PhaseNoise.sense.listPy.iqWindow.typePy.get() \n
		No command help available \n
			:return: window_function: No help available"""
		response = self._core.io.query_str(f'SENSe:LIST:IQWindow:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.WindowFunction)
