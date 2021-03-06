from django.db import models
import uuid

class JobBoard(models.Model):
    """A job board is a source from which job posts and other elements are obtained."""
    jobboard_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    jobboard_name = models.CharField(max_length=250)
    home_page = models.URLField(null=True)
    search_page = models.URLField(null=True)


class ListingTag(models.Model):
    """A listing tag profiles a job opportunity based on whether or not it is remote-friendly."""
    listingtag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    listingtag_name = models.CharField(max_length=250)


class Scrape(models.Model):
    """A scrape is an automated session wherein the database is either populated or not."""
    scrape_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scrape_date = models.DateField(auto_now=False, auto_now_add=False)
    entries_scraped = models.IntegerField(null=True)
    scrape_duration = models.DurationField(null=True)
    scrape_success = models.BooleanField()


class ScrapeJobBoard(models.Model):
    """A scrape occurs regularly on a given job board over time."""
    scrapejobboard_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    scrape = models.ForeignKey('scraper.Scrape',on_delete=models.CASCADE,)
    job_board = models.ForeignKey('scraper.JobBoard',on_delete=models.CASCADE,)


class JobBoardListingTag(models.Model):
    """A listing tag is is an idiosyncratic tag belonging to a certain job board."""
    jobboardlistingtag_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    job_board = models.ForeignKey('scraper.JobBoard',on_delete=models.CASCADE,)
    listing_tag = models.ForeignKey('scraper.ListingTag',on_delete=models.CASCADE,)
