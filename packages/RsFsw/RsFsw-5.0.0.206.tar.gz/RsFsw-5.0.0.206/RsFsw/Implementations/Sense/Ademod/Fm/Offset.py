from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, result_type: enums.ResultTypeC) -> None:
		"""SCPI: [SENSe]:ADEMod:FM:OFFSet \n
		Snippet: driver.sense.ademod.fm.offset.set(result_type = enums.ResultTypeC.AVERage) \n
		No command help available \n
			:param result_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(result_type, enums.ResultTypeC)
		self._core.io.write(f'SENSe:ADEMod:FM:OFFSet {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.ResultTypeC:
		"""SCPI: [SENSe]:ADEMod:FM:OFFSet \n
		Snippet: value: enums.ResultTypeC = driver.sense.ademod.fm.offset.get() \n
		No command help available \n
			:return: result_type: No help available"""
		response = self._core.io.query_str(f'SENSe:ADEMod:FM:OFFSet?')
		return Conversions.str_to_scalar_enum(response, enums.ResultTypeC)
