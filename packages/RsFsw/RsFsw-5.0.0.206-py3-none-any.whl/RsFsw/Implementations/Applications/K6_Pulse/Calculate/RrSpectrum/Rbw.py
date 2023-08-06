from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Rbw:
	"""Rbw commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("rbw", core, parent)

	def set(self, rbw: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:RRSPectrum:RBW \n
		Snippet: driver.applications.k6Pulse.calculate.rrSpectrum.rbw.set(rbw = 1.0, window = repcap.Window.Default) \n
		Defines the resolution bandwidth for the Result Range Spectrum. \n
			:param rbw: Unit: Hz
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(rbw)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:RRSPectrum:RBW {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:RRSPectrum:RBW \n
		Snippet: value: float = driver.applications.k6Pulse.calculate.rrSpectrum.rbw.get(window = repcap.Window.Default) \n
		Defines the resolution bandwidth for the Result Range Spectrum. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: rbw: Unit: Hz"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:RRSPectrum:RBW?')
		return Conversions.str_to_float(response)
