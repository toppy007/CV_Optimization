from job_advert.job_advert import JobAdvert

def test_job_ad_scraper():
    response = JobAdvert.job_ad_scrapper('https://app.otta.com/jobs/NzNpVWNM')

    assert response is not None