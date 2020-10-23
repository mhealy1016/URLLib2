import urllib.request


try:
    # url = 'https://www.glassdoor.com/job-listing/qa-analyst-contract-jam-city-JV_IC1147401_KO0,19_KE20,28.htm?jl=3637910709&pos=127&ao=1096475&s=58&guid=0000017543a11331a0268b46e5360d6b&src=GD_JOB_VIEW&t=SR&vt=w&uido=C065625FF185741B0DEBC5E064C43792&cs=1_8fbadae9&cb=1603157431914&jobListingId=3637910709&ctt=1603157750927'
    url = 'https://www.glassdoor.com/job-listing/full-stack-software-engineer-carbon3d-JV_IC1147394_KO0,28_KE29,37.htm?jl=3669446882&pos=118&ao=954035&s=58&guid=000001754bd09ddeb82ba41cc4ae515a&src=GD_JOB_VIEW&t=SR&vt=w&uido=C065625FF185741B0DEBC5E064C43792&cs=1_1f4251f6&cb=1603294765106&jobListingId=3669446882&ctt=1603300992540'
    meh = 'https://www.glassdoor.com/job-listing/full-stack-software-engineer-carbon3d-JV_IC1147394_KO0,28_KE29,37.htm?jl=3669446882&pos=118&ao=954035&s=58&guid=000001754bd09ddeb82ba41cc4ae515a&src=GD_JOB_VIEW&t=SR&vt=w&uido=C065625FF185741B0DEBC5E064C43792&cs=1_1f4251f6&cb=1603294765106&jobListingId=3669446882&ctt=1603301600605'
    # now, with the below headers, we defined ourselves as a simpleton who is
    # still using internet explorer.
    test = 'https://www.glassdoor.com/partner/jobListing.htm?pos=118&amp;ao=954035&amp;s=58&amp;guid=000001754bd09ddeb82ba41cc4ae515a&amp;src=GD_JOB_VIEW&amp;t=SR&amp;vt=w&amp;uido=C065625FF185741B0DEBC5E064C43792&amp;cs=1_1f4251f6&amp;cb=1603294765106&amp;jobListingId=3669446882'
    # headers = {}
    # headers['User-Agent'] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.80 Safari/537.36"
    # req = urllib.request.Request(url, headers = headers)



    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers = {'User-Agent': user_agent, }
    req = urllib.request.Request(meh, None, headers)

    resp = urllib.request.urlopen(req)

    data = resp.read()
    print(data)


   # newLink = resp.geturl()
   # newLink = resp.read()
   # print(newLink.read())

except Exception as e:
    print(str(e))

