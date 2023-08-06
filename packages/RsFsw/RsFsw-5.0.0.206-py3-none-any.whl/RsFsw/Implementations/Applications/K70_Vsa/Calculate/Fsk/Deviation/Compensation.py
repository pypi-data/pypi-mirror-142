from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Compensation:
	"""Compensation commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("compensation", core, parent)

	def set(self, state: bool, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:FSK:DEViation:COMPensation \n
		Snippet: driver.applications.k70Vsa.calculate.fsk.deviation.compensation.set(state = False, window = repcap.Window.Default) \n
		This command defines whether the deviation error is compensated for when calculating the frequency error for FSK
		modulation. Note that this command is maintained for compatibility reasons only. For newer remote programs,
		use [SENSe:]DDEMod:NORMalize:FDERror. \n
			:param state: ON | 1 Scales the reference signal to the actual deviation of the measurement signal. OFF | 0 Uses the entered nominal deviation for the reference signal.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.bool_to_str(state)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:FSK:DEViation:COMPensation {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: CALCulate<n>:FSK:DEViation:COMPensation \n
		Snippet: value: bool = driver.applications.k70Vsa.calculate.fsk.deviation.compensation.get(window = repcap.Window.Default) \n
		This command defines whether the deviation error is compensated for when calculating the frequency error for FSK
		modulation. Note that this command is maintained for compatibility reasons only. For newer remote programs,
		use [SENSe:]DDEMod:NORMalize:FDERror. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: state: ON | 1 Scales the reference signal to the actual deviation of the measurement signal. OFF | 0 Uses the entered nominal deviation for the reference signal."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:FSK:DEViation:COMPensation?')
		return Conversions.str_to_bool(response)
