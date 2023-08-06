from .......Internal.Core import Core
from .......Internal.CommandsGroup import CommandsGroup
from .......Internal import Conversions
from ....... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Mode:
	"""Mode commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("mode", core, parent)

	def set(self, fine_sync: enums.FineSync) -> None:
		"""SCPI: [SENSe]:DDEMod:FSYNc[:MODE] \n
		Snippet: driver.applications.k70Vsa.sense.ddemod.fsync.mode.set(fine_sync = enums.FineSync.DDATa) \n
		This command defines the fine synchronization mode used to calculate results, e.g. the bit error rate. Note:You can
		define a maximum symbol error rate (SER) for the known data in reference to the analyzed data. If the SER of the known
		data exceeds this limit, the default synchronization using the detected data is performed. See [SENSe:]DDEMod:FSYNc:LEVel. \n
			:param fine_sync: KDATa | PATTern | DDATa KDATa (Default) The reference signal is defined as the data sequence from the loaded Known Data file that most closely matches the measured data. PATTern The reference signal is estimated from the defined pattern. This setting requires an activated pattern search, see [SENSe:]DDEMod:SEARch:SYNC:STATe. DDATa The reference signal is estimated from the detected data.
		"""
		param = Conversions.enum_scalar_to_str(fine_sync, enums.FineSync)
		self._core.io.write(f'SENSe:DDEMod:FSYNc:MODE {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.FineSync:
		"""SCPI: [SENSe]:DDEMod:FSYNc[:MODE] \n
		Snippet: value: enums.FineSync = driver.applications.k70Vsa.sense.ddemod.fsync.mode.get() \n
		This command defines the fine synchronization mode used to calculate results, e.g. the bit error rate. Note:You can
		define a maximum symbol error rate (SER) for the known data in reference to the analyzed data. If the SER of the known
		data exceeds this limit, the default synchronization using the detected data is performed. See [SENSe:]DDEMod:FSYNc:LEVel. \n
			:return: fine_sync: KDATa | PATTern | DDATa KDATa (Default) The reference signal is defined as the data sequence from the loaded Known Data file that most closely matches the measured data. PATTern The reference signal is estimated from the defined pattern. This setting requires an activated pattern search, see [SENSe:]DDEMod:SEARch:SYNC:STATe. DDATa The reference signal is estimated from the detected data."""
		response = self._core.io.query_str(f'SENSe:DDEMod:FSYNc:MODE?')
		return Conversions.str_to_scalar_enum(response, enums.FineSync)
