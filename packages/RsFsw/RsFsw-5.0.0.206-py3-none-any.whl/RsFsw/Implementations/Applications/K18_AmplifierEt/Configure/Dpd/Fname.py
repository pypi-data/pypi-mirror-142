from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fname:
	"""Fname commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fname", core, parent)

	def set(self, filename: str) -> None:
		"""SCPI: CONFigure:DPD:FNAMe \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.fname.set(filename = '1') \n
		This command defines a name for the DPD correction table.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
			:param filename: String containing the DPD table file name.
		"""
		param = Conversions.value_to_quoted_str(filename)
		self._core.io.write(f'CONFigure:DPD:FNAMe {param}')

	def get(self) -> str:
		"""SCPI: CONFigure:DPD:FNAMe \n
		Snippet: value: str = driver.applications.k18AmplifierEt.configure.dpd.fname.get() \n
		This command defines a name for the DPD correction table.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
			:return: filename: String containing the DPD table file name."""
		response = self._core.io.query_str(f'CONFigure:DPD:FNAMe?')
		return trim_str_response(response)
