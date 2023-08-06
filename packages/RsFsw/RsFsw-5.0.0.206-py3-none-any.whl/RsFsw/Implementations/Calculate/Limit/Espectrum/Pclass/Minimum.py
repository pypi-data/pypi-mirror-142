from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Minimum:
	"""Minimum commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("minimum", core, parent)

	def set(self, level: float, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, subBlock=repcap.SubBlock.Default, powerClass=repcap.PowerClass.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum<sb>:PCLass<pc>:MINimum \n
		Snippet: driver.calculate.limit.espectrum.pclass.minimum.set(level = 1.0, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, subBlock = repcap.SubBlock.Default, powerClass = repcap.PowerClass.Default) \n
		This command defines the lower limit of a particular power class.
			INTRO_CMD_HELP: Note: \n
			- The first power class always has a lower limit of -200 dBm.
			- The lower limit of a power class must always be the same as the upper limit of the previous power class.
			- The power class must already exist (see method RsFsw.Calculate.Limit.Espectrum.Pclass.Count.set) . \n
			:param level: Range: -200 dBm to 199.9 dBm, Unit: dBm
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
		"""
		param = Conversions.decimal_value_to_str(level)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum{subBlock_cmd_val}:PCLass{powerClass_cmd_val}:MINimum {param}')

	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, subBlock=repcap.SubBlock.Default, powerClass=repcap.PowerClass.Default) -> float:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum<sb>:PCLass<pc>:MINimum \n
		Snippet: value: float = driver.calculate.limit.espectrum.pclass.minimum.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, subBlock = repcap.SubBlock.Default, powerClass = repcap.PowerClass.Default) \n
		This command defines the lower limit of a particular power class.
			INTRO_CMD_HELP: Note: \n
			- The first power class always has a lower limit of -200 dBm.
			- The lower limit of a power class must always be the same as the upper limit of the previous power class.
			- The power class must already exist (see method RsFsw.Calculate.Limit.Espectrum.Pclass.Count.set) . \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
			:return: level: Range: -200 dBm to 199.9 dBm, Unit: dBm"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum{subBlock_cmd_val}:PCLass{powerClass_cmd_val}:MINimum?')
		return Conversions.str_to_float(response)
