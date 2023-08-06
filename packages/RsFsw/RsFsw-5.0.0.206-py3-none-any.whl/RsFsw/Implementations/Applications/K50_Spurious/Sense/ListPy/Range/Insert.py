from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Insert:
	"""Insert commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("insert", core, parent)

	def set(self, direction: enums.LeftRightDirection, rangePy=repcap.RangePy.Default) -> None:
		"""SCPI: [SENSe]:LIST:RANGe<ri>:INSert \n
		Snippet: driver.applications.k50Spurious.sense.listPy.range.insert.set(direction = enums.LeftRightDirection.LEFT, rangePy = repcap.RangePy.Default) \n
		Adds a range right or left to the selected one. If the command is used on a range that does not yet exist, the range and
		all with lower indices up to this one are created. \n
			:param direction: LEFT | RIGHt
			:param rangePy: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Range')
		"""
		param = Conversions.enum_scalar_to_str(direction, enums.LeftRightDirection)
		rangePy_cmd_val = self._cmd_group.get_repcap_cmd_value(rangePy, repcap.RangePy)
		self._core.io.write(f'SENSe:LIST:RANGe{rangePy_cmd_val}:INSert {param}')
