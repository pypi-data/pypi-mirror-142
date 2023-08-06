from ...........Internal.Core import Core
from ...........Internal.CommandsGroup import CommandsGroup
from ...........Internal import Conversions
from ........... import enums
from ........... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, format_py: enums.PucchFormat, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> None:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc:PUCCh:FORMat \n
		Snippet: driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.pucch.formatPy.set(format_py = enums.PucchFormat.F1, carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		This command selects the PUCCH format for a specific subframe. The command is available if you have selected PUCCH format
		selection on subframe basis with method RsFsw.Applications.K10x_Lte.Configure.Lte.Uplink.Cc.Pucch.FormatPy.set. \n
			:param format_py: F1 (F1) F1A (F1a) F1B (F1b) F2 (F2) F2A (F2a) F2B (F2b) F3 (F3)
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
		"""
		param = Conversions.enum_scalar_to_str(format_py, enums.PucchFormat)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		self._core.io.write(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:PUCCh:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default, subframe=repcap.Subframe.Default) -> enums.PucchFormat:
		"""SCPI: CONFigure[:LTE]:UL[:CC<cc>]:SUBFrame<sf>:ALLoc:PUCCh:FORMat \n
		Snippet: value: enums.PucchFormat = driver.applications.k10Xlte.configure.lte.uplink.cc.subframe.alloc.pucch.formatPy.get(carrierComponent = repcap.CarrierComponent.Default, subframe = repcap.Subframe.Default) \n
		This command selects the PUCCH format for a specific subframe. The command is available if you have selected PUCCH format
		selection on subframe basis with method RsFsw.Applications.K10x_Lte.Configure.Lte.Uplink.Cc.Pucch.FormatPy.set. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:param subframe: optional repeated capability selector. Default value: Nr0 (settable in the interface 'Subframe')
			:return: format_py: F1 (F1) F1A (F1a) F1B (F1b) F2 (F2) F2A (F2a) F2B (F2b) F3 (F3)"""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		subframe_cmd_val = self._cmd_group.get_repcap_cmd_value(subframe, repcap.Subframe)
		response = self._core.io.query_str(f'CONFigure:LTE:UL:CC{carrierComponent_cmd_val}:SUBFrame{subframe_cmd_val}:ALLoc:PUCCh:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.PucchFormat)
