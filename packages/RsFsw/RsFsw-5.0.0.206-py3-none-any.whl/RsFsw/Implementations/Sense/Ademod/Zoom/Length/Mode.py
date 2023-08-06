from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, mode: enums.AutoManualMode) -> None:
		"""SCPI: [SENSe]:ADEMod:ZOOM:LENGth:MODE \n
		Snippet: driver.sense.ademod.zoom.length.mode.set(mode = enums.AutoManualMode.AUTO) \n
		The command defines whether the length of the zoom area for the analog-demodulated measurement data is defined
		automatically or manually in the specified window. \n
			:param mode: AUTO | MAN AUTO (Default:) The number of sweep points is used as the zoom length. MAN The zoom length is defined manually using [SENSe:]ADEModn:ZOOM:LENGth.
		"""
		param = Conversions.enum_scalar_to_str(mode, enums.AutoManualMode)
		self._core.io.write(f'SENSe:ADEMod:ZOOM:LENGth:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.AutoManualMode:
		"""SCPI: [SENSe]:ADEMod:ZOOM:LENGth:MODE \n
		Snippet: value: enums.AutoManualMode = driver.sense.ademod.zoom.length.mode.get() \n
		The command defines whether the length of the zoom area for the analog-demodulated measurement data is defined
		automatically or manually in the specified window. \n
			:return: mode: AUTO | MAN AUTO (Default:) The number of sweep points is used as the zoom length. MAN The zoom length is defined manually using [SENSe:]ADEModn:ZOOM:LENGth."""
		response = self._core.io.query_str(f'SENSe:ADEMod:ZOOM:LENGth:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.AutoManualMode)
