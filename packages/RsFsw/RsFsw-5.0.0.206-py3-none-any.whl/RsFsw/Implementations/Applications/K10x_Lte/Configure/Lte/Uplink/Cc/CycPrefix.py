from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class CycPrefix:
	"""CycPrefix commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("cycPrefix", core, parent)

	def set(self, prefix_length: enums.PrefixLength, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:CYCPrefix \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.cycPrefix.set(prefix_length = enums.PrefixLength.AUTO, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the cyclic prefix. \n
			:param prefix_length: NORM Normal cyclic prefix length EXT Extended cyclic prefix length AUTO Automatic cyclic prefix length detection
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(prefix_length, enums.PrefixLength)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:CYCPrefix {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.PrefixLength:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:CYCPrefix \n
		Snippet: value: enums.PrefixLength = driver.applications.k10Xlte.configure.lte.uplink.cc.cycPrefix.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the cyclic prefix. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: prefix_length: NORM Normal cyclic prefix length EXT Extended cyclic prefix length AUTO Automatic cyclic prefix length detection"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:CYCPrefix?')
		return Conversions.str_to_scalar_enum(response, enums.PrefixLength)
