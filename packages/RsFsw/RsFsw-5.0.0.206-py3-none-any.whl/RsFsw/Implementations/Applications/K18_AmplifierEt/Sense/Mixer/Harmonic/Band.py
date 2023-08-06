from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Band:
	"""Band commands group definition. 2 total commands, 0 Subgroups, 2 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("band", core, parent)

	def set(self, arg_0: enums.Band) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic:BAND \n
		Snippet: driver.applications.k18AmplifierEt.sense.mixer.harmonic.band.set(arg_0 = enums.Band.A) \n
		No command help available \n
			:param arg_0: No help available
		"""
		param = Conversions.enum_scalar_to_str(arg_0, enums.Band)
		self._core.io.write(f'SENSe:MIXer:HARMonic:BAND {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.Band:
		"""SCPI: [SENSe]:MIXer:HARMonic:BAND \n
		Snippet: value: enums.Band = driver.applications.k18AmplifierEt.sense.mixer.harmonic.band.get() \n
		No command help available \n
			:return: arg_0: No help available"""
		response = self._core.io.query_str(f'SENSe:MIXer:HARMonic:BAND?')
		return Conversions.str_to_scalar_enum(response, enums.Band)

	def preset(self) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic:BAND:PRESet \n
		Snippet: driver.applications.k18AmplifierEt.sense.mixer.harmonic.band.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'SENSe:MIXer:HARMonic:BAND:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: [SENSe]:MIXer:HARMonic:BAND:PRESet \n
		Snippet: driver.applications.k18AmplifierEt.sense.mixer.harmonic.band.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'SENSe:MIXer:HARMonic:BAND:PRESet', opc_timeout_ms)
