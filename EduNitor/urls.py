"""EduNitor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
import app.views as av


urlpatterns = [
    ########## index page paths ###################
    ##############################################
    path('',av.index),
    path('LoginOrg', av.org_login),
    path('SignUpOrg',av.org_register),
    path('LoginUser', av.user_login),
    path('VerifyEmail',av.verifyEmail),
    path('logout',av.logout),
    path('contact',av.contact),
    path('team',av.team),
    path('faq', av.faq),
    #password change for organization by verfying the email
    path('org-forgot-password',av.org_forgot_password),
    path('org-forgot-password-otp-verify', av.org_forgot_password_otp_verify),
    path('org-forgot-password-change-pass', av.org_forgot_password_change_password),
    #password change for employee by verifying the email
    path('user-forgot-password',av.user_forgot_password),
    path('user-forgot-password-otp-verify', av.user_forgot_password_otp_verify),
    path('user-forgot-password-change-pass', av.user_forgot_password_change_password),
    ################################################
    ################################################


    ###############   organization  #################
    #################################################
    path('org_index', av.org_index),
    ## under employee options###########
    path('create-emp',av.add_emp),
    path('read-emp',av.read_emp),
    #under the view page contain the three view, update, delete options
    path('view-emp/<int:eid>', av.view_emp),
    path('update-emp/<int:eid>', av.update_emp),
    path('del-emp/<int:eid>', av.del_emp),
    #
    path('org-view-attendance', av.org_view_attendance),
    path('emp-leaves', av.org_emp_leave_views),
    path('org-emp-leave-approval/<int:pk>/',av.org_emp_leave_approval, name="org-emp-leave-approval"),
    ###################################

    ## under monitoring options########
    path('view-app-web', av.view_app_web),
    path('depth-view-app-web', av.depth_view_app_web),
    path('ss-monitoring', av.ss_monitoring),
    path('power-monitoring', av.power_monitoring),
    ###################################

    ######### under project options ########
    path('create-proj',av.create_proj),
    path('read-proj', av.read_proj),
    
    # ✅ First step: View list of tasks in a project
    path('projectwise-tasks/<int:pid>', av.view_project_tasks, name='view_project_tasks'),

    # ✅ Second step: Dashboard of that project
    # path('project-dashboard/<int:pid>', av.projectwise_task, name='projectwise_task'),
    path('project-dashboard/<int:task_id>/<int:result_id>/', av.projectwise_task, name='projectwise_task'),

    path('del-proj/<int:pid>', av.del_proj),
    #view page options
    path('update-task/<int:pk>/', av.update_task, name="update-task"),
    path('delete-task/<int:pk>/', av.delete_task, name="delete-task"),

    path('assign-proj',av.assign_proj_emp),
    path('select-unassign', av.select_unassign, name="select-unassign"),
    path('unassign-employee', av.unassign_employee, name="unassign-employee"),
    path('unassign-emp/<int:eid>', av.unassign_emp),
    #########################################

    ######## board option ##################
    path('create-board',av.create_board),
    path('read-boards', av.read_boards),
    path('boardwise-tasks/<int:bid>', av.boardwise_task),
    path('del-board/<int:bid>', av.del_board),

    #########################################



    ########## Productivity  ################
    path('create-wp', av.create_wp),
    path('edit-wp', av.read_edit_wp),
    path('del-wp/<int:wid>', av.del_wp),
    path('work-productivity-check', av.work_productivity_check),
    path('logDashboard', av.logDashboard),
    path('rank-productivity', av.rank_productivity),#error
    #########################################

    ########## Task option ##################
    path('overview-task', av.overview_task, name="overview-task"),#error
    path('create-task', av.create_task),
    path('read-task', av.read_tasks),
    ########################################

    ######### Meeting option ##############
    path('create-meet', av.create_meet),
    path('read-meet', av.read_meet),
    path('edit-meet/<int:mid>', av.edit_meet),
    path('del-meet/<int:mid>', av.del_meet),
    #######################################

    ######### Notice option ###############
    path('overview-notice', av.overview_notices, name="overview-notice"),
    path('create-notice', av.create_notice),
    path('read-notice', av.read_notices),
    path('update-notice/<int:pk>/', av.update_notice, name="update-notice"),
    path('delete-notice/<int:pk>/', av.delete_notice, name="delete-notice"),
    


    
    ########## report problem ,change password and logout###
    path('org_report_problems',av.report_org),
    path('org_change_password',av.org_change_password),
    path('logout',av.logout),
    ########################################################


    
    path('get_emps_by_project/<int:pid>', av.get_emps_by_project),
    path('get_emps_not_in_project/<int:pid>', av.get_emps_not_in_project),
    

    
    
 
    
    
    
    
    
    path('view-project-wise-employees', av.view_project_wise_employees),
    path('get_prod_details/<str:eidanddate>', av.get_prod_details),
    
    
    
    path('get_emp_logged_in_count_today', av.get_emp_logged_in_count_today),


   #### employeee paths ####################################################
    path('user_index', av.user_index),
    path('emp-profile',av.user_profile),
    path('emp-view-notices', av.emp_view_notices),
    path('user-read-meets', av.user_read_meets),
    path('user-view-app-web', av.user_view_app_web),
    path('user-depth-view-app-web', av.user_depth_view_app_web),
    path('user-ss-monitoring', av.user_ss_monitoring),
    path('user-power-monitoring', av.user_power_monitoring),
    path('user-work-productivity-check', av.user_work_productivity_check),
    path('user-view-projects', av.user_view_projects),
    path('user-projectwise-tasks/<int:pid>', av.user_projectwise_task),
    path('user-overview-task', av.user_overview_task),
    path('emp-view-tasks', av.emp_view_tasks),
    path('emp-update-tasks/<int:tid>', av.emp_update_tasks),
    path('user-view-attendance', av.user_view_attendance),
    path('user-apply-emp-leaves', av.user_apply_emp_leaves),
    path('user-view-emp-leaves', av.user_view_emp_leaves),
    path('user_report_problems', av.report_emp),
    path('user_change_password', av.user_change_password),



]

handler404 = "app.views.error_404_view"
