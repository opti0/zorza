from django.urls import path
from django.views.decorators.cache import never_cache

from .views import *

urlpatterns = [
    # TIMETABLES
    path('', show_timetable, name='timetable'),
    path('class/<int:class_id>/', show_class_timetable, name='class_timetable'),
    path('groups/<group_ids>/', show_groups_timetable, name='groups_timetable'),
    path('room/<int:room_id>/', show_room_timetable, name='room_timetable'),
    path('teacher/<int:teacher_id>/', show_teacher_timetable, name='teacher_timetable'),
    path('rooms/', RoomsDatePeriodSelectView.as_view(), name='rooms'),
    path('rooms/<date>/<period>/', show_rooms, name='rooms'),
    path('schedules/', show_schedules, name='schedules'),
    path('calendar/edit/', edit_calendar, name='edit_calendar'),
    

    # SUBSTITUTIONS
    path('substitutions/add/', never_cache(AddSubstitutionsView1.as_view()), name='add_substitutions1'),
    path('substitutions/add/<int:teacher_id>/<date>/', add_substitutions2, name='add_substitutions2'),
    path('substitutions/delete/<int:substitution_id>/', delete_substitution, name='delete_substitution'),
    path('substitutions/print/', PrintSubstitutionsView.as_view(), name='print_substitutions'),
    path('substitutions/print/<date>/', show_substitutions, name='show_substitutions_as_html'),
    path('substitutions/import/', never_cache(SubstitutionsImportView.as_view()), name='import_substitutions'),
    
    # RESERVATIONS
    path('reservation/add/', AddReservationView.as_view(), name='add_reservation'),
    
    # PERSONALIZATION
    path('personalize/<int:class_id>/', personalize, name='personalize'),
    path('customize', Customize.as_view(), name='customize'),
    
    # OTHER
    path('display/', display, name='display'),
    path('api/1/bell/', timetable_bell_api, name='timetable_bell_api')
]
