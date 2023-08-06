from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:DPD:AMXM[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.dpd.amxm.state.set(state = False) \n
		This command turns AM/AM and AM/PM predistortion on and off (at the same time) .
			INTRO_CMD_HELP: Alternatively, you can do that with: \n
			- method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.Amam.State.set and
			- method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.AmPm.State.set
		However, using method RsFsw.Applications.K18_AmplifierEt.Configure.Dpd.Amxm.State.set is the smoother way.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on polynomial DPD (method RsFsw.Applications.K18_AmplifierEt.Configure.Ddpd.State.set) . \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:DPD:AMXM:STATe {param}')
