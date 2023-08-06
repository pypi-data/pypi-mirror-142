from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: CONFigure:PSWeep:ADJust:LEVel[:STATe] \n
		Snippet: driver.applications.k18AmplifierEt.configure.psweep.adjust.level.state.set(state = False) \n
		This command turns synchronization of the generator output level and the analyzer reference level on and off. When you
		synchronize the levels, it is recommended to also define the expected gain of the DUT with method RsFsw.Applications.
		K18_AmplifierEt.Configure.Psweep.Expected.Gain.set.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select 'Generator Power' as one of the parameters. \n
			:param state: ON | OFF | 1 | 0
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'CONFigure:PSWeep:ADJust:LEVel:STATe {param}')

	def get(self) -> bool:
		"""SCPI: CONFigure:PSWeep:ADJust:LEVel[:STATe] \n
		Snippet: value: bool = driver.applications.k18AmplifierEt.configure.psweep.adjust.level.state.get() \n
		This command turns synchronization of the generator output level and the analyzer reference level on and off. When you
		synchronize the levels, it is recommended to also define the expected gain of the DUT with method RsFsw.Applications.
		K18_AmplifierEt.Configure.Psweep.Expected.Gain.set.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select 'Generator Power' as one of the parameters. \n
			:return: state: ON | OFF | 1 | 0"""
		response = self._core.io.query_str(f'CONFigure:PSWeep:ADJust:LEVel:STATe?')
		return Conversions.str_to_bool(response)
