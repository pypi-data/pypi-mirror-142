from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class FormatPy:
	"""FormatPy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("formatPy", core, parent)

	def set(self, data_type: enums.IqDataFormat, store=repcap.Store.Default) -> None:
		"""SCPI: MMEMory:STORe<n>:IQ:FORMat \n
		Snippet: driver.applications.k14Xnr5G.massMemory.store.iq.formatPy.set(data_type = enums.IqDataFormat.FloatComplex=FLOat32,COMPlex, store = repcap.Store.Default) \n
		No command help available \n
			:param data_type: No help available
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
		"""
		param = Conversions.enum_scalar_to_str(data_type, enums.IqDataFormat)
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		self._core.io.write_with_opc(f'MMEMory:STORe{store_cmd_val}:IQ:FORMat {param}')

	# noinspection PyTypeChecker
	def get(self, store=repcap.Store.Default) -> enums.IqDataFormat:
		"""SCPI: MMEMory:STORe<n>:IQ:FORMat \n
		Snippet: value: enums.IqDataFormat = driver.applications.k14Xnr5G.massMemory.store.iq.formatPy.get(store = repcap.Store.Default) \n
		No command help available \n
			:param store: optional repeated capability selector. Default value: Pos1 (settable in the interface 'Store')
			:return: data_type: No help available"""
		store_cmd_val = self._cmd_group.get_repcap_cmd_value(store, repcap.Store)
		response = self._core.io.query_str_with_opc(f'MMEMory:STORe{store_cmd_val}:IQ:FORMat?')
		return Conversions.str_to_scalar_enum(response, enums.IqDataFormat)
