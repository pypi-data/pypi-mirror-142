from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Center:
	"""Center commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("center", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure[:NR5G]:CENTer \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.center.set() \n
		This command synchronizes the global multicarrier frequency to the current center frequency (= center of all carriers) .
		Use method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.GmcFreq.set to query the global multicarrier frequency. \n
		"""
		self._core.io.write(f'CONFigure:NR5G:CENTer')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure[:NR5G]:CENTer \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.center.set_with_opc() \n
		This command synchronizes the global multicarrier frequency to the current center frequency (= center of all carriers) .
		Use method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.GmcFreq.set to query the global multicarrier frequency. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:NR5G:CENTer', opc_timeout_ms)
