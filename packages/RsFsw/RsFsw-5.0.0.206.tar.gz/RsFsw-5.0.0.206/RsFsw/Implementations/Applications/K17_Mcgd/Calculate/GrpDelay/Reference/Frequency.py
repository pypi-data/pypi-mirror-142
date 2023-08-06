from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Frequency:
	"""Frequency commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("frequency", core, parent)

	def set(self, ref_carr_freq: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:GRPDelay:REFerence:FREQuency \n
		Snippet: driver.applications.k17Mcgd.calculate.grpDelay.reference.frequency.set(ref_carr_freq = 1.0, window = repcap.Window.Default) \n
		Determines the frequency of the reference carrier used for relative group delay calculation. The group delay measured at
		this frequency is used as a reference. \n
			:param ref_carr_freq: numeric value
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(ref_carr_freq)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:GRPDelay:REFerence:FREQuency {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:GRPDelay:REFerence:FREQuency \n
		Snippet: value: float = driver.applications.k17Mcgd.calculate.grpDelay.reference.frequency.get(window = repcap.Window.Default) \n
		Determines the frequency of the reference carrier used for relative group delay calculation. The group delay measured at
		this frequency is used as a reference. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: ref_carr_freq: numeric value"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:GRPDelay:REFerence:FREQuency?')
		return Conversions.str_to_float(response)
