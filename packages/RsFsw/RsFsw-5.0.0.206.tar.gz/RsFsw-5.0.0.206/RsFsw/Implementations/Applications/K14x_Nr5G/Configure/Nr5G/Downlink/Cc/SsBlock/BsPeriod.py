from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class BsPeriod:
	"""BsPeriod commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("bsPeriod", core, parent)

	def set(self, periodicity: enums.BurstSetPeriodicity, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:BSPeriod \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.bsPeriod.set(periodicity = enums.BurstSetPeriodicity.AUTO, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the burst set periodicity of a synchronization signal block. \n
			:param periodicity: AUTO Determines the burst set periodicity of the signal automatically. MS05 | MS10 | MS20 | MS40 Selects one of the following periodicities: 5 ms, 10 ms, 20 ms, 40 ms
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(periodicity, enums.BurstSetPeriodicity)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:BSPeriod {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.BurstSetPeriodicity:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:BSPeriod \n
		Snippet: value: enums.BurstSetPeriodicity = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.bsPeriod.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the burst set periodicity of a synchronization signal block. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: periodicity: AUTO Determines the burst set periodicity of the signal automatically. MS05 | MS10 | MS20 | MS40 Selects one of the following periodicities: 5 ms, 10 ms, 20 ms, 40 ms"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:BSPeriod?')
		return Conversions.str_to_scalar_enum(response, enums.BurstSetPeriodicity)
