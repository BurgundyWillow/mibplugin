from mibplugin.loader.MibLoader import MibLoader
import os


os.environ['PYSNMP_MIB_DIRS'] = os.path.join(os.path.dirname(__file__), 'thispointsnowhere')

print(os.path.join(os.path.dirname(__file__), 'thispointsnowhere'))

def load_mibs(mib_names, compiled_mib_path = None, dependant_mib_path = [], source_mib_path = []):
    """
    Load Mibs, compiling them should the need arise. If unable to load, the mibs are compiled and saved to the compiled path or a temp location if it is not
    given.

    example - load_mibs(['INFINERA-GX-MIB'], compiled_mib_path = <dir as a pathlike[str] object>, dependant_mib_path=[file://dirpathasurl], source_mib_path=[file://dirpathurl])

    :param mib_names: Names of mibs to load as a list
    :type mib_names: list[str]
    :param compiled_mib_path: The path where the mibs are in their compiled form. If left empty, the mibs are compiled to temp.
    :type compiled_mib_path: str
    :param dependant_mib_path: List of directories where dependant mibs are, in the form URLs - file://, http://, etc.
    :type dependant_mib_path: list[str]
    :param source_mib_path: List of directories where required mibs that need to be compiled are
    :type source_mib_path: list[str]
    :return: A MibLoader object that can be passed around to SNMP functions. This should also be passed onto the close_mib_viewer function.
    :rtype: MibLoader

    """

    mib_loader = MibLoader(compiled_mib_path=compiled_mib_path, source_mib_path=source_mib_path,
                           dependant_mib_paths=dependant_mib_path)

    mib_loader.load(mib_names=mib_names)
    return mib_loader

def close_mib_viewer(mib_loader):
    """
    Call after opening mib object at the end after viewing the mib.

    :param mib_loader: Mib object returned by load_mibs
    :return: None
    """


    mib_loader.cleanup_temp()



