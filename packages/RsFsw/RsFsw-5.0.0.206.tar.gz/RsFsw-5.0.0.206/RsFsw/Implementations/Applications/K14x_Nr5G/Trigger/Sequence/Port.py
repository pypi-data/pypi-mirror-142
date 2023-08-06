from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Port:
	"""Port commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("port", core, parent)

	def set(self, port: enums.Port) -> None:
		"""SCPI: TRIGger[:SEQuence]:PORT \n
		Snippet: driver.applications.k14Xnr5G.trigger.sequence.port.set(port = enums.Port.PORT1) \n
		This command selects the trigger port for measurements with devices that have several trigger ports. \n
			:param port: PORT1 PORT2 PORT3
		"""
		param = Conversions.enum_scalar_to_str(port, enums.Port)
		self._core.io.write(f'TRIGger:SEQuence:PORT {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Port:
		"""SCPI: TRIGger[:SEQuence]:PORT \n
		Snippet: value: enums.Port = driver.applications.k14Xnr5G.trigger.sequence.port.get() \n
		This command selects the trigger port for measurements with devices that have several trigger ports. \n
			:return: port: PORT1 PORT2 PORT3"""
		response = self._core.io.query_str(f'TRIGger:SEQuence:PORT?')
		return Conversions.str_to_scalar_enum(response, enums.Port)
