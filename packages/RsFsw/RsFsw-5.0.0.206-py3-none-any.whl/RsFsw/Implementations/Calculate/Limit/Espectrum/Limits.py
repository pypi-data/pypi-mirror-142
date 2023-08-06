from typing import List

from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Limits:
	"""Limits commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("limits", core, parent)

	def set(self, max_1: List[float], window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum<sb>:LIMits \n
		Snippet: driver.calculate.limit.espectrum.limits.set(max_1 = [1.1, 2.2, 3.3], window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, subBlock = repcap.SubBlock.Default) \n
		This command sets or queries up to 4 power classes in one step. You can only define values for the number of power
		classes defined by method RsFsw.Calculate.Limit.Espectrum.Pclass.Count.set. \n
			:param max_1: Defines the value range for power class 1 as -200 to Max1. Only available for CALC:LIM:ESP:PCL:COUNT =2 If only 2 power classes are defined, the value range for power class 2 is defined as Max1 to 200. Range: -199 to + 199 , Unit: DBM
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.list_to_csv_str(max_1)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum{subBlock_cmd_val}:LIMits {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, subBlock=repcap.SubBlock.Default) -> List[float]:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum<sb>:LIMits \n
		Snippet: value: List[float] = driver.calculate.limit.espectrum.limits.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, subBlock = repcap.SubBlock.Default) \n
		This command sets or queries up to 4 power classes in one step. You can only define values for the number of power
		classes defined by method RsFsw.Calculate.Limit.Espectrum.Pclass.Count.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: max_1: Defines the value range for power class 1 as -200 to Max1. Only available for CALC:LIM:ESP:PCL:COUNT =2 If only 2 power classes are defined, the value range for power class 2 is defined as Max1 to 200. Range: -199 to + 199 , Unit: DBM"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_bin_or_ascii_float_list(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum{subBlock_cmd_val}:LIMits?')
		return response
