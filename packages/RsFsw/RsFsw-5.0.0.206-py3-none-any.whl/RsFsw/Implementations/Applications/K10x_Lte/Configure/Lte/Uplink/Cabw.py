from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Cabw:
	"""Cabw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cabw", core, parent)

	def set(self, bandwidth: enums.BandwidthLteA) -> None:
		"""SCPI: CONFigure[:LTE]:UL:CABW \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cabw.set(bandwidth = enums.BandwidthLteA.B1010) \n
		This command selects the channel bandwidth(s) of the carriers in MC ACLR measurements. \n
			:param bandwidth: B520 First carrier: 5 MHz, second carrier: 20 MHz bandwidth. B1020 First carrier: 10 MHz, second carrier: 20 MHz bandwidth. B1515 First carrier: 15 MHz, second carrier: 15 MHz bandwidth. B1520 First carrier: 15 MHz, second carrier: 20 MHz bandwidth. B2020 First carrier: 20 MHz, second carrier: 20 MHz bandwidth. USER Custom combination of bandwidths. Define the bandwidths of both carriers with method RsFsw.Applications.K10x_Lte.Configure.Lte.Uplink.Cc.Bw.set.
		"""
		param = Conversions.enum_scalar_to_str(bandwidth, enums.BandwidthLteA)
		self._core.io.write(f'CONFigure:LTE:UL:CABW {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.BandwidthLteA:
		"""SCPI: CONFigure[:LTE]:UL:CABW \n
		Snippet: value: enums.BandwidthLteA = driver.applications.k10Xlte.configure.lte.uplink.cabw.get() \n
		This command selects the channel bandwidth(s) of the carriers in MC ACLR measurements. \n
			:return: bandwidth: B520 First carrier: 5 MHz, second carrier: 20 MHz bandwidth. B1020 First carrier: 10 MHz, second carrier: 20 MHz bandwidth. B1515 First carrier: 15 MHz, second carrier: 15 MHz bandwidth. B1520 First carrier: 15 MHz, second carrier: 20 MHz bandwidth. B2020 First carrier: 20 MHz, second carrier: 20 MHz bandwidth. USER Custom combination of bandwidths. Define the bandwidths of both carriers with method RsFsw.Applications.K10x_Lte.Configure.Lte.Uplink.Cc.Bw.set."""
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CABW?')
		return Conversions.str_to_scalar_enum(response, enums.BandwidthLteA)
