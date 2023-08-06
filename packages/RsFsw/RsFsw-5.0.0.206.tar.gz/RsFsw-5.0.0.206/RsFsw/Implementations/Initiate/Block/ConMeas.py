from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal import Conversions


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class ConMeas:
	"""ConMeas commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("conMeas", core, parent)

	def set(self, group_name: str = None) -> None:
		"""SCPI: INITiate:BLOCk:CONMeas \n
		Snippet: driver.initiate.block.conMeas.set(group_name = '1') \n
		No command help available \n
			:param group_name: No help available
		"""
		param = ''
		if group_name:
			param = Conversions.value_to_quoted_str(group_name)
		self._core.io.write(f'INITiate:BLOCk:CONMeas {param}'.strip())
