from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Correction:
	"""Correction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("correction", core, parent)

	def set(self) -> None:
		"""SCPI: CALCulate:PMETer:LEVel:CORRection \n
		Snippet: driver.applications.k18AmplifierEt.calculate.pmeter.level.correction.set() \n
		Calculates the level correction for power sensors. \n
		"""
		self._core.io.write(f'CALCulate:PMETer:LEVel:CORRection')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CALCulate:PMETer:LEVel:CORRection \n
		Snippet: driver.applications.k18AmplifierEt.calculate.pmeter.level.correction.set_with_opc() \n
		Calculates the level correction for power sensors. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CALCulate:PMETer:LEVel:CORRection', opc_timeout_ms)
