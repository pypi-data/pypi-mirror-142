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

	def set(self, filter_type: enums.FilterTypeNr5G) -> None:
		"""SCPI: [SENSe]:BWIDth[:RESolution]:TYPE \n
		Snippet: driver.applications.k14Xnr5G.sense.bandwidth.resolution.typePy.set(filter_type = enums.FilterTypeNr5G.CFILter) \n
		No command help available \n
			:param filter_type: No help available
		"""
		param = Conversions.enum_scalar_to_str(filter_type, enums.FilterTypeNr5G)
		self._core.io.write(f'SENSe:BWIDth:RESolution:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FilterTypeNr5G:
		"""SCPI: [SENSe]:BWIDth[:RESolution]:TYPE \n
		Snippet: value: enums.FilterTypeNr5G = driver.applications.k14Xnr5G.sense.bandwidth.resolution.typePy.get() \n
		No command help available \n
			:return: filter_type: No help available"""
		response = self._core.io.query_str(f'SENSe:BWIDth:RESolution:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.FilterTypeNr5G)
