from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Offset:
	"""Offset commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("offset", core, parent)

	def set(self, offset: float, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: [SENSe]:FREQuency:CENTer[:CC<cc>]:OFFSet \n
		Snippet: driver.applications.k14Xnr5G.sense.frequency.center.cc.offset.set(offset = 1.0, carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the general frequency offset.
			INTRO_CMD_HELP: For measurements on multiple component carriers, the command defines the frequency offset for a component carrier. The effect of the command depends on the syntax: \n
			- When you omit the [CC<cc>] syntax element, the command defines the overall frequency offset. In that case, the value is added to the measurement frequency and, in case of measurements with component carriers, the center frequency of the component carriers.
			- When you include the [CC<cc>] syntax element, the command defines the offset of the component carrier relative the first component carrier. In that case, the command is not available for the first component carrier - thus, ...:CC1:... is not possible.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select the first component carrier (CC1) as the reference point for the frequency offset (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Orel.set) . \n
			:param offset: numeric value • General frequency offset: frequency offset in Hz. • Component carrier offset: frequency offset relative to the first component carrier in Hz. Unit: Hz
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.decimal_value_to_str(offset)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'SENSe:FREQuency:CENTer:CC{carrierComponent_cmd_val}:OFFSet {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> float:
		"""SCPI: [SENSe]:FREQuency:CENTer[:CC<cc>]:OFFSet \n
		Snippet: value: float = driver.applications.k14Xnr5G.sense.frequency.center.cc.offset.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command defines the general frequency offset.
			INTRO_CMD_HELP: For measurements on multiple component carriers, the command defines the frequency offset for a component carrier. The effect of the command depends on the syntax: \n
			- When you omit the [CC<cc>] syntax element, the command defines the overall frequency offset. In that case, the value is added to the measurement frequency and, in case of measurements with component carriers, the center frequency of the component carriers.
			- When you include the [CC<cc>] syntax element, the command defines the offset of the component carrier relative the first component carrier. In that case, the command is not available for the first component carrier - thus, ...:CC1:... is not possible.
			INTRO_CMD_HELP: Prerequisites for this command \n
			- Select the first component carrier (CC1) as the reference point for the frequency offset (method RsFsw.Applications.K14x_Nr5G.Configure.Nr5G.Orel.set) . \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: offset: numeric value • General frequency offset: frequency offset in Hz. • Component carrier offset: frequency offset relative to the first component carrier in Hz. Unit: Hz"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'SENSe:FREQuency:CENTer:CC{carrierComponent_cmd_val}:OFFSet?')
		return Conversions.str_to_float(response)
