from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class NgParameter:
	"""NgParameter commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("ngParameter", core, parent)

	def set(self, ng_method: enums.NgMethod, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PHICh:NGParameter \n
		Snippet: driver.applications.k10Xlte.configure.lte.downlink.cc.phich.ngParameter.set(ng_method = enums.NgMethod.AUTO, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the method that determines the number of PHICH groups in a subframe. \n
			:param ng_method: No help available
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(ng_method, enums.NgMethod)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PHICh:NGParameter {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.NgMethod:
		"""SCPI: CONFigure[:LTE]:DL[:CC<cc>]:PHICh:NGParameter \n
		Snippet: value: enums.NgMethod = driver.applications.k10Xlte.configure.lte.downlink.cc.phich.ngParameter.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the method that determines the number of PHICH groups in a subframe. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: ng_method: No help available"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:LTE:DL:CC{carrierComponent_cmd_val}:PHICh:NGParameter?')
		return Conversions.str_to_scalar_enum(response, enums.NgMethod)
