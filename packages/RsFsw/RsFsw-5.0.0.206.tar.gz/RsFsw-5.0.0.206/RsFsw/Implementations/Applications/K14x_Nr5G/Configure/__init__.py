from .....Internal.Core import Core
from .....Internal.CommandsGroup import CommandsGroup


# noinspection PyPep8Naming,PyAttributeOutsideInit,SpellCheckingInspection
class Configure:
	"""Configure commands group definition. 365 total commands, 3 Subgroups, 1 group commands"""

	def __init__(self, core: Core, parent):
		self._core = core
		self._cmd_group = CommandsGroup("configure", core, parent)

	@property
	def generator(self):
		"""generator commands group. 7 Sub-classes, 0 commands."""
		if not hasattr(self, '_generator'):
			from .Generator import Generator
			self._generator = Generator(self._core, self._cmd_group)
		return self._generator

	@property
	def settings(self):
		"""settings commands group. 2 Sub-classes, 0 commands."""
		if not hasattr(self, '_settings'):
			from .Settings import Settings
			self._settings = Settings(self._core, self._cmd_group)
		return self._settings

	@property
	def nr5G(self):
		"""nr5G commands group. 27 Sub-classes, 0 commands."""
		if not hasattr(self, '_nr5G'):
			from .Nr5G import Nr5G
			self._nr5G = Nr5G(self._core, self._cmd_group)
		return self._nr5G

	def preset(self) -> None:
		"""SCPI: CONFigure:PRESet \n
		Snippet: driver.applications.k14Xnr5G.configure.preset() \n
		No command help available \n
		"""
		self._core.io.write(f'CONFigure:PRESet')

	def preset_with_opc(self, opc_timeout_ms: int = -1) -> None:
		"""SCPI: CONFigure:PRESet \n
		Snippet: driver.applications.k14Xnr5G.configure.preset_with_opc() \n
		No command help available \n
		Same as preset, but waits for the operation to complete before continuing further. Use the RsFsw.utilities.opc_timeout_set() to set the timeout value. \n
			:param opc_timeout_ms: Maximum time to wait in milliseconds, valid only for this call."""
		self._core.io.write_with_opc(f'CONFigure:PRESet', opc_timeout_ms)

	def clone(self) -> 'Configure':
		"""Clones the group by creating new object from it and its whole existing subgroups
		Also copies all the existing default Repeated Capabilities setting,
		which you can change independently without affecting the original group"""
		new_group = Configure(self._core, self._cmd_group.parent)
		self._cmd_group.synchronize_repcaps(new_group)
		return new_group
