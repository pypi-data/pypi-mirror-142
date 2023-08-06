from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Source:
	"""Source commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("source", core, parent)

	def set(self, if_source: enums.IfSource) -> None:
		"""SCPI: OUTPut:IF[:SOURce] \n
		Snippet: driver.applications.k18AmplifierEt.output.ifreq.source.set(if_source = enums.IfSource.HVIDeo) \n
		No command help available \n
			:param if_source: No help available
		"""
		param = Conversions.enum_scalar_to_str(if_source, enums.IfSource)
		self._core.io.write(f'OUTPut:IF:SOURce {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.IfSource:
		"""SCPI: OUTPut:IF[:SOURce] \n
		Snippet: value: enums.IfSource = driver.applications.k18AmplifierEt.output.ifreq.source.get() \n
		No command help available \n
			:return: if_source: No help available"""
		response = self._core.io.query_str(f'OUTPut:IF:SOURce?')
		return Conversions.str_to_scalar_enum(response, enums.IfSource)
