from ....Internal.Core import Core
from ....Internal.CommandsGroup import CommandsGroup
from ....Internal.Utilities import trim_str_response


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class HwInfo:
	"""HwInfo commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("hwInfo", core, parent)

	def get(self) -> str:
		"""SCPI: DIAGnostic:SERVice:HWINfo \n
		Snippet: value: str = driver.diagnostic.service.hwInfo.get() \n
		This command queries hardware information. \n
			:return: hardware: String containing the following information for every hardware component. component: name of the hardware component serial#: serial number of the component order#: order number of the component model: model of the component code: code of the component revision: revision of the component subrevision: subrevision of the component"""
		response = self._core.io.query_str(f'DIAGnostic:SERVice:HWINfo?')
		return trim_str_response(response)
