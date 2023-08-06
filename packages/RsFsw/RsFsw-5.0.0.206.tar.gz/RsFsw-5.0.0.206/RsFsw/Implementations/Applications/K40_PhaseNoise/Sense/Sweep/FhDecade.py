from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FhDecade:
	"""FhDecade commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fhDecade", core, parent)

	def set(self) -> None:
		"""SCPI: [SENSe]:SWEep:FHDecade \n
		Snippet: driver.applications.k40PhaseNoise.sense.sweep.fhDecade.set() \n
		This command stops the measurement in the current half decade and continues measuring in the subsequent half decade. \n
		"""
		self._core.io.write(f'SENSe:SWEep:FHDecade')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:SWEep:FHDecade \n
		Snippet: driver.applications.k40PhaseNoise.sense.sweep.fhDecade.set_with_opc() \n
		This command stops the measurement in the current half decade and continues measuring in the subsequent half decade. \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:SWEep:FHDecade', opc_timeout_ms)
