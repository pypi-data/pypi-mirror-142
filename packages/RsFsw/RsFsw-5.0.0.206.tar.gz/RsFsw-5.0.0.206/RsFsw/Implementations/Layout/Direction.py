from ...Internal.Core import Core
from ...Internal.CommandsGroup import CommandsGroup
from ...Internal import Conversions
from ... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Direction:
	"""Direction commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("direction", core, parent)

	# noinspection PyTypeChecker
	def get(self) -> enums.XyDirection:
		"""SCPI: LAYout:DIRection \n
		Snippet: value: enums.XyDirection = driver.layout.direction.get() \n
		No command help available \n
			:return: direction: No help available"""
		response = self._core.io.query_str_with_opc(f'LAYout:DIRection?')
		return Conversions.str_to_scalar_enum(response, enums.XyDirection)
