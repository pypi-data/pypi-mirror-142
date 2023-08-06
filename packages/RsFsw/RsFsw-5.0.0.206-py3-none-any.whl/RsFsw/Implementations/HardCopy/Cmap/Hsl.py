from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Types import DataType
from ....Internal.StructBase import StructBase
from ....Internal.ArgStruct import ArgStruct
from ....Internal.ArgSingleList import ArgSingleList
from ....Internal.ArgSingle import ArgSingle
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Hsl:
	"""Hsl commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hsl", core, parent)

	def set(self, hue: float, sat: float, lum: float, item=repcap.Item.Default) -> None:
		"""SCPI: HCOPy:CMAP<it>:HSL \n
		Snippet: driver.hardCopy.cmap.hsl.set(hue = 1.0, sat = 1.0, lum = 1.0, item = repcap.Item.Default) \n
		This command selects the color for various screen elements in print jobs. \n
			:param hue: hue tint Range: 0 to 1
			:param sat: sat saturation Range: 0 to 1
			:param lum: lum brightness Range: 0 to 1
			:param item: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Cmap')
		"""
		param = ArgSingleList().compose_cmd_string(ArgSingle('hue', hue, DataType.Float), ArgSingle('sat', sat, DataType.Float), ArgSingle('lum', lum, DataType.Float))
		item_cmd_val = self._cmd_group.get_repcap_cmd_value(item, repcap.Item)
		self._core.io.write(f'HCOPy:CMAP{item_cmd_val}:HSL {param}'.rstrip())

	# noinspection PyTypeChecker
	class HslStruct(StructBase):
		"""Response structure. Fields: \n
			- Hue: float: hue tint Range: 0 to 1
			- Sat: float: sat saturation Range: 0 to 1
			- Lum: float: lum brightness Range: 0 to 1"""
		__meta_args_list = [
			ArgStruct.scalar_float('Hue'),
			ArgStruct.scalar_float('Sat'),
			ArgStruct.scalar_float('Lum')]

		def __init__(self):
			StructBase.__init__(self, self)
			self.Hue: float = None
			self.Sat: float = None
			self.Lum: float = None

	def get(self, item=repcap.Item.Default) -> HslStruct:
		"""SCPI: HCOPy:CMAP<it>:HSL \n
		Snippet: value: HslStruct = driver.hardCopy.cmap.hsl.get(item = repcap.Item.Default) \n
		This command selects the color for various screen elements in print jobs. \n
			:param item: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Cmap')
			:return: structure: for return value, see the help for HslStruct structure arguments."""
		item_cmd_val = self._cmd_group.get_repcap_cmd_value(item, repcap.Item)
		return self._core.io.query_struct(f'HCOPy:CMAP{item_cmd_val}:HSL?', self.__class__.HslStruct())
