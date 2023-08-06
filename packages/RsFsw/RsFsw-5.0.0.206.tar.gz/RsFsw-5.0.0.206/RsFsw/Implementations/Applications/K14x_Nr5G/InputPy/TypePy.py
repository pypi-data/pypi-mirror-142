from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, state: enums.InputSelect) -> None:
		"""SCPI: INPut:TYPE \n
		Snippet: driver.applications.k14Xnr5G.inputPy.typePy.set(state = enums.InputSelect.INPut1) \n
		The command selects the input path. \n
			:param state: No help available
		"""
		param = Conversions.enum_scalar_to_str(state, enums.InputSelect)
		self._core.io.write(f'INPut:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.InputSelect:
		"""SCPI: INPut:TYPE \n
		Snippet: value: enums.InputSelect = driver.applications.k14Xnr5G.inputPy.typePy.get() \n
		The command selects the input path. \n
			:return: state: No help available"""
		response = self._core.io.query_str(f'INPut:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.InputSelect)
