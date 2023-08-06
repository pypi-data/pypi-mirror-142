from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DpiPower:
	"""DpiPower commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dpiPower", core, parent)

	def set(self, power: float) -> None:
		"""SCPI: CONFigure:REFSignal:CWF:DPIPower \n
		Snippet: driver.applications.k18AmplifierEt.configure.refSignal.cwf.dpiPower.set(power = 1.0) \n
		This command defines the peak input power of the DUT. This is necessary when you turn off method RsFsw.Applications.
		K18_AmplifierEt.Configure.RefSignal.Cwf.EtGenerator.State.set (otherwise, the command has no effect) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Generate reference signal with a waveform file \n
			:param power: numeric value Unit: dBm
		"""
		param = Conversions.decimal_value_to_str(power)
		self._core.io.write(f'CONFigure:REFSignal:CWF:DPIPower {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:REFSignal:CWF:DPIPower \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.refSignal.cwf.dpiPower.get() \n
		This command defines the peak input power of the DUT. This is necessary when you turn off method RsFsw.Applications.
		K18_AmplifierEt.Configure.RefSignal.Cwf.EtGenerator.State.set (otherwise, the command has no effect) .
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Generate reference signal with a waveform file \n
			:return: power: numeric value Unit: dBm"""
		response = self._core.io.query_str(f'CONFigure:REFSignal:CWF:DPIPower?')
		return Conversions.str_to_float(response)
