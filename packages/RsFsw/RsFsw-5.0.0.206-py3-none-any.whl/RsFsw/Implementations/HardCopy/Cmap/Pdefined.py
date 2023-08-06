from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions
from .... import enums
from .... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Pdefined:
	"""Pdefined commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("pdefined", core, parent)

	def set(self, color: enums.Color, item=repcap.Item.Default) -> None:
		"""SCPI: HCOPy:CMAP<it>:PDEFined \n
		Snippet: driver.hardCopy.cmap.pdefined.set(color = enums.Color.BLACk, item = repcap.Item.Default) \n
		This command selects a predefined color for various screen elements in print jobs. \n
			:param color: BLACk | BLUE | BROWn | GREen | CYAN | RED | MAGenta | YELLow | WHITe | DGRay | LGRay | LBLue | LGReen | LCYan | LRED | LMAGenta
			:param item: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Cmap')
		"""
		param = Conversions.enum_scalar_to_str(color, enums.Color)
		item_cmd_val = self._cmd_group.get_repcap_cmd_value(item, repcap.Item)
		self._core.io.write(f'HCOPy:CMAP{item_cmd_val}:PDEFined {param}')

	# noinspection PyTypeChecker
	def get(self, item=repcap.Item.Default) -> enums.Color:
		"""SCPI: HCOPy:CMAP<it>:PDEFined \n
		Snippet: value: enums.Color = driver.hardCopy.cmap.pdefined.get(item = repcap.Item.Default) \n
		This command selects a predefined color for various screen elements in print jobs. \n
			:param item: optional repeated capability selector. Default value: Ix1 (settable in the interface 'Cmap')
			:return: color: BLACk | BLUE | BROWn | GREen | CYAN | RED | MAGenta | YELLow | WHITe | DGRay | LGRay | LBLue | LGReen | LCYan | LRED | LMAGenta"""
		item_cmd_val = self._cmd_group.get_repcap_cmd_value(item, repcap.Item)
		response = self._core.io.query_str(f'HCOPy:CMAP{item_cmd_val}:PDEFined?')
		return Conversions.str_to_scalar_enum(response, enums.Color)
