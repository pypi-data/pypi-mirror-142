from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Window:
	"""Window commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("window", core, parent)

	def set(self, window_type: enums.SpectrumWindowType, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:RRSPectrum:WINDow \n
		Snippet: driver.applications.k6Pulse.calculate.rrSpectrum.window.set(window_type = enums.SpectrumWindowType.BARTlett, window = repcap.Window.Default) \n
		Defines the RBW for the Result Range Spectrum. The same window types are available as for Parameter Spectrum displays
		(see 'Window functions') . \n
			:param window_type: RECTangle | BARTlett | HAMMing | HANNing | BLACkman
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(window_type, enums.SpectrumWindowType)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:RRSPectrum:WINDow {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.SpectrumWindowType:
		"""SCPI: CALCulate<n>:RRSPectrum:WINDow \n
		Snippet: value: enums.SpectrumWindowType = driver.applications.k6Pulse.calculate.rrSpectrum.window.get(window = repcap.Window.Default) \n
		Defines the RBW for the Result Range Spectrum. The same window types are available as for Parameter Spectrum displays
		(see 'Window functions') . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: window_type: RECTangle | BARTlett | HAMMing | HANNing | BLACkman"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:RRSPectrum:WINDow?')
		return Conversions.str_to_scalar_enum(response, enums.SpectrumWindowType)
