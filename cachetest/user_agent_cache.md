```py
Python 3.8.10 (default, Mar 15 2022, 12:22:08) 
Type 'copyright', 'credits' or 'license' for more information
IPython 7.13.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 
   ...: import diskcache as dc #use diskcache
   ...:  
   ...: cache = dc.Cache('tmp')
   ...:  
   ...: with open('agents.txt') as f: #read user-agents
   ...:     for user_agent in f: 
   ...:         if (len(user_agent) < 100) and ("Test:" not in user_agent): 
   ...:             if user_agent in cache: #check if seen already
   ...:                 pass 
   ...:             else: 
   ...:                 print("new agent:", user_agent) #print new user-agent
   ...:                 cache[user_agent] = True #cache it
   ...:                                                                                        
new agent: Mozilla/5.0 (compatible; Nmap Scripting Engine; http://nmap.org/book/nse.html)

new agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:10.0.2) Gecko/20100101 Firefox/10.0.2

new agent: -

new agent: Mozilla/5.0 (X11; Linux i686; rv:10.0.2) Gecko/20100101 Firefox/10.0.2

new agent: Mozilla/5.0 (X11; Linux i686; rv:5.0.1) Gecko/20100101 Firefox/5.0.1

new agent: Mozilla/5.0 (X11; Linux i686; rv:2.0.1) Gecko/20100101 Firefox/4.0.1

new agent: A9WFXewh9PjH6EP39aFwSMgz9jmW422XT2kK1iN6iFZ4KpQsJ56zY5UfImxxdjQOsUxbBvaLaAujCjJ3Avy3yzGxK9p

new agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)

new agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)

new agent: Mozilla/5.0 (Windows NT 6.1; rv:7.0.1) Gecko/20100101 Firefox/7.0.1

new agent: ArsRvwvYzLkOe2EyPTBKpsQhBut2nifjbs1LXyk3TNnkSh1WsCc8m2agik11dhASZUN8t0pDcQljcmgvtdxl8zDPP5c

new agent: gNDO0EeCcrKeNxRjbXmQ2JOdj3VZikq5Bov5gLiHS4Pnjo0jYF2iLuCkfgMLHE6e1vtJngaxb21pfCz

new agent: Mozilla/5.0 (X11; Linux i686 on x86_64; rv:10.0.2) Gecko/20100101 Firefox/10.0.2

new agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)

new agent: Nessus SOAP v0.0.1 (Nessus.org)

new agent: NetSupport Manager/1.0

new agent: webmin

new agent: */*

new agent: Nessus

new agent: NESSUS::SOAP

new agent: oh sure

new agent: "; system(id);#

new agent: mercuryboard_user_agent_sql_injection.nasl'

new agent: Mozilla/4.0 (compatible; gallery_203.nasl; Googlebot)

new agent: Fastream NETFile Server

new agent: Mozilla/4.0 (Windows XP 5.1) Java/1.6.0_23

new agent: Mozilla Firefox

new agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0.2) Gecko/20100101 Firefox/10.0.2

new agent: Mozilla/5.0 (X11; Linux i686 on x86_64; rv:5.0.1) Gecko/20100101 Firefox/5.0.1

new agent: Microsoft-WebDAV-MiniRedir/5.1.2600

new agent: chucky

new agent: Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:11.0) Gecko/20100101 Firefox/11.0

new agent: XMLHTTP/1.0

new agent: xmlrpclib.py/1.0.1 (by www.pythonware.com)

new agent: Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1

new agent: Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; .NET CLR 2.0.50727; .NET CLR 1.1.4322)

new agent: MSFrontPage/4.0

new agent: Mozilla/4.0 (compatible; SPIPE/1.0)

new agent: Opera/10.00 (Windows NT 5.1; U; en) Presto/2.2.0

new agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:9.0.1) Gecko/20100101 Firefox/9.0.1

new agent: Chucky12345768/1.0

new agent: TnOfjohbqPcewt2QtUE6d9rl1y3DrkQ0SvIj4H

new agent: Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)

new agent: fPPc8Hor7FMPjs4PLxvUUL8a1wee2AFTShyop245RLTKo49fPewFCdYranjTAcI

new agent: zxENHbZltTBZd085nxR7w7d32yqimUlf7RL2t5rgxaCjSitCXJKu6k3WN1WZpc2WvoOfA9cfHZQpq

new agent: <?php eval($_POST['q34798287']);?>

new agent: <?eval($_POST['q69129384']);?>

new agent: <?eval($_POST['q65325241']);?>

new agent: <?php eval($_POST['q15428251']);?>

new agent: <?eval($_POST['q13631916']);?>

new agent: <?php eval($_POST['q58632758']);?>

new agent: <?eval($_POST['q31999379']);?>

new agent: Mozilla/5.0 (Windows NT 5.1; rv:11.0) Gecko/20100101 Firefox/11.0

new agent: kHsUGdKI4QGC1VCTqX7Pr7WrZXKEHxdDmJrq2OFWz1rTEgxNXxHSwN

new agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)

new agent: Wget/1.11.4

new agent: MSFrontPage/5.0

new agent: DirBuster-0.12 (http://www.owasp.org/index.php/Category:OWASP_DirBuster_Project)

new agent: HHdJbkexI3538R8FmRYLxYUBV7wg5VXMa7mf40kU0kiv2WLWhiGzKOZLnWNjTyUQmodQzZV9djqQIdJek

new agent: <script>alert(12345)</script>

new agent: Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; .NET CLR 1.1.4322)

new agent: nUbKpJkgeXZXNYz86PFuvKq0l1Hv4VwClYDUlwuEOZiIfxUHJi

new agent: 123456' generate sql error

new agent: SomeCustomInjectedHeader:injected_by_wvs

new agent: http://some-inexistent-website.acu/some_inexistent_file_with_long_name

new agent: 1some_inexistent_file_with_long_name

new agent: http://testphp.vulnweb.com/acunetix_file_inclusion_test?

new agent: )

new agent: !(()&&!|*|*|

new agent: ^(#$!@#$)(()))******

new agent: &cat /etc/passwd

new agent: &cat /etc/passwd&

new agent: cat /etc/passwd

new agent: `cat /etc/passwd`

new agent: |cat /etc/passwd#

new agent: 268435455

new agent: ;cat /etc/passwd;

new agent: ||cat /etc/passwd

new agent: 1e309

new agent: M3YxbElVcDkwTkxPNVNxaQ==

new agent: '"'");|]*{%0d%0a<%00>

new agent: &dir

new agent: print(md5(acunetix_wvs_security_test));die();/*

new agent: |dir

new agent: ${@print(md5(acunetix_wvs_security_test))}

new agent: ../../../../../../../../../../etc/passwd

new agent: ../../../../../../../../../../etc/passwd%00.png

new agent: /../..//../..//../..//../..//../..//etc/passwd%00

new agent: acunetix_wvs_invalid_filename

new agent: login

new agent: login/.

new agent: 1'

new agent: \xc0 xa7

new agent: 1"

new agent: \xc0\xa2

new agent: JyI=

new agent: \xbf'\xbf"

new agent: \xf0''\xf0""

new agent: //www.acunetix.tst

new agent: '"

new agent: <!--

new agent: '"()&%1<ScRiPt >prompt(945646)</ScRiPt>

new agent: OTU4MjA0

new agent: ${@print(md5(acunetix_wvs_security_test))}\

new agent: .\\./.\\./.\\./.\\./.\\./.\\./etc/passwd

new agent: /etc/passwd

new agent: ../..//../..//../..//../..//../..//../..//../..//../..//etc/passwd

new agent: ../.../.././../.../.././../.../.././../.../.././../.../.././../.../.././etc/passwd

new agent: ..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%af..%c0%afetc/passwd

new agent: file:///etc/passwd

new agent: /\../\../\../\../\../\../\../etc/passwd

new agent: ../../../../../../../../../../windows/win.ini

new agent: c:/windows/win.ini

new agent: ../../../../../../../../../../windows/win.ini%00

new agent: ..%5c..%5c..%5c..%5c..%5c..%5c..%5c..%5cwindows%5cwin.ini

new agent: /.\\./.\\./.\\./.\\./.\\./.\\./windows/win.ini

new agent: ../..//../..//../..//../..//../..//../..//../..//../..//windows/win.ini

new agent: ../.../.././../.../.././../.../.././../.../.././../.../.././../.../.././windows/win.ini

new agent: 62NHJwWk

new agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)' and sleep(4)='

new agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)" and sleep(4)="

new agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)' or (sleep(4)+1) limit 1 --

new agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)" or (sleep(4)+1) limit 1 --

new agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'=sleep(4)='

new agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)"=sleep(4)="

new agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)'; waitfor delay '0:0:4' --

new agent: Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0)"; waitfor delay '0:0:4' --

new agent: 4lX2BJxaPChB3PrZWg0d8GtWmF7L9UusFNY9QZuxLVTkLMiDxV9bg3PK8zDIpAdnybdjbX

new agent: uYw6aXPltl0lpjG8ac4snO4RqmVjdS84XnLGU6dMReOMaswJ6vRb5OKroWC

new agent: Wget/1.12 (linux-gnu)

new agent: Mozilla/5.0 SF/2.03b

new agent: UFc5UTlydXcxUTRqcEdvWg==

new agent: index.php

new agent: index.php/.

new agent: Tv6y3zIh

new agent: '"()&%1<ScRiPt >prompt(969975)</ScRiPt>

new agent: OTQxODk5

new agent: sfish'"'"'"'"

new agent: sfish''''""""

new agent: sfish'"

new agent: sfish\'\"

new agent: sfish\\'\\"

new agent: ZVVIWDVBOENlVHkwYkxZQg==

new agent: phpmyadmin.css.php

new agent: phpmyadmin.css.php/.

new agent: jxQLBwtB

new agent: '"()&%1<ScRiPt >prompt(921561)</ScRiPt>

new agent: OTE3MjM5

new agent: MUxiOENscHBndVVORWFLbA==

new agent: Documentation.html

new agent: Documentation.html/.

new agent: '"()&%1<ScRiPt >prompt(975146)</ScRiPt>

new agent: OTA4MTA4

new agent: 0Eh6buTm

new agent: w3af.sourceforge.net

new agent: Mozilla/4.0 (compatible; MSIE 5.0; Windows NT;)

new agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:10.0.2) Gecko/20100101 Firefox/10.0.2

new agent: Wget/1.10.2 (Red Hat modified)

new agent: Mozilla/5.0 (X11; Linux i686; rv:9.0.1) Gecko/20100101 Firefox/9.0.1

new agent: Python-urllib/2.6

new agent: cadaver/0.23.3 neon/0.29.0

new agent: <!--#exec cmd="dir"-->

new agent: nessus=<!--#exec cmd="dir"-->

new agent: <!--#exec cmd="cat /etc/passwd"-->

new agent: nessus=<!--#exec cmd="cat /etc/passwd"-->

new agent: <!--#include file="nessus897043736.html"-->

new agent: nessus=<!--#include file="nessus897043736.html"-->


In [2]: with open('agents.txt') as f: #nothing gets printed because all the user-agents have been seen before and are in cache
   ...:     for user_agent in f: 
   ...:         if (len(user_agent) < 100) and ("Test:" not in user_agent): 
   ...:             if user_agent in cache: 
   ...:                 pass 
   ...:             else: 
   ...:                 print("new agent:", user_agent) 
   ...:                 cache[user_agent] = True 
   ...:                                                                                        

In [3]:                                                                                        
```
