from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Real:
	"""Real commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("real", core, parent)

	def set(self, real: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SYNC:CSWeight:SHFRame:REAL \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.sync.csWeight.shFrame.real.set(real = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the signal weight for the real part of the signal in the second half frame.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on custom sync signal weight (method RsFsw.Applications.K10x_Lte.Configure.Lte.Downlink.Cc.Sync.CsWeight.State.set) . \n
			:param real: Range: -1 to 1
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(real)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SYNC:CSWeight:SHFRame:REAL {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:SYNC:CSWeight:SHFRame:REAL \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.sync.csWeight.shFrame.real.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the signal weight for the real part of the signal in the second half frame.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Turn on custom sync signal weight (method RsFsw.Applications.K10x_Lte.Configure.Lte.Downlink.Cc.Sync.CsWeight.State.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: real: Range: -1 to 1"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:SYNC:CSWeight:SHFRame:REAL?')
		return Conversions.str_to_float(response)
