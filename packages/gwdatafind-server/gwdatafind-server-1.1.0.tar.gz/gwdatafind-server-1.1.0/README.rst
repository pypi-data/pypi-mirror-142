===================
 GWDataFind Server
===================

This module defines a Flask App that serves URLs based on the contents of a diskcache.

Requirements
============
* Python >= 3.4
* Flask >= 1.0.0

Apache + Gunicorn configuration
===============================

This service runs under Gunicorn behind an Apache proxy, which is used to
verify X.509 certificates. The certificate information is then passed to the
application in the header where the subject is authenticated against a grid-mapfile.

Add the following to the Apache system config file, e.g. /etc/sysconfig/httpd on CentOS 7 ::

    OPENSSL_ALLOW_PROXY_CERTS=1

Edit the appropriate 443 virtual host configuration to add ::

  # Using Apache as a proxy to gunicorn
    ProxyPass "/LDR" "http://127.0.0.1:8080/" retry=0
    ProxyPassReverse "/LDR" "http://127.0.0.1:8080/"
  
    <Location "/LDR/">
         SSLRequireSSL
         SSLVerifyClient optional
         SSLVerifyDepth 10
         SSLOptions +ExportCertData +StrictRequire +LegacyDNStringFormat
         SSLOptions +StdEnvVars
         RequestHeader set SSL_CLIENT_S_DN "%{SSL_CLIENT_S_DN}s"
         RequestHeader set SSL_CLIENT_I_DN "%{SSL_CLIENT_I_DN}s"
    </Location>

Start a gunicron instance with ::

    /usr/bin/gunicorn-3.6 --bind=127.0.0.1:8080 --workers=5 "gwdatafind_server:create_app()"

Sample configuration file can be put into /etc/gwdatafind-server.ini ::

    [LDRDataFindServer]
    # frame cache file
    framecachefile = <path_to>/ascii_cache.dat
    framecachetimeout = 10
    # grid-mapfile
    gridmapcachefile = <path_to>/grid-mapfile
    gridmapcachetimeout = 60
    # optional parameters
    site_exclude_pattern = ^X$
    frametype_exclude_pattern = .+EXCLUDE.+
    frametype_include_pattern = .+_TEST_\d+
    filter_preference = """{'^file': ['preferred', 'hdfs']}"""

Client API
==========

The GWDataFind Server runs as a daemon providing a RESTful interface via Gunicorn + Apache.
There is also a client application ``gw_data_find`` for command line usage.

The URLs supported areliwted below.  They all support HTTP GET,HEAD, and OPTIONS methods.

+-----------------------------------------------------------------------+--------------------------+
| URL (add ``HTTP[S]://<host>[:<port>]/LDR`` to beginning               |  Function                |
+=======================================================================+==========================+
| ``/services/data/v1/``                                                | Show URLs (debugging)    |
+-----------------------------------------------------------------------+--------------------------+
| ``/services/data/v1/<ext>.json``                                      | Show observatories       |
+-----------------------------------------------------------------------+--------------------------+
| ``/services/data/v1/<ext>/<site>.json``                               | Show tags (frame types)  |
+-----------------------------------------------------------------------+--------------------------+
| ``/services/data/v1/<ext>/<site>/<tag>/latest.json``                  | Show latest              |
+-----------------------------------------------------------------------+--------------------------+
| ``/services/data/v1/<ext>/<site>/<tag>/<start>,<end>.json``           | Show URLs                |
+-----------------------------------------------------------------------+--------------------------+
| ``/services/data/v1/<ext>/<site>/<tag>/<start>,<end>/<urltype>.json`` | Show URLs of one type    |
|                                                                       | (file,URL)               |
+-----------------------------------------------------------------------+--------------------------+
| ``/services/data/v1/<ext>/<site>/<tag>/segments.json``                | Show all available       |
|                                                                       | segments                 |
+-----------------------------------------------------------------------+--------------------------+
| ``/services/data/v1/<ext>/<site>/<tag>/segments/<start>,<end>.json``  | Show avalable segments   |
|                                                                       | in a time interval       |
+-----------------------------------------------------------------------+--------------------------+
| ``/services/data/v1/<ext>/<site>/<tag>/latest.json``                  | Show latest URL          |
+-----------------------------------------------------------------------+--------------------------+
| ``/services/data/v1/<ext>/<site>/<tag>/<filename>.json``              | Show a single URL        |
+-----------------------------------------------------------------------+--------------------------+


