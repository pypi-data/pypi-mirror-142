from .........Internal.Core import Core
from .........Internal.CommandsGroup import CommandsGroup
from .........Internal import Conversions
from ......... import enums
from ......... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Detection:
	"""Detection commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("detection", core, parent)

	def set(self, mode: enums.AutoManualMode, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:DETection \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.detection.set(mode = enums.AutoManualMode.AUTO, carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns automatic detection of the synchronization signal configuration on and off. \n
			:param mode: AUTO Automatically detects the following synchronization signal properties. • Subcarrier spacing • SS/PBCH block pattern • RB offset • Additional subcarrier offset • Cell ID MANual Lets you configure the SS/PBCH block manually.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManualMode)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:DETection {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.AutoManualMode:
		"""SCPI: CONFigure[:NR5G]:DL[:CC<cc>]:SSBLock:DETection \n
		Snippet: value: enums.AutoManualMode = driver.applications.k14Xnr5G.configure.nr5G.downlink.cc.ssBlock.detection.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command turns automatic detection of the synchronization signal configuration on and off. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: mode: AUTO Automatically detects the following synchronization signal properties. • Subcarrier spacing • SS/PBCH block pattern • RB offset • Additional subcarrier offset • Cell ID MANual Lets you configure the SS/PBCH block manually."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:DL:CC{carrierComponent_cmd_val}:SSBLock:DETection?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
