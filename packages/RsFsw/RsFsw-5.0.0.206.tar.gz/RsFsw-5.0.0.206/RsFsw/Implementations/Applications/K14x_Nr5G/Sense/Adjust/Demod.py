from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Demod:
	"""Demod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demod", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:ADJust:DEMod \n
		Snippet: driver.applications.k14Xnr5G.sense.adjust.demod.set() \n
		This command automatically demodulates the signal once. For continuous automatic demodulation, use method RsFsw.
		Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Demod.Auto.set. \n
		"""
		self._core.io.write(f'SENSe:ADJust:DEMod')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:ADJust:DEMod \n
		Snippet: driver.applications.k14Xnr5G.sense.adjust.demod.set_with_opc() \n
		This command automatically demodulates the signal once. For continuous automatic demodulation, use method RsFsw.
		Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.Demod.Auto.set. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:ADJust:DEMod', opc_timeout_ms)
