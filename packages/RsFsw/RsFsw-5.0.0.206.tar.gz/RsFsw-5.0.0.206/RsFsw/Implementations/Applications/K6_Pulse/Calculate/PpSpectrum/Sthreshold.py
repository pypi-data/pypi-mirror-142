from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sthreshold:
	"""Sthreshold commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sthreshold", core, parent)

	def set(self, threshold: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PPSPectrum:STHReshold \n
		Snippet: driver.applications.k6Pulse.calculate.ppSpectrum.sthreshold.set(threshold = 1.0, window = repcap.Window.Default) \n
		Defines the minimum section size. Sections that are smaller than the threshold are ignored and considered to be part of
		the detected gap. For more information see 'Parameter spectrum calculation'. \n
			:param threshold: Minimum section size as a percentage of the block size (see method RsFsw.Applications.K6_Pulse.Calculate.Pspectrum.BlockSize.set) Range: 0 to 100
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(threshold)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PPSPectrum:STHReshold {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:PPSPectrum:STHReshold \n
		Snippet: value: float = driver.applications.k6Pulse.calculate.ppSpectrum.sthreshold.get(window = repcap.Window.Default) \n
		Defines the minimum section size. Sections that are smaller than the threshold are ignored and considered to be part of
		the detected gap. For more information see 'Parameter spectrum calculation'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: threshold: Minimum section size as a percentage of the block size (see method RsFsw.Applications.K6_Pulse.Calculate.Pspectrum.BlockSize.set) Range: 0 to 100"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PPSPectrum:STHReshold?')
		return Conversions.str_to_float(response)
