from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	def set(self, configure: enums.ConfigMode, window=repcap.Window.Default) -> None:
		"""SCPI: SENSe[:WINDow<n>]:DISPlay:RWConfig:CONFigure \n
		Snippet: driver.applications.k149Uwb.sense.window.display.rwConfig.configure.set(configure = enums.ConfigMode.DEFault, window = repcap.Window.Default) \n
		Sets the configuration setting for this window. \n
			:param configure: DEFault | USER
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
		"""
		param = Conversions.enum_scalar_to_str(configure, enums.ConfigMode)
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		self._core.io.write(f'SENSe:WINDow{window_cmd_val}:DISPlay:RWConfig:CONFigure {param}')

	# noinspection PyTypeChecker
	def get(self, window=repcap.Window.Default) -> enums.ConfigMode:
		"""SCPI: SENSe[:WINDow<n>]:DISPlay:RWConfig:CONFigure \n
		Snippet: value: enums.ConfigMode = driver.applications.k149Uwb.sense.window.display.rwConfig.configure.get(window = repcap.Window.Default) \n
		Sets the configuration setting for this window. \n
			:param window: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Window')
			:return: configure: DEFault | USER"""
		window_cmd_val = self._cmd_group.get_repcap_cmd_value(window, repcap.Window)
		response = self._core.io.query_str(f'SENSe:WINDow{window_cmd_val}:DISPlay:RWConfig:CONFigure?')
		return Conversions.str_to_scalar_enum(response, enums.ConfigMode)
