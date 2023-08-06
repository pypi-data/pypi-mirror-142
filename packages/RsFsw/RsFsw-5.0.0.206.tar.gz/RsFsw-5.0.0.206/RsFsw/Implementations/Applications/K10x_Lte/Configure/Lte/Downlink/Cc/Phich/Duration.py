from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Duration:
	"""Duration commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("duration", core, parent)

	def set(self, duration: enums.PrefixLength, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PHICh:DURation \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.phich.duration.set(duration = enums.PrefixLength.AUTO, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PHICH duration. \n
			:param duration: NORM Normal EXT Extended
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(duration, enums.PrefixLength)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PHICh:DURation {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.PrefixLength:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PHICh:DURation \n
		Snippet: value: enums.PrefixLength = driver.applications.k10Xlte.configure.lte.downlink.cc.phich.duration.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the PHICH duration. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: duration: NORM Normal EXT Extended"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PHICh:DURation?')
		return Conversions.str_to_scalar_enum(response, enums.PrefixLength)
