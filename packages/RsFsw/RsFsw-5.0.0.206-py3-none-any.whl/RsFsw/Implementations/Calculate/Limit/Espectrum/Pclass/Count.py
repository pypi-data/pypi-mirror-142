from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Count:
	"""Count commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("count", core, parent)

	def set(self, no_power_classes: float, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, subBlock=repcap.SubBlock.Default, powerClass=repcap.PowerClass.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum<sb>:PCLass<pc>:COUNt \n
		Snippet: driver.calculate.limit.espectrum.pclass.count.set(no_power_classes = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, subBlock = repcap.SubBlock.Default, powerClass = repcap.PowerClass.Default) \n
		This command sets the number of power classes to be defined. This command must be executed before any new power class
		values can be defined using method RsFsw.Calculate.Limit.Espectrum.Pclass.Maximum.set and method RsFsw.Calculate.Limit.
		Espectrum.Pclass.Minimum.set. \n
			:param no_power_classes: 1 to 4
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
		"""
		param = Conversions.decimal_value_to_str(no_power_classes)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum{subBlock_cmd_val}:PCLass{powerClass_cmd_val}:COUNt {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, subBlock=repcap.SubBlock.Default, powerClass=repcap.PowerClass.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum<sb>:PCLass<pc>:COUNt \n
		Snippet: value: float = driver.calculate.limit.espectrum.pclass.count.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, subBlock = repcap.SubBlock.Default, powerClass = repcap.PowerClass.Default) \n
		This command sets the number of power classes to be defined. This command must be executed before any new power class
		values can be defined using method RsFsw.Calculate.Limit.Espectrum.Pclass.Maximum.set and method RsFsw.Calculate.Limit.
		Espectrum.Pclass.Minimum.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
			:return: no_power_classes: 1 to 4"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum{subBlock_cmd_val}:PCLass{powerClass_cmd_val}:COUNt?')
		return Conversions.str_to_float(response)
