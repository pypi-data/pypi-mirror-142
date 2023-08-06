from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Auto:
	"""Auto commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("auto", core, parent)

	def set(self, auto_patt_search: enums.AutoManualMode) -> None:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:AUTO \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.search.sync.auto.set(auto_patt_search = enums.AutoManualMode.AUTO) \n
		This command links the pattern search to the type of signal. When a signal is marked as patterned, pattern search is
		switched on automatically. \n
			:param auto_patt_search: AUTO | MANual
		"""
		param = Conversions.enum_scalar_to_str(auto_patt_search, enums.AutoManualMode)
		self._core.io.write(f'SENSe:DDEMod:SEARch:SYNC:AUTO {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoManualMode:
		"""SCPI: [SENSe]:DDEMod:SEARch:SYNC:AUTO \n
		Snippet: value: enums.AutoManualMode = driver.applications.k70Vsa.sense.ddemod.search.sync.auto.get() \n
		This command links the pattern search to the type of signal. When a signal is marked as patterned, pattern search is
		switched on automatically. \n
			:return: auto_patt_search: AUTO | MANual"""
		response = self._core.io.query_str(f'SENSe:DDEMod:SEARch:SYNC:AUTO?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
