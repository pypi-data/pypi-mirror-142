from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Select:
	"""Select commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("select", core, parent)

	def set(self, location: enums.DataSourceLocation, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: [SENSe][:LTE][:CC<cc>]:LOCation:SELect \n
		Snippet: driver.applications.k10Xlte.sense.lte.cc.location.select.set(location = enums.DataSourceLocation.AMD, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the data source of the constellation diagram. \n
			:param location: AMD After the MIMO decoder BMD Before the MIMO decoder
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(location, enums.DataSourceLocation)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'SENSe:LTE:CC{carrierComponent_cmd_val}:LOCation:SELect {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.DataSourceLocation:
		"""SCPI: [SENSe][:LTE][:CC<cc>]:LOCation:SELect \n
		Snippet: value: enums.DataSourceLocation = driver.applications.k10Xlte.sense.lte.cc.location.select.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the data source of the constellation diagram. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: location: AMD After the MIMO decoder BMD Before the MIMO decoder"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'SENSe:LTE:CC{carrierComponent_cmd_val}:LOCation:SELect?')
		return Conversions.str_to_scalar_enum(response, enums.DataSourceLocation)
