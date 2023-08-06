from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, param: enums.PulseFreqItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PSPectrum:FREQuency \n
		Snippet: driver.applications.k6Pulse.calculate.pspectrum.frequency.set(param = enums.PulseFreqItems.CRATe, window = repcap.Window.Default) \n
		Configures the Parameter Spectrum result display. \n
			:param param: POINt | PPFRequency | RERRor | PERRor | DEViation | CRATe Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Frequency parameters'. POINt Frequency at measurement point PPFRequency Pulse-Pulse Frequency Difference RERRor Frequency Error (RMS) PERRor Frequency Error (Peak) DEViation Frequency Deviation CRATe Chirp Rate
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(param, enums.PulseFreqItems)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PSPectrum:FREQuency {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.PulseFreqItems:
		"""SCPI: CALCulate<n>:PSPectrum:FREQuency \n
		Snippet: value: enums.PulseFreqItems = driver.applications.k6Pulse.calculate.pspectrum.frequency.get(window = repcap.Window.Default) \n
		Configures the Parameter Spectrum result display. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: param: POINt | PPFRequency | RERRor | PERRor | DEViation | CRATe Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Frequency parameters'. POINt Frequency at measurement point PPFRequency Pulse-Pulse Frequency Difference RERRor Frequency Error (RMS) PERRor Frequency Error (Peak) DEViation Frequency Deviation CRATe Chirp Rate"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PSPectrum:FREQuency?')
		return Conversions.str_to_scalar_enum(response, enums.PulseFreqItems)
