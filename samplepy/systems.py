from samplepy.io import (
    export_to_file,
    import_from_file,
)

class System(object):
    """
    A basic system.
    
    Parameters
    ----------
    name: string
        Name of the system
    filename: string
        Name of the file from which to import components of the system
    override_components: list
        List of components to override if filename is not provided
    kwargs:
        Any remaining attributes to set
    
    Returns
    -------
    None
    
    Examples
    --------
    >>> s = samplepy.System('a_system.mat', 'my_system', [])
    
    """
    
    def __init__(
        self,
        name='',
        filename='',
        override_components='',
        **kwargs,
    ):
        if filename:
            self.components = import_from_file(filename)
        elif override_components:
            self.components = override_components
        else:
            self.components = []
        self.name = name
        self.size = size
        
    def set_components(self, newname):
        """
        Change the system name.
        
        Parameters
        ----------
        newname: string
            New name of the system
        
        Returns
        -------
        None
        """
        self.name = newname
        
    def set_components(self, components):
        """
        Change the system components.
        
        Parameters
        ----------
        components: list
            List of components to override the existing ones
        
        Returns
        -------
        None
        """
        self.components = components
        
    def save(self, filename):
        """
        Save the system to a file.
        
        Parameters
        ----------
        filename: string
            Name of the file to save
        
        Returns
        -------
        None
        """
        export_to_file(self.components, filename)
        
        