from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Y:
	"""Y commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("y", core, parent)

	def set(self, level: float, window=repcap.Window.Default) -> None:
		"""SCPI: CALCulate<n>:MASK:LOWer:SHIFt:Y \n
		Snippet: driver.calculate.mask.lower.shift.y.set(level = 1.0, window = repcap.Window.Default) \n
		This command shifts the lower frequency mask vertically by a specified distance. Positive values move the mask upwards,
		negative values shift the mask downwards. Before making any changes to a frequency mask, you have to select one by name
		with method RsFsw.Calculate.Mask.Name.set. \n
			:param level: Defines the distance of the shift. The shift is relative to the current position. Unit: dB
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
		"""
		param = Conversions.decimal_value_to_str(level)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'CALCulate{window_cmd_val}:MASK:LOWer:SHIFt:Y {param}')

	def get(self, window=repcap.Window.Default) -> float:
		"""SCPI: CALCulate<n>:MASK:LOWer:SHIFt:Y \n
		Snippet: value: float = driver.calculate.mask.lower.shift.y.get(window = repcap.Window.Default) \n
		This command shifts the lower frequency mask vertically by a specified distance. Positive values move the mask upwards,
		negative values shift the mask downwards. Before making any changes to a frequency mask, you have to select one by name
		with method RsFsw.Calculate.Mask.Name.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:return: level: Defines the distance of the shift. The shift is relative to the current position. Unit: dB"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:MASK:LOWer:SHIFt:Y?')
		return Conversions.str_to_float(response)
