from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BlockSize:
	"""BlockSize commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("blockSize", core, parent)

	def set(self, block_size: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:PSPectrum:BLOCksize \n
		Snippet: driver.applications.k6Pulse.calculate.pspectrum.blockSize.set(block_size = 1.0, window = repcap.Window.Default) \n
		Defines the size of blocks used in Pulse-to-Pulse Spectrum calculation. The block size also determines the resulting RBW
		of the Pulse-to-Pulse Spectrum (see method RsFsw.Applications.K6_Pulse.Calculate.Pspectrum.Rbw.get_) .
		For more information see 'Parameter spectrum calculation'. \n
			:param block_size: Range: 8 to 100k
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(block_size)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:PSPectrum:BLOCksize {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:PSPectrum:BLOCksize \n
		Snippet: value: float = driver.applications.k6Pulse.calculate.pspectrum.blockSize.get(window = repcap.Window.Default) \n
		Defines the size of blocks used in Pulse-to-Pulse Spectrum calculation. The block size also determines the resulting RBW
		of the Pulse-to-Pulse Spectrum (see method RsFsw.Applications.K6_Pulse.Calculate.Pspectrum.Rbw.get_) .
		For more information see 'Parameter spectrum calculation'. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: block_size: Range: 8 to 100k"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:PSPectrum:BLOCksize?')
		return Conversions.str_to_float(response)
