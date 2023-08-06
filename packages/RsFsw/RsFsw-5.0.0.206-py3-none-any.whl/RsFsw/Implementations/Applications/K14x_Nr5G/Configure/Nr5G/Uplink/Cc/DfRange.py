from ........Internal.Core import Core
from ........Internal.CommandsGroup import CommandsGroup
from ........Internal import Conversions
from ........ import enums
from ........ import repcap


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class DfRange:
	"""DfRange commands group definition. 1 total commands, 0 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("dfRange", core, parent)

	def set(self, deployment: enums.DeploymentFrange, carrierComponent=repcap.CarrierComponent.Default) -> None:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:DFRange \n
		Snippet: driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.dfRange.set(deployment = enums.DeploymentFrange.EHIGh, carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the deployment frequency range of the signal. \n
			:param deployment: LOW Deployment in FR1 ≤ 3 GHz. MIDDle Deployment in FR1 3 GHz. HIGH Deployment in FR2.
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
		"""
		param = Conversions.enum_scalar_to_str(deployment, enums.DeploymentFrange)
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		self._core.io.write(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:DFRange {param}')

	# noinspection PyTypeChecker
	def get(self, carrierComponent=repcap.CarrierComponent.Default) -> enums.DeploymentFrange:
		"""SCPI: CONFigure[:NR5G]:UL[:CC<cc>]:DFRange \n
		Snippet: value: enums.DeploymentFrange = driver.applications.k14Xnr5G.configure.nr5G.uplink.cc.dfRange.get(carrierComponent = repcap.CarrierComponent.Default) \n
		This command selects the deployment frequency range of the signal. \n
			:param carrierComponent: optional repeated capability selector. Default value: Nr1 (settable in the interface 'Cc')
			:return: deployment: LOW Deployment in FR1 ≤ 3 GHz. MIDDle Deployment in FR1 3 GHz. HIGH Deployment in FR2."""
		carrierComponent_cmd_val = self._cmd_group.get_repcap_cmd_value(carrierComponent, repcap.CarrierComponent)
		response = self._core.io.query_str(f'CONFigure:NR5G:UL:CC{carrierComponent_cmd_val}:DFRange?')
		return Conversions.str_to_scalar_enum(response, enums.DeploymentFrange)
