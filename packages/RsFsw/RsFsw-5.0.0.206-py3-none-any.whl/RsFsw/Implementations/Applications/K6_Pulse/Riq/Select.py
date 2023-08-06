from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, source: enums.InputSourceC) -> None:
		"""SCPI: RIQ:SELect \n
		Snippet: driver.applications.k6Pulse.riq.select.set(source = enums.InputSourceC.BARKer) \n
		This command selects the reference IQ source for time sidelobe measurements. \n
			:param source: FIQ | PFM | BARKer | EBARker FIQ A custom waveform is loaded from an iq.tar file. The file to be imported is defined by method RsFsw.Applications.K6_Pulse.Riq.Fiq.Path.set. PFM A polynomial is used to define the signal's phase. BARKer A Barker waveform with a specified primary code is used. EBARker A Barker waveform with a specified primary and secondary code is used.
		"""
		param = Conversions.enum_scalar_to_str(source, enums.InputSourceC)
		self._core.io.write(f'RIQ:SELect {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.InputSourceC:
		"""SCPI: RIQ:SELect \n
		Snippet: value: enums.InputSourceC = driver.applications.k6Pulse.riq.select.get() \n
		This command selects the reference IQ source for time sidelobe measurements. \n
			:return: source: FIQ | PFM | BARKer | EBARker FIQ A custom waveform is loaded from an iq.tar file. The file to be imported is defined by method RsFsw.Applications.K6_Pulse.Riq.Fiq.Path.set. PFM A polynomial is used to define the signal's phase. BARKer A Barker waveform with a specified primary code is used. EBARker A Barker waveform with a specified primary and secondary code is used."""
		response = self._core.io.query_str(f'RIQ:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.InputSourceC)
