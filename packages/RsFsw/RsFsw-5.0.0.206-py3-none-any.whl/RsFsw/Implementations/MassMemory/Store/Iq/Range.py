from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup
from .....Internal import Conversions
from ..... import enums
from ..... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Range:
	"""Range commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("range", core, parent)

	def set(self, range_type: enums.IqRangeType, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:IQ:RANGe \n
		Snippet: driver.massMemory.store.iq.range.set(range_type = enums.IqRangeType.CAPTure, store = repcap.Store.Default) \n
		No command help available \n
			:param range_type: No help available
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = Conversions.enum_scalar_to_str(range_type, enums.IqRangeType)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write(f'MMEMory:STORe{store_cmd_val}:IQ:RANGe {param}')

	# noinspection PyTypeChecker
	def get(self, store=repcap.Store.Default) -> enums.IqRangeType:
		"""SCPI: MMEMory:STORe<n>:IQ:RANGe \n
		Snippet: value: enums.IqRangeType = driver.massMemory.store.iq.range.get(store = repcap.Store.Default) \n
		No command help available \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: range_type: No help available"""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		response = self._core.io.query_str(f'MMEMory:STORe{store_cmd_val}:IQ:RANGe?')
		return Conversions.str_to_scalar_enum(response, enums.IqRangeType)
