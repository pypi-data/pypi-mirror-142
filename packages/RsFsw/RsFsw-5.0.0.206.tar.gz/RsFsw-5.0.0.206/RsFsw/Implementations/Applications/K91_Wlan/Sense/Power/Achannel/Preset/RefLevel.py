from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class RefLevel:
	"""RefLevel commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("refLevel", core, parent)

	def set(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:POWer:ACHannel:PRESet:RLEVel \n
		Snippet: driver.applications.k91Wlan.sense.power.achannel.preset.refLevel.set() \n
		No command help available \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:POWer:ACHannel:PRESet:RLEVel', opc_timeout_ms)
