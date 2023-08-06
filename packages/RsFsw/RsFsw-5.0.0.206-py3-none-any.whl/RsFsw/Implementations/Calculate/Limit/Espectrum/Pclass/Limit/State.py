from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: enums.LimitState, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, subBlock=repcap.SubBlock.Default, powerClass=repcap.PowerClass.Default) -> None:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum<sb>:PCLass<pc>:LIMit[:STATe] \n
		Snippet: driver.calculate.limit.espectrum.pclass.limit.state.set(state = enums.LimitState.ABSolute, window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, subBlock = repcap.SubBlock.Default, powerClass = repcap.PowerClass.Default) \n
		This command selects the limit check mode for each power class. \n
			:param state: ABSolute | RELative | AND | OR ABSolute Evaluates only limit lines with absolute power values RELative Evaluates only limit lines with relative power values AND Evaluates limit lines with relative and absolute power values. A negative result is returned if both limits fail. OR Evaluates limit lines with relative and absolute power values. A negative result is returned if at least one limit failed.
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
		"""
		param = Conversions.enum_scalar_to_str(state, enums.LimitState)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		self._core.io.write(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum{subBlock_cmd_val}:PCLass{powerClass_cmd_val}:LIMit:STATe {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default, limitIx=repcap.LimitIx.Default, subBlock=repcap.SubBlock.Default, powerClass=repcap.PowerClass.Default) -> enums.LimitState:
		"""SCPI: CALCulate<n>:LIMit<li>:ESPectrum<sb>:PCLass<pc>:LIMit[:STATe] \n
		Snippet: value: enums.LimitState = driver.calculate.limit.espectrum.pclass.limit.state.get(window = repcap.Window.Default, limitIx = repcap.LimitIx.Default, subBlock = repcap.SubBlock.Default, powerClass = repcap.PowerClass.Default) \n
		This command selects the limit check mode for each power class. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Calculate')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param powerClass: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Pclass')
			:return: state: ABSolute | RELative | AND | OR ABSolute Evaluates only limit lines with absolute power values RELative Evaluates only limit lines with relative power values AND Evaluates limit lines with relative and absolute power values. A negative result is returned if both limits fail. OR Evaluates limit lines with relative and absolute power values. A negative result is returned if at least one limit failed."""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		powerClass_cmd_val = self._cmd_group.get_repcap_cmd_value(powerClass, repcap.PowerClass)
		response = self._core.io.query_str(f'CALCulate{window_cmd_val}:LIMit{limitIx_cmd_val}:ESPectrum{subBlock_cmd_val}:PCLass{powerClass_cmd_val}:LIMit:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.LimitState)
