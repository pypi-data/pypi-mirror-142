from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Types import DataType
from .......Internal.ArgSingleList import ArgSingleList
from .......Internal.ArgSingle import ArgSingle
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Current:
	"""Current commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("current", core, parent)

	def get(self, counter: enums.Counter = None) -> int:
		"""SCPI: [SENSe]:SWEep:COUNt:CURRent \n
		Snippet: value: int = driver.applications.k70Vsa.sense.sweep.count.current.get(counter = enums.Counter.CAPTure) \n
		This command queries the current statistics counter value which indicates how many result ranges have been evaluated. For
		results that use the capture buffer as a source, the number of used capture buffers can be queried. \n
			:param counter: CAPTure | STATistics STATistics Returns the number of result ranges that have been evaluated. CAPTure Returns the number of used capture buffers evaluated.
			:return: count: No help available"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('counter', counter, DataType.Enum, enums.Counter, is_optional=True))
		response = self._core.io.query_str(f'SENSe:SWEep:COUNt:CURRent? {param}'.rstrip())
		return Conversions.str_to_int(response)
