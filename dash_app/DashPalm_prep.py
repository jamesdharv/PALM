
## Libraries 
import rpy2.robjects.packages as rpackages
import pandas as pd 
import numpy as np 

# working with dataframes 
from rpy2.robjects.conversion import localconverter
import rpy2.robjects as ro
from rpy2.robjects import pandas2ri
from rpy2.robjects.vectors import StrVector 

# TODO: suppress system warnings from imports 
# some odd reason, I need to run thi
from rpy2.robjects.packages import importr
utils = importr('utils') 
# getting ready to download these packages... 
importr('PALM') 
importr('Hmisc') 
rpackages.importr('ggpubr')


def rpy_2py(df): 
    ''' convenient function that will convert rpy object to a pandas data.frame 
    '''
    with localconverter(ro.default_converter + pandas2ri.converter):
        return(ro.conversion.rpy2py(df))

    
def py2_rpy(df): 
    ''' convenient function that will convert a pandas data.frame to rpy object that can then be used 
        for R functions 
    '''
    with localconverter(ro.default_converter + pandas2ri.converter):
        return(ro.conversion.py2rpy(df))
    
    
def sample_overlap(mat, meta):
    ''' overlap the datamtrix with emtadata for selecting available samples only 
    '''
    # create bridging robject 
    r = ro.r 
    
    # load robject functions - intersect & colnames 
    r.intersect = ro.r['intersect'] 
    r.colnames = ro.r['colnames'] 
    overlap = r.intersect(meta[0], r.colnames(mat))
    
    # convert rpy object to py object and overlap data
    mat_py = rpy_2py(mat)
    meta_py = rpy_2py(meta)
    mat_py = mat_py.loc[:, list(overlap)]
    meta_py = meta_py.loc[meta_py['Sample'].isin(list(overlap)), ]
    meta_py.index = ro.r['ann'][0] 
    return (mat_py, meta_py) 

def apply_na_threshold(data, threshold=0.4): 
    '''
    '''
    # calculate how many NA's in each row 
    data['number_NA'] = data.isna().sum(axis=1) 
    filtered_data = data.loc[data['number_NA'] <= len(data.columns)*0.4, ]
    filtered_data.drop(columns=['number_NA'],inplace=True)
    return filtered_data 

def load_data(matrix_fp, meta_fp): 
    ''' 
    '''
    # create bridging robject 
    r = ro.r 
    
    # loads robjects named "data"  and "ann" 
    datamatrix_r = ro.r['load'](matrix_fp)
    datamatrix_r = ro.r['data'] # users can choose data here  
    metadata_r = ro.r['load'](meta_fp)
    metadata_r = ro.r['ann'] # users could choose data here 

    
    datamatrix, metadata = sample_overlap(datamatrix_r, metadata_r) 
    
    # TODO: should this cut-off be added to dash app UI? 
    # DEFAULT - 0.4 of number of columns 
    datamatrix = apply_na_threshold(datamatrix) 

    return(datamatrix, metadata)  


def run_lmeVariance(matrix, metadata, featureSet): 
    '''
    '''
    # load lmeVariance object function and run 
    lmeVariance = ro.r['lmeVariance'] 
    lmem_res = rpy_2py(lmeVariance(ann=py2_rpy(metadata), 
                           mat=py2_rpy(matrix), 
                           featureSet=featureSet, 
                           meanThreshold=1
                          ))
    mean_vals = lmem_res.loc[:, 'mean'] 
    lmem_res['mean_log10'] = np.log10(lmem_res['mean'] + 1) 
    return lmem_res 


def run_outlier_detection(metadata, datamatrix, z_cutoff=2): 
    '''
    '''
    # robject of outlierDetect function 
    outlierDetect = ro.r['outlierDetect']
    outlier_res = outlierDetect(ann = py2_rpy(metadata), 
                                mat = py2_rpy(datamatrix), 
                                z_cutoff=z_cutoff
                               )
    outlier_res_py = rpy_2py(outlier_res) 
    
    # add categorical variables 
    outlier_res_py.loc[outlier_res_py['z'] > 0, 'zgroup'] = "> Z" 
    outlier_res_py.loc[outlier_res_py['z'] < 0, 'zgroup'] = "< -Z" 
    
    outlier_res_py['z_cutoff'] = z_cutoff 
    return outlier_res_py  


def gen_dash_app():
    '''
    '''
    pass 


def run(datamatrix_filepath, metadata_filepath): 
    ''' main function 
        1. load datasets 
        2. setting up; running custom functions 
        3. generate App in new tab 
    '''
    # TODO: some variables to be set be user. 
    # maybe move these to app UI?
    featureSet=ro.StrVector(('PTID', 'Time'))
    meanThreshold = 1
    z_cutoff = 2 
    
    datamatrix, metadata = load_data(datamatrix_filepath, metadata_filepath)
    lmem_df = run_lmeVariance(datamatrix, metadata, featureSet) 
    outlier_res_py = run_outlier_detection(metadata, datamatrix, z_cutoff) 
    
    #import pdb; pdb.set_trace() 
    #gen_dash_app()
    return (datamatrix, metadata, lmem_df, outlier_res_py)  


if __name__ == "__main__": 
    import sys
    datamatrix_filepath = sys.argv[1] 
    metadata_filepath = sys.argv[2] 
    out_dir = sys.argv[3] 
    run(datamatrix_filepath, metadata_filepath) 
    