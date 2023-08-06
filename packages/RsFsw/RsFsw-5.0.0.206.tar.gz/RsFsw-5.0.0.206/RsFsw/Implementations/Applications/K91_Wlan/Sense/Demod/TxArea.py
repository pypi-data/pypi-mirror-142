from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TxArea:
	"""TxArea commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("txArea", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:DEMod:TXARea \n
		Snippet: driver.applications.k91Wlan.sense.demod.txArea.set(state = False) \n
		If enabled, the R&S FSW WLAN application initially performs a coarse burst search on the input signal in which increases
		in the power vs time trace are detected. Further time-consuming processing is then only performed where bursts are
		assumed. This improves the measurement speed for signals with low duty cycle rates. However, for signals in which the
		PPDU power levels differ significantly, this option should be disabled as otherwise some PPDUs may not be detected. \n
			:param state: ON | OFF | 0 | 1 ON | 1 A coarse burst search is performed based on the power levels of the input signal. OFF | 0 No pre-evaluation is performed, the entire signal is processed.
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:DEMod:TXARea {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:DEMod:TXARea \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.demod.txArea.get() \n
		If enabled, the R&S FSW WLAN application initially performs a coarse burst search on the input signal in which increases
		in the power vs time trace are detected. Further time-consuming processing is then only performed where bursts are
		assumed. This improves the measurement speed for signals with low duty cycle rates. However, for signals in which the
		PPDU power levels differ significantly, this option should be disabled as otherwise some PPDUs may not be detected. \n
			:return: state: ON | OFF | 0 | 1 ON | 1 A coarse burst search is performed based on the power levels of the input signal. OFF | 0 No pre-evaluation is performed, the entire signal is processed."""
		response = self._core.io.query_str(f'SENSe:DEMod:TXARea?')
		return Conversions.str_to_bool(response)
