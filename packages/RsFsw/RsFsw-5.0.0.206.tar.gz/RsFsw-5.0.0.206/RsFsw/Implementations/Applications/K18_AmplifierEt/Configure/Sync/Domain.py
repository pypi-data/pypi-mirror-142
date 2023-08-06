from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Domain:
	"""Domain commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("domain", core, parent)

	def set(self, domain: enums.SyncDomain) -> None:
		"""SCPI: CONFigure:SYNC:DOMain \n
		Snippet: driver.applications.k18AmplifierEt.configure.sync.domain.set(domain = enums.SyncDomain.IQDirect) \n
		This command selects the synchronization method. \n
			:param domain: IQDirect I/Q data for the reference signal is directly correlated with the reference and measured signal. IQPDiff Correlation on the phase differentiated I/Q data. MAGNitude Correlation on the magnitude of the I/Q data with no regard for phase information. TRIGger It is assumed that the capture is triggered at the start of the reference waveform.
		"""
		param = Conversions.enum_scalar_to_str(domain, enums.SyncDomain)
		self._core.io.write(f'CONFigure:SYNC:DOMain {param}')

	# noinspection PyTypeChecker
	def get(self) -> enums.SyncDomain:
		"""SCPI: CONFigure:SYNC:DOMain \n
		Snippet: value: enums.SyncDomain = driver.applications.k18AmplifierEt.configure.sync.domain.get() \n
		This command selects the synchronization method. \n
			:return: domain: IQDirect I/Q data for the reference signal is directly correlated with the reference and measured signal. IQPDiff Correlation on the phase differentiated I/Q data. MAGNitude Correlation on the magnitude of the I/Q data with no regard for phase information. TRIGger It is assumed that the capture is triggered at the start of the reference waveform."""
		response = self._core.io.query_str(f'CONFigure:SYNC:DOMain?')
		return Conversions.str_to_scalar_enum(response, enums.SyncDomain)
