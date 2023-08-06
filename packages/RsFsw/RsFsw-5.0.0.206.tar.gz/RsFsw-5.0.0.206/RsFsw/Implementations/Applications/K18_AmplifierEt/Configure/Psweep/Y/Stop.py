from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Stop:
	"""Stop commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("stop", core, parent)

	def set(self, stop: float) -> None:
		"""SCPI: CONFigure:PSWeep:Y:STOP \n
		Snippet: driver.applications.k18AmplifierEt.configure.psweep.y.stop.set(stop = 1.0) \n
		This command defines the stop value for the second parameter controlled by the parameter sweep. \n
			:param stop: numeric value whose unit depends on the parameter type you have selected with method RsFsw.Applications.K18_AmplifierEt.Configure.Psweep.Y.Setting.set: • Hz in case of the center frequency • dBm in case of the output level • s in case of the delay between envelope and RF signal • V in case of the envelope bias
		"""
		param = Conversions.decimal_value_to_str(stop)
		self._core.io.write(f'CONFigure:PSWeep:Y:STOP {param}')

	def get(self) -> float:
		"""SCPI: CONFigure:PSWeep:Y:STOP \n
		Snippet: value: float = driver.applications.k18AmplifierEt.configure.psweep.y.stop.get() \n
		This command defines the stop value for the second parameter controlled by the parameter sweep. \n
			:return: stop: numeric value whose unit depends on the parameter type you have selected with method RsFsw.Applications.K18_AmplifierEt.Configure.Psweep.Y.Setting.set: • Hz in case of the center frequency • dBm in case of the output level • s in case of the delay between envelope and RF signal • V in case of the envelope bias"""
		response = self._core.io.query_str(f'CONFigure:PSWeep:Y:STOP?')
		return Conversions.str_to_float(response)
