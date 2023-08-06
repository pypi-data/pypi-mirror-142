from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pattern:
	"""Pattern commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pattern", core, parent)

	def set(self, pattern: enums.SyncSignalPattern, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:PATTern \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.pattern.set(pattern = enums.SyncSignalPattern.A, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the pattern of a synchronization signal block.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select manual configuration mode for SS (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.SsBlock.Detection.set) . \n
			:param pattern: A | B | C | D | E The SSB patterns are linked to the subcarrier spacing. Patterns A, D and E cannot be set. They are always selected automatically when you select a subcarrier spacing of 15 kHz (pattern A) , 120 kHz (pattern D) and 240 kHz (pattern E) . For these subcarrier spacing, the command is a query only. For subcarrier spacing of 30 kHz, you can select pattern B or C.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(pattern, enums.SyncSignalPattern)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:PATTern {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.SyncSignalPattern:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:PATTern \n
		Snippet: value: enums.SyncSignalPattern = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.pattern.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the pattern of a synchronization signal block.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select manual configuration mode for SS (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.SsBlock.Detection.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: pattern: A | B | C | D | E The SSB patterns are linked to the subcarrier spacing. Patterns A, D and E cannot be set. They are always selected automatically when you select a subcarrier spacing of 15 kHz (pattern A) , 120 kHz (pattern D) and 240 kHz (pattern E) . For these subcarrier spacing, the command is a query only. For subcarrier spacing of 30 kHz, you can select pattern B or C."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:PATTern?')
		return Conversions.str_to_scalar_enum(response, enums.SyncSignalPattern)
