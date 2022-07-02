class BasicComponent(object):
    """
    A basic component.
    
    Parameters
    ----------
    name: string
        Name of the component
    size: string
        Size of the component
    kwargs:
        Any remaining attributes to set
    
    Returns
    -------
    None
    
    Examples
    --------
    >>> bc = samplepy.BasicComponent('my_component', 'small')
    
    """
    
    def __init__(
        self,
        name='',
        size='',
        **kwargs,
    ):
        self.name = name
        self.size = size
        
    def set_name(self, newname):
        """
        Change the component name.
        
        Parameters
        ----------
        newname: string
            New name of the component.
        
        Returns
        -------
        None
        """
        self.name = newname
        
    def change_size(self, newsize):
        """
        Change the size of the component.
        
        Parameters
        ----------
        newsize: string
            New size of the component.
        
        Returns
        -------
        None
        """
        self.size = newsize
        