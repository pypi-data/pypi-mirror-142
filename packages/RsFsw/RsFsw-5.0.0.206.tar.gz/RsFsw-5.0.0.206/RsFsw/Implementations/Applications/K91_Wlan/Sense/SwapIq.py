from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class SwapIq:
	"""SwapIq commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("swapIq", core, parent)

	def set(self, state: bool) -> None:
		"""SCPI: [SENSe]:SWAPiq \n
		Snippet: driver.applications.k91Wlan.sense.swapIq.set(state = False) \n
		This command defines whether or not the recorded I/Q pairs should be swapped (I<->Q) before being processed. Swapping I
		and Q inverts the sideband. This is useful if the DUT interchanged the I and Q parts of the signal; then the R&S FSW can
		do the same to compensate for it. For GSM measurements: Try this function if the TSC can not be found. \n
			:param state: ON | 1 I and Q signals are interchanged Inverted sideband, Q+j*I OFF | 0 I and Q signals are not interchanged Normal sideband, I+j*Q
		"""
		param = Conversions.bool_to_str(state)
		self._core.io.write(f'SENSe:SWAPiq {param}')

	def get(self) -> bool:
		"""SCPI: [SENSe]:SWAPiq \n
		Snippet: value: bool = driver.applications.k91Wlan.sense.swapIq.get() \n
		This command defines whether or not the recorded I/Q pairs should be swapped (I<->Q) before being processed. Swapping I
		and Q inverts the sideband. This is useful if the DUT interchanged the I and Q parts of the signal; then the R&S FSW can
		do the same to compensate for it. For GSM measurements: Try this function if the TSC can not be found. \n
			:return: state: ON | 1 I and Q signals are interchanged Inverted sideband, Q+j*I OFF | 0 I and Q signals are not interchanged Normal sideband, I+j*Q"""
		response = self._core.io.query_str(f'SENSe:SWAPiq?')
		return Conversions.str_to_bool(response)
