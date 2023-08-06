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

	def set(self, reference_mode: enums.ReferenceMode, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:UNIT:FREQuency \n
		Snippet: driver.applications.k6Pulse.calculate.unit.frequency.set(reference_mode = enums.ReferenceMode.ABSolute, window = repcap.Window.Default) \n
		Switches between relative (default) and absolute frequency values. This setting applies to Pulse Frequency, Result Range
		Spectrum, Parameter Distribution and Parameter Trend result displays. \n
			:param reference_mode: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.enum_scalar_to_str(reference_mode, enums.ReferenceMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:UNIT:FREQuency {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.ReferenceMode:
		"""SCPI: CALCulate<n>:UNIT:FREQuency \n
		Snippet: value: enums.ReferenceMode = driver.applications.k6Pulse.calculate.unit.frequency.get(window = repcap.Window.Default) \n
		Switches between relative (default) and absolute frequency values. This setting applies to Pulse Frequency, Result Range
		Spectrum, Parameter Distribution and Parameter Trend result displays. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: reference_mode: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:UNIT:FREQuency?')
		return Conversions.str_to_scalar_enum(response, enums.ReferenceMode)
