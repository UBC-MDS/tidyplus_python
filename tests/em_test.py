import numpy as np
import pytest
import pandas as pd

from tidyplusPy import em
from tidyplusPy import mmm

d = {'v_num': [4.1,np.nan,12.2,11,3.4,1.6,3.3,5.5], 'v_char': ['one','two','','two','two','one','two','two']}
data = pd.DataFrame(data=d)
col = list(data["v_num"])
dat = [1,2,3,np.nan]
def test_input():
    """
    Tests incorrect/unacceptable input data.
    These should raise a type error.
    check data type
    """

    with pytest.raises(TypeError):
        em( data = 'some string' )

    with pytest.raises(TypeError):
        em( data = False )

    with pytest.raises(TypeError):
        em( data = 2 )

    with pytest.raises(TypeError):
        em( data = np.array([0, np.nan, 2]) )


def missings():
    """
    Check the missing values
    These should raise a value error.
    """

    empty_array = np.array([])

    with pytest.raises(ValueError):
        em( data = empty_array )
        
    
    assert isinstance(data, pd.DataFrame)
    assert isinstance(list(data["v_num"]),list)
    assert isinstance(data.v_char[1],str)
    assert sum(data.v_num.isnull()) > 0
    assert sum(data.v_char=='') > 0
    
   # df.columns[df.isnull().any()]
    
    
#### New tests


### Check for inputes for both EM 

def em_array_match():
    with pytest.raises(TypeError("Input for EM can only be nd array")):
        em(data,loops = 50)
def em_run_array_match():
    with pytest.raises(TypeError("Input for EM can only be nd array")):
        em_run(data,loops = 50)
 


    

