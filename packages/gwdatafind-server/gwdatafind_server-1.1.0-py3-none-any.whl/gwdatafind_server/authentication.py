# -*- coding: utf-8 -*-
# Copyright (2020) University of Wisconsin-Milwaukee
# Licensed under GPLv3+ - see LICENSE

"""Authentication for the GWDataFind Server
"""

import re
from flask import request, current_app
from functools import wraps

__author__ = 'Duncan Meacher <duncan.meacher@ligo.org>'

# SciTokens Audience
AUD = "https://ligo.org/oauth"
# SciTokens Scope
SCP = "read:/protected"


def _get_auth_type():
    config = current_app.config
    authType = config['authorization']

    if authType == 'virtual_host':
        request_ip = request.environ.get(
            "SERVER_ADDR",
            request.environ.get(
                "HTTP_X_FORWARDED_HOST",
                request.remote_addr,
            ),
        )

        try:
            authType = config[request_ip]["authorization"]
        except KeyError:
            current_app.logger.info('Auth type not found,'
                                    ' using full authentication.')
            authType = "grid-mapfile,scitoken"

    if authType == "None":
        return None

    if isinstance(authType, str):
        return [x.strip() for x in authType.split(",")]

    return authType


def _validate_scitoken(request, audience=None, scope=None):
    raise NotImplementedError("SciTokens not yet implemented. Use X.509 "
                              "proxy certificate")


def _validate_x509(request):
    # Get subject and issuer from header
    subject_dn_header = request.headers.get("SSL_CLIENT_S_DN")

    # Clean up impersonation proxies. See:
    # https://git.ligo.org/lscsoft/gracedb/-/blob/master/gracedb/api/backends.py#L119
    subject_pattern = re.compile(r'^(.*?)(/CN=\d+)*$')
    subject = subject_pattern.match(subject_dn_header).group(1)

    # Check if subject is contained within grid-mapfile
    gridmap = current_app.get_gridmap_data()
    for line in gridmap:
        if subject == line:
            break
    else:
        raise RuntimeError("Subject not in grid-mapfile")
    current_app.logger.info('User X.509 proxy certificate authorised.')


def validate(func):
    @wraps(func)
    def validator(*args, **kwargs):
        try:
            authType = _get_auth_type()
            if authType is None:
                current_app.logger.info('View request, no authentication '
                                        'required')
            else:
                # Check for SciToken in header
                if (
                    'scitoken' in authType
                    and 'Authorization' in request.headers
                   ):
                    current_app.logger.info('View request with SciToken.')
                    try:
                        _validate_scitoken(request, audience=AUD, scope=SCP)
                    except NotImplementedError as exc:
                        msg = "SciToken authentication failed: {!r}"\
                              .format(exc)
                        current_app.logger.info('View request error:'
                                                '{}'.format(msg))
                        content = {"Error, {}.".format(msg): ""}
                        return content, 403
                # Else, check for X.509 certificate info in header
                elif (
                      'grid-mapfile' in authType
                      and 'SSL_CLIENT_S_DN' in request.headers
                      and 'SSL_CLIENT_I_DN' in request.headers
                     ):
                    current_app.logger.info("View request with X.509 proxy "
                                            "certificate.")
                    try:
                        _validate_x509(request)
                    except RuntimeError as exc:
                        msg = "X.509 authentication failed: {!r}".format(exc)
                        current_app.logger.info('View request error:'
                                                '{}'.format(msg))
                        content = {"Error, {}.".format(msg): ""}
                        return content, 403
                else:
                    raise RuntimeError("No Authentication Header or X.509 "
                                       "cert info in header")

            return func(*args, **kwargs)
        except RuntimeError as exc:
            msg = "Authentication failed: {!r}".format(exc)
            current_app.logger.info('View request error:'
                                    '{}'.format(msg))
            content = {"Error, {}.".format(msg): ""}
            return content, 403
    return validator
