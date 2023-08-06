from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class State:
	"""State commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("state", core, parent)

	def set(self, state: enums.LimitState, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default, limitIx=repcap.LimitIx.Default) -> None:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:LIMit<li>:STATe \n
		Snippet: driver.applications.k10Xlte.sense.espectrum.range.limit.state.set(state = enums.LimitState.ABSolute, subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param state: No help available
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
		"""
		param = Conversions.enum_scalar_to_str(state, enums.LimitState)
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		self._core.io.write(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:LIMit{limitIx_cmd_val}:STATe {param}')

	# noinspection PyTypeChecker
	def get(self, subBlock=repcap.SubBlock.Default, rangePy=repcap.RangePy.Default, limitIx=repcap.LimitIx.Default) -> enums.LimitState:
		"""SCPI: [SENSe]:ESPectrum<sb>:RANGe<ri>:LIMit<li>:STATe \n
		Snippet: value: enums.LimitState = driver.applications.k10Xlte.sense.espectrum.range.limit.state.get(subBlock = repcap.SubBlock.Default, rangePy = repcap.RangePy.Default, limitIx = repcap.LimitIx.Default) \n
		No command help available \n
			:param subBlock: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Espectrum')
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
			:param limitIx: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Limit')
			:return: state: No help available"""
		subBlock_cmd_val = self._cmd_group.get_repcap_cmd_value(subBlock, repcap.SubBlock)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		limitIx_cmd_val = self._cmd_group.get_repcap_cmd_value(limitIx, repcap.LimitIx)
		response = self._core.io.query_str(f'SENSe:ESPectrum{subBlock_cmd_val}:RANGe{rangePy_cmd_val}:LIMit{limitIx_cmd_val}:STATe?')
		return Conversions.str_to_scalar_enum(response, enums.LimitState)
