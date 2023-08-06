from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ......Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Logo:
	"""Logo commands group definition. 2 total commands, 1 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("logo", core, parent)

	@property
	def control(self):
		"""control commands group. 0 Sub-classes, 1 commands."""
		if not hasattr(self, '_control'):
			from .Control import Control
			self._control = Control(self._core, self._cmd_group)
		return self._control

	def set(self, arg_0: str) -> None:
		"""SCPI: HCOPy:TREPort:ITEM:LOGO \n
		Snippet: driver.hardCopy.treport.item.logo.set(arg_0 = '1') \n
		This command selects a graphic (for example a company logo) that is shown at the top of each page in the test report. Use
		method RsFsw.HardCopy.Treport.Item.Logo.Control.set to select the conditions under which the picture is shown. \n
			:param arg_0: String containing the location and name of the picture.
		"""
		param = Conversions.value_to_quoted_str(arg_0)
		self._core.io.write(f'HCOPy:TREPort:ITEM:LOGO {param}')

	def get(self) -> str:
		"""SCPI: HCOPy:TREPort:ITEM:LOGO \n
		Snippet: value: str = driver.hardCopy.treport.item.logo.get() \n
		This command selects a graphic (for example a company logo) that is shown at the top of each page in the test report. Use
		method RsFsw.HardCopy.Treport.Item.Logo.Control.set to select the conditions under which the picture is shown. \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'HCOPy:TREPort:ITEM:LOGO?')
		return trim_str_response(response)

	def clone(self) -> 'Logo':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Logo(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
