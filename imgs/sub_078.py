'''
Author: Xiya Liu
Date: 2022-05-06 19:33:49
LastEditors: doulemint 871251700@qq.com
LastEditTime: 2022-06-04 17:32:11
FilePath: /MiceMRI_Pipelinev3/Scripts/configs/sub_078.py
Description: 

'''


debug = True
thread_num = 3
workflow_path = "./workflows/sub_067.md"
log_path = "./workflows/sub_067.log"
miceflow_path = "/share/user_data/xiya/pratice/MiceMRI_Pipelinev3/miceflow"


####fmri registration

bids_path = "/share/user_data/xiya/awake_mice/bids/"
T2_path = "/share/user_data/xiya/awake_mice/bids_intact/sub-067/ses-1/anat/sub-067_ses-1_T2w.nii.gz"
fmri_path = "/share/user_data/xiya/awake_mice/bids_intact/sub-067/ses-1/func/sub-067_ses-1_task_rest_bold.nii.gz"
preprocess_out_dir = "/share/user_data/xiya/awake_mice/bids_derivative"
t2_mask_path = "/share/user_data/xiya/awake_mice/bids_intact/sub-067/ses-1/anat/sub-067_ses-1_T2w_manual_mask.nii.gz"

cut_frame = 0

smooth=False #fmri regresition 
fwhm=6 #post-prorcess fwhm
t_r =1