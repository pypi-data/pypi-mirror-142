from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class X:
	"""X commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("x", core, parent)

	def set(self, frequency: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MASK:LOWer:SHIFt:X \n
		Snippet: driver.calculate.mask.lower.shift.x.set(frequency = 1.0, window = repcap.Window.Default) \n
		This command shifts the lower frequency mask horizontally by a specified distance. Positive values move the mask to the
		right, negative values shift the mask to the left. Before making any changes to a frequency mask, you have to select one
		by name with method RsFsw.Calculate.Mask.Name.set. \n
			:param frequency: Defines the distance of the shift. Unit: Hz
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(frequency)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MASK:LOWer:SHIFt:X {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:MASK:LOWer:SHIFt:X \n
		Snippet: value: float = driver.calculate.mask.lower.shift.x.get(window = repcap.Window.Default) \n
		This command shifts the lower frequency mask horizontally by a specified distance. Positive values move the mask to the
		right, negative values shift the mask to the left. Before making any changes to a frequency mask, you have to select one
		by name with method RsFsw.Calculate.Mask.Name.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: frequency: Defines the distance of the shift. Unit: Hz"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MASK:LOWer:SHIFt:X?')
		return Conversions.str_to_float(response)
