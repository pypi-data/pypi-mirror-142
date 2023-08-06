from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Calc:
	"""Calc commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("calc", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:DDEMod:PRESet:CALC \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.preset.calc.set() \n
		This command selects a predefined 'signal overview' consisting of four windows. The top left window (1) shows magnitude
		data from capture buffer, the top right window (2) spectrum data from capture buffer, the bottom left window (3) the
		result summary and the bottom right window (4) constellation I/Q data. Using this setup, scripts written for R&S FSV
		instruments will continue to work. \n
		"""
		self._core.io.write(f'SENSe:DDEMod:PRESet:CALC')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:DDEMod:PRESet:CALC \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.preset.calc.set_with_opc() \n
		This command selects a predefined 'signal overview' consisting of four windows. The top left window (1) shows magnitude
		data from capture buffer, the top right window (2) spectrum data from capture buffer, the bottom left window (3) the
		result summary and the bottom right window (4) constellation I/Q data. Using this setup, scripts written for R&S FSV
		instruments will continue to work. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:DDEMod:PRESet:CALC', opc_timeout_ms)
