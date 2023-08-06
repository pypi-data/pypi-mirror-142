from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class PsOffset:
	"""PsOffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("psOffset", core, parent)

	def set(self, offset: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PSOFfset \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.psOffset.set(offset = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the symbol offset for PDSCH allocations relative to the start of the subframe. The offset applies to
		all subframes. \n
			:param offset: AUTO Automatically determines the symbol offset. numeric value Manual selection of the symbol offset. Range: 0 to 4
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(offset)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PSOFfset {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PSOFfset \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.psOffset.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the symbol offset for PDSCH allocations relative to the start of the subframe. The offset applies to
		all subframes. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: offset: AUTO Automatically determines the symbol offset. numeric value Manual selection of the symbol offset. Range: 0 to 4"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PSOFfset?')
		return Conversions.str_to_float(response)
