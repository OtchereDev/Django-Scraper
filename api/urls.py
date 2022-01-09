from django.urls import path

from api.views import ActivateScrapping, GetFilteredJobsByCompanyName, GetFilteredJobsByCreated, GetFilteredJobsByLocation, GetFilteredJobsBySalary, GetFilteredJobsByTag, GetJobs, GetJobsFromDocs, GetJobsLocation, GetJobsTags

urlpatterns = [
    path("get-refresh-jobs/",ActivateScrapping.as_view()),
    path("get-companies/",GetJobsFromDocs.as_view()),
    path("get-tags/",GetJobsTags.as_view()),
    path("get-locations/",GetJobsLocation.as_view()),
    path("get-filter-job-tag/",GetFilteredJobsByTag.as_view()),
    path("get-filter-job-salary/",GetFilteredJobsBySalary.as_view()),
    path("get-filter-job-created_at/", GetFilteredJobsByCreated.as_view()),
    path("get-filter-job-location/",GetFilteredJobsByLocation.as_view()),
    path("get-filter-job-company_name/",GetFilteredJobsByCompanyName.as_view()),
    path("get-all-jobs/",GetJobs.as_view())
]