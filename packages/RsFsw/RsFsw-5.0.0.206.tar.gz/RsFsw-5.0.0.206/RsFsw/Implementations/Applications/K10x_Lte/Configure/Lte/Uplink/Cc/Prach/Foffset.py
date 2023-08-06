from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Foffset:
	"""Foffset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("foffset", core, parent)

	def set(self, offset: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PRACh:FOFFset \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.prach.foffset.set(offset = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the PRACH frequency offset. The command is available for preamble formats 0 to 3. \n
			:param offset: numeric value (integer only) Frequency offset in terms of resource blocks.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(offset)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PRACh:FOFFset {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:PRACh:FOFFset \n
		Snippet: value: float = driver.applications.k10Xlte.configure.lte.uplink.cc.prach.foffset.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the PRACH frequency offset. The command is available for preamble formats 0 to 3. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: offset: numeric value (integer only) Frequency offset in terms of resource blocks."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:PRACh:FOFFset?')
		return Conversions.str_to_float(response)
