from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class InputPy:
	"""InputPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("inputPy", core, parent)

	def set(self, source: enums.InputSourceLte) -> None:
		"""SCPI: [SENSe]:INPut \n
		Snippet: driver.applications.k10Xlte.sense.inputPy.set(source = enums.InputSourceLte.AIQ) \n
		No command help available \n
			:param source: No help available
		"""
		param = Conversions.enum_scalar_to_str(source, enums.InputSourceLte)
		self._core.io.write(f'SENSe:INPut {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.InputSourceLte:
		"""SCPI: [SENSe]:INPut \n
		Snippet: value: enums.InputSourceLte = driver.applications.k10Xlte.sense.inputPy.get() \n
		No command help available \n
			:return: source: No help available"""
		response = self._core.io.query_str(f'SENSe:INPut?')
		return Conversions.str_to_scalar_enum(response, enums.InputSourceLte)
