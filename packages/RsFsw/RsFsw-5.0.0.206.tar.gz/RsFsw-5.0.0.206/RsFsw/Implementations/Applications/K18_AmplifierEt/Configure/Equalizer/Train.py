from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Train:
	"""Train commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("train", core, parent)

	def set(self) -> None:
		"""SCPI: CONFigure:EQUalizer:TRAin \n
		Snippet: driver.applications.k18AmplifierEt.configure.equalizer.train.set() \n
		This command initiates a training sequence for the equalizer filter. Note that you have to synchronize the measurement
		before you can initiate a training sequence.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Define a filter length (method RsFsw.Applications.K18_AmplifierEt.Configure.Equalizer.FilterPy.Length.set) . \n
		"""
		self._core.io.write(f'CONFigure:EQUalizer:TRAin')

	def set_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:EQUalizer:TRAin \n
		Snippet: driver.applications.k18AmplifierEt.configure.equalizer.train.set_with_opc() \n
		This command initiates a training sequence for the equalizer filter. Note that you have to synchronize the measurement
		before you can initiate a training sequence.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Define a filter length (method RsFsw.Applications.K18_AmplifierEt.Configure.Equalizer.FilterPy.Length.set) . \n
		Same as set, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:EQUalizer:TRAin', opc_timeout_ms)
