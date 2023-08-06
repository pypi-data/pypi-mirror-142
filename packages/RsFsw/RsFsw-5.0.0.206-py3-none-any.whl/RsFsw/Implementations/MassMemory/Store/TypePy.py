from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class TypePy:
	"""TypePy commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("typePy", core, parent)

	def set(self, type_py: enums.StoreType) -> None:
		"""SCPI: MMEMory:STORe:TYPE \n
		Snippet: driver.massMemory.store.typePy.set(type_py = enums.StoreType.CHANnel) \n
		This command defines whether the data from the entire instrument or only from the current channel is stored with the
		subsequent MMEM:STOR... command. \n
			:param type_py: INSTrument | CHANnel INSTrument Stores data from the entire instrument. CHANnel Stores data from an individual channel.
		"""
		param = Conversions.enum_scalar_to_str(type_py, enums.StoreType)
		self._core.io.write(f'MMEMory:STORe:TYPE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.StoreType:
		"""SCPI: MMEMory:STORe:TYPE \n
		Snippet: value: enums.StoreType = driver.massMemory.store.typePy.get() \n
		This command defines whether the data from the entire instrument or only from the current channel is stored with the
		subsequent MMEM:STOR... command. \n
			:return: type_py: INSTrument | CHANnel INSTrument Stores data from the entire instrument. CHANnel Stores data from an individual channel."""
		response = self._core.io.query_str(f'MMEMory:STORe:TYPE?')
		return Conversions.str_to_scalar_enum(response, enums.StoreType)
