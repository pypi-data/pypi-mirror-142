from ......Internal.Core import Core
from ......Internal.CommandsGroup import CommandsGroup
from ......Internal import Conversions
from ...... import enums
from ...... import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Sband:
	"""Sband commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("sband", core, parent)

	def set(self, value: enums.NormalInverted, outputConnector=repcap.OutputConnector.Default) -> None:
		"""SCPI: OUTPut<up>:IF:SBANd \n
		Snippet: driver.applications.k70Vsa.output.ifreq.sband.set(value = enums.NormalInverted.INVerted, outputConnector = repcap.OutputConnector.Default) \n
		This command queries the sideband provided at the 'IF OUT 2 GHz' connector compared to the sideband of the RF signal. The
		sideband depends on the current center frequency. \n
			:param value: No help available
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
		"""
		param = Conversions.enum_scalar_to_str(value, enums.NormalInverted)
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		self._core.io.write(f'OUTPut{outputConnector_cmd_val}:IF:SBANd {param}')

	# noinspection PyTypeChecker
	def get(self, outputConnector=repcap.OutputConnector.Default) -> enums.NormalInverted:
		"""SCPI: OUTPut<up>:IF:SBANd \n
		Snippet: value: enums.NormalInverted = driver.applications.k70Vsa.output.ifreq.sband.get(outputConnector = repcap.OutputConnector.Default) \n
		This command queries the sideband provided at the 'IF OUT 2 GHz' connector compared to the sideband of the RF signal. The
		sideband depends on the current center frequency. \n
			:param outputConnector: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Output')
			:return: value: NORMal The sideband at the output is identical to the RF signal. INVerted The sideband at the output is the inverted RF signal sideband."""
		outputConnector_cmd_val = self._cmd_group.get_repcap_cmd_value(outputConnector, repcap.OutputConnector)
		response = self._core.io.query_str(f'OUTPut{outputConnector_cmd_val}:IF:SBANd?')
		return Conversions.str_to_scalar_enum(response, enums.NormalInverted)
