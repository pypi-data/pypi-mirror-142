from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HfOffset:
	"""HfOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hfOffset", core, parent)

	def set(self, half_frame: enums.HalfFrame, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:HFOFfset \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.hfOffset.set(half_frame = enums.HalfFrame.ONE, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the half frame that contains the synchronization signal.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a SSB periodicity > 5 ms (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.SsBlock.BsPeriod.set) . \n
			:param half_frame: ZERO SSB in first half frame. ONE SSB in second half frame.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(half_frame, enums.HalfFrame)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:HFOFfset {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.HalfFrame:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:HFOFfset \n
		Snippet: value: enums.HalfFrame = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.hfOffset.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the half frame that contains the synchronization signal.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select a SSB periodicity > 5 ms (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Downlink.Cc.SsBlock.BsPeriod.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: half_frame: ZERO SSB in first half frame. ONE SSB in second half frame."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:HFOFfset?')
		return Conversions.str_to_scalar_enum(response, enums.HalfFrame)
