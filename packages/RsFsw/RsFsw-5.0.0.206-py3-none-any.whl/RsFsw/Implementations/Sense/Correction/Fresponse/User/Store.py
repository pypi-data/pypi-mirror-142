from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Store:
	"""Store commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("store", core, parent)

	def set(self, file_path: str) -> None:
		"""SCPI: [SENSe]:CORRection:FRESponse:USER:STORe \n
		Snippet: driver.sense.correction.fresponse.user.store.set(file_path = '1') \n
		Stores a saveset for a user-defined frequency response correction scenario. By default, the saveset is stored in the
		C:/R_S/INSTR/USER/FResponse directory. \n
			:param file_path: string
		"""
		param = Conversions.value_to_quoted_str(file_path)
		self._core.io.write(f'SENSe:CORRection:FRESponse:USER:STORe {param}')
