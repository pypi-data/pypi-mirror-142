from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mbwidth:
	"""Mbwidth commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mbwidth", core, parent)

	def set(self, bandwidth: enums.WbBandwidth) -> None:
		"""SCPI: TRACe:IQ:WBANd:MBWidth \n
		Snippet: driver.applications.k14Xnr5G.trace.iq.wband.mbwidth.set(bandwidth = enums.WbBandwidth.AUTO) \n
		No command help available \n
			:param bandwidth: No help available
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.WbBandwidth)
		self._core.io.write(f'TRACe:IQ:WBANd:MBWidth {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.WbBandwidth:
		"""SCPI: TRACe:IQ:WBANd:MBWidth \n
		Snippet: value: enums.WbBandwidth = driver.applications.k14Xnr5G.trace.iq.wband.mbwidth.get() \n
		No command help available \n
			:return: bandwidth: No help available"""
		response = self._core.io.query_str(f'TRACe:IQ:WBANd:MBWidth?')
		return Conversions.str_to_scalar_enum(response, enums.WbBandwidth)
