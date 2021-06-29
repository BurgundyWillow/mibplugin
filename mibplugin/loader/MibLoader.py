from mibplugin.compile.CompileMib import CompileMib
from mibplugin.temporaryContainer.TempDir import TempDir

class MibLoader:

    def __init__(self, compiled_mib_path = None, source_mib_path = [], dependant_mib_paths = []):

        self.mib_compilation = CompileMib()
        self.temporary_dir = TempDir()
        if compiled_mib_path is None:
            self.compiled_mib_path = self.temporary_dir.get_full_path()
        else:
            self.compiled_mib_path = compiled_mib_path
        self.mib_compilation.AsnSources(sources=source_mib_path)
        self.mib_compilation.AsnSources(sources=dependant_mib_paths)


    def load(self, mib_names):
        self.mib_compilation.loadMib(mib_path=self.compiled_mib_path, mib_names=mib_names)
        return self.mib_compilation.getMibBuilder()

    def load_dir(self, mib_names):
        self.mib_compilation.loadMib(mib_path=self.compiled_mib_path, mib_names=mib_names)
        return temp_dir.get_full_path()

    def cleanup_temp(self):
        self.temporary_dir.cleanupDir()
        del self.temporary_dir





