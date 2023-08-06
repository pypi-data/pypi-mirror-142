from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Csubframes:
	"""Csubframes commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("csubframes", core, parent)

	def set(self, sub_frames: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:CSUBframes \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.csubframes.set(sub_frames = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the number of configurable subframes in the downlink signal. \n
			:param sub_frames: Range: 0 to 39
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(sub_frames)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:CSUBframes {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:CSUBframes \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.downlink.cc.csubframes.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the number of configurable subframes in the downlink signal. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: sub_frames: Range: 0 to 39"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:CSUBframes?')
		return Conversions.str_to_float(response)
