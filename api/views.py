from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from api.firebase.firestoreConfig import filterByField, getCompanyLocation, getCompanyNames, getJobTags
from rest_framework import status

from api.main import getJobs

class ActivateScrapping(GenericAPIView):
    def get(self,request,*args,**kwargs):
        try:
            getJobs()

            return Response({"message":"Jobs has successfully been scrapped"},status=status.HTTP_200_OK)
        except Exception:
            return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetJobsFromDocs(GenericAPIView):
    def get(self,request,*args,**kwargs):
        try:
            companies = getCompanyNames()

            return Response({"companies": companies},status=status.HTTP_200_OK)

        except:
            return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetJobsTags(GenericAPIView):
    def get(self,request,*args,**kwargs):
        try:
            tags = getJobTags()

            return Response({"tags":tags},status=status.HTTP_200_OK)

        except:
            return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetFilteredJobsByCompanyName(GenericAPIView):
    def get(self,request,*args,**kwargs):
        try:
            name = request.GET.get("company_name")

            value = filterByField("company_name",name)

            if not name:
                return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  

            return Response({"result":value},status=status.HTTP_200_OK)

        except:
            return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetFilteredJobsByTag(GenericAPIView):
    def get(self,request,*args,**kwargs):
        try:
            name = request.GET.get("tag")
            
            if not name:
                return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


            value = filterByField("tag",name)  

            return Response({"result":value},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetFilteredJobsByLocation(GenericAPIView):
    def get(self,request,*args,**kwargs):
        try:
            name = request.GET.get("location")
            print("ll:",name)
            if not name:
                return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


            value = filterByField("location",name)  

            return Response({"result":value},status=status.HTTP_200_OK)

        except Exception as e:
            print("ee:",e)
            return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetFilteredJobsBySalary(GenericAPIView):
    def get(self,request,*args,**kwargs):
        try:
            name = request.GET.get("salary")

            if not name:
                return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


            value = filterByField("salary",name)  

            return Response({"result":value},status=status.HTTP_200_OK)

        except:
            return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)



class GetFilteredJobsByCreated(GenericAPIView):
    def get(self,request,*args,**kwargs):
        try:
            name = request.GET.get("created_at")

            if not name:
                return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


            value = filterByField("created_at",name)  

            return Response({"result":value},status=status.HTTP_200_OK)

        except:
            return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class GetJobs(GenericAPIView):
    def get(self,request,*args,**kwargs):
        try:

            value = filterByField("exx","exxx")  

            return Response({"result":value},status=status.HTTP_200_OK)

        except:
            return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetJobsLocation(GenericAPIView):
    def get(self,request,*args,**kwargs):
        try:
            locations = getCompanyLocation()

            return Response({"locations":locations},status=status.HTTP_200_OK)

        except:
            return Response({"error":"Sorry could not handle the request"},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

