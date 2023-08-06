from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def get(self) -> float:
		"""SCPI: CONFigure:DDPD:COUNt:CURRent \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.ddpd.count.current.get() \n
		This command queries the process of the direct DPD sequence (number of current iteration) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on direct DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) .
			- Start a DPD sequence (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.start) . \n
			:return: iterations: No help available"""
		response = self._core.io.query_str(f'CONFigure:DDPD:COUNt:CURRent?')
		return Conversions.str_to_float(response)
