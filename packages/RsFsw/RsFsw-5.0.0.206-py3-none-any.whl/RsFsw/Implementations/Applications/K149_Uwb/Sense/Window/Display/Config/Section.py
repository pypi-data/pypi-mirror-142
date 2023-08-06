from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Section:
	"""Section commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("section", core, parent)

	def set(self, section: enums.Section, window=repcap.Window.Default) -> None:
		"""SCPI: SENSe[:WINDow<n>]:DISPlay:CONFig:SECTion \n
		Snippet: driver.applications.k149Uwb.sense.window.display.config.section.set(section = enums.Section.DATA, window = repcap.Window.Default) \n
		No command help available \n
			:param section: No help available
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.enum_scalar_to_str(section, enums.Section)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:WINDow{window_cmd_val}:DISPlay:CONFig:SECTion {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.Section:
		"""SCPI: SENSe[:WINDow<n>]:DISPlay:CONFig:SECTion \n
		Snippet: value: enums.Section = driver.applications.k149Uwb.sense.window.display.config.section.get(window = repcap.Window.Default) \n
		No command help available \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: section: No help available"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:WINDow{window_cmd_val}:DISPlay:CONFig:SECTion?')
		return Conversions.str_to_scalar_enum(response, enums.Section)
