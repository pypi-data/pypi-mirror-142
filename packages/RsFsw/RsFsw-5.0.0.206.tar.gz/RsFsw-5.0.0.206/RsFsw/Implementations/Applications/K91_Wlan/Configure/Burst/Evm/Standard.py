from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Standard:
	"""Standard commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("standard", core, parent)

	def set(self, evm_standard: str) -> None:
		"""SCPI: CONFigure:BURSt:EVM:STANdard \n
		Snippet: driver.applications.k91Wlan.configure.burst.evm.standard.set(evm_standard = '1') \n
		This command defines or queries the standard version to be used for the EVM measurement. This command is only available
		for IEEE 802.11b and g (DSSS) \n
			:param evm_standard: 'Std802_11b_1999' | 'Std802_11b_2012' | 'Std802_11b_2016' 'Std802_11b_1999' EVM measurement based on the IEEE 802.11b specification prior to 2012. 'Std802_11b_2012' EVM measurement based on the IEEE 802.11b specification from 2012. 'Std802_11b_2016' EVM measurement based on the IEEE 802.11b specification from 2016.
		"""
		param = Conversions.value_to_quoted_str(evm_standard)
		self._core.io.write(f'CONFigure:BURSt:EVM:STANdard {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:BURSt:EVM:STANdard \n
		Snippet: value: str = driver.applications.k91Wlan.configure.burst.evm.standard.get() \n
		This command defines or queries the standard version to be used for the EVM measurement. This command is only available
		for IEEE 802.11b and g (DSSS) \n
			:return: evm_standard: 'Std802_11b_1999' | 'Std802_11b_2012' | 'Std802_11b_2016' 'Std802_11b_1999' EVM measurement based on the IEEE 802.11b specification prior to 2012. 'Std802_11b_2012' EVM measurement based on the IEEE 802.11b specification from 2012. 'Std802_11b_2016' EVM measurement based on the IEEE 802.11b specification from 2016."""
		response = self._core.io.query_str(f'CONFigure:BURSt:EVM:STANdard?')
		return trim_str_response(response)
