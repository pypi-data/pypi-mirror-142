import os
current_dir = os.path.dirname(os.path.abspath(__file__))
# we need to set the runtime of pythonnet to use netcoreapp instead of netframework
from clr_loader import get_coreclr
from pythonnet import set_runtime
# we get the core runtime configuration from the runtimeconfig file
rt = get_coreclr(os.path.join(current_dir, 'runtimeconfig.json'))

# we set the pythonnet runtime to use the core runtime we loaded from the config file
set_runtime(rt)

import clr
dlls = os.path.join(current_dir, 'dlls')
import sys
sys.path.append(dlls)
clr.AddReference('PrimaTestCaseLibrary')
from PrimaITestCaseLibrary.OutputView import IOutputViewer, OutputStringType
from PrimaTestCaseLibrary.BusinessTestCaseLibrary import MessageBuilderImpl, TestProjectImpl, ScriptSessionImpl
from PrimaTestCaseLibrary.Utils import Andi
import logging

class PythonOutputViewer(IOutputViewer):
    __namespace__ = "PrimaITestCaseLibrary.OutputView"
    def __init__(self, name) -> None:
        self.logger = logging.getLogger('andi.' + name)
    
    def log(self, msg):
        self.logger.debug(msg)
    def log(self, msg, ty):
        if ty == OutputStringType.Error:
            self.logger.error(msg)
            return
        if ty == OutputStringType.Warning:
            self.logger.warning(msg)
            return
        if ty == OutputStringType.Success or ty == OutputStringType.Information:
            self.logger.info(msg)
        self.logger.debug(msg)
    def clear(self):
        pass

class AndiApi(dict):
    def __init__(self, *args, **kwargs):
        super(AndiApi, self).__init__(*args, **kwargs)
        self.__dict__ = self

    @property
    def message_builder(self):
        """message builder object."""
        return self['message_builder']

    @property
    def andi(self):
        """andi object."""
        return self['andi']

    @property
    def channels(self):
        """project channels"""
        return self['channels']
    
    @property
    def databases(self):
        """project databases"""
        return self['databases']
    
    @property
    def messages(self):
        """project messages"""
        return self['messages']

# give user ability to load project
__project = TestProjectImpl()
__project.SetOutputViewer("python", PythonOutputViewer('default'))
message_builder = MessageBuilderImpl(__project)
ScriptSessionImpl.getInstance().IOutputViewer = PythonOutputViewer('andi.session')
andi = Andi(__project)
def load_project(atp) -> AndiApi:
    project = TestProjectImpl.Deserialize(atp)
    project.SetOutputViewer("python", PythonOutputViewer(project.name))
    scope = AndiApi()
    scope['__project'] = project
    scope['andi'] = Andi(project)
    scope['message_builder'] = MessageBuilderImpl(project)
    scope['channels'] = {}
    scope['databases'] = {}
    scope['messages'] = {}
    if project.Adapters:
        for channel in project.Adapters.Adapters:
            scope['channels'][channel.name] = channel.__implementation__
            scope[channel.name] = channel.__implementation__
    if project.DataBases:
        for db in project.DataBases.DataBases:
            scope['databases'][db.name] = db.__implementation__
            scope[db.name] = db.__implementation__
    if project.Messages:
        for msg in project.Messages.Messages:
            scope['messages'][msg.name] = msg.__implementation__
            scope[msg.name] = msg.__implementation__
    return scope
