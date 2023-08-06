from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Scale:
	"""Scale commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("scale", core, parent)

	def set(self, arg_0: bool, window=repcap.Window.Default) -> None:
		"""SCPI: HCOPy:PAGE:WINDow<1|2>:SCALe \n
		Snippet: driver.hardCopy.page.window.scale.set(arg_0 = False, window = repcap.Window.Default) \n
		This command determines the scaling of the windows in the printout for method RsFsw.HardCopy.Content.set. \n
			:param arg_0: 1 | 0 | ON | OFF 1 | ON Each window is scaled to fit the page size optimally, not regarding the aspect ratio of the original display. If more than one window is printed on one page (see method RsFsw.HardCopy.Page.Window.Count.set) , each window is printed in equal size. ('Size to fit') 0 | OFF Each window is printed as large as possible while maintaining the aspect ratio of the original display. ('Maintain aspect ratio')
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.bool_to_str(arg_0)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'HCOPy:PAGE:WINDow{window_cmd_val}:SCALe {param}')

	def get(self, window=repcap.Window.Default) -> bool:
		"""SCPI: HCOPy:PAGE:WINDow<1|2>:SCALe \n
		Snippet: value: bool = driver.hardCopy.page.window.scale.get(window = repcap.Window.Default) \n
		This command determines the scaling of the windows in the printout for method RsFsw.HardCopy.Content.set. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: arg_0: 1 | 0 | ON | OFF 1 | ON Each window is scaled to fit the page size optimally, not regarding the aspect ratio of the original display. If more than one window is printed on one page (see method RsFsw.HardCopy.Page.Window.Count.set) , each window is printed in equal size. ('Size to fit') 0 | OFF Each window is printed as large as possible while maintaining the aspect ratio of the original display. ('Maintain aspect ratio')"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'HCOPy:PAGE:WINDow{window_cmd_val}:SCALe?')
		return Conversions.str_to_bool(response)
