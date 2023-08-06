from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Value:
	"""Value commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("value", core, parent)

	def set(self, power: float, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, subBlock=repcap.SubBlock.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum<sb>:VALue \n
		Snippet: driver.calculate.limit.espectrum.value.set(power = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, subBlock = repcap.SubBlock.Default) \n
		This command activates the manual limit line selection as and specifies the expected power as a value. Depending on the
		entered value, the associated predefined limit lines is selected. This command has the same effect as a combination of
		the CALC:LIM:ESP:MODE MAN and the method RsFsw.Calculate.Limit.Espectrum.Pclass.Exclusive.set commands; however, the
		power class to be used is not defined directly, but via the expected power. As opposed to CALC:LIM:ESP:MODE AUTO, the
		power class is not re-assigned to the input signal power dynamically, but only once when the command is executed. \n
			:param power: integer Range: -200 to 199
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
		"""
		param = Conversions.decimal_value_to_str(power)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum{subBlock_cmd_val}:VALue {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, subBlock=repcap.SubBlock.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum<sb>:VALue \n
		Snippet: value: float = driver.calculate.limit.espectrum.value.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, subBlock = repcap.SubBlock.Default) \n
		This command activates the manual limit line selection as and specifies the expected power as a value. Depending on the
		entered value, the associated predefined limit lines is selected. This command has the same effect as a combination of
		the CALC:LIM:ESP:MODE MAN and the method RsFsw.Calculate.Limit.Espectrum.Pclass.Exclusive.set commands; however, the
		power class to be used is not defined directly, but via the expected power. As opposed to CALC:LIM:ESP:MODE AUTO, the
		power class is not re-assigned to the input signal power dynamically, but only once when the command is executed. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:return: power: integer Range: -200 to 199"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum{subBlock_cmd_val}:VALue?')
		return Conversions.str_to_float(response)
