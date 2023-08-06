from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Fnnf:
	"""Fnnf commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("fnnf", core, parent)

	def set(self, frame_number: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FNNF \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.fnnf.set(frame_number = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the 5G NR system frame number. \n
			:param frame_number: irrelevant
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(frame_number)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FNNF {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:FNNF \n
		Snippet: value: float = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.fnnf.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the 5G NR system frame number. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: frame_number: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:FNNF?')
		return Conversions.str_to_float(response)
