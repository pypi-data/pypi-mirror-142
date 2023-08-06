from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Gain:
	"""Gain commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("gain", core, parent)

	def set(self, gain: float) -> None:
		"""SCPI: CONFigure:PSWeep:EXPected:GAIN \n
		Snippet: driver.applications.k18AmplifierEt.configure.psweep.expected.gain.set(gain = 1.0) \n
		This command defines the expected gain of the DUT. This is necessary when you synchronize the generator output level and
		the reference level of the analyzer method RsFsw.Applications.K18_AmplifierEt.Configure.Psweep.Adjust.Level.State.set =
		ON.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select 'Generator Power' as one of the parameters. \n
			:param gain: numeric value Unit: dB
		"""
		param = Conversions.decimal_value_to_str(gain)
		self._core.io.write(f'CONFigure:PSWeep:EXPected:GAIN {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:PSWeep:EXPected:GAIN \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.psweep.expected.gain.get() \n
		This command defines the expected gain of the DUT. This is necessary when you synchronize the generator output level and
		the reference level of the analyzer method RsFsw.Applications.K18_AmplifierEt.Configure.Psweep.Adjust.Level.State.set =
		ON.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select 'Generator Power' as one of the parameters. \n
			:return: gain: numeric value Unit: dB"""
		response = self._core.io.query_str(f'CONFigure:PSWeep:EXPected:GAIN?')
		return Conversions.str_to_float(response)
