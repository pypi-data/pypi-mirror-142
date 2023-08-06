from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Phase:
	"""Phase commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("phase", core, parent)

	def set(self, param: enums.PulsePhaseItems, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PSPectrum:PHASe \n
		Snippet: driver.applications.k6Pulse.calculate.pspectrum.phase.set(param = enums.PulsePhaseItems.DEViation, window = repcap.Window.Default) \n
		Configures the Parameter Spectrum result display. \n
			:param param: POINt | PPPHase | RERRor | PERRor | DEViation Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Phase parameters'. POINt Pulse phase at measurement point PPPHase Pulse-Pulse Phase Difference RERRor Phase Error (RMS) PERRor Phase Error (Peak) DEViation Phase Deviation
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(param, enums.PulsePhaseItems)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PSPectrum:PHASe {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.PulsePhaseItems:
		"""SCPI: CALCulate<n>:PSPectrum:PHASe \n
		Snippet: value: enums.PulsePhaseItems = driver.applications.k6Pulse.calculate.pspectrum.phase.get(window = repcap.Window.Default) \n
		Configures the Parameter Spectrum result display. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: param: POINt | PPPHase | RERRor | PERRor | DEViation Pulse parameter to be displayed on the x-axis. For a description of the available parameters see 'Phase parameters'. POINt Pulse phase at measurement point PPPHase Pulse-Pulse Phase Difference RERRor Phase Error (RMS) PERRor Phase Error (Peak) DEViation Phase Deviation"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PSPectrum:PHASe?')
		return Conversions.str_to_scalar_enum(response, enums.PulsePhaseItems)
