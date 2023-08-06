from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from .......Internal.Utilities import trim_str_response
from ....... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DemodSetting:
	"""DemodSetting commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("demodSetting", core, parent)

	def set(self, file: str, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: MMEMory:LOAD[:CC<cc>]:DEModsetting \n
		Snippet: driver.applications.k10Xlte.massMemory.load.cc.demodSetting.set(file = '1', carrierComponent = repcap.CarrierComponent.Default) \n
		This command restores previously saved demodulation settings. The file must be of type .allocation and depends on the
		link direction that was currently selected when the file was saved. You can load only files with correct link directions. \n
			:param file: String containing the path and name of the file.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.value_to_quoted_str(file)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'MMEMory:LOAD:CC{carrierComponent_cmd_val}:DEModsetting {param}')

	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> str:
		"""SCPI: MMEMory:LOAD[:CC<cc>]:DEModsetting \n
		Snippet: value: str = driver.applications.k10Xlte.massMemory.load.cc.demodSetting.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command restores previously saved demodulation settings. The file must be of type .allocation and depends on the
		link direction that was currently selected when the file was saved. You can load only files with correct link directions. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: file: String containing the path and name of the file."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'MMEMory:LOAD:CC{carrierComponent_cmd_val}:DEModsetting?')
		return trim_str_response(response)
