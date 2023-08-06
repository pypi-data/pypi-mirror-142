from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal.Types import DataType
from .......Internal.StructBase import StructBase
from .......Internal.ArgStruct import ArgStruct
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Modulation:
	"""Modulation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("modulation", core, parent)

	def set(self, tx_filter: str, rx_filter: str) -> None:
		"""SCPI: [SENSe]:DEMod:FILTer:MODulation \n
		Snippet: driver.applications.k91Wlan.sense.demod.filterPy.modulation.set(tx_filter = '1', rx_filter = '1') \n
		This command selects the transmit (TX) and receive (RX) filters. The names of the filters correspond to the file names; a
		query of all available filters is possible by means of the [SENSe:]DEMod:FILTer:CATalog? command. This command is only
		available for IEEE 802.11b measurements. \n
			:param tx_filter: File name of the transmit filter
			:param rx_filter: File name of the receive filter
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('tx_filter', tx_filter, DataType.String), ArgSingle('rx_filter', rx_filter, DataType.String))
		self._core.io.write(f'SENSe:DEMod:FILTer:MODulation {param}'.rstrip())

	# noinspection PyTypeChecker
	class ModulationStruct(StructBase):
		"""Response structure. Fields: \n
			- Tx_Filter: str: File name of the transmit filter
			- Rx_Filter: str: File name of the receive filter"""
		__meta_args_list = [
			ArgStruct.scalar_str('Tx_Filter'),
			ArgStruct.scalar_str('Rx_Filter')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Tx_Filter: str = None
			self.Rx_Filter: str = None

	def get(self) -> ModulationStruct:
		"""SCPI: [SENSe]:DEMod:FILTer:MODulation \n
		Snippet: value: ModulationStruct = driver.applications.k91Wlan.sense.demod.filterPy.modulation.get() \n
		This command selects the transmit (TX) and receive (RX) filters. The names of the filters correspond to the file names; a
		query of all available filters is possible by means of the [SENSe:]DEMod:FILTer:CATalog? command. This command is only
		available for IEEE 802.11b measurements. \n
			:return: structure: for return value, see the help for ModulationStruct structure arguments."""
		return self._core.io.query_struct(f'SENSe:DEMod:FILTer:MODulation?', self.__class__.ModulationStruct())
