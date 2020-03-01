"""Test API
This module cointains the test cases for the API views of the jobsdatabucket
Django application.

Examples
    python manage.py test --pattern="test_*" jobsdatabucket.tests

"""
import pprint, time, pytz, json, datetime
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIRequestFactory, URLPatternsTestCase, RequestsClient, APIClient
from jobsdatabucket.models import JobPost, JobPostCompany, JobPostListingTag, JobPostScrape, JobPostTechnology
from jobsdatabucket.api.serializers import JobPostSerializer, JobPostCompanySerializer, JobPostListingTagSerializer, JobPostScrapeSerializer, JobPostTechnologySerializer
from jobsdatabucket.api.views import JobPostViewSet, JobPostCompanyViewSet, JobPostListingTagViewSet, JobPostScrapeViewSet, JobPostTechnologyViewSet

client = RequestsClient()

class TestJobPostAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobPostViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobposts/')

        self.valid_jobpost = {
            "job_title":"CharField",
            "date_posted":"DateField",
            "apply_link":"URLField",
            "job_description":"CharField",
        }

    def test_create_jobpost(self):
        response = self.client.post(self.url, self.valid_jobpost, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobPost.objects.count(), 1)


    def test_update_jobpost(self):
        post = self.client.post(self.url, self.valid_jobpost, format='json')
        self.assertEqual(JobPost.objects.get().<field>.<attr>, "<before_value>")

        jobpost_pk = str(JobPost.objects.get().jobpost_id)

        data = {
            "job_title":"CharField",
            "date_posted":"DateField",
            "apply_link":"URLField",
            "job_description":"CharField",
        }

        request = self.factory.put('api/jobposts/', data, format='json')
        response = self.view(request, pk=jobpost_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobPost.objects.count(), 1)
        self.assertEqual(JobPost.objects.get().<field>.<attr>, "<after value>")


class TestJobPostCompanyAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobPostCompanyViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobpostcompanies/')
        self.jobpost_endpoint = ('http://127.0.0.1:8000/api/jobposts/')
        self.company_endpoint = ('http://127.0.0.1:8000/api/companies/')

        self.valid_jobpostcompany = {
            "job_post":{                
                "job_title":"CharField",
                "date_posted":"DateField",
                "apply_link":"URLField",
                "job_description":"CharField",
               },
            "company":{                
                "company_name":"CharField",
                "hiring_from":"CharField",
               },
        }

    def test_create_jobpostcompany(self):
        response = self.client.post(self.url, self.valid_jobpostcompany, format='json')
        job_post = str(JobPostCompany.objects.get().job_post)
        company = str(JobPostCompany.objects.get().company)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobPostCompany.objects.count(), 1)
        self.assertEqual(job_post, '<model __str__ value>')
        self.assertEqual(company, '<model __str__ value>')


    def test_update_jobpostcompany(self):
        post = self.client.post(self.url, self.valid_jobpostcompany, format='json')
        self.assertEqual(JobPostCompany.objects.get().<field>.<attr>, "<before_value>")

        jobpostcompany_pk = str(JobPostCompany.objects.get().jobpostcompany_id)
        jobpost_pk = str(JobPost.objects.get().jobpost_id)
        company_pk = str(Company.objects.get().company_id)

        data = {
            "jobpostcompany_id":jobpostcompany_pk,
            "job_post":{                
                "job_title":"CharField",
                "date_posted":"DateField",
                "apply_link":"URLField",
                "job_description":"CharField",
               },
            "company":{                
                "company_name":"CharField",
                "hiring_from":"CharField",
               },
        }

        request = self.factory.put('api/jobpostcompanies/', data, format='json')
        response = self.view(request, pk=jobpostcompany_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobPost.objects.count(), 1)
        self.assertEqual(Company.objects.count(), 1)
        self.assertEqual(JobPostCompany.objects.count(), 1)
        self.assertEqual(JobPostCompany.objects.get().<field>.<attr>, "<after value>")


class TestJobPostListingTagAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobPostListingTagViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobpostlistingtags/')
        self.jobpost_endpoint = ('http://127.0.0.1:8000/api/jobposts/')
        self.listingtag_endpoint = ('http://127.0.0.1:8000/api/listingtags/')

        self.valid_jobpostlistingtag = {
            "job_post":{                
                "job_title":"CharField",
                "date_posted":"DateField",
                "apply_link":"URLField",
                "job_description":"CharField",
               },
            "listing_tag":{                
                "listingtag_name":"CharField",
               },
        }

    def test_create_jobpostlistingtag(self):
        response = self.client.post(self.url, self.valid_jobpostlistingtag, format='json')
        job_post = str(JobPostListingTag.objects.get().job_post)
        listing_tag = str(JobPostListingTag.objects.get().listing_tag)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobPostListingTag.objects.count(), 1)
        self.assertEqual(job_post, '<model __str__ value>')
        self.assertEqual(listing_tag, '<model __str__ value>')


    def test_update_jobpostlistingtag(self):
        post = self.client.post(self.url, self.valid_jobpostlistingtag, format='json')
        self.assertEqual(JobPostListingTag.objects.get().<field>.<attr>, "<before_value>")

        jobpostlistingtag_pk = str(JobPostListingTag.objects.get().jobpostlistingtag_id)
        jobpost_pk = str(JobPost.objects.get().jobpost_id)
        listingtag_pk = str(ListingTag.objects.get().listingtag_id)

        data = {
            "jobpostlistingtag_id":jobpostlistingtag_pk,
            "job_post":{                
                "job_title":"CharField",
                "date_posted":"DateField",
                "apply_link":"URLField",
                "job_description":"CharField",
               },
            "listing_tag":{                
                "listingtag_name":"CharField",
               },
        }

        request = self.factory.put('api/jobpostlistingtags/', data, format='json')
        response = self.view(request, pk=jobpostlistingtag_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobPost.objects.count(), 1)
        self.assertEqual(ListingTag.objects.count(), 1)
        self.assertEqual(JobPostListingTag.objects.count(), 1)
        self.assertEqual(JobPostListingTag.objects.get().<field>.<attr>, "<after value>")


class TestJobPostScrapeAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobPostScrapeViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobpostscrapes/')
        self.jobpost_endpoint = ('http://127.0.0.1:8000/api/jobposts/')
        self.scrape_endpoint = ('http://127.0.0.1:8000/api/scrapes/')

        self.valid_jobpostscrape = {
            "job_post":{                
                "job_title":"CharField",
                "date_posted":"DateField",
                "apply_link":"URLField",
                "job_description":"CharField",
               },
            "scrape":{                
                "scrape_date":"DateField",
                "entries_scraped":"IntegerField",
                "scrape_duration":"DurationField",
                "scrape_success":"BooleanField",
               },
        }

    def test_create_jobpostscrape(self):
        response = self.client.post(self.url, self.valid_jobpostscrape, format='json')
        job_post = str(JobPostScrape.objects.get().job_post)
        scrape = str(JobPostScrape.objects.get().scrape)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobPostScrape.objects.count(), 1)
        self.assertEqual(job_post, '<model __str__ value>')
        self.assertEqual(scrape, '<model __str__ value>')


    def test_update_jobpostscrape(self):
        post = self.client.post(self.url, self.valid_jobpostscrape, format='json')
        self.assertEqual(JobPostScrape.objects.get().<field>.<attr>, "<before_value>")

        jobpostscrape_pk = str(JobPostScrape.objects.get().jobpostscrape_id)
        jobpost_pk = str(JobPost.objects.get().jobpost_id)
        scrape_pk = str(Scrape.objects.get().scrape_id)

        data = {
            "jobpostscrape_id":jobpostscrape_pk,
            "job_post":{                
                "job_title":"CharField",
                "date_posted":"DateField",
                "apply_link":"URLField",
                "job_description":"CharField",
               },
            "scrape":{                
                "scrape_date":"DateField",
                "entries_scraped":"IntegerField",
                "scrape_duration":"DurationField",
                "scrape_success":"BooleanField",
               },
        }

        request = self.factory.put('api/jobpostscrapes/', data, format='json')
        response = self.view(request, pk=jobpostscrape_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobPost.objects.count(), 1)
        self.assertEqual(Scrape.objects.count(), 1)
        self.assertEqual(JobPostScrape.objects.count(), 1)
        self.assertEqual(JobPostScrape.objects.get().<field>.<attr>, "<after value>")


class TestJobPostTechnologyAPIView(APITestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.view = JobPostTechnologyViewSet.as_view({'get': 'list', 'post': 'create', 'put': 'update'})
        self.url = ('http://127.0.0.1:8000/api/jobposttechnologies/')
        self.jobpost_endpoint = ('http://127.0.0.1:8000/api/jobposts/')
        self.technology_endpoint = ('http://127.0.0.1:8000/api/technologies/')

        self.valid_jobposttechnology = {
            "job_post":{                
                "job_title":"CharField",
                "date_posted":"DateField",
                "apply_link":"URLField",
                "job_description":"CharField",
               },
            "technology":{                
                "technology_name":"CharField",
               },
        }

    def test_create_jobposttechnology(self):
        response = self.client.post(self.url, self.valid_jobposttechnology, format='json')
        job_post = str(JobPostTechnology.objects.get().job_post)
        technology = str(JobPostTechnology.objects.get().technology)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(JobPostTechnology.objects.count(), 1)
        self.assertEqual(job_post, '<model __str__ value>')
        self.assertEqual(technology, '<model __str__ value>')


    def test_update_jobposttechnology(self):
        post = self.client.post(self.url, self.valid_jobposttechnology, format='json')
        self.assertEqual(JobPostTechnology.objects.get().<field>.<attr>, "<before_value>")

        jobposttechnology_pk = str(JobPostTechnology.objects.get().jobposttechnology_id)
        jobpost_pk = str(JobPost.objects.get().jobpost_id)
        technology_pk = str(Technology.objects.get().technology_id)

        data = {
            "jobposttechnology_id":jobposttechnology_pk,
            "job_post":{                
                "job_title":"CharField",
                "date_posted":"DateField",
                "apply_link":"URLField",
                "job_description":"CharField",
               },
            "technology":{                
                "technology_name":"CharField",
               },
        }

        request = self.factory.put('api/jobposttechnologies/', data, format='json')
        response = self.view(request, pk=jobposttechnology_pk)
        response.render()

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(JobPost.objects.count(), 1)
        self.assertEqual(Technology.objects.count(), 1)
        self.assertEqual(JobPostTechnology.objects.count(), 1)
        self.assertEqual(JobPostTechnology.objects.get().<field>.<attr>, "<after value>")


